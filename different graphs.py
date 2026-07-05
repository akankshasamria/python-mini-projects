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


fig = plt.figure(figsize=(15, 9))

ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

ax1.plot(x, y,c = '#ff3300',marker = '+',markersize = '8',linestyle = '-.', label = 'sin')
ax1.set_xlabel('linear values',fontsize = 15)
ax1.set_ylabel('sin', fontsize = 15)
ax1.set_title('Sin', fontsize = 20) 


ax2.scatter(x, z, c = 'green', marker = '*',s =50,label ='cos')
plt.show()


fig = plt.figure(figsize=(15, 9))

ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)



plt.plot(x, y,c = '#ff3300',marker = '+',markersize = '8',linestyle = '-.', label = 'sin')
ax1.set_xlabel('sin', fontsize =15)
ax1.set_ylabel('sin', fontsize = 15)
ax1.set_title('Sin', fontsize = 20) 


marks = [92 ,93 ,74 ,91 ,75]
names =["Akanksha", "Yuvraj" ,"selja" ,"Tushar" ,"pooja"]

fig = plt.figure(figsize=(10, 5))
bar_list = plt.bar(names, marks, color ='#37213B', width = 0.6)   
bar_list[-1].set_color('red')
plt.show()


fig = plt.figure(figsize=(10, 5))
bar_list = plt.barh(names, marks, color ='#37213B')   
bar_list[-1].set_color('red')
plt.show()


x = np.random.normal(0, 4, 1000000)
plt.hist(x, bins = 100)
plt.show()

ice_creams = [30, 23, 12, 21, 4, 10]
names = ["mango", "orange", "butterscotch", "vanilla", "rubdi kulfi", "pineapple"]
plt.pie(ice_creams, labels = names)
plt.show()


x = np.random.normal(110, 50,(100, 3))
plt.boxplot(x)
plt.show()


plt.violinplot(x)
plt.show()

subjects = ['Python', 'C++', 'Java', 'AI']
percentages = [85, 70, 60, 95]
plt.figure(figsize=(8,5))

bars = plt.bar(subjects, percentages)
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        f'{height}%',
        ha='center',
        va='bottom'
    )
plt.xlabel('Subjects')
plt.ylabel('Percentage')
plt.title('Subject-wise Percentage')
plt.ylim(0, 100)
plt.show()


plt.bar(subjects, percentages,
        color=['red', 'blue', 'green', 'orange'])

Student = ['A', 'B', 'C', 'D']
Percentage = [78, 85, 92, 67]
df = pd.DataFrame({
    'Student': ['A', 'B', 'C', 'D'],
    'Percentage': [78, 85, 92, 67]
})

bars = plt.bar(df['Student'], df['Percentage'])

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f'{bar.get_height()}%',
        ha='center'
    )
plt.show()
plt.bar(Student, Percentage, color= ['red', 'blue', 'green', 'orange'])
plt.show()

