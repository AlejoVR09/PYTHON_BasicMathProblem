from sympy import * 
init_printing( use_latex='mathjax' )
x = Symbol('x')
expr = x**4 - 3*x**2
# ^^ esta es nuestra expresion
expr_d = Derivative(expr, x, evaluate=True)
# ^^ esta es la derivada de nuestra expresion
Eq(expr_d, 0)

solve(Eq(expr_d, 0))
