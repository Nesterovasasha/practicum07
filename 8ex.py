import math

def min_questions(N):
    return math.ceil(math.log(N, 2))

N = int(input("Введите число N: "))
print(f"Минимальное количество вопросов, которые позволят гарантированно отгадать число - {min_questions(N)}")