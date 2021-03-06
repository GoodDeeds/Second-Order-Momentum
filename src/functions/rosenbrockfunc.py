# RosenBrock function
# Global mininma at (a, a**2)

import numpy as np
from function import Function


class RosenbrockFunc(Function):
    
    def __init__(self, a=1, b=100):
        self.a = a
        self.b = b
    
    def f(self, x):
        assert x.shape[0] == 2, "Passed point is not 2 dimensional"
        return (self.a - x[0])**2 + self.b*(x[1]-x[0]**2)**2
        
    def grad_f(self, x):
        assert x.shape[0] == 2, "Passed point is not 2 dimensional"
        grad_f_x1 = -2*(self.a - x[0]) - 4*self.b*(x[1] - x[0]**2)*x[0]
        grad_f_x2 = 2*self.b*(x[1] - x[0]**2)
        return np.array([grad_f_x1, grad_f_x2])
        
    def grad2_f(self, x):
        assert x.shape[0] == 2, "Passed point is not 2 dimensional"
        second_term = -4*self.b*x[0]
        grad2_f_x1_x1 = 2 - 4*self.b*(x[1] - x[0]**2) + 8*self.b*x[0]**2
        grad2_f_x2_x2 = 2*self.b
        return np.array([[grad2_f_x1_x1, second_term], [second_term, grad2_f_x2_x2]])
        
    def fstar(self):
        return 0
        
    def __str__(self):
        return "Rosenbrock Function"
        
    def levels(self):
        return np.linspace(0, 10000, 15)
        
    def domain(self):
        return [[-3, 3],[-6, 6]]
        
    def start_x(self):
        return np.array([2, 3])
        
