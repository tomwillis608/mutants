from mutants.calculations import calculate_metric
from mutants.calculations import choose_metric
from mutants.calculations import METRIC_LOC
from mutants.calculations import METRIC_MTTR

def test_calculate_metric_happy() -> None:
    """Test calculate_metric happy path."""
    result = calculate_metric()
    assert result is not None

def test_calculate_metric_8_8() -> None:
    """Test calculate_metric path."""
    result = calculate_metric(88, 88)
    assert result > 0

def test_chose_metric_mttr() -> None:
    """Test choose_metric happy path."""
    result = choose_metric(1,1)
    assert result == METRIC_MTTR


def test_chose_metric_loc() -> None:
    """Test choose_metric happy path."""
    result = choose_metric(1,2)
    assert result != METRIC_MTTR





