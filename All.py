import numpy as np

#All
#Tüm elemanların verilen şartı sağlayıp sağlamadığını kontrol etmek için kullanılır. 

a = np.arange(20).reshape(4,5)
print(a)
print(np.all(a>-1)) #True/False döndürür.

filt = a>-1
print(np.all(filt))
print(np.all(a>-1, axis=1))
print(np.all(a>-1, axis=0))

a=np.arange(1,21).reshape(4,5)

print(np.all(a>8,axis=1))