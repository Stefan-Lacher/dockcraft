"""this is the test mock for integration tests"""

import os
from src.DockCraft.general.dockcraft_reader import DockerfileReader


def test_dockcraft_reader() -> None:
    """
    This test verifies that the DockerfileReader correctly reads and returns
    the content of a standard Dockerfile.
    """
    # Ensure the path to the Dockerfile is correct relative to the current test directory
    file_path = "src/tests/integration/test_data/DockerfileStandard"

    # Verify that the test data file exists before proceeding
    assert os.path.exists(file_path), f"Test Dockerfile {file_path} does not exist."

    # Create an instance of DockerfileReader and read the content
    reader = DockerfileReader(file_path)
    content = reader.get_content()

    # Expected content from the DockerfileStandard
    expected_content = [
        "FROM ubuntu:18.04\n",
        "\n",
        "RUN apt-get update && apt-get install -y curl\n",
    ]

    # Verify that the content read matches the expected content
    assert (
        content == expected_content
    ), "The content read from the Dockerfile does not match the expected content."


def test_dockcraft_reader_new_lines() -> None:
    """
    This test verifies that the DockerfileReader correctly reads and returns
    the content of a Dockerfile with a lot of new lines.
    """
    # Ensure the path to the Dockerfile is correct relative to the current test directory
    file_path = "src/tests/integration/test_data/DockerfileNewLines"

    # Verify that the test data file exists before proceeding
    assert os.path.exists(file_path), f"Test Dockerfile {file_path} does not exist."

    # Create an instance of DockerfileReader and read the content
    reader = DockerfileReader(file_path)
    content = reader.get_content()

    # Expected content from the DockerfileStandard
    expected_content = [
        "FROM ubuntu:18.04\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "RUN apt-get update && apt-get install -y curl\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
    ]

    # Verify that the content read matches the expected content
    assert (
        content == expected_content
    ), "The content read from the Dockerfile does not match the expected content."


def test_dockcraft_reader_spaces_after() -> None:
    """
    This test verifies that the DockerfileReader correctly reads and returns
    the content of a Dockerfile with a lot of spaces.
    """
    # Ensure the path to the Dockerfile is correct relative to the current test directory
    file_path = "src/tests/integration/test_data/DockerfileSpacesAfter"

    # Verify that the test data file exists before proceeding
    assert os.path.exists(file_path), f"Test Dockerfile {file_path} does not exist."

    # Create an instance of DockerfileReader and read the content
    reader = DockerfileReader(file_path)
    content = reader.get_content()

    # Expected content from the DockerfileStandard
    expected_content = [
        "FROM ubuntu:18.04                              \n",
        "                  \n",
        "RUN apt-get update && apt-get install -y curl                      \n",
        "                  ",
    ]

    # Verify that the content read matches the expected content
    assert (
        content == expected_content
    ), "The content read from the Dockerfile does not match the expected content."


def test_dockcraft_reader_spaces_before() -> None:
    """
    This test verifies that the DockerfileReader correctly reads and returns
    the content of a Dockerfile with a lot of spaces.
    """
    # Ensure the path to the Dockerfile is correct relative to the current test directory
    file_path = "src/tests/integration/test_data/DockerfileSpacesBefore"

    # Verify that the test data file exists before proceeding
    assert os.path.exists(file_path), f"Test Dockerfile {file_path} does not exist."

    # Create an instance of DockerfileReader and read the content
    reader = DockerfileReader(file_path)
    content = reader.get_content()

    # Expected content from the DockerfileStandard
    expected_content = [
        "                              FROM ubuntu:18.04\n",
        "                              \n",
        "                              RUN apt-get update && apt-get install -y curl\n",
        "                              ",
    ]

    # Verify that the content read matches the expected content
    assert (
        content == expected_content
    ), "The content read from the Dockerfile does not match the expected content."
