import pandas as pd

# Create Frequency Table
iris = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
iris.sample(5)
# Check the count by species
iris_gb = iris.groupby('species')
iris_gb.size()

# Calculate the means
iris_gb.mean()
# A single column
iris_gb['sepal_length'].mean()
# Two columns
iris_gb[['sepal_length', 'petal_length']].mean()

# Calculate the min
iris_gb.min()
# Calculate the max
iris_gb.max()
# Calculate the median
iris_gb.median()
# Calculate the SD
iris_gb.std()

# Index of the largest records
iris_gb.idxmax()

# Records of larges sepal length by group
sepal_largest = iris.loc[iris_gb['sepal_length'].idxmax()]
sepal_largest

# Reset index
iris_gb.max().reset_index()
iris.groupby('species', as_index=False).max()

# Aggregate operations
iris_gb[['sepal_length', 'petal_length']].agg(["min", "mean"])
list(dir(iris_gb))

# Different aggregations by columns
iris_gb.agg({"sepal_length": ["min", "max"], "petal_length": ["mean", "std"]})

# Named Aggregations
iris_gb.agg(
    sepal_min=pd.NamedAgg(column="sepal_length", aggfunc="min"),
    sepal_max=pd.NamedAgg(column="sepal_length", aggfunc="max"),
    petal_mean=pd.NamedAgg(column="petal_length", aggfunc="mean"),
    petal_std=pd.NamedAgg(column="petal_length", aggfunc="std")
)

iris_gb.agg(
    sepal_min=("sepal_length", "min"),
    sepal_max=("sepal_length", "max"),
    petal_mean=("petal_length", "mean"),
    petal_std=("petal_length", "std")
)

# Function objects
iris_gb.agg(pd.Series.mean)

iris_gb.agg(["min", pd.Series.mean])

# Custom function
def double_length(x):
    return 2*x.mean()

iris_gb.agg(double_length)

# Use a lambda function
iris_gb.agg(lambda x: x.mean())