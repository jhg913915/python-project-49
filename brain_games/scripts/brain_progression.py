from brain_games.games.progression_game import progression_game
from brain_games.engine import run_game


TASK = 'What number is missing in the progression?'


def main():
    run_game(progression_game, TASK)


if __name__ == '__main__':
    main()