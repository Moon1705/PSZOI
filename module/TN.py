import scipy.integrate as integrate
import math

class TN:
    def __init__(self, m0, sig0):
        self.m0 = m0 * 10000
        self.sig0 = sig0 * 10000
        self.m = self.m_func(self.m0, self.sig0)
        self.sig = self.sig_func(self.m0, self.sig0)

    def m_func(self, m0, sig0):
        return m0 + self.__k(m0 / sig0) * sig0

    def sig_func(self, m0, sig0):
        return sig0 * math.sqrt(1 + self.__k(m0 / sig0) * (m0 / sig0) - math.pow(self.__k(m0 / sig0), 2))

    def p_func(self, t):
        return self.__c(self.m0 / self.sig0) * (0.5 - self.__F_0((t - self.m0) / self.sig0))

    def f_func(self, t):
        return (1 / (self.sig0 * math.sqrt(2 * math.pi))) * math.exp(-pow((t - self.m0), 2)/(2 * self.sig0 * self.sig0))
    
    def __F_0(self, y):
        return (1 / math.sqrt(2 * math.pi)) * integrate.quad(lambda x: math.exp(-x * x / 2), 0, y)[0]

    def __c(self, y):
        return 1 / (0.5 + self.__F_0(y))

    def __k(self, y):
        return (self.__c(y) / math.sqrt(2 * math.pi)) * math.exp(-y * y / 2)
