import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
arr1=np.array([[1,2,3],[4,5,6]])

print(f"Dimension : {arr1.ndim}")  # number of dimensions
print(f"Shape of array : {arr1.shape}")  # shape of the array
print(f"Total elements in array : {arr1.size}")  # total number of elements
print(f"Data type of array elements : {arr1.dtype}")  # data type
print(f"Size of each element in bytes : {arr1.itemsize}")  # size of each element
print(f"Total size of the array in bytes : {arr1.nbytes}")  # total size in bytes

# Speacial Arrays
zArray=np.zeros((3,2))
print("Zero Array : \n",zArray)
oArray=np.ones((2,3))
print("One Array : \n",oArray)
eArray=np.eye(4)
print("Identity Array : \n",eArray)
# rArray=np.random.rand(3,3)
# print("Random Array : \n",rArray)

nArray=np.arange(0,12,2)
print("Array with range : \n",nArray)
print("Reshaped array : \n",nArray.reshape(2,3))
lArray=np.linspace(0,1,5)
print("Linearly spaced array : \n",lArray)