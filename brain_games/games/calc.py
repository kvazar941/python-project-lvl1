"""Calc module."""
import random

from brain_games.game_logic import games_logic

rules_game = 'What is the result of the expression?.'
expr = []
cor_answ = []


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
        operator = random.SystemRandom().choice('+-*')
        expr.append('{0} {1} {2}'.format(rand_num_one, operator, rand_num_two))
        if operator == '+':
            res = rand_num_one + rand_num_two
            cor_answ.append(str(res))
        elif operator == '-':
            res = rand_num_one - rand_num_two
            cor_answ.append(str(res))
        elif operator == '*':
            res = rand_num_one * rand_num_two
            cor_answ.append(str(res))
        counter_question += 1
    return games_logic.main(rules_game, expr, cor_answ)


if __name__ == '__main__':
    main()
