import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv").\
    sample(20, random_state=1234).reset_index(drop=True)
df

df.sort_values("year").head()

df.sort_values("year") is df

df.sort_values("year", inplace=True)
df.head()

df.sort_values("year", ignore_index=True).head()

df.sort_values(["year", "passengers"]).head()

df.sort_values("year", ascending=False).head()

df.sort_values(["year", "passengers"], ascending=[False, True]).head()

df.sort_values(["year", "month"]).head()

def numeric_value_for_month(x):
    if x.name == "year":
        return x
    months = ["January", "February", "March", "April",
        "May", "June", "July", "August",
        "Septempber", "October", "November", "December"]
    return x.map(dict(zip(months, range(0, len(months)))))

df.sort_values(["year", "month"], key=numeric_value_for_month).head()

from pandas.api.types import CategoricalDtype

cat_month = CategoricalDtype(["January", "February", "March", "April",
    "May", "June", "July", "August",
    "Septempber", "October", "November", "December"],
    ordered=True)

df["month"] = df["month"].astype(cat_month)
df.sort_values(["year", "month"]).head()

import numpy as np

# Create a NAN
df.iloc[2, 2] = np.nan
df.head()

df.sort_values(["year", "passengers"], na_position="first").head()