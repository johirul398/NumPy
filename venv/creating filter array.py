import numpy as np
a=np.array([1,56,2,3,4,5,12,57,98,11,34])
x=[]
for w in a:
    if w>42:
        x.append(True)
    else:
        x.append(False)
c=a[x]
print(c)
