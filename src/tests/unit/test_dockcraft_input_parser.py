"""the test module for the InputParser class in the DockCraft package."""

from src.DockCraft.general.dockcraft_input_parser import InputParser


def test_default_arguments() -> None:
    """Test that the default arguments are set correctly."""
    parser = InputParser(args=[])
    parsed_args = parser.parse()

    assert parsed_args.path == "."
    assert parsed_args.recursive is False
    assert parsed_args.verbose is False


def test_custom_path_argument() -> None:
    """Test that a custom path argument is parsed correctly."""
    parser = InputParser(args=["--path", "/custom/path"])
    parsed_args = parser.parse()

    assert parsed_args.path == "/custom/path"
    assert parsed_args.recursive is False
    assert parsed_args.verbose is False


def test_recursive_flag() -> None:
    """Test that the recursive flag is parsed correctly."""
    parser = InputParser(args=["--recursive"])
    parsed_args = parser.parse()

    assert parsed_args.path == "."
    assert parsed_args.recursive is True
    assert parsed_args.verbose is False


def test_verbose_flag() -> None:
    """Test that the verbose flag is parsed correctly."""
    parser = InputParser(args=["--verbose"])
    parsed_args = parser.parse()

    assert parsed_args.path == "."
    assert parsed_args.recursive is False
    assert parsed_args.verbose is True


def test_all_arguments() -> None:
    """Test that all arguments are parsed correctly together."""
    parser = InputParser(args=["--path", "/custom/path", "--recursive", "--verbose"])
    parsed_args = parser.parse()

    assert parsed_args.path == "/custom/path"
    assert parsed_args.recursive is True
    assert parsed_args.verbose is True


def test_short_flags() -> None:
    """Test that short flags are parsed correctly."""
    parser = InputParser(args=["-p", "/custom/path", "-r", "-v"])
    parsed_args = parser.parse()

    assert parsed_args.path == "/custom/path"
    assert parsed_args.recursive is True
    assert parsed_args.verbose is True
