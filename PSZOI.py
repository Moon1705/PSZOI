import math
from functools import reduce
from prettytable import PrettyTable
import scipy.integrate as integrate
import numpy as np

class PSZOI:
    def __init__(self, input_data):
        self.input_data = input_data
        self.m = [element.m for element in self.input_data]
        self.sig = [element.sig for element in self.input_data]
        self.T_1c = self.__T_1c_func()
        self.p = self.__p_func()
        self.f = self.__f_func()
        self.lambd = self.__lambd_func()
        for t in range(11):
            self.f[t].append(self.p[t][-1] * self.lambd[t][-1])
        
    def __T_1c_func(self):
        h = 100000
        r = (h / 3) * (1 + sum([3 + (pow(-1, k) * self.input_data[0].p_func(k * h) * self.input_data[1].p_func(k * h) * self.input_data[2].p_func(k * h) * self.input_data[3].p_func(k * h)  * self.input_data[4].p_func(k * h) * self.input_data[5].p_func(k * h)  * self.input_data[6].p_func(k * h) * self.input_data[7].p_func(k * h)) for k in range(1, 11)]))
        return r

    def __p_func(self):
        p = []
        for t in range(11):
            t_i = t * 100000
            p_i = [element.p_func(t_i) for element in self.input_data]
            p.append(p_i + [reduce(lambda x, y: x * y, p_i)])
        return p
    
    def __f_func(self):
        f = []
        for t in range(11):
            t_i = t * 100000
            f_i = [element.f_func(t_i) for element in self.input_data]
            f.append(f_i)
        return f

    def __lambd_func(self):
        lambd = []
        for t in range(11):
            t_i = t * 10000
            lambd_i = []
            for j in range(len(self.input_data)):
                if self.f[t][j] == 0:
                    lambd_j = 0
                else:
                    lambd_j = self.f[t][j] / self.p[t][j]
                lambd_i.append(lambd_j)
            # lambd_i = [self.f[t][j] / self.p[t][j] for j in range(len(self.input_data))]
            lambd.append(lambd_i + [sum(lambd_i)])
        return lambd
    
    def show(self):
        tables = [PrettyTable() for _ in range(4)]
        tables[0].field_names = ["МЗ 1", "МЗ 2", "МЗ 3", "МЗ 4", "МЗ 5", "МЗ 6", "МЗ 7", "МЗ 8"]
        tables[0].add_row(list(map(lambda x: int(round(x / 10000)), self.m)))
        tables[0].add_row(list(map(lambda x: int(round(x / 10000)), self.sig)))
        for i in range(11):
            tables[1].add_column(f"{i} * 10^(5)", list(map(lambda x: int(round(x * 10000)), self.p[i])))
            tables[2].add_column(f"{i} * 10^(5)", list(map(lambda x: round(x * 1000000, 3), self.f[i])))
            tables[3].add_column(f"{i} * 10^(5)", list(map(lambda x: round(x * 1000000, 3), self.lambd[i])))
        for i in range(4):
            print(tables[i])
        print(f"T_1c = {self.T_1c}")
