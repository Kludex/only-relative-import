from typer import Typer, Argument, Option, echo, Exit
from pathlib import Path
from os import devnull
import contextlib
from typing import List

from libcst.codemod import CodemodContext, parallel_exec_transform_with_prettyprint

from only_relative_import.main import OnlyRelativeImportCommand

app = Typer(help="Only allow relative imports! 😅")


@app.command()  # type: ignore[misc]
def main(
    files: List[Path] = Argument(..., help="Files to run the linter on.", exists=True),
    package_name: str = Option(
        ..., help="The name of the package to check for absolute imports."
    ),
) -> None:
    transformer = OnlyRelativeImportCommand(CodemodContext(), package_name=package_name)

    with open(devnull, "w") as null:
        with contextlib.redirect_stderr(null):
            result = parallel_exec_transform_with_prettyprint(
                transformer, [str(file) for file in files], show_successes=True, jobs=1
            )
    if result.failures > 0:
        echo("Found absolute imports!")
        raise Exit(code=1)


if __name__ == "__main__":
    app()
