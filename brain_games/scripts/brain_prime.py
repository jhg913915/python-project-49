from brain_games.games.prime_game import prime_game
from brain_games.engine import run_game


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run_game(prime_game, TASK)


if __name__ == '__main__':
    main()