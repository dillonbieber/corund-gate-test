def discount(total_cents: int, percent_off: int) -> int:
    """Take percent_off percent off total_cents, flooring the discount."""
    return total_cents - (total_cents * percent_off) // 100
