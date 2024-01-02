import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Video_Games.csv")

best_selling = data.groupby("Year_of_Release")["Global_Sales"].sum()

top_genres = data.groupby("Genre")["Global_Sales"].sum()

f, axes = plt.subplots(1, 2, figsize=(10, 7))

sns.lineplot(x=best_selling.index, y=best_selling.values, ax=axes[0])
sns.barplot(x=top_genres.index, y=top_genres.values, ax=axes[1])
axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, fontsize=7)
plt.show()