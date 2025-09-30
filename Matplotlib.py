
import matplotlib.pyplot as plt

x = ['mond', 'tuesd', 'wed', 'thursd', 'frid',' saturd', 'sund']
y = [20,56,34,10,89,32,54]
plt.plot(x, y, linewidth = 3, color = 'blue', linestyle = '--', marker = 'o', label = 'bakery sales % ')
plt.xlabel(' Days of the week! ')
plt.ylabel('Sales percentage! ')
plt.title('bakery weekly sale! ')
plt.legend(loc = 'upper left')
plt.xlim()
plt.ylim(0, 99)
plt.xticks(['mond', 'tuesd', 'wed', 'thursd', 'frid',' saturd', 'sund'], ['d1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7'])
plt.grid(linewidth = 1, linestyle = ':', color = 'gray')
plt.show()


# import matplotlib.pyplot as plt
# marks = [40,41,43,42,45,56,88,66,77,82,90,93,63,87,61,53,59,60]

# plt.hist(marks, bins= 5, color = 'purple', edgecolor = 'gold')
# plt.xlabel('students')
# plt.ylabel('marks')
# plt.title('range of the students')
# plt.legend()

# plt.show()
# import matplotlib.pyplot as plt 
# regions = ['south', 'north', 'east', 'west']
# product = [30, 1, 49, 20]

# plt.pie(product, labels = regions , autopct = '%1.1f%%' )
# plt.title('regions data %')
# plt.legend()
# plt.show()
# import matplotlib.pyplot as plt 
# regions = ['south', 'north', 'east', 'west']
# product = [30, 1, 49, 20]

# plt.pie(product, labels = regions , colors = ['green', 'gold', 'orange' , 'black'] , autopct = '%1.1f%%' )
# plt.title('regions data %')
# plt.legend()
# plt.show()

# days = ['D1', 'D2', 'D3', 'D4', 'D5']
# sales = [1000, 4000, 2550, 850 , 3300]

# plt.bar(days, sales, color = 'orange', label= 'Each day sales')
# plt.xlabel('no of days')
# plt.ylabel('sales outcomes ')
# plt.title('product sales comparison ')
# plt.legend()
# plt.show()



# plt.plot(x, y, linewidth = 3, color = 'blue', linestyle = '--', marker = 'o', label = 'bakery sales % ')
# plt.xlabel(' Days of the week! ')
# plt.ylabel('Sales percentage! ')
# plt.title('bakery weekly sale! ')
# plt.legend(loc = 'upper left')
# plt.grid(linewidth = 1, linestyle = ':', color = 'gray')
# plt.show()

# import matplotlib.pyplot as plt

# x = ['mond', 'tuesd', 'wed', 'thursd', 'frid',' saturd', 'sund']
# y = [20,56,34,10,89,32,54]


# plt.plot(x, y, linewidth = 3, color = 'r', linestyle = '--', marker = 'o', label = 'bakery sales % ')
# plt.xlabel(' Days of the week! ')
# plt.ylabel('Sales percentage! ')
# plt.title('bakery weekly sale! ')
# plt.legend(loc = 'upper left')
# plt.show()

# import matplotlib.pyplot as plt
# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]

# plt.plot(x, y)
# plt.grid(True)   # turn on grid
# plt.show()
# import matplotlib.pyplot as plt

# def my_plot():          # custom function
#     x = [1, 2, 3, 4]
#     y = [2, 4, 6, 8]
#     plt.plot(x, y)
#     plt.title("My Function Plot")
#     plt.show()

# my_plot()   # call the function


# import matplotlib.pyplot as plt
# x = [1,2,3,4,5,6]
# y = [15,30,10,18,25,100]

# plt.plot(x, y)
# plt.show()
# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [2, 4, 6, 8]

# plt.plot(x, y, marker='o')  
# plt.show()
# import matplotlib.pyplot as plt
# x = [1, 2, 3]
# y1 = [2, 4, 6]
# y2 = [1, 2, 3]

# plt.plot(x, y1, label="Double")   # first line
# plt.plot(x, y2, label="Same")     # second line

# plt.legend()   # show legend box
# plt.show()

# x = [1, 2, 3]
# y = [2, 4, 6]

# plt.plot(x, y, label="Double Line")  # add label to the line
# plt.legend()  # show legend with that label
# plt.show()
# import matplotlib.pyplot as plt
# plt.plot([1,2,3], [2,4,6], color='red')  
# plt.show()
# plt.plot([1,2,3], [2,4,6], linestyle='--')  
# plt.show()


# x = [1, 2, 3]
# y = [2, 4, 6]

# plt.plot(x, y)
# plt.title("Simple Line Plot")   # add title
# plt.show()

