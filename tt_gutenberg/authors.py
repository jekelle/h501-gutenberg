import pandas as pd


AUTHORS_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"


def list_authors(by_languages=False, alias=False):
  

    df = pd.read_csv(AUTHORS_URL)

    if alias and "alias" in df.columns:
        authors = df["alias"].dropna().unique().tolist()
    else:
        authors = df["author"].dropna().unique().tolist()

    if by_languages and "language" in df.columns:
        grouped = df.groupby("language")["author"].apply(list).to_dict()
        return grouped

    return authors
