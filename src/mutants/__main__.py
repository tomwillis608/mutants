"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Mutants."""


if __name__ == "__main__":
    main(prog_name="mutants")  # pragma: no cover
