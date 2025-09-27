import pandas as pd
customer_profile = pd.DataFrame({
    "name" : ['ali','haider','usman'],
    "customer_id" : [1,2,3]
})
customer_transc = pd.DataFrame({
    "customer_id" : [1,2,3],
    "transaction_id" : [500,600,700]
})

print(customer_profile)

print(customer_transc)

merged_df = pd.merge(customer_profile,customer_transc, on="customer_id", how="inner")
print(merged_df)

new_customer = pd.DataFrame({
    "name" : ['alia', 'ryan'],
    "customer_id" : [4,5]

})
new_transaction = pd.DataFrame({
    "customer_id" : [4,5],
    "transaction_id" : [300,400]
})

merged_new = pd.merge(new_customer,new_transaction, on="customer_id", how="inner")
print(merged_new)

final_task = pd.concat([merged_df,merged_new], axis= 0, ignore_index=True)
print(final_task)

final_task.to_csv("customer_id_merging.csv", index= False)


# joining

# import pandas as pd
# df1 = pd.DataFrame({
#     "name" : ['ali', 'usman ', 'haider'],
#     "id" : [7,8,9]
# },
# index = [0,1,2]
# )

# df2 = pd.DataFrame({
#     "dpt" : ['telecom', 'software', 'hardware']
# },
# index=[1,2,4]
# )
# joined = df1.join(df2, how="inner")
# print(joined)

# df1 = pd.DataFrame({
#     "name" : ['ali','haider','kamran'],
#     "id" : [1,2,3]
# })
# df2 = pd.DataFrame({
#     "name" : ['usman','farhan','adnan'],
#     "id" : [5,6,7]
# })

# concatenation = pd.concat([df1,df2], axis=0, ignore_index=False)
# print(concatenation)

# df1 = pd.DataFrame({
#     "name" : ['ali','haider','kamran'],
#     "id" : [1,2,3]
# })
# df2 = pd.DataFrame({
#     "name" : ['usman','farhan','adnan'],
#     "id" : [5,6,7]
# })

# concat = pd.concat([df1,df2], axis=1, ignore_index=True)
# print(concat)

#  basic synatx
# df.merge(df1, df2, on="coulmn_name", how="type of data")
# import  pandas as pd
# df1 = pd.DataFrame({
#     "id" : [1,2,3,4],
#     "name" : ['farhan','taha', 'soban','ali']
# })
# df2 = pd.DataFrame({
#     "id" : [3,4,5,6],
#     "order" : [10,20,30,40]
# })
# merged = pd.merge(df1,df2, on ="id", how="left")
# print(merged)
# import  pandas as pd
# df1 = pd.DataFrame({

#     "name" : ['farhan','taha']
# })
# df2 = pd.DataFrame({
#     "order" : [10,20]
# })
# merged = pd.merge(df1,df2, how="cross")
# print("cross joining :->>>>>>>")
# print(merged)

# import  pandas as pd
# df1 = pd.DataFrame({
#     "id" : [1,2,3,4],
#     "name" : ['farhan','taha', 'soban','ali']
# })
# df2 = pd.DataFrame({
#     "id" : [3,4,5,6],
#     "order" : [10,20,30,40]
# })
# merged = pd.merge(df1,df2, on ="id", how="right")
# print("right joining :->>>>>>>")
# print(merged)



# import  pandas as pd
# df1 = pd.DataFrame({
#     "id" : [1,2,3,4],
#     "name" : ['farhan','taha', 'soban','ali']
# })
# df2 = pd.DataFrame({
#     "id" : [3,4,5,6],
#     "order" : [10,20,30,40]
# })
# merged = pd.merge(df1,df2, on ="id", how="outer")
# print(merged)


# import pandas as pd
# # customeres dataFrame
# df_customers = pd.DataFrame({
#     "customer_id" : [1,2,3,4],
#     "name" : ['ali','usman','haider','shenwari']
# })
# # orders dataFrame
# df_order = pd.DataFrame({
#     "customer_id" : [2,3,4,5],
#     "order_amount" : [40,50,60,70]
# })
# df_merged = pd.merge(df_customers,df_order, on="customer_id", how="inner")
# print(df_merged)