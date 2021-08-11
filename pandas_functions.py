import pandas as pd

df = pd.DataFrame({
    "Student": ['John', 'Jennifer', 'Jeff', 'Joshua', 'Jack', 'Jeremy', 'Jason'],
    "Score": [95, 100, 94, 99, 88, 92, 89]
})
df
# Find the largest 3 scores
df.sort_values("Score", ascending=False).head(3)
# Find the smallest 3 scores
df.sort_values("Score", ascending=True).head(3)
df.nlargest(3, "Score")
df.nsmallest(3, "Score")

df.groupby("Student").idxmax()


df = pd.DataFrame({
    "group": [1, 1, 1, 2, 2, 2, 3, 3, 3],
    "name": ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"],
    "score": [97, 93, 92, 94, 95, 93, 100, 92, 93]
})
df
df.groupby("group")["score"].max()

record_indices = df.groupby("group")["score"].idxmax()
record_indices
df.loc[record_indices]

df["score_dichotomized"] = pd.qcut(df["score"], 2, labels=['bottom50', 'top50'])
df

import datetime
start_date = datetime.datetime(2021, 1, 1)
first_week = [start_date + datetime.timedelta(days=x) for x in range(7)]
pd.DatetimeIndex(first_week)

pd.date_range(start='1/1/2021', periods=7)