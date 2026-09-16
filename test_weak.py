from calc import discount


def test_discount_returns_an_integer():
    assert isinstance(discount(1000, 10), int)
