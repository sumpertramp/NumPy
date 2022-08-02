import numpy as np #numpy kütüphanesi import edildi

#Numpy arrayleri homojen olmalı. Yani içerisinde tek tip veri tipi olabilir.

x = np.array ([1,2,3,4]) #array (dizi) tanımlandı 
print(x)
print(type(x[1])) #Array'in bir elemanının türüne bakıldı. integer

y = np.array(["a", "b", "c"]) #String türünde array yaratıldı.
print(y)
print(type(y[1])) #Array'in bir elemanının türüne bakıldı. string

z = np.array([1,2,3,"a"]) #Karışık türde elemanları bulunan bir dizi yaratıldı.
print(z)
print(type(z[1])) #Görüldüğü gibi tüm elemanları dizi olarak algıladı.

a = np.array([1,2,3,"5"]) 
print(a)
print(type(a[1])) #Stringin içeriği sayı olmasına rağmen tüm elemanları string olarak algıladı.

b = np.array([1,2,3,4.5])
print(b)
print(type(b[1])) #Burada da son eleman float olduğu için tüm elemanları floata dönüştürdü.

c = np.array([1,2,3,4.5,"2"]) 
print(c)
print(type(c[1])) #Burada float ve int eleman olmasına karşılık tüm elemanları string olarak algıladı.

#NOT! Öncelik string, sonra float, sonra int

