import numpy as np

#Reshaping Bir dizinin şeklini değiştirmek, yeniden şekillendirmek
#Reshape yapacağımız yapının yaptıktan sonraki yapıyla aynı eleman 
#sayısına sahip olması gerekiyor, yani size'ları aynı olacak

a = np.arange(1,11)
print(a)
print(a.ndim)
print(a.size)

b = a.reshape(2,5) ##Burada eleman sayısı tutmazsa hata alırız
print(b)
print(b.ndim) 
print(b.size)

#c = a.reshape(6,2) #Burada eleman sayısı tutmadığı için hata aldık

#-1 boyuta karar vermek

d = a.reshape(-1,2)
print(d) 

#Yeni boyut eklemek
e = np.arange(1,11)
print(e[np.newaxis, :])
print(e[np.newaxis :].shape)

# column vektor
print(e[:, np.newaxis])
print(e[:, np.newaxis].shape)

#Veya none yazarak yapabiliriz
print(a[None, :])
print(a[:, None])

