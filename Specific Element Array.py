from re import X
import numpy as np

#Belirtilen bir elemandan array oluşturmak

x = np.full((4,5), 5) #4 sütun 5 satırdan oluşan ve elemanları 5 elementinden oluşan bir array yaratıldı
print(x)

#print(np.full(4,5,5)) #Burada dizi tipi belirtilmediği için hata verdi

print(np.full(4,5)) #4 sütun 1 satırlı 5'lerden oluşan bir dizi yaratıldı.

print(np.full(4,5), "a") #a elemanıyla 5 sütun 4 satırdan oluşan bir dizi yaratıldı

print(np.full(4,5), 5.2) #5.2 float türünde elemanla 4 satır 5 sütundan oluşan bir dizi yaratıldı

print(np.full((4,5), 5.2, dtype = "str")) #Veritipi string olan ve 5'lerden oluşan (5.2'yi 5'e yuvarlayarak string yaptı) 4 satır 5 sütunlu bir dizi yaratıldı

print(np.full((4,5), 5.2)) #Aynı dizinin tür değiştirmeden gerçekleştirilmesi