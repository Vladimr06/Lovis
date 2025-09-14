n = int(input("Введите размер массива: "))
arr = []
for i in range(n):
    num = int(input(f"Введите элемент {i+1}: "))
    arr.append(num)
print("Введённый массив:", arr)

