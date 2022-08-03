import numpy as np

print(np.zeros(10)) #10 sütun 1 satırlık sıfırlardan oluşan bir dizi oluşturdu

print(np.zeros(10, dtype = str)) #İçi boş 10 adet stringli bir dizi oluşturdu

#Elemanları 0'lardan oluşan multimensional array oluşturmak

print(np.zeros((3,4))) #3 sütunlu 4 satırlı 0'lardan oluşan bir dizi

#print(np.zeros(3,4)) #Burda dizi tipi type mi list mi belirtilmediği için hata verdi


print(np.zeros([3,4])) #3 sütun 4 satırdan oluşan list tipinde bir dizi oluşturdu

print(np.zeros([3,8,8])) # 3 adet  satır 8 sütunlu 0'lardan oluşan list türünde bir dizi oluşturdu

print(np.zeros(2, dtype = int)) #int türünde 2 sütun 1 satırlı bir dizi oluşturdu

print(np.zeros((1,2), dtype = int)) #2 sütun 1 satırdan oluşan, int türünde list içinde list oluşturdu

print(np.zeros((2,3), dtype = bool)) #2 satır 1 sütundan oluşan boolean türünde list içinde list oluşturuldu 