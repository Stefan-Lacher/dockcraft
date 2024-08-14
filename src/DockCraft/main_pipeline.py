"""this is the main pipeline for DockCraft"""

# pylint: disable=R0903, W0107

from .general import DockerfileReader


class DockCraftPipeline:
    """the main pipeline for DockCraft"""

    def __init__(self) -> None:
        """
        the initializer for the DockCraft pipeline

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        pass

    def _prep_dockerfile_reader(self, file_path: str) -> None:
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
        reader = DockerfileReader(file_path=file_path)
        reader.print_content()
