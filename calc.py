def discount(total_cents: int, percent_off: int) -> int:
    return total_cents - (total_cents * percent_off) // 100
