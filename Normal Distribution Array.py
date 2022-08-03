import numpy as np

#Normal distribution(dağılım)'dan örnekler almak

print(np.random.normal(0,1, (4,5))) #4 satır 5 sütunlu bir dizi oluşturacak şekilde örnekler aldı

print(np.random.normal(0,100,(4,5)))

print(np.random.normal(10,100, (4,5)))

print(np.random.normal(10,1,(4,5)))