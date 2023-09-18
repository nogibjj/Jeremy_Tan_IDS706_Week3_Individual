import polars as pl


# Data Loading and Preprocessing:
def load_and_preprocess(csv):
    """loads the data"""
    general_df = pl.read_csv(csv)
    return general_df


# DataFrame Operations:
def filter_by_party(df, party):
    """filters by party"""
    filtered_df = df.filter(pl.col("party") == party)
    return filtered_df


def filter_by_state(df, state):
    """filters by state"""
    filtered_df = df.filter(pl.col("state") == state)
    return filtered_df


def filter_by_term(df, term):
    """filters by term"""
    filtered_df = df.filter(pl.col("term") == term)
    return filtered_df


# Data Exploration and Analysis:
def count_by_party(df):
    """counts by party"""
    party_counts = df.groupby("party").count()
    return party_counts


# Data Visualization:
def plot_party_counts(df):
    """plots the party counts"""
    party_counts = df.groupby("party").count()
    party_counts.plot()
    return party_counts


def plot_party_counts_by_state(df):
    """plots the party counts by state"""
    party_counts = df.groupby(["party", "state"]).count()
    party_counts.plot()
    return party_counts


# Data Exporting:
def export_csv(df, filename):
    """exports the data to a csv"""
    df.to_csv(filename)
