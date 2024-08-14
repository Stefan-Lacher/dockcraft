"""this is the unit test for the main pipeline"""

# pylint: disable=W0613

from unittest.mock import patch, MagicMock

from src.DockCraft.main_pipeline import DockCraftPipeline


@patch("os.path.isdir", return_value=True)
@patch("src.DockCraft.main_pipeline.DockerfileReader")
@patch("src.DockCraft.main_pipeline.DockCraftFinder")
def test_pipeline_initialization(
    mock_finder_class: MagicMock, mock_reader_class: MagicMock, mock_isdir: MagicMock
) -> None:
    """
    Test that the DockCraftPipeline initializes correctly and calls the required methods.
    """
    # Setup mocks
    mock_finder_instance = mock_finder_class.return_value
    mock_finder_instance.find_dockerfiles.return_value = ["Dockerfile1", "Dockerfile2"]

    mock_reader_instance = mock_reader_class.return_value

    # Initialize DockCraftPipeline
    DockCraftPipeline(general_path="test_path")

    # Assertions for finder
    mock_finder_class.assert_called_once_with("test_path")
    mock_finder_instance.find_dockerfiles.assert_called_once_with(recursive=True)

    # Assertions for reader
    assert mock_reader_class.call_count == 2
    mock_reader_class.assert_any_call(file_path="Dockerfile1")
    mock_reader_class.assert_any_call(file_path="Dockerfile2")
    mock_reader_instance.print_content.assert_called()


@patch("os.path.isdir", return_value=True)
@patch("src.DockCraft.main_pipeline.DockerfileReader")
@patch("src.DockCraft.main_pipeline.DockCraftFinder")
def test_pipeline_no_dockerfiles(
    mock_finder_class: MagicMock, mock_reader_class: MagicMock, mock_isdir: MagicMock
) -> None:
    """
    Test that the DockCraftPipeline handles the case with no Dockerfiles correctly.
    """
    # Setup mocks
    mock_finder_instance = mock_finder_class.return_value
    mock_finder_instance.find_dockerfiles.return_value = []

    # Initialize DockCraftPipeline
    DockCraftPipeline(general_path="test_path")

    # Assertions for finder
    mock_finder_class.assert_called_once_with("test_path")
    mock_finder_instance.find_dockerfiles.assert_called_once_with(recursive=True)

    # Ensure DockerfileReader is never called
    mock_reader_class.assert_not_called()


@patch("os.path.isdir", return_value=True)
@patch("src.DockCraft.main_pipeline.DockerfileReader")
@patch("src.DockCraft.main_pipeline.DockCraftFinder")
def test_pipeline_multiple_dockerfiles(
    mock_finder_class: MagicMock, mock_reader_class: MagicMock, mock_isdir: MagicMock
) -> None:
    """
    Test that the DockCraftPipeline correctly processes multiple Dockerfiles.
    """
    # Setup mocks
    mock_finder_instance = mock_finder_class.return_value
    mock_finder_instance.find_dockerfiles.return_value = [
        "Dockerfile1",
        "Dockerfile2",
        "Dockerfile3",
    ]

    mock_reader_instance = mock_reader_class.return_value

    # Initialize DockCraftPipeline
    DockCraftPipeline(general_path="test_path")

    # Assertions for finder
    mock_finder_class.assert_called_once_with("test_path")
    mock_finder_instance.find_dockerfiles.assert_called_once_with(recursive=True)

    # Assertions for reader
    assert mock_reader_class.call_count == 3
    mock_reader_class.assert_any_call(file_path="Dockerfile1")
    mock_reader_class.assert_any_call(file_path="Dockerfile2")
    mock_reader_class.assert_any_call(file_path="Dockerfile3")
    assert mock_reader_instance.print_content.call_count == 3
