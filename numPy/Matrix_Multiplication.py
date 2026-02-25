import numpy as np
arr1= np.array([[1,2],[4,5]])
print("First Matrix: ",arr1)
arr2=np.array([[4,5],[1,2]])
print("Second Matrix: ",arr2)

#Matrix Multiplication by dot() method
print(np.dot(arr1,arr2),"\n")

#Matrix Multiplication by @ Symbol
print(arr1 @ arr2,"\n")

#Matrix Multiplication by matmul() method
print(np.matmul(arr1,arr2),"\n")

