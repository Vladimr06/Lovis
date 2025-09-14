def find_range(numbers):
    if numbers:
        pass
    else: return 0
    max_num = max(numbers)
    min_num = min(numbers)
    return max_num - min_num
list1 = [2, 2, 2, 7, 3]
print(f"Разница для {list1}: {find_range(list1)}") 
