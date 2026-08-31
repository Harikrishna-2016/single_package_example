"""example_package cli entry point.

TODO: cli docstring
"""

# TODO: this is a starting point for adding CLI functionality.
# if the package does not need a CLI, this file can be removed.
# Otherwise, expand upon this as needed.

import click

import example_package


@click.command()
@click.version_option()
# TODO:template add verbosity mixin
def _cli() -> None:
    example_package.main()


if __name__ == "__main__":
    _cli()
