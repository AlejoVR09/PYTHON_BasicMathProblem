import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return x**2

def dy(f):
  h=0.00000000001
  return (f(x+h)-f(x))/h

x=np.linspace(-10,10,1000)
y=f(x)
dy=dy(f)

plt.grid()
plt.plot(x,dy,'r')
plt.plot(x,y,'b')
