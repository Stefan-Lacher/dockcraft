"""this is the unit test for dockcraft_file_finder.py"""

# pylint: disable=R0801

from typing import Any
import pytest
from src.DockCraft.general.dockcraft_file_finder import DockCraftFinder


def test_find_dockerfiles(tmp_path: Any) -> None:
    """
    Test that the DockCraftFinder correctly
    identifies Dockerfiles in a directory.
    """
    # Setup: create a temporary directory with a few files
    dockerfile_path = tmp_path / "Dockerfile"
    dockerfile_path.touch()

    other_file_path = tmp_path / "not_a_dockerfile.txt"
    other_file_path.touch()

    # Test finding Dockerfiles
    finder = DockCraftFinder(str(tmp_path))
    dockerfiles = finder.find_dockerfiles()

    assert len(dockerfiles) == 1
    assert dockerfiles[0] == str(dockerfile_path)


def test_find_dockerfiles_recursive(tmp_path: Any) -> None:
    """
    Test that the DockCraftFinder correctly
    identifies Dockerfiles in a directory and its subdirectories.
    """
    # Setup: create a temporary directory with subdirectories and Dockerfiles
    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()

    dockerfile_path_1 = tmp_path / "Dockerfile"
    dockerfile_path_1.touch()

    dockerfile_path_2 = sub_dir / "Dockerfile"
    dockerfile_path_2.touch()

    # Test finding Dockerfiles recursively
    finder = DockCraftFinder(str(tmp_path))
    dockerfiles = finder.find_dockerfiles(recursive=True)

    assert len(dockerfiles) == 2
    assert str(dockerfile_path_1) in dockerfiles
    assert str(dockerfile_path_2) in dockerfiles


def test_dockerfile_finder_not_a_directory() -> None:
    """
    This test verifies that DockCraftFinder raises a NotADirectoryError
    when the provided path is not a valid directory.
    """
    # Assume 'some_file.txt' is a path to a file, not a directory
    file_path = "some_file.txt"

    # Using pytest.raises to check for the exception
    with pytest.raises(
        NotADirectoryError, match=f"The path {file_path} is not a valid directory."
    ):
        DockCraftFinder(file_path)
