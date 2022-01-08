import math
from tabulate import tabulate


eps = 0.0001

def function(x1, x2):
    return math.pow(5*x1 - x2, 4) + math.pow(x1-2, 2) + x1 - 2*x2 + 12


def negative_transpose_gradient_function(x1, x2):
    y1 = 20*math.pow(5*x1 - x2, 3) + 2*(x1-2) + 1
    y2 = -4*math.pow(5*x1 - x2, 3) - 2
    return [-y1, -y2]


def function_alpha(x1, x2, alpha, d):
    x1 = x1 + alpha*d[0]
    x2 = x2 + alpha*d[1]
    return function(x1, x2)

def minimize(x1, x2, d, alpha, a, b):
    while abs(b - a) > eps:
        if function_alpha(x1, x2, alpha + eps, d) < function_alpha(x1, x2, alpha, d):
            a = alpha
        else:
            b = alpha
        alpha = (a + b) / 2
    return alpha

def length(x):
    return math.sqrt(x[0]*x[0] + x[1]*x[1])

def steepest_decent(x1, x2):
    d = negative_transpose_gradient_function(x1, x2)
    table = [[x1,x2,function(x1, x2)]]
    while length(d) > eps and math.sqrt(x1*x1 + x2*x2) > eps:
        alpha = minimize(x1, x2, d, 10, 0, 20)
        x1 = x1 + alpha*d[0]
        x2 = x2 + alpha*d[1]
        d = negative_transpose_gradient_function(x1, x2)
        table.append([x1,x2,function(x1, x2)])
    print(tabulate(table, headers=['x1', 'x2', 'f(x1, x2)']))
    return [x1, x2]

steepest_decent(1, 5)

