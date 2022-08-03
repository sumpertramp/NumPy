#Array data tipini manuel olarak belirlemek. 

import numpy as np

x = np.array([1,2,3,4.6])
print(x) #float olarak çıktı verdi

y = np.array([1,2,3,4.6], dtype="int32")
print(y) #integer olarak çıktı verdi

z = np.array([1,2,3,4], dtype= "str")
print(z) #string olarak çıktı verdi.

#a = np.array(["a"], dtype = "int32")
#print(a) #string karakter inte dönüştürelemediği için hata verdi

b = np.array(["5"], dtype = "int32")
print(b) #integer olarak çıktı verdi