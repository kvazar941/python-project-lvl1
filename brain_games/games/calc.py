"""Calc module."""
import random

from brain_games.game_logic import games_logic

rules_game = 'What is the result of the expression?.'
question = []
correct_answer = []


def generating_question(num_one, oper, num_two):
    """
    Generate question.

    Args:
        num_one: int
        num_two: int
        oper: str

    Returns:
        str
    """
    return '{0} {1} {2}'.format(num_one, oper, num_two)


def generating_correct_answer(num_one, oper, num_two):
    """
    Generate correct answer.

    Args:
        num_one: int
        num_two: int
        oper: str

    Returns:
        str
    """
    if oper == '+':
        return (str(num_one + num_two))
    elif oper == '-':
        return (str(num_one - num_two))
    elif oper == '*':
        return (str(num_one * num_two))


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        number_one = random.SystemRandom().randint(1, 100)
        number_two = random.SystemRandom().randint(1, 100)
        operator = random.SystemRandom().choice('+-*')
        question.append(generating_question(number_one, operator, number_two))
        corr_answ = generating_correct_answer(number_one, operator, number_two)
        correct_answer.append(corr_answ)
        counter_question += 1
    return games_logic.main(rules_game, question, correct_answer)


if __name__ == '__main__':
    main()
