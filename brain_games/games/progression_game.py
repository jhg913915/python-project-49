import random


MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_START_NUMBER = 1
MAX_START_NUMBER = 50


def progression_game():
    start = random.randint(MIN_START_NUMBER, MAX_START_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = [start + step * i for i in range(length)]
    problem_index = random.randint(0, length - 1)
    result = progression[problem_index]
    progression[problem_index] = ".."
    progression_str = ' '.join(str(x) for x in progression)
    return progression_str, result