from scipy.special import gamma, gammainc
import math

class G:
    def __init__(self, alfa, betta):
        self.alfa = alfa
        self.betta = betta * 1000
        self.m = self.m_func(self.alfa, self.betta)
        self.sig = self.sig_func(self.alfa, self.betta)

    def m_func(self, alfa, betta):
        return alfa * betta

    def sig_func(self, alfa, betta):
        return math.sqrt(alfa) * betta

    def p_func(self, t):
        return 1 - gammainc(self.alfa, t / self.betta)

    def f_func(self, t):
        return ((pow(t, (self.alfa - 1))) / (pow(self.betta, self.alfa) * gamma(self.alfa))) * math.exp(-(t / self.betta))
