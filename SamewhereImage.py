import pandas as pd
import matplotlib.pylab as plt

x1 = pd.read_csv('Lyangchi1.csv')
y1 = x1.pop('Data')
x2 = pd.read_csv('Lyangchi2.csv')
y2 = x2.pop('Data')
x3 = pd.read_csv('Lyangchi3.csv')
y3 = x3.pop('Data')
x4 = pd.read_csv('Lyangchi4.csv')
y4 = x4.pop('Data')
x5 = pd.read_csv('Lyangchi5.csv')
y5 = x5.pop('Data')
x6 = pd.read_csv('Lyangchi6.csv')
y6 = x6.pop('Data')
plt.ylim([0,1200000])
plt.scatter(x1,y1,s=1, label='1')
plt.scatter(x2,y2,s=1, label='2')
plt.scatter(x3,y3,s=1, label='3')
plt.scatter(x4,y4,s=1, label='4')
plt.scatter(x5,y5,s=1, label='5')
plt.scatter(x6,y6,s=1, label='6')
plt.legend()
plt.savefig('Yangchi.png')
plt.show()