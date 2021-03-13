import numpy as np
arr=np.array([12,3,4,5,6])
x=arr.view()
arr[0]=65
print(x)
print(arr)
