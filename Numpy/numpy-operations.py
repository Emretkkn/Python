import numpy as np

numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
print(numbers1)
# print(numbers2)
result = numbers1 + numbers2
result = numbers1 - 10
result = numbers1 * numbers2
result = numbers1 * 3
result = numbers1 / numbers2
result = numbers1 / 3
result = np.sin(numbers1)
result = np.cos(numbers2)
result = np.tan(numbers1)
result = np.sqrt(numbers2)
result = np.log(numbers2)
multi_numbers1 = numbers1.reshape(2,3)
multi_numbers2 = numbers2.reshape(2,3)
result = np.vstack((multi_numbers1,multi_numbers2)) # Vertical stack
result = np.hstack((multi_numbers1,multi_numbers2)) # Horizontal stack
# print(multi_numbers1)
# print(multi_numbers2)
result = numbers1 >= 50 # Bool döndürür
result = numbers1 % 2 == 0 # Tek çift
print(result)
print(numbers1[result])
