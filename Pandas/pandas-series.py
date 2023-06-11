import numpy as np
import pandas as pd
# # pandas_series = pd.Series()
# random_numbers = np.random.randint(10,100,6)
# numbers = [10,20,30,40,50]
# letters = ["a","b","c","d","e"]
# letters = ["a","b","c","d",30]
# dictionary = {"a":10,"b":20,"c":30,"d":40}
# # pandas_series = pd.Series(numbers)
# # pandas_series = pd.Series(letters)
# # pandas_series = pd.Series(5,[0,1,2,3]) # Index numarası yollar.
# pandas_series = pd.Series([10,20,30,40,50],["a","b","c","d","e"]) # İstenilen key bilgisini yollar.
# # pandas_series = pd.Series(dictionary)
# # pandas_series = pd.Series(random_numbers) # numpy ile kullanım
# result = pandas_series[0]
# result = pandas_series["a"]
# result = pandas_series[-1]
# result = pandas_series[:3]
# result = pandas_series[-2:]
# result = pandas_series[::-1]
# result = pandas_series[['a','e']]
# result = pandas_series.ndim
# result = pandas_series.dtype
# result = pandas_series.shape
# result = pandas_series.sum()
# result = pandas_series.max()
# result = pandas_series.argmax()
# result = pandas_series + pandas_series
# result = pandas_series + pandas_series
# result = np.sqrt(pandas_series)
# result = pandas_series > 30
# result = pandas_series % 2 == 0
# print(pandas_series[result])
# print(result)
renault2018 = pd.Series([10,20,30,40],["clio","megane","taliant","kangoo"])
renault2019 = pd.Series([25,45,10,50],["clio","zoe","taliant","captur"])
example = pd.Series([10,20,30,40],["a","b","c","d"])
total = renault2018 + renault2019
print(total["clio"])
