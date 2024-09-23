import pandas as pd

wine_reviews = pd.read_excel("winemag-data-130k-v2.xlsx", index_col='taster_name')
print(wine_reviews.head(13))