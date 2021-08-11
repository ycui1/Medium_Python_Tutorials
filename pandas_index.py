with open("data.csv", "w") as file:
    file.write("""date,temperature,humidity
07/01/21,95,50
07/02/21,94,55
07/03/21,94,56""")

import pandas as pd
import numpy as np

pd.read_csv("data.csv", parse_dates=["date"])

pd.read_csv("data.csv", parse_dates=["date"], index_col="date")

df = pd.read_csv("data.csv", parse_dates=["date"])
df.set_index("date", drop=False)

df0 = pd.DataFrame(np.random.rand(5, 3), columns=list("ABC"))
df0
df1 = df0[df0.index % 2 == 0]
df1
df1.reset_index(drop=True)


df0["team"] = ["X", "X", "Y", "Y", "Y"]
df0
df0.groupby("team").mean()

df0.groupby("team").mean().reset_index()

df0.groupby("team", as_index=False).mean()

df0.sort_values("A")
df0.sort_values("A", ignore_index=True)

df0
df0.drop_duplicates("team", ignore_index=True)

df0
better_index = ["X1", "X2", "Y1", "Y2", "Y3"]
df0.index = better_index
df0

df0.to_csv("exported_file.csv", index=False)