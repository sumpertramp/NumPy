import numpy as np

#Shape (Biçimlemek)
x = np.zeros((2,3))
print(x)
print(x.shape)

y = np.zeros((2,5,4))
print(y)
print(y.shape)

#ndim dizinin kaç boyutlu olduğunu bulmak için
print(x.ndim)
print(y.ndim)

#size Dizinin eleman sayısını verir
print(x.size)
print(y.size)

#dtype Dizi elemanın türünü verir. Str, int, float vs.
print(x.dtype)
print(y.dtype)