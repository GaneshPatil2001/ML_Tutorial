import numpy as np
arr1= np.array([[1,2],[4,6]])
print("Given array : ",arr1,"\n")

print("Adding 5 to the whole array: ",arr1+5,"\n")

arr2=np.array([[3],[2]])
print("Addition: ",arr1+arr2)

#Axis Concept
print("\nColumn Based addition : ",np.sum(arr1,axis=0))

print("\nRow Based addition : ",np.sum(arr1,axis=1))



