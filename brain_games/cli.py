import prompt


def welcome_user():
    name = prompt.string('Welcome to Brain Games\nMay I have your name? ')
    print('Hello, {}!'.format(name))