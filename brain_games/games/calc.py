"""Calc module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'What is the result of the expression?.'


def generating_question():
    """
    Generate question.

    Returns:
        tuple
    """
    number_one = random.SystemRandom().randint(1, 100)
    number_two = random.SystemRandom().randint(1, 100)
    operator = random.SystemRandom().choice('+-*')

    return (number_one, operator, number_two)


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


def generating_question_answer():
    """
    Generate question and answer.

    Yields:
        str, str
    """
    while True:  # noqa: WPS457
        questions = generating_question()
        answers = generating_correct_answer(*questions)
        yield '{0} {1} {2}'.format(*questions), answers


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.main(RULES_GAME, generating_question_answer())


if __name__ == '__main__':
    main()
