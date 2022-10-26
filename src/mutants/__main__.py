"""Command-line interface."""
import click


@click.command()
def main() -> None:
    """Mutants."""


if __name__ == "__main__": # pragma: no mutate
    main(prog_name="mutants")  # pragma: no cover no mutate
