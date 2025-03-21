"""
Logistic映射与混沌系统研究
"""



import numpy as np
import matplotlib.pyplot as plt
def logistic(r):
    x=0.5
    num=[x]
    for i in range(0,61):
        t=r*x*(1-x)
        x=t
        num.append(t)
    return num


print(logistic(2))
print(logistic(3.2))
print(logistic(3.45))
print(logistic(3.6))
num2=logistic(2)
num3_2=logistic(3.2)
num3_45=logistic(3.45)
num3_6=logistic(3.6)
x=np.arange(61)
for i in x:
    plt.plot(i,num2[i],'r-s',i,num3_2[i],'g-^',i,num3_45[i],'y-^',i,num3_6[i],'b-o')
plt.show()
for r in np.arange(2.6,4,0.001):
    a=0.5
    for i in range(0, 251):
            t = r * a * (1 - a)
            a = t
            if i>=100:
              plt.plot(r,a,'b-s')
plt.show()


