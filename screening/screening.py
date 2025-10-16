# DISTINCT() function
# instead of coding df[col].drop_duplicates() for every column one-by-one
# this shows all distinct values and its count from all 'object' or 'categorical' type columns of DataFrame
import pandas as pd

def distinct(df):
  result []
  cat_cols = df.select_dtypes(include=['object', 'categorical']).columns
  for col in cat_cols:
    vc = df[col].value_counts(dropna=False).reset_index()
    vc.columns = ['values', 'count']
    vc.insert(0, 'column', col)
    result.append(vc)
  with pd.option_context('display.max_rows', None):
    return pd.concat(result, ignore_index=True)
