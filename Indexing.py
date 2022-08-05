import numpy as np

a = np.arange(1,21).reshape(4,5)
print(a)
print(a[0])
print(a[1])
print(a[0][0])
print(a[1,1])
print(a[0,1])
print(a.ndim)
print(a[0].ndim)

#Arraydeki elemanı değiştirme

a[1,1] = 10 #7'nin yerine 10 yazdık
print(a)

#Eğer float eklersek
a[1,1] = 20.5
print(a) #int olarak ekledi

#String olarak

a[1,1] = "30"
print(a) #Yine int'e çevirerek değiştirdi

#Hem string hem float bir değer koyarsak hata veriyor. 
#a[1,1] = "30.5" #Bu kod hata veriyor.

#Slice Indexing 

b = np.arange(1,21).reshape(4,5)
print(b)
print(a[1])
print(a[0:3])
print(a[:2])
print(a[0:])
print(a[:,3]) #Sadece 3. colom'un tüm row'larını aldık.
print(a[::2,3])
print(a[0,:])
print(a[:2,:3])
print(a[0:2,0:3])
print(a[::,:4])




