"""
Test goes here

"""

from main import general_describe, custom_describe, save_to_markdown

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


def test_describe():
    """test describe is actually working"""
    describe_test = general_describe(example_csv)
    assert describe_test.shape == (8, 2)


def test_two_describes():
    """test .describe with custom describe function"""
    describe_test = general_describe(example_csv)
    custom_test = custom_describe(example_csv, "age")
    assert describe_test.loc["mean", "age"] == custom_test["mean"]
    assert describe_test.loc["std", "age"] == custom_test["std"]
    assert describe_test.loc["25%", "age"] == custom_test["25 quantile"]


def test_summary_and_viz_to_markdown():
    """converts to markdown()"""
    save_to_markdown(example_csv)


if __name__ == "__main__":
    test_describe()
    test_two_describes()
    test_summary_and_viz_to_markdown()
