import pandas as pd
mpg_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")
mpg_df.columns
df = mpg_df.drop(columns="cylinders displacement acceleration".split())
df.head()

# import sqlite3
# con = sqlite3.connect("medium.sqlit")
# df.to_sql()

df[(df['origin'] == "usa") & (df['weight'] > 4900)]

df.head(3)
df.iloc[3:6, :]

df['origin'].unique()

df.sort_values(['mpg', 'weight'], ascending=[False, True])

df[df['origin'].isin(['japan', 'europe'])]
df[~df['origin'].isin(['usa'])]

df.groupby('origin').size()

df.groupby(['origin', 'model_year']).size()

df_summary = df.groupby('origin', as_index=False).size().rename(columns={"size": "car_count"})
df_summary

df.agg({"mpg": ["mean", "min", "max"]})

df.groupby('origin').agg(
    mean_mpg=("mpg", "mean"),
    min_hp=("horsepower", "min")
)

df.merge(df_summary, on="origin")

df.loc[df["name"] == "ford torino", "weight"]
df.loc[df["name"] == "ford torino", "weight"] = 3459
df.loc[df["name"] == "ford torino", "weight"]

new_records = df.tail(2)
pd.concat([df, new_records]).reset_index(drop=True)

df.drop(df[df['name'] == 'ford torino'].index)

df['full_year'] = df['model_year'] + 1900

df.drop(columns=["mpg", "horsepower"])

pd.concat([df, df])
