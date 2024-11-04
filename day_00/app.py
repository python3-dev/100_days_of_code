"""Main application."""


def is_valid(number_: int | str, check_digit: int | str | None = None) -> bool:
    """Check whether number_ is valid.

    Implementation of Luhn's algorithm.

    Parameters
    ----------
    number_ : int | str
        Input number.

    check_digit : int | str | None
        Check digit.

    Returns
    -------
    bool
        Return True if valid.

    Raises
    ------
    ValueError
        If input is not a number.

    """
    condensed_number: str = str(number_).strip().replace(" ", "")
    if not condensed_number.isdigit():
        raise ValueError

    if check_digit is None:
        check_digit = int(condensed_number[-1])
        payload: str = condensed_number[:-1]
    else:
        check_digit = int(check_digit)
        payload = condensed_number

    if len(payload) < 2:
        return False

    payload_sum: int = get_checksum(payload)

    return (10 - (payload_sum % 10)) % 10 == check_digit


def get_checksum(payload_: str) -> int:
    """Get checksum.

    Parameters
    ----------
    payload_ : str
        Payload string.

    Returns
    -------
    int
        Payload sum.

    """
    payload_sum: int = 0

    for index, digit_ in enumerate(payload_[::-1]):
        digit = int(digit_)
        if index % 2 == 0:
            if digit < 5:
                payload_sum += digit * 2
            else:
                payload_sum += (digit - 5) * 2 + 1
        else:
            payload_sum += digit

    return payload_sum
