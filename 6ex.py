N = int(input("Введите число N: "))

followers = 1
followers_list = [1, ]

while followers <= N:
    followers = followers * 2
    followers_list.append(followers)

print(followers_list)