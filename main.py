from module.Exp import Exp
from module.G import G
from module.N import N
from module.R import R
from module.TN import TN
from module.W import W
import math
from functools import reduce
from prettytable import PrettyTable


class PSZOI:
    def __init__(self, input_data):
        self.input_data = input_data
        self.m = [element.m for element in self.input_data]
        self.sig = [element.sig for element in self.input_data]
        self.T_1c = self.__T_1c_func()
        self.p = self.__p_func()
        self.f = self.__f_func()
        self.lambd = self.__lambd_func()
        
    def __T_1c_func(self):
        h = 100000
        return (h / 3) * (1 + sum([3 + pow(-1, k) * reduce(lambda x, y: x * y, [element.p_func(k * h) for element in self.input_data]) for k in range(1, 11)]))
    
    def __p_func(self):
        p = []
        for t in range(11):
            t_i = t * 0.00001
            p_i = [element.p_func(t_i) for element in self.input_data]
            p.append(p_i + [reduce(lambda x, y: x * y, p_i)])
        return p
    
    def __f_func(self):
        f = []
        for t in range(11):
            t_i = t * 0.00001
            f_i = [element.f_func(t_i) for element in self.input_data]
            f.append(f_i + [sum(f_i)])
        return f

    def __lambd_func(self):
        lambd = []
        for t in range(11):
            lambd_i = [self.f[t][i] / self.p[t][i] for i in range(len(self.input_data) + 1)]
            lambd.append(lambd_i)
        return lambd
    
    def show(self):
        tables = [PrettyTable() for _ in range(4)]
        tables[0].field_names = ["МЗ 1", "МЗ 2", "МЗ 3", "МЗ 4", "МЗ 5", "МЗ 6", "МЗ 7", "МЗ 8"]
        tables[0].add_row(list(map(lambda x: int(round(x / 10000)), self.m)))
        tables[0].add_row(list(map(lambda x: int(round(x / 10000)), self.sig)))
        for i in range(11):
            tables[1].add_column(f"{i} * 10^(-5)", list(map(lambda x: int(round(x * 10000)), self.p[i])))
            tables[2].add_column(f"{i} * 10^(-5)", list(map(lambda x: round(x * 1000000, 3), self.f[i])))
            tables[3].add_column(f"{i} * 10^(-5)", list(map(lambda x: round(x * 1000000, 3), self.lambd[i])))
        print("Вариант 10\n")
        for i in range(4):
            print(tables[i])
        print(f"T_1c = {int(self.T_1c * 0.001)}")


if __name__ == '__main__':
    input_data = [TN(59,19), Exp(44), TN(70,28), G(12,78), R(39), N(84,20), W(5,65), TN(57,17)]
    pszoi = PSZOI(input_data)
    pszoi.show()
