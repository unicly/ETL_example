from src.utils import convert_date_format


def test_convert_date_format_for_format():
    result = convert_date_format("2022-01-01")
    assert (result == "01/01/2022") is True
