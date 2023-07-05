import numpy as np
import matplotlib.pyplot as plt


"""
This function is the representation of the quadratic math function, it recieve as parameter a set of values call "X" what
are meant to be evaluated
Esta funcion es la representacion de una funcion cuadratica, que recibe como parametro en conjunto de valores X que sera
evaluado
"""
def f(x):
  return x**2

"""
This function is the representation of the derivate of f(x) that recieve as parameter the math function,
in its body we have h what represent the approaching value of the function to 0 (limit)
Esta funcion es la representacion de la derivada de f(X) que recibe como parametro la funcion,
en el cuerpo de la tenemos a h que es el valor al que se aproxima la funcion (limite)
"""
def dy(f):
  h=0.00000000001
  return (f(x+h)-f(x))/h

x=np.linspace(-10,10,1000)
y=f(x)
dy=dy(f)

plt.grid()
plt.plot(x,y,'b')
plt.plot(x,dy,'r')
