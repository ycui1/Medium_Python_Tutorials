import pandas as pd

s0 = pd.Series([1, 2, 3])
s1 = pd.Series([10, 20, 30])
s2 = pd.Series([100, 200, 300])
df = pd.DataFrame({'col 0': s0, 'col 1': s1, 'col 2': s2})
df.index = ['row 0', 'row 1', 'row 2']
df

# Use a dictionary object
s0.map({1: 1, 2: 4, 3: 9})

# Use a lambda function
s0.map(lambda x: x*x)

# Use a regular function
def square(x):
    return x*x
s0.map(square)

df['col 3'] = df['col 0'].map(lambda x: x*x)
df.loc['row 3'] = df.loc['row 2'].map(lambda x: x+1)
df

# Use a lambda function
df['col 4'] = df.apply(
    lambda x: x['col 0'] * x['col 1'],
    axis=1
)

# Use a regular function
def create_col(x, n):
    return x['col 0'] * n
df['col 5'] = df.apply(create_col, axis=1, args=(5,))

df

# Use apply() on the Series object
s0.apply(lambda x: pd.Series([x, 2*x, 3*x]))

# Create two columns using a column of DataFrame
df[['col 6', 'col 7']] = df['col 5'].apply(lambda x: pd.Series([x*2, x*3]))
df

df[['col 8', 'col 9']] = df.apply(
    lambda x: [x['col 6'] + 1, x['col 7'] + 2],
    axis=1,
    result_type='expand'
)
df

