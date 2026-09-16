def discount(total_cents: int, percent_off: int) -> int:
    if not 0 <= percent_off <= 100:
        raise ValueError("percent_off must be between 0 and 100")
    return total_cents - (total_cents * percent_off) // 100
