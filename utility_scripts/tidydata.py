import pandas as pd
data = pd.read_csv('/Users/kaito/Downloads/YFP_values.csv',index_col=0)
tidydata = data.pivot(columns='Slice', values='Mean').apply(lambda x: pd.Series(x.dropna().values))