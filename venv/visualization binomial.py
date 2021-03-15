from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sus
x=sus.distplot(random.binomial(n=5,p=.5,size=1000),hist=True,kde=False)
plt.show()
