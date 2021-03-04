import scipy.integrate as integrate
import math

class N:
    def __init__(self, m, sig):
        self.m = m * 10000
        self.sig = sig * 10000

    def p_func(self, t):
        return 0.5 - self.__F_0((t - self.m) / self.sig)

    def f_func(self, t):
        return (1 / (self.sig * math.sqrt(2 * math.pi))) * math.exp(-pow((t - self.m), 2) / ( 2 * self.sig * self.sig))
    
    def __F_0(self, y):
        return (1 / math.sqrt(2 * math.pi)) * integrate.quad(lambda x: math.exp(-x * x / 2), 0, y)[0]
