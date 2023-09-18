"""
Main cli or app entry point
"""

from mylib.lib import load_and_preprocess


def general_describe(csv):
    """general_describe"""
    general_df = load_and_preprocess(csv)
    return general_df.describe()
