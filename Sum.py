from re import X
import numpy as np

#Sum
#Verilen Condition'ı kaç elemanın sağladığını bulalım.

a = np.arange(1,21).reshape(4,5)
print(a)
print(np.sum(a))

filt = a<5
print(np.sum(filt)) #Filtreye uyan kaç tane eleman varsa onun sayısını verdi.

a[filt]
print(np.sum(a[filt])) #Burada filtreli elemanların toplamı alındı. 

print(np.sum(a[(a>5)&(a<9)])) 
filt = ~((a>5)&(a<9))
print(np.sum(a[filt]))

print(np.sum(~((a>5)&(a<9))))

print(np.sum(a[~((a>5)&(a<9))]))

#Belirli axis üzerinde toplama

print(np.sum(a, axis = 0).shape) #Rowları toplayıp ayrı ayrı yazdı

print(np.sum(a, axis = 1))

 