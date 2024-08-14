"""the unit test for the dockcraft reader"""

# pylint: disable=W0613

from unittest.mock import mock_open, patch, MagicMock
import logging
import pytest

from src.DockCraft.general.dockcraft_reader import DockerfileReader


# Test for the __init__ method
def test_dockerfile_reader_file_not_found() -> None:
    """this test tests the case where the file does not exist"""
    with pytest.raises(FileNotFoundError):
        DockerfileReader("non_existent_file")


# Corrected patch targets
@patch("src.DockCraft.general.dockcraft_reader.os.path.exists", return_value=True)
@patch(
    "src.DockCraft.general.dockcraft_reader.open",
    new_callable=mock_open,
    read_data="FROM python:3.8\nRUN pip install pytest",
)
def test_dockerfile_reader_reading_file(
    mock_open_: MagicMock, mock_exists: MagicMock
) -> None:
    """this test tests the case where the file exists"""
    reader = DockerfileReader("dummy_path")

    # Check that the file was attempted to be read
    mock_open_.assert_called_once_with("dummy_path", "r", encoding="utf-8")

    # Check that the content is read correctly
    assert reader.get_content() == ["FROM python:3.8\n", "RUN pip install pytest"]


@patch("src.DockCraft.general.dockcraft_reader.os.path.exists", return_value=True)
@patch(
    "src.DockCraft.general.dockcraft_reader.open",
    new_callable=mock_open,
    read_data="FROM python:3.8\nRUN pip install pytest",
)
def test_dockerfile_reader_get_content(
    mock_open_: MagicMock, mock_exists: MagicMock
) -> None:
    """this test tests the get_content method"""
    reader = DockerfileReader("dummy_path")
    content = reader.get_content()

    assert content == ["FROM python:3.8\n", "RUN pip install pytest"]



@patch("src.DockCraft.general.dockcraft_reader.os.path.exists", return_value=True)
@patch(
    "src.DockCraft.general.dockcraft_reader.open",
    new_callable=mock_open,
    read_data="FROM python:3.8\nRUN pip install pytest",
)
def test_dockerfile_reader_print_content(
    mock_open_: MagicMock, mock_exists: MagicMock, caplog: pytest.LogCaptureFixture
) -> None:
    """this test tests the print_content method"""
    reader = DockerfileReader("dummy_path")
    
    with caplog.at_level(logging.DEBUG):
        reader.print_content()
    
    # Ensure the logging output matches the expected content
    assert "FROM python:3.8" in caplog.text
    assert "RUN pip install pytest" in caplog.text

