import numpy as np

#Ardışık sayılardan array oluşturmak

print(np.arange(0,12)) #0'dan 12'e kadar tüm numaralardan oluşan bir dizi oluşturdu. 
#NOT 0 dahil 12 dahil değil

print(np.arange(2,12)) #'den başlayarak 12 'e kadar tüm numaralardan oluşan bir dizi oluşturdu
#NOT 2 dahil 12 dahil değil

print(np.arange(2,12,2)) #2'denb başlayarak 12'e kadar sayıları 2'şer 2'şer artırarak bir dizi oluşturdu
#NOT! 2 dahil, 12 dahil değil

print(np.arange(2,12,-2)) #İçi boş bir dizi oluşturdu Çünki 3. satıra 2 girdiğimizde 2'şer 2'şer geriye doğru sayma işlemi oluşturduk

print(np.arange(12,2,-2)) #12'den 2'e kadar geriye sayan bir dizi oluşturuldu
#NOT! 2 dahil değil



