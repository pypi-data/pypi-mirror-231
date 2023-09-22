import logging

import click

import crumbcutter


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("username_gistname_pair", metavar="<username>/<gist_description>")
@click.option(
    "-o",
    "--output-dir",
    default=".",
    type=click.Path(),
    show_default=True,
    help="Directory where file will render to. Defaults to current directory.",
)
@click.option("--no-input", "-x", is_flag=True, help="eXtremely fast rendering. No user input. Use default values.")
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Verbose output for debugging.",
)
@click.version_option(version="1.0.0", prog_name="crumbcutter")
def cli(username_gistname_pair: str, output_dir: str, no_input: bool, verbose: bool):
    """
    crumbcutter

        template a single-file GitHub gist

    - Template ONE gist file
    - Nothing else!
    - Optional `crumbcutter.json` for default values

    Use cookiecutter for more than one file.

    Given a GitHub username and gist name,
    crumbcutter fetches the gist, prompts for required inputs,
    and renders the template. The file is saved to a specified
    directory or current working directory if none specified.

    Usage:

        crumbcutter <username>/<gist-name>
        crumbcutter octocat/crumbcutter-file
    """
    if verbose:
        click.echo("Running in verbose mode...")
        logging.basicConfig(level=logging.DEBUG)
    try:
        crumbcutter.main(username_gistname_pair, output_dir, no_input)
    except ValueError:
        click.echo("Invalid format for <username>/<gist_description>.")
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        if verbose:
            logging.exception("Detailed error:")


if __name__ == "__main__":
    cli()
