#Fancy Indexing
#Şimdiye kadar hep belirli elemanları, belirli kesitlerdeki elemanları, 
#veya belirli sayıda atlaya atlaya elamanları almayı gördük. 
#Fancy Indexing ile birden fazla belirli indexlerdeki elemanları 
#bana döndür diyebilmiş olacağız. 

import numpy as np

x = np.arange(1,15)
print(x)

idxs = [4,5,7,11]
print(x[idxs]) #Seçtipğimiz index'teki değerleri çağırdı. 

a = np.arange(12).reshape(3,4)
print(a)

print(a[0:2,1])
print(a[0:2,1].shape)
print(a[0:2,1:3])
print(a[0:2,1:3].shape) 

print(a[0, [1,3]])
print(a[0:,[1,3]])

a = np.arange(20).reshape(4,5)
print(a)

idx1 = [1,3,2]
idx2 = [3,0,2]
print(a[idx1,idx2])
#print(a[idx1][idx2].shape) Bu kod hata veriyor.

#Fancy indexing sonucunu belirli değerlere eşitlemek

print(x)
x[[1,2,3]] = 20
print(x)

x = np.arange(9)
print(x)

x[[1,2,3]] = [100,200,300]
print(x)
