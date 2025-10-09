import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd

# val = sns.load_dataset("penguins").head(10)
# sns.barplot(data = val , x = "bill_length_mm" , y =  "bill_depth_mm" , )
# plt.show()

# val = sns.load_dataset("penguins")
# sns.barplot(data = val , x = "island" , y = "bill_length_mm" , hue = True , estimator="mean" )
# plt.xlabel("island plot")
# plt.ylabel("bill_length_mm")
# plt.show()

# val = sns.load_dataset("penguins")
# sns.barplot(data = val , x = "island" , y = "bill_length_mm" , hue = "sex" )
# plt.xlabel("island plot")
# plt.ylabel("bill_length_mm")
# plt.show()

# val = sns.load_dataset("penguins")
# sns.barplot(data = val , x = "island" , y = "bill_length_mm" , hue = "sex" , ci = 4)
# plt.xlabel("island plot")
# plt.ylabel("bill_length_mm")
# plt.show()

# val = sns.load_dataset("penguins")
# sns.barplot(data = val , x = "island" , y = "bill_length_mm" , hue = "sex" , ci = 99)
# plt.xlabel("island plot")
# plt.ylabel("bill_length_mm")
# plt.show()

# val = sns.load_dataset("penguins")
# sns.barplot(data = val , x = "island" , y = "bill_length_mm" , hue = "sex" , ci = 4 , n_boot= 8)
# plt.xlabel("island plot")
# plt.ylabel("bill_length_mm")
# plt.show()

val = sns.load_dataset("penguins").head(15)
sns.barplot(data=val, x="bill_length_mm", y="bill_length_mm", hue="sex", orient="h", color="blue" ,
            saturation=90, errcolor="green")
plt.title("bill_length vs bill_depth")
plt.show()