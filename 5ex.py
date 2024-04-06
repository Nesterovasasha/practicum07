N = int(input("Введите значение N: "))

side_length = 1
volumes_list = []

while True:
    volume = side_length ** 3
    if volume <= N:
        volumes_list.append(volume)
        side_length += 1
    else:
        break

print(f"Объемы кубиков (в куб. см):{volumes_list}")