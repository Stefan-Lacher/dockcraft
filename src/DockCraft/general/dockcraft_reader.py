"""
this module is responsible for reading the dockerfile 
and returning the data in a usable format
"""

import os
from typing import List


class DockerfileReader:
    """the class responsible for reading the Dockerfile"""

    def __init__(self, file_path: str) -> None:
        """
        Initializes the DockerfileReader with the path to the Dockerfile.

        Parameters
        ----------
        file_path : str
            Path to the Dockerfile.

        Returns
        -------
        None

        Raises
        ------
        FileNotFoundError
            If the file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")

        self.file_path = file_path
        self.content = self._read_dockerfile()

    def _read_dockerfile(self) -> List[str]:
        """
        Reads the Dockerfile and returns its content.

        Parameters
        ----------
        None

        Returns
        -------
        List of lines in the Dockerfile.
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
        return content

    def get_content(self) -> List[str]:
        """
        Returns the content of the Dockerfile.

        Parameters
        ----------
        None

        Returns
        -------
        List of lines in the Dockerfile.
        """
        return self.content

    def print_content(self) -> None:
        """
        Prints the content of the Dockerfile.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for line in self.content:
            print(line, end="")


if __name__ == "__main__":  # pragma: no cover
    reader = DockerfileReader("src/tests/integration/test_data/DockerfileStandard")
    reader.print_content()
