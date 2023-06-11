# Value Types number, string can't references
x = 6
y= 15

x = y
y = 18
# print(x,y)
# Reference type => List
listA = ["Green","Red","Blue"]
ListB = ["Cyan","Purple","Black"]

listA = ListB
listA[0] = "Hazel"
print(listA, ListB)
