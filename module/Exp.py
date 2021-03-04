import math

class Exp:
    def __init__(self, lam):
        self.lam = lam * 0.00000001
        self.m = self.m_func(self.lam)
        self.sig = self.sig_func(self.lam)
    
    def m_func(self, lam):
        return 1 / lam
    
    def sig_func(self, lam):
        return 1 / lam

    def p_func(self, t):
        return math.exp(-self.lam * t)

    def f_func(self, t):
        return self.lam * math.exp(-self.lam * t)
