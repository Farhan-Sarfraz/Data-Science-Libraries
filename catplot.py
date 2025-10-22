import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips")

sns.catplot(x="day",y="total_bill",data=data)
plt.title("cat plot in seaborn")
plt.show()

sns.catplot(x="day",y="total_bill",data=data,kind="box")
plt.title("cat plot in seaborn")
plt.show()

sns.catplot(x="day",y="total_bill",data=data,kind="violin")
plt.title("cat plot in seaborn")
plt.show()


sns.catplot(x="day",y="total_bill",data=data,kind="box",palette="Set2")
plt.title("cat plot in seaborn")
plt.show()

sns.catplot(x="day",y="total_bill",data=data,kind="strip")
plt.title("cat plot in seaborn")
plt.show()

sns.catplot(x="day",data=data,hue="sex",kind="count",palette="Set2")
plt.title("cat plot in seaborn")
plt.show()

sns.catplot(x="total_bill",data=data,hue="sex",kind="count",palette="Set2")
plt.title("cat plot in seaborn")
plt.show()

sns.catplot(x="day",data=data,hue="sex",kind="box",palette="Set2",jitter=True)
plt.title("cat plot in seaborn")
plt.show()