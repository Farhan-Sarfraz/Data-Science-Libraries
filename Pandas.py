import pandas as pd

data = {
    "name" : ['ali', 'usman','haider', 'mubariz', 'shahyan', 'farhan'],
    'age' : [33,44,55,23,54,47],
    "salary" : [23000,78000,56000,45000,65000,98000],
    "performance score" : [56,87,90,67,82,40]
}

df = pd.DataFrame(data)
filtered = df[(df['salary'] > 30000 ) & (df['age'] > 30)]
print(filtered)
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