def validate_amount(amount: float) -> float:

    if amount <= 0:
        raise ValueError(
            "Amount must be greater than zero."
        )

    return round(amount, 2)