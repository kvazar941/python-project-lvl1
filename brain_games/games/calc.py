"""Calc module."""
import random

from brain_games.game_logic import games_logic

rules_game = 'What is the result of the expression?.'
expres = []
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
        operand = random.SystemRandom().choice('+', '-', '*')
        expres.append('{0} {1} {2}'.format(rand_num_one, operand, rand_num_two))
        if rand_num_one % 2 == 0:
            cor_answ.append('yes')
        else:
            cor_answ.append('no')
        counter_question += 1
    return games_logic.main(rules_game, expres, cor_answ)


if __name__ == '__main__':
    main()
