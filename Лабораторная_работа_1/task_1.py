numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

wrong_index = numbers.index(None)
numbers[wrong_index] = (sum((sum(numbers[:wrong_index]), sum(numbers[wrong_index + 1:]))) / len(numbers))

print("Измененный список:", numbers)
