count = 0
previous_temp = float(input("Введите температуру: "))
current_temp = float(input("Введите температуру: "))

while current_temp != 0:
    if current_temp < previous_temp:
        count += 1
    previous_temp = current_temp
    current_temp = float(input("Введите температуру: "))

print("Количество раз, когда температура уменьшилась: ", count)