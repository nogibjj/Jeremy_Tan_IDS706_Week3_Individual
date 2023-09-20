import pandas as pd
import matplotlib.pyplot as plt


# Data Loading and Preprocessing:
def load_and_preprocess(csv):
    """loads the data"""
    general_df = pd.read_csv(csv)
    return general_df


# Data Operations
def process_mean(general_df, col):
    """returns the mean of a specific col in dataframe"""
    general_mean = general_df[col].mean()
    return general_mean


def process_median(general_df, col):
    """returns the median of a specific col in dataframe"""
    general_median = general_df[col].median()
    return general_median


def process_std(general_df, col):
    """returns the std of a specific col in dataframe"""
    general_std = general_df[col].std()
    return general_std


def process_quantile(general_df, col, quantile_num):
    """returns the quantile specified of a specific col in dataframe"""
    general_quantile = general_df[col].quantile(quantile_num)
    return general_quantile


# Data Vizualization
def congress_histogram_viz(general_df, jupyter_render):
    """generate a histogram of age of distbution of congress members"""
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["age"], bins=20, edgecolor="black")
    plt.title("Age Distribution of Congress Members")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    if not jupyter_render:
        plt.savefig("congress_age.png")
    else:
        plt.show()


def congress_line_viz(general_df, jupyter_render):
    """generate a line chart of pary affiliation over time"""
    general_df["start_date"] = pd.to_datetime(general_df["termstart"])
    general_df["year"] = general_df["start_date"].dt.year
    party_counts = general_df.groupby(["year", "party"]).size().unstack(fill_value=0)
    party_counts.plot(kind="line", figsize=(12, 8), colormap="Set1")
    plt.title("Party Affiliation Over Time")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.legend(title="Party")
    if not jupyter_render:
        plt.savefig("congress_party.png")
    else:
        plt.show()


def congress_bar_viz(general_df, jupyter_render):
    """generate a bar graph of state distrubution of congress members"""
    gender_counts = general_df["state"].value_counts()
    plt.figure(figsize=(15, 6))
    gender_counts.plot(kind="bar", color="salmon")
    plt.title("State Distribution of Congress Members")
    plt.xlabel("State")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    if not jupyter_render:
        plt.savefig("congress_state.png")
    else:
        plt.show()
