import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10)
y = (x**6-4)+50000*np.sin(3*x)*np.cos(3/2*x)*np.cos(6*x) + 150000*(np.exp(-(x*2)**2))
y2 = x*0+600000
y3 = (x**6-4)


plt.rcParams.update({'figure.autolayout': True})
plt.figure(figsize=(4,3))

plt.plot(x,y3,x,y3+250000,x,y3+500000,x,y3+750000,x,y3+1000000,x,y2, 'r--', color='k')
plt.annotate("$E_F$",xy=(3,650000))
plt.xticks([],[])
plt.yticks([],[])
plt.xlabel("$y$")
plt.ylabel("$E$")
plt.show()
