import typer

from .dataAcquisition import dataAcquisition
from .dataAcquisition import test


app = typer.Typer()
app.command()(dataAcquisition)


if __name__ == "__main__":
    app()
    #typer.run()
# python -m src.main   <-- use this script on command line