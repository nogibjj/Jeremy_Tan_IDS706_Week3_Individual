"""
Test goes here

"""

from mylib.lib import (
    load_and_preprocess,
    process_mean,
    process_quantile,
    process_median,
    process_std,
)

example_csv = "https://raw.githubusercontent.com/fivethirtyeight/data/master/congress-age/congress-terms.csv"


def test_load_and_preprocess():
    """test that loading the csv will work"""
    general_df = load_and_preprocess(example_csv)
    assert general_df is not None
    assert general_df.shape == (18635, 13)


def test_stats():
    """test that checks the data operations is working"""
    general_df = load_and_preprocess(example_csv)
    mean_test = process_mean(general_df, "age")
    quantile_test = process_quantile(general_df, "age", 0.25)
    median_test = process_median(general_df, "age")
    std_test = process_std(general_df, "age")
    describe_test = general_df.describe()
    assert describe_test.loc["mean", "age"] == mean_test
    assert describe_test.loc["std", "age"] == std_test
    assert describe_test.loc["25%", "age"] == quantile_test
    assert median_test == 53.0


if __name__ == "__main__":
    test_load_and_preprocess()
    test_stats()
