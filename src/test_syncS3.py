from .syncS3 import output


def test_output():
    i = 0
    assert output(i) == i + 1
