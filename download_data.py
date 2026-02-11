import pandas as pd

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2022/2022-12-27/tlBooks.csv"
df = pd.read_csv(url)
df.to_csv('gutenberg.csv', index=False)

print(f"Success! Dataset has {len(df)} rows and {len(df.columns)} columns")
print("Saved as gutenberg.csv")
