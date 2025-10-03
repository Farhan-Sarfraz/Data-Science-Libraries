# import matplotlib.pyplot as plt

# study_time = [1,2,3,4,5,6,7,8]
# exam_marks = [20,30,40,50,60,70,80,90]

# plt.scatter(study_time, exam_marks, color = 'green', marker = 's', label = 'student studied time')
# plt.xlabel('studied time ')
# plt.ylabel('student obtained marks ')
# plt.legend('upper left side')
# plt.title('student relationship with time and marks ')
# plt.grid(True)

# plt.show()

# import matplotlib.pyplot as plt

# plt.scatter([1,2,3,4], [45,55,77,90], color = 'red', marker = '^', label = 'Class A')
# plt.scatter([1,2,3,4], [70,80,90,40], color = 'green', marker = 'o', label = 'Class B')

# plt.xlabel('study time')
# plt.ylabel('marks obtained')
# plt.title('Class A and Class B Student Data')
# plt.legend()
# plt.grid(True)

# plt.show()


# import matplotlib.pyplot as plt 

# x = [1,2,3,4]
# y = [15,20,25,30]

# plt.subplot(1,2,1)
# plt.title('line chart')
# plt.plot(x, y)

# plt.subplot(1,2,2)
# plt.title('bar char')
# plt.bar(x, y)

# plt.tight_layout()
# plt.show()


# import matplotlib.pyplot as plt

# fig , ax = plt.subplots(1,2, figsize= (10,5))

# x = [1,2,3,4]
# y = [15,40,25,30]

# ax[0].plot(x, y)
# ax[0].set_title('line chart')

# ax[1].bar(x, y)
# ax[1].set_title('bar chart')

# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [30,78,27,56]

plt.plot(x,y, color = 'green', marker = 'o')
plt.title('students marks in subject')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.grid(True)

plt.savefig('line_plot.png', dpi = 300 , bbox_inches = 'tight')
plt.show()