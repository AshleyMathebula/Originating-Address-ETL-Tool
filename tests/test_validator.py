from transform.validator import clean_validate_and_format


def test_valid_address_is_formatted():
    raw_addresses = ["ABC123"]

    result = clean_validate_and_format(raw_addresses)

    assert result == ["regex 1,1,ABC123"]


def test_duplicate_addresses_are_removed():
    raw_addresses = ["ABC123", "ABC123"]

    result = clean_validate_and_format(raw_addresses)

    assert len(result) == 1
    assert result == ["regex 1,1,ABC123"]


def test_invalid_address_is_skipped():
    raw_addresses = ["ABC123", "BAD@ADDRESS"]

    result = clean_validate_and_format(raw_addresses)

    assert result == ["regex 1,1,ABC123"]


def test_wildcard_address_is_formatted():
    raw_addresses = ["PROMO?*"]

    result = clean_validate_and_format(raw_addresses)

    assert result == ["regex 1,1,PROMO[0-9]*"]


def test_empty_address_is_skipped():
    raw_addresses = ["", "   ", "ABC123"]

    result = clean_validate_and_format(raw_addresses)

    assert result == ["regex 1,1,ABC123"]