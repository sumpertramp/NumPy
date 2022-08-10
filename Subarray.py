#Subarray 
#Arrayimizin bir alt parçasına erişip onunla işlem yapmayı göreceğiz. 

import numpy as np

a = np.arange(1,21).reshape(4,5)
print(a)

b = a[:2,:3]
print(b)
print(b.ndim)
b[0,0] = 100
print(b)
print(a) #adaki de 100 oldu. 

#copy() metodunu kullanırsak subarrayın değerinin değişmesi orjinal arrayi etkilemez.

a = np.arange(1,21).reshape(4,5)
print(a)
b = a[:2,:3].copy()
print(b)
b[0,0] = 100
print(b)
print(a) #Etkilenmedi
  