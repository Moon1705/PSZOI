from scipy.special import gamma
import math

class W:
    def __init__(self, alfa, betta):
        self.alfa = alfa
        self.betta = betta * 10000
        self.m = self.m_func(self.alfa, self.betta)
        self.sig = self.sig_func(self.alfa, self.betta)

    def m_func(self, alfa, betta):
        return betta * gamma(1 + 1 / alfa)

    def sig_func(self, alfa, betta):
        return betta * math.sqrt(gamma(1 + (2 / alfa)) - pow(gamma(1 + (1 / alfa)), 2))

    def p_func(self, t):
        return math.exp(-pow(t / self.betta, self.alfa))

    def f_func(self, t):
        return ((self.alfa * pow(t, (self.alfa - 1))) / pow(self.betta, self.alfa)) * math.exp(-pow(t / self.betta, self.alfa))
