import matplotlib.pyplot as plt
import numpy as np

x,y=np.loadtxt('vdp-korr.csv',delimiter=' ',unpack=True)

plt.rcParams.update({'figure.autolayout': True})
plt.figure(figsize=(4,3))

plt.plot(x,y)
plt.xscale('log')
plt.xlabel("$Q$")
plt.ylabel("$f(Q)$")
plt.show()
