from codeoceansdk import IO


def test_get_dataframe_from_from_url():
    input_url = "https://codeocean-public-data.s3.amazonaws.com/unit_test/test.tsv"
    test_frame = IO.get_dataframe_from_url(input_url)
    assert len(test_frame) == 1
    assert list(test_frame.columns) == ["header1", "header2"]
    assert test_frame[test_frame["header1"] == "test"]["header2"].values == "test2"
