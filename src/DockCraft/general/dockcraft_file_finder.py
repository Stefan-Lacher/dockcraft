"""
this module is responsible for finding the Dockerfiles in the specified directory
"""

# pylint: disable=R0903

import logging
import os
from typing import List


class DockCraftFinder:
    """A class responsible for finding Dockerfiles in a given directory."""

    def __init__(self, directory_path: str) -> None:
        """
        Initializes the DockerfileFinder with the path to the directory.

        Parameters
        ----------
        directory_path : str
            Path to the directory to search for Dockerfiles.

        Returns
        -------
        None

        Raises
        ------
        NotADirectoryError
            If the provided path is not a directory.
        """
        if not os.path.isdir(directory_path):
            raise NotADirectoryError(
                f"The path {directory_path} is not a valid directory."
            )
        logging.debug(f"Initializing DockerfileFinder with directory: {directory_path}")
        self.directory_path = directory_path

    def find_dockerfiles(self, recursive: bool = False) -> List[str]:
        """
        Finds Dockerfiles in the specified directory.

        Parameters
        ----------
        recursive : bool, optional
            Whether to search recursively through subdirectories (default is False).

        Returns
        -------
        List of paths to Dockerfiles found in the directory.
        """
        dockerfile_list = []
        for root, _, files in os.walk(self.directory_path):
            for file in files:
                logging.debug(f"Checking file: {file}")
                if (
                    file == "Dockerfile"
                    or file == "dockerfile"
                    or file.startswith("Dockerfile")
                ):
                    dockerfile_list.append(os.path.join(root, file))
                    logging.info("Found Dockerfile: %s", os.path.join(root, file))
            if not recursive:
                break
        logging.info(f"Found {len(dockerfile_list)} Dockerfiles")
        return dockerfile_list


if __name__ == "__main__":  # pragma: no cover
    DEFINED_DIRECTORY = "src"
    finder = DockCraftFinder(directory_path=DEFINED_DIRECTORY)

    # Find Dockerfiles without searching subdirectories
    dockerfiles = finder.find_dockerfiles()
    print("Dockerfiles found:", dockerfiles)

    # Find Dockerfiles, including those in subdirectories
    dockerfiles_recursive = finder.find_dockerfiles(recursive=True)
    print("Dockerfiles found (recursive):", dockerfiles_recursive)
