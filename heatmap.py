import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


data =sns.load_dataset("anagrams").head(10)
x = data.drop(columns=("attnr"),axis=1)
sns.heatmap(x , vmax=20,vmin=0,cmap="winter_r")
plt.show()
data =sns.load_dataset("anagrams").head(10)
x = data.drop(columns=("attnr"),axis=1)
sns.heatmap(x , vmax=20,vmin=0,annot=True,cmap="winter_r")
plt.show()



# data = np.linspace(1,10,20).reshape(4,5)

# sns.heatmap(data)
# plt.show()