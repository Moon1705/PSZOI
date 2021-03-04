from module.Exp import Exp
from module.G import G
from module.N import N
from module.R import R
from module.TN import TN
from module.W import W
from PSZOI import PSZOI


input_data = [TN(59,19), Exp(44), TN(70,28), G(12,78), R(39), N(84,20), W(5,65), TN(57,17)]
pszoi = PSZOI(input_data)
pszoi.show()
