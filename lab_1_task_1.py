numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers_without_None = numbers[:4] + numbers[5:]
new_4 = sum(numbers_without_None) / (len(numbers))
new_numbers = numbers_without_None[:4] + [new_4] + numbers_without_None[4:]
print("Измененный список:", new_numbers)

