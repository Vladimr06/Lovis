rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        num = int(input(f"Введите элемент [{i+1},{j+1}]: "))
        row.append(num)
    matrix.append(row)

print("\nВведённый массив:")
for row in matrix:
    print(row)

print("\nСуммы по строкам:")
for i, row in enumerate(matrix):
    print(f"Сумма строки {i+1}: {sum(row)}")

