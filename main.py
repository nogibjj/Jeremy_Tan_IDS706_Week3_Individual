"""
Main cli or app entry point
"""

from mylib.lib import (
    load_and_preprocess,
    process_mean,
    process_quantile,
    process_median,
    process_std,
    congress_histogram_viz,
    congress_line_viz,
    congress_bar_viz,
)


def general_describe(csv):
    """general describe"""
    general_df = load_and_preprocess(csv)
    return general_df.describe()


def custom_describe(csv, col):
    """custom describe"""
    general_df = load_and_preprocess(csv)
    describe_dict = {
        "name": col,
        "mean": process_mean(general_df, col),
        "std": process_std(general_df, col),
        "median": process_median(general_df, col),
        "25 quantile": process_quantile(general_df, col, 0.25),
    }
    return describe_dict


def general_viz_combined(general_df, jupyter_render):
    """saves all the figures at once"""
    congress_histogram_viz(general_df, jupyter_render)
    congress_line_viz(general_df, jupyter_render)
    congress_bar_viz(general_df, jupyter_render)


def save_to_markdown(csv):
    """save summary report to markdown"""
    general_df = load_and_preprocess(csv)
    describe_df = general_describe(csv)
    markdown_table1 = describe_df.to_markdown()
    general_viz_combined(general_df, False)
    # Write the markdown table to a file
    with open("congress_summary.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz](congress_age.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz2](congress_party.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![congress_viz3](congress_state.png)\n")
