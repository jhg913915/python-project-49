from brain_games.games.gcd_game import gcd_game
from brain_games.engine import run_game


TASK = 'Find the greatest common divisor of given numbers.'


def main():
    run_game(gcd_game, TASK)


if __name__ == '__main__':
    main()