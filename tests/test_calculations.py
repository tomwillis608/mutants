from mutants.calculations import calculate_metric
from mutants.calculations import choose_metric

def test_calculate_metric_happy() -> None:
    """Test calculate_metric happy path."""
    result = calculate_metric()
    assert result == 2

def test_chose_metric_happy() -> None:
    """Test choose_metric happy path."""
    result = choose_metric()
    assert result == 21

def test_calculate_metric_8_8() -> None:
    """Test calculate_metric path."""
    result = calculate_metric(8, 8)
    assert result == 2

def test_chose_metric_10() -> None:
    """Test choose_metric path."""
    result = choose_metric(1, 2)
    assert result == 10
