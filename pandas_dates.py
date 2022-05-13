text_data = """date,category,balance
01/01/2022,A,100
02/02/2022,B,200
03/12/2022,C,300"""

with open("dates_text.csv", "w") as file:
    file.write(text_data)

import pandas as pd
df = pd.read_csv("dates_text.csv")
df.dtypes

df = pd.read_csv("dates_text.csv", parse_dates=["date"])
df.dtypes

text_data_cols = """y,m,d,category,balance
2022,01,01,A,100
2022,02,02,B,200
2022,03,12,C,300"""
with open("dates_text_cols.csv", "w") as file:
    file.write(text_data_cols)

df_cols = pd.read_csv("dates_text_cols.csv", parse_dates={"date": ["y", "m", "d"]})
df_cols

df = pd.read_csv("dates_text.csv", parse_dates=["date"], dayfirst=True)
df

text_data_fmt = """date,category,balance
Jan_01_2022,A,100
Feb_02_2022,B,200
Mar_12_2022,C,300"""

with open("custom_dt_fmt.csv", "w") as file:
    file.write(text_data_fmt)

pd.read_csv("custom_dt_fmt.csv", parse_dates=["date"], infer_datetime_format=True)


from datetime import datetime
pd.read_csv("custom_dt_fmt.csv", parse_dates=["date"], date_parser=lambda x: datetime.strptime(x, "%b_%d_%Y"))

pd.to_datetime("Jan 01, 2022")

pd.to_datetime(["01/01/2022", "01/02/2022", "01/03/2022"])

pd.to_datetime(pd.Series(["01/01/2022", "01/02/2022", "01/03/2022"]))


import datetime
start_date = datetime.datetime(2022, 12, 1)
one_week = [start_date + datetime.timedelta(days=x) for x in range(7)]
pd.DatetimeIndex(one_week)

pd.date_range(start="12/01/2022", end="12/07/2022")

data = {"timestamp": ["01/01/2022 09:01:00", "01/02/2022 08:55:44", "05/01/2022 22:01:00"],
        "category": list('ABC')}
df = pd.DataFrame(data)
df.dtypes
df["timestamp"] = pd.to_datetime(df["timestamp"])
df.dtypes

df["date"] = df["timestamp"].dt.date
df["time"] = df["timestamp"].dt.time
df

df["timestamp"].dt.year
df["timestamp"].dt.month
df["timestamp"].dt.weekday