import numpy as np

#Random integarlar ile array oluşturmak

print(np.random.randint(1,10, (3,4)))

print(np.random.randint(1,10, (3,5,5)))

print(np.random.randint(1,2))

d= {}

for i in range(20000):
    val = np.random.randint(1,11)
    if val not in d:
        d[val] = 1
    else:
        d[val] += 1
print(d)