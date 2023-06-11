# def my_decorator(func):
#     def wrapper(name):
#         print("Fonksiyondan önceki işlemler.")
#         func(name)
#         print("Fonksiyondan sonraki işlemler.")
#     return wrapper

# def selaminaleykum():
#     print("SA")
# @my_decorator
# def greeting(name):
#     print("GREEEEEETING", name)
# greeting("Emre")

# sayHello = my_decorator(selaminaleykum)
# sayHello()
# sayGreeting = my_decorator(greeting)
# sayGreeting()
import time
import math
def calculate_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print(f"Fonksiyon {func.__name__} {finish-start} saniye sürdü.")
    return wrapper


@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def faktoriyel(a):
    print(math.factorial(a))

usalma(2,4)
faktoriyel(3)
