import numpy as np

#Bir aralığı belirli bir sayıya bölmek

print(np.linspace(1,2, num = 3)) #1-2 aralığını 3'e bölerek 3 elemanlı dizi elde ettik

print(np.linspace(1,2,3)) #Yukarıdaki kodla aynı çıktıyı verdi

print(np.linspace(1,2, num = 3, endpoint = False)) #Son sayıyı dahil etmeden aralığı 3'e böldü

print(np.linspace(0,1,30)) #0-1 aralığından 30 adet eleman üreterek dizi oluşturdu

#Float türünde de belirtilen sayıya bölerek dizi elde edebiliyoruz

print(np.linspace(1.5, 4.7, 3))