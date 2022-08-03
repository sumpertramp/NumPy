import numpy as np

#Array işlemleri

# * (çarpma) işlemi iki list arasında tanımsızdır, hata verir.

a = [1,2,3]
b = [2,4,8]
#print(a*b) Beklendiği gibi hata verdi

#List ile integer çarpılırsa ard arda concatenation(birleşim) yapar
print(a*3)

# * (çarpma) operatörü iki numpy arasında tanımlanır. Element-wise(eleman bazlı) çarpma yapar
a = np.array([1,2,3])
b = np.array([2,4,8])
print(a*b)

# Element-wise çarpım yaptığı için çarpılan iki array'in eleman sayısı aynı olmalıdır.
'''x1 = np.array([1,2,3])
x2 = np.array([2,4,8,10])
print(x1*x2)''' #Beklendiği gibi hata verdi

# Normalde + işlemi iki adet list için concatenation(birleştirme) yapar
y1 = [1,2,3]
y2 = [2,4,8]
print(y1 + y2)
