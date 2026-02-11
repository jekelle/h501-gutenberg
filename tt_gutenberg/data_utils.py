import pandas as pd

def load_gutenberg_data(filepath='gutenberg.csv'):
    """Load the Gutenberg dataset."""
    return pd.read_csv(filepath)

def clean_aliases(df):
    """Remove messy/invalid values from alias column."""
    # Remove NaN, empty strings, and non-string values
    df = df[df['alias'].notna()]
    df = df[df['alias'].str.strip() != '']
    return df

def count_translations(df):
    """Count number of translations per author alias."""
    return df.groupby('alias').size().reset_index(name='translation_count')
