"""
Log into Nextstrain.org and save credentials for later use.

The first time you log in, you'll be prompted for your Nextstrain.org username
and password.  After that, locally-saved authentication tokens will be used and
automatically renewed as needed when you run other `nextstrain` commands
requiring log in.  You can also re-run this `nextstrain login` command to force
renewal if you want.  You'll only be prompted for your username and password if
the locally-saved tokens are unable to be renewed or missing entirely.

If you log out of Nextstrain.org on other devices/clients (like your web
browser), you may be prompted to re-enter your username and password by this
command sooner than usual.

Your password itself is never saved locally.
"""
from functools import partial
from getpass import getpass
from inspect import cleandoc
from os import environ
from ..authn import current_user, login, renew
from ..errors import UserError


getuser = partial(input, "Username: ")


def register_parser(subparser):
    parser = subparser.add_parser("login", help = "Log into Nextstrain.org")

    parser.add_argument(
        "--username", "-u",
        metavar = "<name>",
        help    = "The username to log in as.  If not provided, the :envvar:`NEXTSTRAIN_USERNAME`"
                  " environment variable will be used if available, otherwise you'll be"
                  " prompted to enter your username.",
        default = environ.get("NEXTSTRAIN_USERNAME"))

    parser.add_argument(
        "--no-prompt",
        help    = "Never prompt for a username/password;"
                  " succeed only if there are login credentials in the environment or"
                  " existing valid/renewable tokens saved locally, otherwise error. "
                  " Useful for scripting.",
        action  = 'store_true')

    parser.add_argument(
        "--renew",
        help    = "Renew existing tokens, if possible. "
                  " Useful to refresh group membership information (for example) sooner"
                  " than the tokens would normally be renewed.",
        action  = "store_true")

    parser.epilog = cleandoc("""
        For automation purposes, you may opt to provide environment variables instead
        of interactive input and/or command-line options:

        .. envvar:: NEXTSTRAIN_USERNAME

            Username on nextstrain.org.  Ignored if :option:`--username` is also
            provided.

        .. envvar:: NEXTSTRAIN_PASSWORD

            Password for nextstrain.org user.  Required if :option:`--no-prompt` is
            used without existing valid/renewable tokens.
        """)

    return parser


def run(opts):
    if opts.renew:
        user = renew()
        if not user:
            raise UserError("Renewal failed or not possible.  Please login again.")
        return

    user = current_user()

    if not user:
        username = opts.username
        password = environ.get("NEXTSTRAIN_PASSWORD")

        if opts.no_prompt and (username is None or password is None):
            raise UserError("No Nextstrain.org credentials found and --no-prompt prevents interactive login.")

        print("Logging into Nextstrain.org…")
        print()

        if username is not None:
            print(f"Username: {username}")
        else:
            username = prompt(getuser)

        if password is not None:
            print("Password: (from environment)")
        else:
            password = prompt(getpass)

        print()

        user = login(username, password)
        print()
    else:
        if opts.username is not None and opts.username != user.username:
            raise UserError(f"""
                Login requested for {opts.username}, but {user.username} is already logged in.
                
                Please logout first if you want to switch users.
                """)

    print(f"Logged into nextstrain.org as {user.username}.")
    print("Log out with `nextstrain logout`.")


def prompt(prompter):
    try:
        return prompter()
    except (EOFError, KeyboardInterrupt):
        print()
        raise UserError("Aborted by user input")
