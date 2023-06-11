# def greeting(name):
#     print('hello', name)

# print(greeting("Emre"))
# print(greeting)

# merhaba = greeting
# print(merhaba)
# print(greeting)

# del merhaba
# print(merhaba)

# encapsulation
# def outer(num1):
#     def inner_increment(num1):
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2)
# outer(8)

# def factorial(number):
#     if not isinstance(number,int):
#         raise TypeError("Number must be an integer")
#     if not number >= 0:
#         raise ValueError("Number must be Zero or Positive")
#     def inner_factorial(number):
#         if number <= 1:
#             return 1
#         return number * inner_factorial(number -1)
#     return inner_factorial(number)

# try:
#     print(factorial(-1))
# except Exception as ex:
#     print(ex)