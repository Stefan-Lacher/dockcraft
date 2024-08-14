"""this is the integration test for the dockcraft file finder module"""

# pylint: disable=R1729, R0801

from typing import Any
import os
import pytest
from src.DockCraft.general.dockcraft_file_finder import DockCraftFinder


def test_find_single_dockerfile(tmp_path: Any) -> None:
    """
    Test finding a single Dockerfile in a directory.
    """
    # Setup: create a single Dockerfile in the temp directory
    dockerfile_path = tmp_path / "Dockerfile"
    dockerfile_path.touch()

    finder = DockCraftFinder(str(tmp_path))
    dockerfiles = finder.find_dockerfiles()

    # Verify that the Dockerfile is found
    assert len(dockerfiles) == 1
    assert dockerfiles[0] == str(dockerfile_path)


def test_find_multiple_dockerfiles_in_subdirs(tmp_path: Any) -> None:
    """
    Test finding multiple Dockerfiles in nested subdirectories with recursion.
    """
    # Setup: create a directory structure with Dockerfiles in subdirectories
    sub_dir_1 = tmp_path / "subdir1"
    sub_dir_1.mkdir()
    dockerfile_path_1 = sub_dir_1 / "Dockerfile"
    dockerfile_path_1.touch()

    sub_dir_2 = tmp_path / "subdir2"
    sub_dir_2.mkdir()
    dockerfile_path_2 = sub_dir_2 / "Dockerfile"
    dockerfile_path_2.touch()

    finder = DockCraftFinder(str(tmp_path))
    dockerfiles = finder.find_dockerfiles(recursive=True)

    # Verify that both Dockerfiles are found
    assert len(dockerfiles) == 2
    assert str(dockerfile_path_1) in dockerfiles
    assert str(dockerfile_path_2) in dockerfiles


def test_find_no_dockerfiles(tmp_path: Any) -> None:
    """
    Test that no Dockerfiles are found in an empty directory.
    """
    finder = DockCraftFinder(str(tmp_path))
    dockerfiles = finder.find_dockerfiles()

    # Verify that no Dockerfiles are found
    assert len(dockerfiles) == 0


def test_find_dockerfile_non_directory(tmp_path: Any) -> None:
    """
    Test that DockCraftFinder raises NotADirectoryError when given a non-directory path.
    """
    # Setup: create a regular file instead of a directory
    file_path = tmp_path / "not_a_directory.txt"
    file_path.touch()

    with pytest.raises(
        NotADirectoryError, match=f"The path {file_path} is not a valid directory."
    ):
        DockCraftFinder(str(file_path))


def test_find_dockerfile_with_defined_path() -> None:
    """
    Test finding a Dockerfile with a defined path.
    """
    # Setup: create a Dockerfile in a specific directory
    test_dir = "src/tests/integration/test_data"

    finder = DockCraftFinder(test_dir)
    dockerfiles = finder.find_dockerfiles()

    # Verify that the Dockerfile is found
    assert len(dockerfiles) == 4
    assert all([os.path.isfile(dockerfile) for dockerfile in dockerfiles])
    assert all([dockerfile.startswith(test_dir) for dockerfile in dockerfiles])

    defined_dockerfile_list = [
        "src/tests/integration/test_data/DockerfileNewLines",
        "src/tests/integration/test_data/DockerfileStandard",
        "src/tests/integration/test_data/DockerfileSpacesBefore",
        "src/tests/integration/test_data/DockerfileSpacesAfter",
    ]

    for found_dockerfile in dockerfiles:
        assert found_dockerfile in defined_dockerfile_list
