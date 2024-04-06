x = int(input("Введите целое число: "))

numbers = (x for x in range(1, x + 1))
result = sum(numbers)
print(f"Сумма первых {x} натуральных чисел: {result}")
