import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns 

data = sns.load_dataset("tips")

sns.countplot(data=data,x="sex" , hue="smoker",palette="ocean")
plt.title("count plot using seaborn")
plt.show()
sns.countplot(data=data,x="sex" , hue="smoker")
plt.title("count plot using seaborn")
plt.show()
data = sns.load_dataset("tips")

sns.countplot(data=data,x="sex")
plt.show()