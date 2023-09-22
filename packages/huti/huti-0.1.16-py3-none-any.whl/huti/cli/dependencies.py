"""
huti.cli.app Module
"""
import typer
from rich import print

import huti.functions

app = typer.Typer(add_completion=False, context_settings={'help_option_names': ['-h', '--help']},
                  name="requirements")


@app.command()
def dependencies(install: bool = True, upgrade: bool = False, extras: list[str] = typer.Option([])):  # noqa: B008
    """
    List or install dependencies for a package from pyproject.toml, project directory (using pyproject.toml)
            or package name. If package name will search on Distribution
    """
    extras = True if extras == [] else extras
    deps = huti.functions.dependencies(install=install, upgrade=upgrade, extras=extras)
    if not install or not upgrade:
        print(deps)
