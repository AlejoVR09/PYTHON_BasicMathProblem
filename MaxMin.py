from sympy import * 

"""
This function refers to a more legible represetation using a tiposetter
x represents the math's variable X
expr represents an expression
"""
init_printing( use_latex='mathjax' )
x = Symbol('x')
expr = x**4 - 3*x**2

"""
expr_d represents the derivation of the expression
Eq is a function to make a equation equal to any value for resolving it
"""
expr_d = Derivative(expr, x, evaluate=True)
Eq(expr_d, 0)


"""
solve is use for resolving equations
"""
solve(Eq(expr_d, 0))
