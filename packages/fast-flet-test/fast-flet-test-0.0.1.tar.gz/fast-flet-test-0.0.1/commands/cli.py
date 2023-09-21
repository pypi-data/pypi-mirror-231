import typer
import os
import shutil
from rich import print
from pathlib import Path
from typing_extensions import Annotated


def _copy_struct(my_path: str):
    path_struct = Path(__file__).parent
    struct = path_struct / my_path

    pwd = Path.cwd()

    for item in struct.iterdir():
        print(f"[green]> 'test' {item} [/green]> ")
        try:
            if item.is_file():
                shutil.copy(item, pwd)
            elif item.is_dir():        
                shutil.copytree(item, pwd / item.name)
        except:
            pass

    print(
        f"[green]> Initializing project: [/green]")
    for folder in os.listdir(str(struct)+"/app"):
        print(f"[bold green] - {folder} [/bold green] created")
    print(f"[blue]● It has finished correctly.[/blue]")


cli_app = typer.Typer()

@cli_app.command()
def version():
    print('[bold green]version:[/bold green] 0.0.1 [green]beta[/green]')


struct_app = typer.Typer()
cli_app.add_typer(struct_app, name='init', help="Enter the --help argument to obtain more information.")

# mvc
@struct_app.command(help='Create a structure: [views,controllers,models]')
def mvc(_async: Annotated[bool, typer.Option("--async")] = False):
    if _async:
        _copy_struct("templates/mvc_async")
    else:
        _copy_struct("templates/mvc")

# app
@struct_app.command(help='Create a structure: app.py [views]')
def app(_async: Annotated[bool, typer.Option("--async")] = False):
    if _async:
        _copy_struct("templates/personalized_async")
    else:
        _copy_struct("templates/personalized")

cli = cli_app
if __name__ == "__main__":
    cli()
