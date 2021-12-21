"""Calc module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'What is the result of the expression?.'


def generate_question():
    """
    Generate question.

    Returns:
        tuple
    """
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    operator = random.choice('+-*')

    return (number_one, operator, number_two)


def generate_correct_answer(num_one, oper, num_two):
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


def generate_question_answer():
    """
    Generate question and answer.

    Returns:
        str, str
    """
    question = generate_question()
    answer = generate_correct_answer(*question)
    return '{0} {1} {2}'.format(*question), answer


def play_calc():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.launch_game(RULES_GAME, generate_question_answer)
