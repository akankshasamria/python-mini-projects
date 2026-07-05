import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

x = np.linspace(0, 10 , 50)
x

np.sin(x)

y = np.sin(x)
z = np.cos(x)

plt.figure(figsize=(15, 9))
plt.plot(x, y,c = '#ff3300',marker = '+',markersize = '8',linestyle = '-.', label = 'sin')
plt.plot([0, 10], [0, 100])
plt.scatter(x, z,c ='green',marker = '*',s = 50, label = 'cos')
plt.xlabel('linear values',fontsize = 15)
plt.ylabel('sin', fontsize = 15)
plt.title('Sin', fontsize = 20) 
plt.xticks(range(0,11))
#plt.yticks(range(0, 11))
#plt.xlim([0, 2*np.pi])
#plt.ylim([-1,1])
plt.grid()
plt.legend()
plt.show()




