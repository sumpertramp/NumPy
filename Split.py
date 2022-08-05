import numpy as np

#SPLİT
#Arraylerin belirli bir aralıklarındaki değerlerini alabilmek için kullanılır.

l = [10,20,30,40,50,60,70,80]
x = np.split(l,[2,6])
print(x) #Python listlerinde de çalışıyor ve sonucu np array olarak döndürüyor.

a = np.array([10,20,30,40,50,60,70,80])
y = np.split(a, [2,6])
print(y) #Görüldüğü gibi python arrayi ile np arrayi aynı sonucu verdi.

x1, x2 = (1,10)
print(x1)
print(x2)

c,d,e = np.split(l, [2,6])
print(c,d,e)
print(type(c))
print(type(c[1]))

#Split'in Sonucunu Birden Çok Değişkene Eşitleme - vsplit

l1 , l2 = (1,10)
print(l1)
print(l2)

f,g,h = np.split(l,[2,6])
print(f)
print(g)
print(h)

a = np.arange(20).reshape(2,10)
print(a)

b = np.vsplit(a, [1])
print(b)

c = np.split(a, [1])[0]
print(c)

#hsplit

d = np.hsplit(a, [2])
print(d)
print(d[0])
print(d[1])
