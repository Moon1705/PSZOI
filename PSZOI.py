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
            t_i = t * 100000
            p_i = [element.p_func(t_i) for element in self.input_data]
            p.append(p_i + [reduce(lambda x, y: x * y, p_i)])
        return p
    
    def __f_func(self):
        f = []
        for t in range(11):
            t_i = t * 10000
            f_i = [element.f_func(t_i) for element in self.input_data]
            f.append(f_i + [sum(f_i)])
        return f

    def __lambd_func(self):
        lambd = []
        for t in range(11):
            t_i = t * 10000
            p_i = [element.p_func(t_i) for element in self.input_data] 
            p_i += [reduce(lambda x, y: x * y, p_i)]
            f_i = [element.f_func(t_i) for element in self.input_data]
            f_i += [sum(f_i)] 
            lambd_i = [f_i[j] / p_i[j] for j in range(len(self.input_data) + 1)]
            lambd.append(lambd_i)
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
        print(f"T_1c = {int(self.T_1c / 1000)}")
