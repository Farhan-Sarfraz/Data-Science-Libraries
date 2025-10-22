import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

data = sns.load_dataset("tips").head(20)

sns.stripplot(x="day",y="total_bill",data=data,jitter=True,hue="sex",size=5,dodge=False,alpha=0.8)
plt.show()
data = sns.load_dataset("tips").head(20)

sns.stripplot(x="day",y="total_bill",data=data,jitter=True,hue="sex",dodge=False,size=5)
plt.show()

data = sns.load_dataset("tips").head(20)

sns.stripplot(x="day",y="total_bill",data=data,jitter=True,hue="sex",size=5)
plt.show()

data = sns.load_dataset("tips").head(20)

sns.stripplot(x="day",y="total_bill",data=data,jitter=True,hue="sex")
plt.show()
data = sns.load_dataset("tips").head(20)

sns.stripplot(x="day",y="total_bill",data=data,jitter=True)
plt.show()
data = sns.load_dataset("tips").head(20)

sns.stripplot(x="day",y="total_bill",data=data)
plt.show()
data = sns.load_dataset("tips").head(10)

sns.stripplot(x="total_bill",y="tip",data=data)
plt.show()

