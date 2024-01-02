import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Video_Games.csv")

sales_per_year = data.groupby("Year_of_Release")["Global_Sales"].sum()

sales_per_genres = data.groupby("Genre")["Global_Sales"].sum()

top_selling_games = data.groupby("Name")["Global_Sales"].sum().sort_values(ascending=False).head()

plt.figure(figsize=(6, 6))
sns.barplot(x=top_selling_games.index, y=top_selling_games.values, palette="pastel")
plt.ylabel("Global Sales (Millions)")
plt.xlabel("Game")

plt.xticks(rotation=20, fontsize=7)

f, axes = plt.subplots(1, 2, figsize=(10, 7))

sns.lineplot(x=sales_per_year.index, y=sales_per_year.values, ax=axes[0])
axes[0].set_xlabel("Year Of Release")
axes[0].set_ylabel("Global Sales (Millions)")
sns.barplot(x=sales_per_genres.index, y=sales_per_genres.values, ax=axes[1], palette="coolwarm")
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, fontsize=7)
plt.show()