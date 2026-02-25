import pandas as pd

def load_gutenberg_data(filepath='gutenberg.csv'):
    """Load the Gutenberg dataset."""
    return pd.read_csv(filepath)

def clean_aliases(df):
    
    df = df[df['alias'].notna()]
    df = df[df['alias'].str.strip() != '']
    return df

def count_translations(df):
 
    return df.groupby('alias').size().reset_index(name='translation_count')
