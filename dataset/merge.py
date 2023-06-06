import pandas as pd

# Assuming you have two datasets: df1 and df2

# Specify the actual datasets to merge
df1 = pd.read_csv('dataset\\ryans.csv',on_bad_lines='skip')
df2 = pd.read_csv('dataset\Startech.csv',on_bad_lines='skip')

# Merge the datasets based on a common column
merged_df = pd.merge(df1, df2, on='RAM')

# Print the merged dataset
print(merged_df)