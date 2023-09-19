"""
SporeStack CLI: `sporestack`
"""

import json
import logging
import os
import sys
import time
from pathlib import Path
from typing import TYPE_CHECKING, Any, Dict, Optional

import typer

if sys.version_info >= (3, 9):  # pragma: nocover
    from typing import Annotated
else:  # pragma: nocover
    from typing_extensions import Annotated

if TYPE_CHECKING:
    from . import api
    from .api_client import APIClient
    from .models import Invoice


HELP = """
SporeStack Python CLI

Optional environment variables:
SPORESTACK_ENDPOINT
*or*
SPORESTACK_USE_TOR_ENDPOINT

TOR_PROXY (defaults to socks5://127.0.0.1:9050 which is fine for most)
"""

_home = os.getenv("HOME", None)
assert _home is not None, "Unable to detect $HOME environment variable?"
HOME = Path(_home)

SPORESTACK_DIR = Path(os.getenv("SPORESTACK_DIR", HOME / ".sporestack"))

# Try to protect files in ~/.sporestack
os.umask(0o0077)

cli = typer.Typer(help=HELP)

HOME = Path(_home)

token_cli = typer.Typer(help="Commands to interact with SporeStack tokens")
cli.add_typer(token_cli, name="token")
server_cli = typer.Typer(help="Commands to interact with SporeStack servers")
cli.add_typer(server_cli, name="server")

_log_level = os.getenv("LOG_LEVEL", "warning").upper()
_numeric_log_level = getattr(logging, _log_level, None)
if _numeric_log_level is None:
    raise ValueError(f"LOG_LEVEL: {_log_level} is invalid. Aborting!")
assert isinstance(_numeric_log_level, int)
logging.basicConfig(level=_numeric_log_level)

DEFAULT_TOKEN = "primary"
DEFAULT_FLAVOR = "vps-1vcpu-1gb"
# Users may have a different key file, but this is the most common.
DEFAULT_SSH_KEY_FILE = HOME / ".ssh" / "id_rsa.pub"

# On disk format
TOKEN_VERSION = 1

WAITING_PAYMENT_TO_PROCESS = "Waiting for payment to process..."


def get_api_endpoint() -> str:
    from .api_client import CLEARNET_ENDPOINT, TOR_ENDPOINT

    api_endpoint = os.getenv("SPORESTACK_ENDPOINT", CLEARNET_ENDPOINT)
    if os.getenv("SPORESTACK_USE_TOR_ENDPOINT", None) is not None:
        api_endpoint = TOR_ENDPOINT
    return api_endpoint


def get_api_client() -> "APIClient":
    from .api_client import APIClient

    return APIClient(api_endpoint=get_api_endpoint())


def make_payment(invoice: "Invoice") -> None:
    import segno

    from ._cli_utils import cents_to_usd

    uri = invoice.payment_uri
    usd = cents_to_usd(invoice.amount)
    expires = epoch_to_human(invoice.expires)

    message = f"""Invoice: {invoice.id}
Invoice expires: {expires} (payment must be confirmed by this time)
Payment URI: {uri}
Pay *exactly* the specified amount. No more, no less.
Resize your terminal and try again if QR code above is not readable.
Press ctrl+c to abort."""
    qr = segno.make(uri)
    # This typer.echos.
    qr.terminal()
    typer.echo(message)
    typer.echo(f"Approximate price in USD: {usd}")
    input("[Press enter once you have made payment.]")


@server_cli.command()
def launch(
    days: Annotated[
        int,
        typer.Option(min=1, max=90, help="Number of days the server should run for."),
    ],
    operating_system: Annotated[str, typer.Option(help="Example: debian-11")],
    hostname: str = "",
    ssh_key_file: Path = DEFAULT_SSH_KEY_FILE,
    flavor: str = DEFAULT_FLAVOR,
    token: str = DEFAULT_TOKEN,
    region: Optional[str] = None,
    quote: bool = typer.Option(True, help="Require manual price confirmation."),
    autorenew: bool = typer.Option(False, help="Automatically renew server."),
    wait: bool = typer.Option(
        True, help="Wait for server to be assigned an IP address."
    ),
) -> None:
    """Launch a server on SporeStack."""
    typer.echo(f"Launching server with token {token}...", err=True)
    _token = load_token(token)

    from . import utils
    from .client import Client

    client = Client(api_client=get_api_client(), client_token=_token)

    typer.echo(f"Loading SSH key from {ssh_key_file}...")
    if not ssh_key_file.exists():
        msg = f"{ssh_key_file} does not exist. "
        msg += "You can try generating a key file with `ssh-keygen`"
        typer.echo(msg, err=True)
        raise typer.Exit(code=1)

    ssh_key = ssh_key_file.read_text()

    machine_id = utils.random_machine_id()

    if quote:
        quote_response = client.server_quote(days=days, flavor=flavor)

        msg = f"Is {quote_response.usd} for {days} day(s) of {flavor} okay?"
        typer.echo(msg, err=True)
        input("[Press ctrl+c to cancel, or enter to accept.]")

    if autorenew:
        typer.echo(
            "Server will be automatically renewed (from this token) to one week of expiration.",  # noqa: E501
            err=True,
        )
        typer.echo(
            "If using this feature, watch your token balance and server expiration closely!",  # noqa: E501
            err=True,
        )

    server = client.token.launch_server(
        machine_id=machine_id,
        days=days,
        flavor=flavor,
        operating_system=operating_system,
        ssh_key=ssh_key,
        region=region,
        hostname=hostname,
        autorenew=autorenew,
    )

    if wait:
        tries = 360
        while tries > 0:
            response = server.info()
            if response.ipv4 != "":
                break
            typer.echo("Waiting for server to build...", err=True)
            tries = tries + 1
            # Waiting for server to spin up.
            time.sleep(10)

        if response.ipv4 == "":
            typer.echo("Server creation failed, tries exceeded.", err=True)
            raise typer.Exit(code=1)
        else:
            print_machine_info(response)
            return

    print_machine_info(server.info())


@server_cli.command()
def topup(
    hostname: str = "",
    machine_id: str = "",
    days: int = typer.Option(...),
    token: str = DEFAULT_TOKEN,
) -> None:
    """Extend an existing SporeStack server's lifetime."""

    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())

    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)

    _token = load_token(token)

    api_client.server_topup(
        machine_id=machine_id,
        days=days,
        token=_token,
    )

    typer.echo(f"Server topped up for {days} day(s)")


def server_info_path() -> Path:
    # Put servers in a subdirectory
    servers_dir = SPORESTACK_DIR / "servers"

    # Migrate existing server.json files into servers subdirectory
    if (
        SPORESTACK_DIR.exists()
        and not servers_dir.exists()
        and len(list(SPORESTACK_DIR.glob("*.json"))) > 0
    ):
        typer.echo(
            f"Migrating server profiles found in {SPORESTACK_DIR} to {servers_dir}.",
            err=True,
        )
        servers_dir.mkdir()
        for json_file in SPORESTACK_DIR.glob("*.json"):
            json_file.rename(servers_dir / json_file.name)

    # Make it, if it doesn't exist already.
    SPORESTACK_DIR.mkdir(exist_ok=True)
    servers_dir.mkdir(exist_ok=True)

    return servers_dir


def token_path() -> Path:
    token_dir = SPORESTACK_DIR / "tokens"

    # Make it, if it doesn't exist already.
    token_dir.mkdir(exist_ok=True, parents=True)

    return token_dir


def get_machine_info(hostname: str) -> Dict[str, Any]:
    """
    Get info from disk.
    """
    directory = server_info_path()
    json_file = directory / f"{hostname}.json"
    if not json_file.exists():
        raise ValueError(f"{hostname} does not exist in {directory} as {json_file}")
    machine_info = json.loads(json_file.read_bytes())
    assert isinstance(machine_info, dict)
    if machine_info["vm_hostname"] != hostname:
        raise ValueError("hostname does not match filename.")
    return machine_info


def pretty_machine_info(info: Dict[str, Any]) -> str:
    msg = "Machine ID (keep this secret!): {}\n".format(info["machine_id"])
    if "vm_hostname" in info:
        msg += "Hostname: {}\n".format(info["vm_hostname"])
    elif "hostname" in info:
        msg += "Hostname: {}\n".format(info["hostname"])

    if "network_interfaces" in info:
        if "ipv6" in info["network_interfaces"][0]:
            msg += "IPv6: {}\n".format(info["network_interfaces"][0]["ipv6"])
        if "ipv4" in info["network_interfaces"][0]:
            msg += "IPv4: {}\n".format(info["network_interfaces"][0]["ipv4"])
    else:
        if "ipv6" in info:
            msg += "IPv6: {}\n".format(info["ipv6"])
        if "ipv4" in info:
            msg += "IPv4: {}\n".format(info["ipv4"])
    expiration = info["expiration"]
    human_expiration = time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime(expiration))
    if "running" in info:
        msg += "Running: {}\n".format(info["running"])
    msg += f"Expiration: {expiration} ({human_expiration})\n"
    time_to_live = expiration - int(time.time())
    hours = time_to_live // 3600
    msg += f"Server will be deleted in {hours} hours."
    return msg


def epoch_to_human(epoch: int) -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S %z", time.localtime(epoch))


def print_machine_info(info: "api.ServerInfo.Response") -> None:
    if info.hostname != "":
        typer.echo(f"Hostname: {info.hostname}")
    else:
        typer.echo("Hostname: (none) (No hostname set)")

    typer.echo(f"Machine ID (keep this secret!): {info.machine_id}")
    if info.ipv6 != "":
        typer.echo(f"IPv6: {info.ipv6}")
    else:
        typer.echo("IPv6: (Not yet assigned)")
    if info.ipv4 != "":
        typer.echo(f"IPv4: {info.ipv4}")
    else:
        typer.echo("IPv4: (Not yet assigned)")
    typer.echo(f"Region: {info.region}")
    typer.echo(f"Flavor: {info.flavor.slug}")
    typer.echo(f"Expiration: {epoch_to_human(info.expiration)}")
    typer.echo(f"Token (keep this secret!): {info.token}")
    if info.deleted_at != 0 or info.deleted:
        typer.echo("Server was deleted!")
        if info.deleted_at != 0:
            typer.echo(f"Server deleted at: {epoch_to_human(info.deleted_at)}")
        if info.deleted_by is not None:
            typer.echo(f"Server deleted by: {info.deleted_by.value}")
        if info.forgotten_at is not None:
            typer.echo(f"Server forgotten at: {info.forgotten_at}")
    else:
        typer.echo(f"Running: {info.running}")
        time_to_live = info.expiration - int(time.time())
        hours = time_to_live // 3600
        typer.echo(f"Server will be deleted in {hours} hours.")
        typer.echo(f"Autorenew: {info.autorenew}")


@server_cli.command(name="list")
def server_list(
    token: str = DEFAULT_TOKEN,
    local: Annotated[
        bool, typer.Option(help="List older servers not associated to token.")
    ] = True,
    show_forgotten: Annotated[
        bool, typer.Option(help="Show deleted and forgotten servers.")
    ] = False,
) -> None:
    """Lists a token's servers."""
    _token = load_token(token)

    from rich.console import Console
    from rich.table import Table

    from .api_client import APIClient
    from .exceptions import SporeStackUserError

    console = Console(width=None if sys.stdout.isatty() else 10**9)

    table = Table(
        title=f"Servers for {token} ({_token})",
        show_header=True,
        header_style="bold magenta",
        caption=(
            "For more details on a server, run "
            "`sporestack server info --machine-id (machine id)`"
        ),
    )

    api_client = APIClient(api_endpoint=get_api_endpoint())

    server_infos = api_client.servers_launched_from_token(token=_token).servers
    machine_id_hostnames = {}

    if local:
        directory = server_info_path()
        for hostname_json in os.listdir(directory):
            hostname = hostname_json.split(".")[0]
            saved_vm_info = get_machine_info(hostname)
            machine_id_hostnames[saved_vm_info["machine_id"]] = hostname

    printed_machine_ids = []

    table.add_column("Machine ID [bold](Secret!)[/bold]", style="dim")
    table.add_column("Hostname")
    table.add_column("IPv4")
    table.add_column("IPv6")
    table.add_column("Expires At")
    table.add_column("Autorenew")

    for info in server_infos:
        if not show_forgotten and info.forgotten_at is not None:
            continue

        typer.echo()

        hostname = info.hostname
        if hostname == "":
            if info.machine_id in machine_id_hostnames:
                hostname = machine_id_hostnames[info.machine_id]
        info.hostname = hostname

        expiration = epoch_to_human(info.expiration)
        if info.deleted_at:
            expiration = f"[bold]Deleted[/bold] at {epoch_to_human(info.deleted_at)}"

        table.add_row(
            info.machine_id,
            info.hostname,
            info.ipv4,
            info.ipv6,
            expiration,
            str(info.autorenew),
        )

        printed_machine_ids.append(info.machine_id)

    console.print(table)

    if local:
        for hostname_json in os.listdir(directory):
            hostname = hostname_json.split(".")[0]
            saved_vm_info = get_machine_info(hostname)
            machine_id = saved_vm_info["machine_id"]
            if machine_id in printed_machine_ids:
                continue

            try:
                upstream_vm_info = api_client.server_info(
                    machine_id=saved_vm_info["machine_id"]
                )
                saved_vm_info["expiration"] = upstream_vm_info.expiration
                saved_vm_info["running"] = upstream_vm_info.running
                typer.echo()
                typer.echo(pretty_machine_info(saved_vm_info))
            except SporeStackUserError as e:
                expiration = saved_vm_info["expiration"]
                human_expiration = time.strftime(
                    "%Y-%m-%d %H:%M:%S %z", time.localtime(saved_vm_info["expiration"])
                )
                msg = hostname
                msg += f" expired ({expiration} {human_expiration}): "
                msg += str(e)
                typer.echo(msg)

    typer.echo()


def _get_machine_id(machine_id: str, hostname: str, token: str) -> str:
    usage = "--hostname *OR* --machine-id must be set."

    if machine_id != "" and hostname != "":
        typer.echo(usage, err=True)
        raise typer.Exit(code=2)

    if machine_id != "":
        return machine_id

    if hostname == "":
        typer.echo(usage, err=True)
        raise typer.Exit(code=2)

    try:
        machine_id = get_machine_info(hostname)["machine_id"]
        assert isinstance(machine_id, str)
        return machine_id
    except Exception:
        pass

    _token = load_token(token)

    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())

    for server in api_client.servers_launched_from_token(token=_token).servers:
        if server.forgotten_at is not None:
            continue
        if server.hostname == hostname:
            return server.machine_id

    typer.echo(
        f"Could not find any servers matching the hostname: {hostname}", err=True
    )
    raise typer.Exit(code=1)


@server_cli.command(name="info")
def server_info(
    hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN
) -> None:
    """Show information about the server."""
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    print_machine_info(api_client.server_info(machine_id=machine_id))


@server_cli.command(name="json")
def server_info_json(
    hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN
) -> None:
    """Info on the server, in JSON format."""
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    typer.echo(api_client.server_info(machine_id=machine_id).json())


@server_cli.command()
def start(hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN) -> None:
    """
    Boots the VM.
    """
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    api_client.server_start(machine_id=machine_id)
    typer.echo(f"{hostname} started.")


@server_cli.command()
def stop(hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN) -> None:
    """Power off the server. (Not a graceful shutdown)"""
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    api_client.server_stop(machine_id=machine_id)
    typer.echo(f"{hostname} stopped.")


@server_cli.command()
def autorenew_enable(
    hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN
) -> None:
    """Enable autorenew on a server."""
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    api_client.autorenew_enable(machine_id=machine_id)
    typer.echo("Autorenew enabled.")


@server_cli.command()
def autorenew_disable(
    hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN
) -> None:
    """
    Disable autorenew on a server.
    """
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    api_client.autorenew_disable(machine_id=machine_id)
    typer.echo("Autorenew disabled.")


@server_cli.command()
def delete(
    hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN
) -> None:
    """Delete the server before its expiration."""
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    api_client.server_delete(machine_id=machine_id)
    # Also remove the .json file
    server_info_path().joinpath(f"{hostname}.json").unlink(missing_ok=True)
    typer.echo(f"{machine_id} was destroyed.")


@server_cli.command()
def forget(
    hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN
) -> None:
    """Forget about a deleted server so that it doesn't show up in server list."""
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    api_client.server_forget(machine_id=machine_id)
    typer.echo(f"{machine_id} was forgotten.")


@server_cli.command()
def update_hostname(
    machine_id: str,
    hostname: Annotated[str, typer.Option()],
) -> None:
    """Update a server's hostname, given its machine ID."""
    from .client import Server

    server = Server(machine_id=machine_id, api_client=get_api_client())

    current_hostname = server.info().hostname
    server.update(hostname=hostname)
    if current_hostname == "":
        typer.echo(f"{machine_id}'s hostname was set to {hostname}.")
    else:
        typer.echo(
            f"{machine_id}'s hostname was updated from {current_hostname} to "
            f"{hostname}."
        )


@server_cli.command()
def rebuild(
    hostname: str = "", machine_id: str = "", token: str = DEFAULT_TOKEN
) -> None:
    """
    Rebuilds the VM with the operating system and SSH key given at launch time.

    Will take a couple minutes to complete after the request is made.
    """
    machine_id = _get_machine_id(machine_id=machine_id, hostname=hostname, token=token)
    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    api_client.server_rebuild(machine_id=machine_id)
    typer.echo(f"{hostname} rebuilding.")


@server_cli.command()
def flavors() -> None:
    """Shows available flavors."""
    from rich.console import Console
    from rich.table import Table

    from ._cli_utils import cents_to_usd, gb_string, mb_string, tb_string
    from .api_client import APIClient

    console = Console(width=None if sys.stdout.isatty() else 10**9)

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Flavor Slug (--flavor)")
    table.add_column("vCPU Cores")
    table.add_column("Memory")
    table.add_column("Disk")
    table.add_column("Bandwidth (per month)")
    table.add_column("Price per day")
    table.add_column("Price per month (30 days)")

    api_client = APIClient(api_endpoint=get_api_endpoint())
    flavors = api_client.flavors().flavors
    for flavor_slug in flavors:
        flavor = flavors[flavor_slug]
        price_per_30_days = flavor.price * 30
        table.add_row(
            flavor_slug,
            str(flavor.cores),
            mb_string(flavor.memory),
            gb_string(flavor.disk),
            tb_string(flavor.bandwidth_per_month),
            f"[green]{cents_to_usd(flavor.price)}[/green]",
            f"[green]{cents_to_usd(price_per_30_days)}[/green]",
        )

    console.print(table)


@server_cli.command()
def operating_systems() -> None:
    """Show available operating systems."""
    from rich.console import Console
    from rich.table import Table

    from .api_client import APIClient

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    api_client = APIClient(api_endpoint=get_api_endpoint())
    table.add_column("Operating System (--operating-system)")
    os_list = api_client.operating_systems().operating_systems
    for operating_system in os_list:
        table.add_row(operating_system)

    console.print(table)


@server_cli.command()
def regions() -> None:
    """Shows regions that servers can be launched in."""
    from rich.console import Console
    from rich.table import Table

    from .api_client import APIClient

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Region Slug (--region)")
    table.add_column("Region Name")

    api_client = APIClient(api_endpoint=get_api_endpoint())
    regions = api_client.regions().regions
    for region in regions:
        table.add_row(region, regions[region].name)

    console.print(table)


def load_token(token: str) -> str:
    token_file = token_path().joinpath(f"{token}.json")
    if not token_file.exists():
        msg = f"Token '{token}' ({token_file}) does not exist. Create it with:\n"
        msg += f"sporestack token create {token} --dollars 20 --currency xmr\n"
        msg += "(Can do more than $20, or a different currency, like btc.)\n"
        msg += (
            "With the token credited, you can launch servers, renew existing ones, etc."
        )
        typer.echo(msg, err=True)
        raise typer.Exit(code=1)

    token_data = json.loads(token_file.read_text())
    assert token_data["version"] == 1
    assert isinstance(token_data["key"], str)
    return token_data["key"]


def save_token(token: str, key: str) -> None:
    token_file = token_path().joinpath(f"{token}.json")
    if token_file.exists():
        msg = f"Token '{token}' already exists in {token_file}. Aborting!"
        typer.echo(msg, err=True)
        raise typer.Exit(code=1)

    token_data = {"version": TOKEN_VERSION, "name": token, "key": key}
    token_file.write_text(json.dumps(token_data))


@token_cli.command(name="create")
def token_create(
    dollars: Annotated[int, typer.Option()],
    currency: Annotated[str, typer.Option()],
    token: Annotated[str, typer.Argument()] = DEFAULT_TOKEN,
) -> None:
    """
    Enables a new token.

    Dollars is starting balance.
    """
    from httpx import HTTPError

    from . import utils

    _token = utils.random_token()

    typer.echo(f"Generated key {_token} for use with token {token}", err=True)

    if Path(SPORESTACK_DIR / "tokens" / f"{token}.json").exists():
        typer.echo("Token already created! Did you mean to `topup`?", err=True)
        raise typer.Exit(1)

    from .api_client import APIClient
    from .exceptions import SporeStackServerError

    api_client = APIClient(api_endpoint=get_api_endpoint())

    response = api_client.token_add(
        token=_token,
        dollars=dollars,
        currency=currency,
    )

    make_payment(response.invoice)

    tries = 360 * 2
    while tries > 0:
        typer.echo(WAITING_PAYMENT_TO_PROCESS, err=True)
        tries = tries - 1
        # FIXME: Wait two hours in a smarter way.
        # Waiting for payment to set in.
        time.sleep(10)
        try:
            response = api_client.token_add(
                token=_token,
                dollars=dollars,
                currency=currency,
            )
        except (SporeStackServerError, HTTPError):
            typer.echo("Received 500 HTTP status, will try again.", err=True)
            continue
        if response.invoice.paid:
            typer.echo(f"{token} has been enabled with ${dollars}.")
            typer.echo(f"{token}'s key is {_token}.")
            typer.echo("Save it, don't share it, and don't lose it!")
            save_token(token, _token)
            return
    raise ValueError(f"{token} did not get enabled in time.")


@token_cli.command(name="import")
def token_import(
    name: str = typer.Argument(DEFAULT_TOKEN),
    key: str = typer.Option(...),
) -> None:
    """Imports a token under the given name."""
    save_token(name, key)


@token_cli.command(name="topup")
def token_topup(
    token: str = typer.Argument(DEFAULT_TOKEN),
    dollars: int = typer.Option(...),
    currency: str = typer.Option(...),
) -> None:
    """Adds balance to an existing token."""
    token = load_token(token)

    from httpx import HTTPError

    from .api_client import APIClient
    from .exceptions import SporeStackServerError

    api_client = APIClient(api_endpoint=get_api_endpoint())

    response = api_client.token_add(
        token,
        dollars,
        currency=currency,
    )

    make_payment(response.invoice)

    tries = 360 * 2
    while tries > 0:
        typer.echo(WAITING_PAYMENT_TO_PROCESS, err=True)
        tries = tries - 1
        # FIXME: Wait two hours in a smarter way.
        try:
            response = api_client.token_add(
                token=token,
                dollars=dollars,
                currency=currency,
            )
        except (SporeStackServerError, HTTPError):
            typer.echo("Received 500 HTTP status, will try again.", err=True)
            continue
        # Waiting for payment to set in.
        time.sleep(10)
        if response.invoice.paid:
            typer.echo(f"Added {dollars} dollars to {token}")
            return
    raise ValueError(f"{token} did not get enabled in time.")


@token_cli.command()
def balance(token: str = typer.Argument(DEFAULT_TOKEN)) -> None:
    """Shows a token's balance."""
    _token = load_token(token)

    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())

    typer.echo(api_client.token_info(token=_token).balance_usd)


@token_cli.command(name="info")
def token_info(token: Annotated[str, typer.Argument()] = DEFAULT_TOKEN) -> None:
    """
    Show information about a token, including balance.

    Burn Rate is calculated per day of servers set to autorenew.

    Days Remaining is for servers set to autorenew, given the remaining balance.
    """
    _token = load_token(token)

    from rich import print

    from .api_client import APIClient
    from .client import Client

    api_client = APIClient(api_endpoint=get_api_endpoint())
    client = Client(api_client=api_client, client_token=_token)

    info = client.token.info()
    print(f"[bold]Token Information for {token} ({_token})[/bold]")
    print(f"Balance: [green]{info.balance_usd}")
    print(f"Total Servers: {info.servers}")
    print(
        f"Burn Rate: [red]{info.burn_rate_usd}[/red] "
        "(per day of servers set to autorenew)"
    )
    print(
        f"Days Remaining: {info.days_remaining} "
        "(for servers set to autorenew, given the remaining balance)"
    )


@token_cli.command()
def servers(token: Annotated[str, typer.Argument()] = DEFAULT_TOKEN) -> None:
    """Returns server info for servers launched by a given token."""
    _token = load_token(token)

    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())

    typer.echo(api_client.servers_launched_from_token(token=_token))


@token_cli.command(name="list")
def token_list() -> None:
    """List tokens."""
    from rich.console import Console
    from rich.table import Table

    console = Console(width=None if sys.stdout.isatty() else 10**9)

    token_dir = token_path()
    table = Table(
        show_header=True,
        header_style="bold magenta",
        caption=f"These tokens are stored in {token_dir}",
    )
    table.add_column("Name")
    table.add_column("Token (this is a globally unique [bold]secret[/bold])")

    for token_file in token_dir.glob("*.json"):
        token = token_file.stem
        key = load_token(token)
        table.add_row(token, key)

    console.print(table)


@token_cli.command(name="invoices")
def token_invoices(token: Annotated[str, typer.Argument()] = DEFAULT_TOKEN) -> None:
    """List invoices."""
    _token = load_token(token)

    from rich.console import Console
    from rich.table import Table

    from ._cli_utils import cents_to_usd
    from .api_client import APIClient
    from .client import Client

    api_client = APIClient(api_endpoint=get_api_endpoint())
    client = Client(api_client=api_client, client_token=_token)

    console = Console(width=None if sys.stdout.isatty() else 10**9)

    table = Table(
        title=f"Invoices for {token} ({_token})",
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("ID")
    table.add_column("Amount")
    table.add_column("Created At")
    table.add_column("Paid At")
    table.add_column("URI")
    table.add_column("TXID")

    for invoice in client.token.invoices():
        if invoice.paid:
            paid = epoch_to_human(invoice.paid)
        else:
            if invoice.expired:
                paid = "[bold]Expired[/bold]"
            else:
                paid = f"Unpaid. Expires: {epoch_to_human(invoice.expires)}"
        table.add_row(
            str(invoice.id),
            cents_to_usd(invoice.amount),
            epoch_to_human(invoice.created),
            paid,
            invoice.payment_uri,
            invoice.txid,
        )

    console.print(table)


@token_cli.command()
def messages(token: str = typer.Argument(DEFAULT_TOKEN)) -> None:
    """Show support messages."""
    token = load_token(token)

    from .api_client import APIClient
    from .client import Client

    api_client = APIClient(api_endpoint=get_api_endpoint())
    client = Client(api_client=api_client, client_token=token)

    for message in client.token.messages():
        typer.echo()
        typer.echo(message.message)
        typer.echo()
        typer.echo(f"Sent at {message.sent_at}, by {message.sender.value}")


@token_cli.command()
def send_message(
    token: str = typer.Argument(DEFAULT_TOKEN), message: str = typer.Option(...)
) -> None:
    """Send a support message."""
    token = load_token(token)

    from .api_client import APIClient
    from .client import Client

    api_client = APIClient(api_endpoint=get_api_endpoint())
    client = Client(api_client=api_client, client_token=token)

    client.token.send_message(message)


@cli.command()
def version() -> None:
    """Returns the installed version."""
    from . import __version__

    typer.echo(__version__)


@cli.command()
def api_changelog() -> None:
    """Shows the API changelog."""
    from rich.console import Console
    from rich.markdown import Markdown

    from .api_client import APIClient

    api_client = APIClient(api_endpoint=get_api_endpoint())
    console = Console()
    console.print(Markdown(api_client.changelog()))


# TODO
# @cli.command()
# def cli_changelog() -> None:
#     """Shows the Python library/CLI changelog."""


@cli.command()
def api_endpoint() -> None:
    """
    Prints the selected API endpoint: Env var: SPORESTACK_ENDPOINT,
    or, SPORESTACK_USE_TOR_ENDPOINT=1
    """
    from . import api_client

    endpoint = get_api_endpoint()
    if ".onion" in endpoint:
        typer.echo(f"{endpoint} using {api_client._get_tor_proxy()}")
        return
    else:
        typer.echo(endpoint)
        return


if __name__ == "__main__":
    cli()
