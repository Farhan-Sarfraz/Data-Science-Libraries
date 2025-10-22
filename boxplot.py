import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips").head(40)

sns.boxplot(x="day", y="total_bill", data=data)
plt.title("Box Plot Total Bill by Day")
plt.show()

sns.boxplot(x="day", y="total_bill", data=data,hue="sex")
plt.title("Box Plot Total Bill by Day")
plt.show()


sns.boxplot(x="day", y="total_bill", data=data,hue="sex",palette="Set2")
plt.title("Box Plot Total Bill by Day")
plt.show()

sns.boxplot(x="day", y="total_bill", data=data,hue="sex",palette="Set2",showmeans=True)
plt.title("Box Plot Total Bill by Day")
plt.show()

sns.boxplot(x="day", y="total_bill", data=data,hue="sex",palette="Set2",showmeans=False)
plt.title("Box Plot Total Bill by Day")
plt.show()
