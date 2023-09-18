"""
Test goes here

"""

from main import general_describe

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


def test_load_and_preprocess():
    describe_test = general_describe(example_csv)
    assert describe_test.shape == (9, 14)
