"""this is the unit test for the main pipeline"""

from src.DockCraft.main_pipeline import DockCraftPipeline


def test_dockcraft_pipeline() -> None:
    """this test tests the main pipeline"""
    pipeline = DockCraftPipeline()
    assert pipeline is not None
