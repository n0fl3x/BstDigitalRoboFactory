import pytest

from robots.validators import validate_json


VALID_JSON_1 = {
    "model": "R2",
    "version": "D2",
    "created": "2022-09-24 18:54:54"
}

VALID_JSON_2 = {
    "model": "R2",
    "kek": 25,
    "version": "D2",
    "created": "2022-09-24 18:54:54"
}

VALID_JSON_3 = {
    "model": "",
    "version": "",
    "created": "2022-09-24 18:54:54"
}


GOOD_CASES = [
    (VALID_JSON_1, True),
    (VALID_JSON_2, True),
    (VALID_JSON_3, True),
]


@pytest.mark.parametrize("json_data, exp_result", GOOD_CASES)
def test_validate_json_good(json_data, exp_result):
    assert validate_json(json_data=json_data) == exp_result


INVALID_JSON_1 = {
    "version": "D2",
    "created": "2022-09-24 18:54:54"
}

INVALID_JSON_2 = {
    "model": 25,
    "version": "D2",
    "created": "2022-09-24 18:54:54"
}

INVALID_JSON_3 = {
    "model": "25",
    "version": None,
    "created": "2022-09-24 18:54:54"
}


BAD_CASES = [
    (INVALID_JSON_1, False),
    (INVALID_JSON_2, False),
    (INVALID_JSON_3, False),
]


@pytest.mark.parametrize("json_data, exp_result", BAD_CASES)
def test_validate_json_bad(json_data, exp_result):
    assert validate_json(json_data=json_data) == exp_result
