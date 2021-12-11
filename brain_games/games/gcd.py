"""gcd module."""
import random

from brain_games.game_logic import games_logic

rules_game = 'Find the greatest common divisor of given numbers.'
expr = []
cor_answ = []


def calculation_nod(num_a, num_b):
    """
    Implement the logic of the game.

    Args:
        num_a: int
        num_b: int

    Returns:
        int
    """
    nod = min(num_a, num_b)
    while nod > 0:
        if num_a % nod == 0 and num_b % nod == 0:
            return nod
        nod -= 1


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        rand_num_one = random.SystemRandom().randint(1, 100)
        rand_num_two = random.SystemRandom().randint(1, 100)
        expr.append('{0} {1}'.format(rand_num_one, rand_num_two))
        cor_answ.append(str(calculation_nod(rand_num_one, rand_num_two)))
        counter_question += 1
    return games_logic.main(rules_game, expr, cor_answ)


if __name__ == '__main__':
    main()
