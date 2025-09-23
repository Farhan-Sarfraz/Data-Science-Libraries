import numpy as np
arr = np.array([ 1,2,3,4,5,6,7,8,9,10])

filter_array = []
for element in arr:
    if element%2 ==0:
        filter_array.append(True)
    else:
        filter_array.append(False)
new_array = arr[filter_array]
print(new_array)
print(filter_array)

# arr = np.array([3,8,3,7,1,5,0,6])
# filter_array = []

# for element in arr:
#     if element > 5:
#         filter_array.append(True)
#     else:
#         filter_array.append(False)

# new_array = arr[filter_array]
# print(new_array)
# print(filter_array)
# arr = np.array([44,55,66,77])
# x = [True, False, True, False]
# filter_array = arr[x]
# print(filter_array)
# print(x)

# arr1 = np.array([6,4,7,3,8,2,9,1,0,5,7])
# arr2 = np.array([True , False, True, False])
# print(np.sort(arr1))
# print(np.sort(arr2))
# arr = ['pakistan', 'india' , 'bangladesh']
# print(np.sort(arr))
# arr = np.array([1,2,3,4,5,4,4])
# print(arr)
# new_arr = np.where(arr == 4)
# print(new_arr)
# arr = np.array([1,2,3,4,5,6])
# arr2 = np.array_split(arr,3)
# print(arr2)

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# new_arr = np.array_split(arr, 4)
# print(new_arr)
# arr1 = np.array([[1,2,3],[10,22,33]])
# arr2 = np.array([[7,8,9],[77,88,99]])
# arr3 = np.concatenate((arr1, arr2 ) ,axis = 1)
# print(arr3)
# arr2= np.array([4,5,6])
# arr3 = np.concatenate((arr1, arr2))
# print(arr3)

# arr = np.array([4,5,6,7])
# for idx, x in np.ndenumerate(arr):
#     print(idx)
#     print(x)
# arr = np.array([[1,2,3,4],[8,9,0,6]])
# for idx, x in np.ndenumerate(arr):
#     print(idx)
#     print(x)
# for i in np.nditer(arr[: , ::2]):
#     print(i)
# for x in np.nditer(arr, flags = ['buffered'], op_dtypes = ['S']):
#     print(x)
# arr = np.array([[1,2,3],[4,5,6]])
# for x in np.nditer(arr):
#     print(x)
#     # print(arr)
# print(arr)
# arr = np.array([1,2,3,4])
# for x in np.nditer(arr):
#     print(x)

# arr=np.array([[5,6,7],[9,8,2]])
# for x in arr:
#     for y in x:
#         print(y)
        
# arr = np.array([[2,3,5,8],[3,4,5,6]])
# print(arr.shape)
# # arr = np.array([1,2,3,4])
# print(arr)
# a = arr.copy()
# arr[0] = 34
# print(arr)
# print(a)
# arr=np.arange(12)
# # print(arr)
# reshaped =arr.reshape((3,4))
# print(reshaped)

# flattened = reshaped.flatten()
# print(flattened)

# ravelled =reshaped.ravel()
# print(ravelled)
# transpose = reshaped.T
# print(transpose)
# arr=np.array([[1,2,3,4,5],[4,5,6,7,8]])
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
# print(arr.ndim)
# print(arr.transpose())
# print(arr.itemsize)
# arr = np.random.random((2,3))
# arr = np.arange(0,10,3)
# print(arr)
# arr = np.array([1,2,3,4,5,7,8,9,0,4,2,])
# print(arr.dtype)

# arr = np.array([2.3,'56',88])
# print(arr.dtype)

# arr=np.array(67)
# arr1=np.array([1,2,3,4,5,6])
# arr2=np.array([[1,2,3],[3,4,5]])
# arr3=np.array([[[1,2,3],[2,3,4]],[[2,3,4],[5,6,7]]])
# print(arr2[1,1:3])
# print(arr2[0:3,0])
# print(arr1[0:6:2])
# print(arr1[::2])
# print(arr1[0:])
# print(arr1[:3])
# print(arr1[:-3])

# print(arr)
# print(arr1[2])
# print(arr2[0,2])
# print(arr3[1,1,2])
# print(arr3[1,1,-2])

# print(arr.ndim)
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)
# print(type(arr))
# print(type(arr1))
# print(type(arr2))
# print(type(arr3))


# arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
# print(arr3d)
# arr2d = np.array([[1,2,3], [3,4,5]])
# print(arr2d)
# arr1d = np.array([1,2,3,4])
# print(arr1d)
# arr = np.array(23)
# print(arr)

# sp_arr = np.zeros((3, 3))
# arr=np.ones((2,3))
# arr1 = np.linspace(0,1,5)
# arr2=np.arange(100)
# arr3 = np.eye(4)
# print(arr3)
# print(sp_arr)
# print(arr)
# print(arr1)
# print(arr2)
# arr = np.array([[1,2,3],[3,4,5],[5,6,7]])
# print(arr)
# print(type(arr))
# print(arr * 2)

# arr = np.array([1,2,3,4])
# print(arr)
# print(type(arr))
# print(arr * 2)