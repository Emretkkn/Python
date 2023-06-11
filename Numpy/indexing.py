import numpy as np
# uret = np.arange(0,100)
# numbers = np.array(uret)
# result = numbers[0:5]
# result = numbers[::-1]
# result = numbers[::]
# result = numbers[::-10]
# numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])  
# result = numbers2[2]
# result = numbers2[1,0]
# result = numbers2[:,0]
# result = numbers2[:,0:2]
# result = numbers2[-1,:]
# result = numbers2[:2,:2]
# print(result)

n1 = np.arange(0,10)
# n2 = n1 # References
n2 = n1.copy()
n2[0] = 50
print(n1)
print(n2)