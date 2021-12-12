"""prime module."""
import random

from brain_games.game_logic import games_logic

rules_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
expr = []
cor_answ = []


def checking_prime_number(num):
    """
    Implement the logic of the game.

    Args:
        num: int

    Returns:
        str
    """
    index = num - 1
    while index > 1:
        if num % index == 0:
            return 'no'
        index -= 1
    return 'yes'


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        rand_num = random.SystemRandom().randint(1, 100)
        expr.append('{0}'.format(rand_num))
        cor_answ.append(checking_prime_number(rand_num))
        counter_question += 1
    return games_logic.main(rules_game, expr, cor_answ)


if __name__ == '__main__':
    main()
