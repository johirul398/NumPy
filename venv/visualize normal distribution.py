from numpy import random
import matplotlib.pyplot as plt 
import seaborn as sus
x=sus.distplot(random.normal(size=1000),hist=False)
plt.show()
