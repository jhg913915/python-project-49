import random


MIN_NUMBER = 1
MAX_NUMBER = 50


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd_game():
    random_int_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_int_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    result = gcd(random_int_1, random_int_2)
    question = f"{random_int_1} {random_int_2}"
    return question, result