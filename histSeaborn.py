import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# values = sns.load_dataset("penguins")
# bill_length_mm
# sns.displot(values , x = "bill_length_mm" ,bins = 7 ,  kde = True , rug = True , color = "r")
# sns.displot(values , x = "sex" ,kde = True ,  color = "green")

# sns.histplot(values, x="bill_depth_mm", kde=True , color = "blue")
# plt.show()

data = sns.load_dataset("penguins")
sns.displot(data , x = "body_mass_g" , kde = True , bins = 9 , color = "r" )
plt.show()