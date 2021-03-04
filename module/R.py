import math

class R:
    def __init__(self, lam):
        self.lam = lam * 0.00000000000001
        self.m = self.m_func(self.lam)
        self.sig = self.sig_func(self.lam)
    
    def m_func(self, lam):
        return math.sqrt(math.pi / (4 * lam))

    def sig_func(self, lam):
        return math.sqrt((4 - math.pi)/(4 * lam))

    def p_func(self, t):
        return math.exp(-self.lam * t * t)

    def f_func(self, t):
        return 2 * self.lam * t * math.exp(-self.lam * t * t)
