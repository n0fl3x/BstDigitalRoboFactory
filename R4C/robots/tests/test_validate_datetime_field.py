import pytest

from robots.validators import validate_datetime_field


GOOD_CASES = [
    ('2022-09-25 18:43:51', True),
    ('1999-01-01 00:00:00', True),
    ('2023-04-01 23:59:59', True),
]


@pytest.mark.parametrize("datetime_text, exp_result", GOOD_CASES)
def test_validate_datetime_field_good(datetime_text, exp_result):
    assert validate_datetime_field(datetime_text=datetime_text) == exp_result


BAD_CASES = [
    ('2022-09-25 18:43:5', False),
    ('2022-09-25 18:43:', False),
    ('2022-09-25 18:43', False),
    ('2022-99-25 18:43:05', False),
    ('-1998-06-25 18:43:05', False),
    ('1998-06-2518:43:05', False),
    ('1998/06/25 18:43:05', False),
    ('1998-06-33 18:43:05', False),
    ('1998-06-25 78:43:05', False),
    ('1998-06-25 14:98:05', False),
    ('1998-06-25 14:54:87', False),
    ('2259-06-25 14:08:87', False),
]


@pytest.mark.parametrize("datetime_text, exp_result", BAD_CASES)
def test_validate_datetime_field_bad(datetime_text, exp_result):
    assert validate_datetime_field(datetime_text=datetime_text) == exp_result
