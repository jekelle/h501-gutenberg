from .data_utils import load_gutenberg_data, clean_aliases, count_translations

def list_authors(by_languages=False, alias=False, filepath='gutenberg.csv'):
    
    df = load_gutenberg_data(filepath)
    
    if alias and by_languages:
       
        df = clean_aliases(df)
        
      
        alias_counts = count_translations(df)
        
        
        alias_counts = alias_counts.sort_values('translation_count', ascending=False)
        
       
        return alias_counts['alias'].tolist()
    
   
    return []
