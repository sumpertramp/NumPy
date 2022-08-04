import numpy as np

#Stack(yığın) mantığını, yeni dimension(boyut) ekleyip o dimension üzerinde concanetation yaparak sağlayabiliriz.

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(a)
print(b)

print(a.shape)
print(b.shape)

print(np.stack([a,b])) #Burada row-coloumn mantığı ile birlikte axis'i otomatik 0 alarak yatay birleştirme yaptı. 

print(np.stack([a,b], axis = 1)) #Burada axisi biz girdik ve dikey birleştirme yaptık.

#Sonuç olarak stack ile yeni bir diemention(boyut) yaratıp onun üzerinde birleştirme yapıyoruz.