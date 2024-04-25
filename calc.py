from src.sub import sub as subtract
from src.sum import sum as summa

q=input("введите 1 для суммы, 2 - для разности: ")
if q=="1":
    print("введите 2 числа для суммы:")
    a=int(input("введите а: "))
    b=int(input("введите b: "))
    print(summa(a,b))
    
else:
    print("введите 2 числа для разности:")
    a=int(input("введите а: "))
    b=int(input("введите b: "))
    print(subtract(a,b))