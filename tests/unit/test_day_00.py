"""Unit tests for day_00."""

import pytest

from day_00.app import get_checksum, is_valid


@pytest.mark.parametrize(
    ("string_", "expected"),
    [
        ("17893729974", True),
        ("5551 0301 4422 3285", True),
        ("5551 0317 8212 1567", True),
        ("5551 0358 7445 1063 ", True),
        (" 5551 0337 0888 8501", True),
        (" 5551 0378 0211 3427 ", True),
        (" 5551 0347 8732 8013 ", True),
        (" 5551 0316 6358 1145 ", True),
        (" 5551 0331 8567 4150 ", True),
        (" 5551 0378 7012 8372 ", True),
        (" 5551 0318 4501 4411 ", True),
        (17893729974, True),
        (5551030144223285, True),
        (5551031782121567, True),
        (5551035874451063, True),
        (5551033708888501, True),
        (5551037802113427, True),
        (5551034787328013, True),
        (5551031663581145, True),
        (5551033185674150, True),
        (5551037870128372, True),
        (5551031845014411, True),
    ],
)
def test_is_valid(string_: str, *, expected: bool) -> None:
    """Test is_valid function."""
    assert is_valid(string_) is expected


@pytest.mark.parametrize(
    ("string_", "check_digit", "expected"),
    [
        ("1789372997", "4", True),
        ("5551 0301 4422 328", "5", True),
        ("5551 0317 8212 156", "7", True),
        ("5551 0358 7445 106 ", "3", True),
        (" 5551 0337 0888 850", "1", True),
        (" 5551 0378 0211 342 ", "7", True),
        (" 5551 0347 8732 801 ", "3", True),
        (" 5551 0316 6358 114 ", "5", True),
        (" 5551 0331 8567 415 ", "0", True),
        (" 5551 0378 7012 837 ", "2", True),
        (" 5551 0318 4501 441 ", "1", True),
        (1789372997, 4, True),
        (555103014422328, 5, True),
        (555103178212156, 7, True),
        (555103587445106, 3, True),
        (555103370888850, 1, True),
        (555103780211342, 7, True),
        (555103478732801, 3, True),
        (555103166358114, 5, True),
        (555103318567415, 0, True),
        (555103787012837, 2, True),
        (555103184501441, 1, True),
    ],
)
def test_is_valid_with_check_digit(
    string_: str, check_digit: str, *, expected: bool
) -> None:
    """Test is_valid function."""
    assert is_valid(string_, check_digit=check_digit) is expected


@pytest.mark.parametrize(
    ("payload", "result"),
    [
        ("1789372997", 56),
        ("5551030144223285", 55),
        ("5551031782121567", 55),
        ("5551035874451063", 64),
        ("5551033708888501", 60),
        ("5551037802113427", 58),
        ("5551034787328013", 63),
        ("5551031663581145", 55),
        ("5551033185674150", 55),
        ("5551037870128372", 70),
        ("5551031845014411", 49),
    ],
)
def test_get_checksum(payload: str, result: int) -> None:
    """Test checksum."""
    assert get_checksum(payload) == result
