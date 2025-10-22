import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset("tips").head(15)
sns.pairplot(data=data,x_vars="total_bill",y_vars="tip",hue="sex",palette="winter",hue_order=["Female","Male"],kind="reg")
plt.show()
data = sns.load_dataset("tips").head(15)
sns.pairplot(data=data,x_vars="total_bill",y_vars="tip",hue="sex",palette="winter",hue_order=["Female","Male"],kind="kde")
plt.show()
data = sns.load_dataset("tips").head(15)
sns.pairplot(data=data,x_vars="total_bill",y_vars="tip",hue="sex",palette="winter",hue_order=["Female","Male"],kind="scatter")
plt.show()
data = sns.load_dataset("tips").head(15)
sns.pairplot(data=data,x_vars="total_bill",y_vars="tip",hue="sex",palette="winter",hue_order=["Female","Male"])
plt.show()
plt.show()
data = sns.load_dataset("tips").head(15)
sns.pairplot(data=data,x_vars="total_bill",y_vars="tip",hue="sex",palette="winter")

plt.show()
data = sns.load_dataset("tips")
sns.pairplot(data=data)

plt.show()

data = sns.load_dataset("tips").head(15)
sns.pairplot(data=data,x_vars="total_bill",y_vars="tip",hue="sex")

plt.show()