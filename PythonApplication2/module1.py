import random
n = int(input("Введите размер массива: "))
arr = [random.randint(0, 100) for _ in range(n)]
print("Сгенерированный массив:",arr)

