"""this is the main pipeline for DockCraft"""

# pylint: disable=R0903, W0107, W1203

import logging
import argparse
from typing import List

from .general import DockerfileReader, DockCraftFinder, InputParser


class DockCraftPipeline:
    """the main pipeline for DockCraft"""

    def __init__(self, general_path: str = ".") -> None:
        """
        the initializer for the DockCraft pipeline

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.parsed_args = self._prep_input_parser()
        if general_path != ".":
            self.general_path = general_path
        else:
            self.general_path = self.parsed_args.path

        self.verbose = self.parsed_args.verbose
        self.recursive = self.parsed_args.recursive
        self._prep_logging()

        self.dockerfile_path_list = self._prep_dockerfile_finder()
        self._prep_dockerfile_reader(file_path_list=self.dockerfile_path_list)

    def _prep_input_parser(self) -> argparse.Namespace:
        """
        the method to prepare the InputParser

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        input_parser = InputParser()
        parsed_args = input_parser.parse()
        return parsed_args

    def _prep_logging(self) -> None:
        """
        the method to prepare the logging

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        log_level = logging.DEBUG if self.verbose else logging.INFO
        logging.basicConfig(
            format="%(asctime)s.%(msecs)03d [%(name)s] %(levelname)s %(filename)s - %(message)s",
            datefmt="%H:%M:%S",
            level=log_level,
            handlers=[logging.StreamHandler()],
        )

    def _prep_dockerfile_finder(self) -> List[str]:
        """
        the method to prepare the DockCraftFinder

        Parameters
        ----------
        directory : str
            the directory to search for Dockerfiles

        Returns
        -------
        None
        """
        finder = DockCraftFinder(self.general_path)
        dockerfile_path_list = finder.find_dockerfiles(recursive=self.recursive)
        return dockerfile_path_list

    def _prep_dockerfile_reader(self, file_path_list: List[str]) -> None:
        """
        the method to prepare the DockerfileReader

        Parameters
        ----------
        file_path : str
            the path to the Dockerfile

        Returns
        -------
        None
        """
        for index, file in enumerate(file_path_list):
            logging.debug("\n")
            logging.debug("#" * 50)
            logging.debug(f"Printing Dockerfile {index + 1} | {file} content")
            reader = DockerfileReader(file_path=file)
            reader.print_content()


if __name__ == "__main__":  # pragma: no cover
    DockCraftPipeline()
