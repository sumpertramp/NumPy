import numpy as np

#Concatenation
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
print(a)
print(b)

#a veya b güncellenemez
x = np.concatenate([a,b]) #Burada iki list birleştirildi
print(x)

#Python listlerini de numpy arraylari ile concatenation'a sokabiliriz.
l1 = [10,11]
print(np.concatenate([a,b,l1]))
l2 = [10,11, "11.2"]
print(np.concatenate([a,b,l2])) #Hepsi float oldu

#Python tuple'larını da numpy arrayleri ile concatenation'a sokabiliriz
l3 = (10,11)
print(np.concatenate([a,b,l3]))

#Size Mismatch (Eleman sayısı uyumsuzluğu)
y = np.array([[1,2,3],[4,5,6]])
print(y)
print(y.size)
print(y.shape)
print(a.size)
print(a.shape)

# shape mismatch
#print(np.concatenate([y,a])) Row-coloumn mantığı uymadığı uymadıpı için hata verdi

print(np.concatenate([y,y]))
print(np.concatenate([y,y], axis=1)) #axis birleştirme doğrultusu ayarlama





