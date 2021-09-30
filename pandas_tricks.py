# %%
import pandas as pd
import numpy as np


# Read a comma-separated file
df = pd.read_csv("the_data.csv")
# Read an Excel spreadsheet
df = pd.read_excel("the_data.xlsx")

# Create a Series from an iterable
integers_s = pd.Series(range(10))

# %%

integers_s = pd.Series(range(10), name="integer")

# Create a DataFrame from a dictionary of lists as values
data_dict = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
data_df0 = pd.DataFrame(data_dict)

# Create a DataFrame from a list
data_list = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
data_df1 = pd.DataFrame(data_list, columns=tuple('abc'))

# Find out how many rows and columns the DataFrame has
df.shape

# Take a quick peak at the beginning and the end of the data
df.head()
df.tail()

# Get the information of the dataset
df.info()

# Get the descriptive stats of the numeric values
df.describe()

# Rename columns using mapping
df.rename({'old_col0': 'col0', 'old_col1': 'col1'}, axis=1)

# Rename columns by specifying columns directly
df.rename(columns={'old_col0': 'col0', 'old_col1': 'col1'})

# Sort data
df.sort_values(by=['col0', 'col1'])

# To examine whether there are duplicate records by using all columns
df.duplicated().any()

# To examine whether there are duplicate records for a particular set of columns
df.duplicated(['col0', 'col1']).any()

# To find out the number of duplicates
df.duplicated().sum()
df.duplicated(keep=False).sum()

# Get the duplicate records
duplicated_indices = df.duplicated(['col0', 'col1'], keep=False)
duplicates = df.loc[duplicated_indices, :].sort_values(by=['col0', 'col1'], ignore_index=True)

# Drop the duplicate records
df.drop_duplicates(['col0', 'col1'], keep="first", inplace=True, ignore_index=True)

# Find out how many missing values for each column
df.isnull().sum()

# Find out how many missing values for the entire dataset
df.isnull().sum().sum()

# Drop the rows with any missing values
df.dropna(axis=0, how="any")

# Drop the rows without 2 or more non-null values
df.dropna(thresh=2)

# Drop the columns with all values missing
df.dropna(axis=1, how="all")

# Fill missing values with 0 or any other value is applicable
df.fillna(value=0)

# Fill missing values with the next valid observation
df.fillna(method="bfill")
# Fill missing values with the last valid observation
df.fillna(method="ffill")

# Fill the missing values with customized mapping for columns
df.fillna(value={"col0": 0, "col1": 999})

# Get the count by group, a 2 by 2 example
df.groupby(['col0', 'col1']).size()

# Get the mean of all applicable columns by group
df.groupby(['col0']).mean()

# Get the mean for a particular column
df.groupby(['col0'])['col1'].mean()

# Request multiple descriptive stats
df.groupby(['col0', 'col1']).agg({
    'col2': ['min', 'max', 'mean'],
    'col3': ['nunique', 'mean']
})

df_wide = pd.DataFrame({'subject': [100, 101, 102],
                        'before_meds': [5.5, 7.7, 6.6],
                        'after_meds': [4.4, 5.8, 4.9]})
df_wide
df_wide.melt(id_vars='subject', value_vars=['before_meds', 'after_meds'],
             var_name=['time_point'], value_name='measure')

df_long = df.melt(id_vars='subject', value_vars=['before_meds', 'after_meds'],
                  var_name=['time_point'], value_name='measure')

df_long.pivot(index="subject", columns="time_point", values="measure")

# Select a column
df_wide['subject']

# Select multiple columns
df_wide[['subject', 'before_meds']]

# Select rows with a specific condition
df_wide[df_wide['subject'] == 100]

df_wide

# Select the first row
df_wide.iloc[0]
df_wide.loc[0]

# Select the first row, but output as DataFrame
df_wide.iloc[[0]]
df_wide.loc[[0]]

# Select the first two rows
df_wide.iloc[0:2]
df_wide.loc[0:1]

# Select the subject with even id numbers, the first two columns
df_wide.iloc[(df_wide['subject'] % 2 == 0).values, 0:2]
df_wide.loc[df_wide['subject'] % 2 == 0, ["subject", "before_meds"]]

# Select the first row, first column
df_wide.iloc[0, 0]
df_wide.loc[0, "subject"]

df_wide.index = [0, 1, 2]

# Create a new column using the map() function
df_wide['before_meds_unit'] = df_wide['before_meds'].map(lambda x: f"{x} ng/ml")

# Create a new column using the apply() function
df_wide['change_meds'] = df_wide.apply(
    lambda x: x['after_meds'] - float(x['before_meds_unit'].split()[0]),
    axis=1
)

# After data conversion
df_wide

# When the data have the same columns, you concatenate them vertically
dfs_a = [df0a, df1a, df2a]
pd.concat(dfs_a, axis=0)

# When the data have the same index, you concatenate them horizontally
dfs_b = [df0b, df1b, df2b]
pd.concat(dfs_b, axis=1)



# Merge DataFrames that have the same merging keys
df_a0 = pd.DataFrame(dict(), columns=['id', 'name', 'gender'])
df_b0 = pd.DataFrame(dict(), columns=['id', 'name', 'transaction'])
merged0 = df_a0.merge(df_b0, how="inner", on=["id", "name"])

# Merge DataFrames that have different merging keys
df_a1 = pd.DataFrame(dict(), columns=['id_a', 'name', 'gender'])
df_b1 = pd.DataFrame(dict(), columns=['id_b', 'transaction'])
merged1 = df_a1.merge(df_b1, how="outer", left_on="id_a", right_on="id_b")

# Drop the unneeded columns
df.drop(['col0', 'col1'], axis=1)

# Write to a csv file, which will keep the index
df.to_csv("filename.csv")

# Write to a csv file without the index
df.to_csv("filename.csv", index=False)

# Write to a csv file without the header
df.to_csv("filename.csv", header=False)
