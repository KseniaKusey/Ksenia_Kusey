num = int(input("Введите число:"))
arr=[]

while num > 0:
    arr.append(num % 10)
    num //=10

arr.reverse()

print("Массив:",arr)