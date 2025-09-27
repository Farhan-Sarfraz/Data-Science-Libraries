import pandas as pd

data = {
    "name" : ['farhan', 'muhammad','ali','haider'],
    "age" : [22,33,32,14],
    "salary" : [4000,2000,3000,1000]
}
df = pd.DataFrame(data)
print(df)
g = df.groupby(["age","name"])["salary"].mean()
g1 = df.groupby(["age","name"])["salary"].max()
g2 = df.groupby(["age","name"])["salary"].min()
g3 = df.groupby(["age","name"])["salary"].std()
g4 = df.groupby(["age","name"])["salary"].count()
print(g)
print(g1)
print(g2)
print(g3)
print(g4)

# import pandas as pd

# data = {
#     "name" : ['farhan', 'muhammad','ali','haider'],
#     "age" : [22,33,32,14],
#     "salary" : [4000,2000,3000,1000]
# }
# df = pd.DataFrame(data)
# print(df)

# grouped = df.groupby("age")["salary"].sum()
# print(grouped)

# avg_sal = df["salary"].mean()
# print(avg_sal)
# max_sal = df["salary"].max()
# print(max_sal)
# min_sal = df["salary"].min()
# print(min_sal)
# sum_sal = df["salary"].sum()
# print(sum_sal)
# import pandas as pd

# data = {
#     "name" : ['farhan', 'muhammad','ali','haider'],
#     "age" : [22,33,32,14],
#     "salary" : [40000,30000,35000,12000]
# }
# df = pd.DataFrame(data)
# print(df)
# print("sorting method. ")
# df.sort_values(by=["age","salary"], ascending=True, inplace=True)
# print(df)
# import pandas as pd

# data = {
#     "name" : ['farhan', 'muhammad','ali','haider'],
#     "age" : [22,33,32,14],
#     "salary" : [40000,30000,35000,12000]
# }
# df = pd.DataFrame(data)
# print(df)
# print("sorting method. ")
# df.sort_values(by="age", ascending=True, inplace=True)
# print(df)

# data = {
#     "time" : [1,2,3,4,5,6],
#     "value" : [10,20,None,40,None,60]
# }
# df = pd.DataFrame(data)
# print(df)
# print("after applying linear interpolation. ")
# df["value"] = df["value"].interpolate(mehtod="linear")
# print(df)

# data = {
#     "name" : ['usman', 'saad', 'taha', 'munir', 'ahmad', 'muhammad',None],
#     "age"  : [23,22,19,24,28,29,None],
#     "salary" : [2500, 7000,5000,3400,5600,5400,None],
#     "performance score" : [54,76,98,90,56,53,None]
# }
# df = pd.DataFrame(data)
# print(df)
# print("after applying handling function. ")
# df["age"].fillna(df['age'].mean(), inplace=True)
# df["salary"].fillna(df["salary"].mean(),inplace= True)
# df["performance score"].fillna(df["performance score"].mean(),inplace= True)
# print(df)
# df.fillna(0, inplace=True)
# print(df)
# df.dropna(inplace = True)
# print(df)

# print(df.isnull())
# print(df.isnull().sum())


# import pandas as pd

# data = {
#     "name" : ['usman', 'saad', 'taha', 'munir', 'ahmad', 'muhammad'],
#     "age"  : [23,22,19,24,28,29],
#     "salary" : [2500, 7000,5000,3400,5600,5400],
#     "performance score" : [54,76,98,90,56,53]
# }
# df = pd.DataFrame(data)
# print(df)
# print("modified data is here below. ")
# df.drop(columns=["salary"], inplace = True)
# print(df)

# df["salary"] = df["salary"] * 2.05
# print(df)

# df.loc[3, "salary"] = 4000
# print(df)
# df["bonus"] = df['salary'] * 0.1
# print(df)

# df.insert(0, 'employee_id', [100,101,102,103,104,105])
# print(df)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# df1 = pd.Series(data)
# print(df1)
# data = {
#     "name" : ['ali', 'usman','haider', 'mubariz', 'shahyan', 'farhan'],
#     'age' : [33,44,55,23,54,47],
#     "salary" : [23000,78000,56000,45000,65000,98000],
#     "performance score" : [56,87,90,67,82,40]
# }

# df = pd.DataFrame(data)
# filtered = df[(df['salary'] > 30000 ) & (df['age'] > 30)]
# print(filtered)
# print("subset with > 30000 salary. ")

# high_salary = df[df['salary'] > 30000]

# print(high_salary)



# import pandas as pd

# data = {
#     "name" : ['ali', 'usman','haider', 'mubariz', 'shahyan', 'farhan'],
#     'age' : [33,44,55,23,54,47],
#     "salary" : [23000,78000,56000,45000,65000,98000],
#     "performance score" : [56,87,90,67,82,40]
# }
# df = pd.DataFrame(data)
# print("showing the dataframe. ")
# print(df)

# print("printing the name of the employee. ")
# name  = df['name']
# print(name)

# print("age of the data. ")
# age = df["age"]
# print(age)

# subject = df[["name", 'age']]
# print(subject)

# import pandas as pd

# data = {
#     "name" : ['ali', 'usman','haider', 'mubariz', 'shahyan', 'farhan'],
#     'age' : [33,44,55,23,54,47],
#     "salary" : [23000,78000,56000,45000,65000,98000],
#     "performance score" : [56,87,90,67,82,40]
# }

# df = pd.DataFrame(data)
# print(df)
# print(f"shape is :",df.shape)
# print(f"coumns are : ", df.columns)

# data = {
#     "name" : ['ali', 'usman','haider', 'mubariz', 'shahyan', 'farhan'],
#     'age' : [33,44,55,23,54,47],
#     "salary" : [23000,78000,56000,45000,65000,98000],
#     "performance score" : [56,87,90,67,82,40]
# }

# df = pd.DataFrame(data)
# print(df)

# print("discriptive statistics explanation. ")
# print(df.describe())
# df = pd.read_json("sample_Data.json")
# print("displyeing the information of the data. ")
# print(df.info())
#  first 5 rows will be displayed
# print(df.head())
# #  last five rows will be displayed
# print(df.tail())

# data = {
#     "name" : ['ali', 'haider', 'usman'],
#     "age" : [23,55,77],
#     "city" : ['jamnegar', 'vehari', 'lodheran']
# }

# df = pd.DataFrame(data)
# print(df)

# # df.to_csv("output.csv", index= False)
# df.to_excel("output.xlsx", index = False)

# # 
# df = pd.read_csv("sales_data_sample.csv", encoding="latin1")
# df =pd.read_json("sample_Data.json")
# df = pd.read_excel("SampleSuperstore.xlsx")

# print(df)

# Series
# s = pd.Series([10, 20, 30, 40], name="Numbers")
# print(s)

# # DataFrame
# data = {
#     "Name": ["Ali", "Sara", "Usman"],
#     "Age": [25, 30, 22],
#     "City": ["Lahore", "Karachi", "Islamabad"]
# }
# df = pd.DataFrame(data)
# print(df)

# df = pd.Series([1,2,3,4], name="numbers")
# print(df)
# df = pd.DataFrame({"name" : ['ali', 'usman', 'haider'], "marks": [50,70,23]})
# print(df)
# df = pd.Series([1,3,4,5,6,7])
# print(df)