import pandas as pd

# Create two DataFrame objects
df0 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df0
df1 = pd.DataFrame({"c": [2, 3, 4], "d": [5, 6, 7]})
df1

# Concatenate DataFrames vertically
pd.concat([df0, df1.rename(columns={"c": "a", "d": "b"})], axis=0)
# Concatenate DataFrames
pd.concat([df0, df1], axis=1)

# on index by default
df2 = df1.copy()
df2.index = [1, 2, 3]
pd.concat([df0, df2], axis=1)
# how to concat by resetting index
pd.concat([df0.reset_index(drop=True), df2.reset_index(drop=True)], axis=1)

# Join these two df using index
df0.join(df1)
df0.join(df2)
df0.join(df2, how="right")
df0.join(df2, how="outer")
df0.join(df2, how="inner")

# Merge
# the same named columns
df0.merge(df1.rename(columns={"c": "a"}), on="a", how="inner")
# different columns
df0.merge(df1, left_on="a", right_on="c")
# cross merging
df0.merge(df1, how="cross")
# suffixes setting
df0.merge(df1.rename(columns={"c": "a", "d": "b"}), on="a", how="outer", suffixes=("_l", "_r"))


# Combine
def taking_larger_square(s1, s2):
    return s1 * s1 if s1.sum() > s2.sum() else s2 * s2


df0.combine(df1.rename(columns={"c": "a", "d": "b"}), taking_larger_square)


# append
df0.append(df1.rename(columns={"c": "a", "d": "b"}))
df0.append({"a": 1, "b": 2}, ignore_index=True)