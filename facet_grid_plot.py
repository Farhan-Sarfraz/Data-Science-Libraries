import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")
g = sns.FacetGrid(data, col="sex")
g.map(sns.histplot, "total_bill")
plt.show()

g = sns.FacetGrid(data, row="smoker", col="sex")
g.map(sns.scatterplot, "total_bill", "tip")
plt.show()
g = sns.FacetGrid(data, col="day", hue="sex", palette="Set2")
g.map(sns.scatterplot, "total_bill", "tip", alpha=0.8)
g.add_legend()
plt.show()
g = sns.FacetGrid(data, col="day", height=4, aspect=0.8)
g.map(sns.kdeplot, "total_bill", fill=True, color="skyblue")
plt.show()

g = sns.FacetGrid(data, col="smoker", row="sex", height=4)
g.map_dataframe(sns.boxplot, x="day", y="total_bill", palette="pastel")
g.add_legend()
g.set_axis_labels("Day", "Total Bill")
g.set_titles(row_template="{row_name}", col_template="{col_name}")
plt.show()
import matplotlib.pyplot as plt

def custom_scatter(x, y, color=None, **kwargs):
    plt.scatter(x, y, color=color, **kwargs)

g = sns.FacetGrid(data, col="day", hue="sex", height=4)
g.map(custom_scatter, "total_bill", "tip")
g.add_legend()
plt.show()
