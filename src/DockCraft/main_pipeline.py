"""this is the main pipeline for DockCraft"""

# pylint: disable=R0903, W0107

from typing import List

from .general import DockerfileReader, DockCraftFinder


class DockCraftPipeline:
    """the main pipeline for DockCraft"""

    def __init__(self, general_path: str = "src") -> None:
        """
        the initializer for the DockCraft pipeline

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.general_path = general_path
        self.dockerfile_path_list = self._prep_dockerfile_finder()
        self._prep_dockerfile_reader(file_path_list=self.dockerfile_path_list)

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
        dockerfile_path_list = finder.find_dockerfiles(recursive=True)
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
            print("\n")
            print("#" * 50)
            print(f"Printing Dockerfile {index + 1} content")
            reader = DockerfileReader(file_path=file)
            reader.print_content()


if __name__ == "__main__":  # pragma: no cover
    DockCraftPipeline(general_path="src/tests/integration/test_data")
