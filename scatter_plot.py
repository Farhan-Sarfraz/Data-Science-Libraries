import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

# val = sns.load_dataset("penguins")
# sns.scatterplot(x = "bill_length_mm" , y =  "bill_depth_mm" , data = val)

# plt.xlabel("island plot")
# plt.ylabel("bill_length_mm")
# plt.show()


# value = sns.load_dataset("penguins").head(20)

# sns.scatterplot(x = "bill_depth_mm" , y = "bill_length_mm" , data = value,hue="sex" , size="sex", style = "sex")
# plt.show()

# value = sns.load_dataset("penguins").head(20)

# sns.scatterplot(x = "bill_depth_mm",y="bill_length_mm",data=value,hue="sex",size="sex",style = "sex",palette="winter",alpha=0.8,)
# plt.show()


value = sns.load_dataset("penguins").head(20)
m = {"Male" : "*" , "Female" : "o"}
sns.scatterplot(x = "bill_depth_mm",y="bill_length_mm",data=value,hue="sex",size="sex",style = "sex",markers = m)
plt.title("advanced scatter plot")
plt.show()