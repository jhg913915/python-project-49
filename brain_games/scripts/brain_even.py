from brain_games.games.even_game import even_game
from brain_games.engine import run_game


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run_game(even_game, TASK)


if __name__ == '__main__':
    main()