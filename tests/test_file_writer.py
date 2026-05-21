from load.file_writer import write_output_file


def test_write_output_file(tmp_path):
    output_file = tmp_path / "cleaned_addresses.txt"

    addresses = [
        "regex 1,1,ABC123",
        "regex 1,1,PROMO[0-9]*",
    ]

    write_output_file(str(output_file), addresses)

    content = output_file.read_text(encoding="utf-8").splitlines()

    assert content == addresses