import numpy as np
from constants import kB
T_C = np.arange(50,90,10)
T_K = T_C + 273.15
p = (10**(8.22127-4006.048/T_K - 0.00060194*T_K - 0.19623*np.log10(T_K)))*133.322
n = p*1e-6/(kB*T_K)
print(n)
print(n/n[0])

