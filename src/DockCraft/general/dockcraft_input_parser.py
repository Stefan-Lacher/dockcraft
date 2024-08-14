"""
the dockcraft_input_parser module provides a class for parsing
"""

import argparse
from typing import List, Optional


class InputParser:
    """A class to handle command-line argument parsing for DockCraft."""

    def __init__(self, args: Optional[List[str]] = None) -> None:
        """
        Initializes the InputParser with optional command-line arguments.

        Parameters
        ----------
        args : List[str], optional
            A list of arguments to parse. If None, defaults to sys.argv.

        Returns
        -------
        None
        """
        self.args = args
        self.parser = argparse.ArgumentParser(
            description="DockCraft - A tool for Dockerfile management"
        )
        self._add_arguments()

    def _add_arguments(self) -> None:
        """Defines and adds command-line arguments to the parser."""
        self.parser.add_argument(
            "-p",
            "--path",
            type=str,
            default=".",
            help="The path to the directory containing Dockerfiles (default is current directory).",
        )
        self.parser.add_argument(
            "-r",
            "--recursive",
            action="store_true",
            help="Search for Dockerfiles recursively in subdirectories.",
        )
        self.parser.add_argument(
            "-v", "--verbose", action="store_true", help="Enable verbose output."
        )

    def parse(self) -> argparse.Namespace:
        """
        Parses the command-line arguments.

        Returns
        -------
        argparse.Namespace
            An object containing the parsed command-line arguments.
        """
        return self.parser.parse_args(self.args)


if __name__ == "__main__": # pragma: no cover
    input_parser = InputParser()
    parsed_args = input_parser.parse()
    print(parsed_args)
    print(parsed_args.path)
    print(parsed_args.recursive)
    print(parsed_args.verbose)
