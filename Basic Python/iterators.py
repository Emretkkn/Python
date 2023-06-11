liste = [1,2,3,4,5]
# for i in liste:
#     print(i)
# print(dir(liste))

# iterator = iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# iterator = iter(liste)
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except StopIteration:
#         break

# class MyClass:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
    
#     def __next__(self):
#         if self.start <= self.stop:
#             x = self.start
#             self.start += 1
#             return x
#         else:
#             raise StopIteration
    
#     def __iter__(self):
#         return self

# list = MyClass(0,30)
# for i in list:
#     print(i)