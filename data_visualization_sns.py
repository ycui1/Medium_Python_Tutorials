import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")
sns.scatterplot(x=df["total_bill"], y=df["tip"])

fig = plt.figure(figsize=(36, 27))
with sns.axes_style("whitegrid"):
    fig.add_subplot()

sns.set_palette("random_thing")

sns.color_palette("Accent")

sns.set_theme(context="talk", style="ticks", palette="Accent")
plt.figure(figsize=(10, 6))
ax: sns.categorical = sns.violinplot(x="day", y="total_bill", data=df)
ax.set_title("Bill Amount by Day")