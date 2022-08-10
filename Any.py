import numpy as np

#Any
#Herhangi bir eleman verilen şartı sağlıyormu diye kontrol etmek için kullanılır. 

a = np.arange(20).reshape(4,5)
print(a)
print(a>17)
print(np.any(a>17))
print(np.any(a>17, axis = 0))
print(np.any(a>17, axis = 1))

a=np.arange(1,21).reshape(4,5)
print(np.any(a>4,axis=0))