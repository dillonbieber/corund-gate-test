import pytest
from calc import discount


def test_discount_rejects_a_percentage_over_100():
    with pytest.raises(ValueError):
        discount(1000, 150)
