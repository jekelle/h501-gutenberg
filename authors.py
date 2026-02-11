from .data_utils import load_gutenberg_data, clean_aliases, count_translations

def list_authors(by_languages=False, alias=False, filepath='gutenberg.csv'):
    """
    List Project Gutenberg authors sorted by various criteria.
    
    Parameters:
    -----------
    by_languages : bool
        If True, sort by translation count
    alias : bool
        If True, return author aliases instead of names
    filepath : str
        Path to the Gutenberg CSV file
        
    Returns:
    --------
    list
        List of author names or aliases
    """
    # Load data using function from data_utils module
    df = load_gutenberg_data(filepath)
    
    if alias and by_languages:
        # Clean the aliases
        df = clean_aliases(df)
        
        # Count translations per alias
        alias_counts = count_translations(df)
        
        # Sort by translation count (descending)
        alias_counts = alias_counts.sort_values('translation_count', ascending=False)
        
        # Return list of aliases
        return alias_counts['alias'].tolist()
    
    # Add other conditions if needed
    return []
