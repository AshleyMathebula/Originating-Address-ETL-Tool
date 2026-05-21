from transform.formatter import format_address, format_addresses


def test_format_normal_address():
    result = format_address("ABC123")

    assert result == "regex 1,1,ABC123"


def test_format_wildcard_address():
    result = format_address("PROMO?*")

    assert result == "regex 1,1,PROMO[0-9]*"


def test_format_empty_address_raises_error():
    try:
        format_address("")
        assert False
    except ValueError:
        assert True


def test_format_multiple_addresses():
    result = format_addresses(["ABC123", "PROMO?*"])

    assert result == [
        "regex 1,1,ABC123",
        "regex 1,1,PROMO[0-9]*",
    ]