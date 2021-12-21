"""GCD module."""
import math
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Find the greatest common divisor of given numbers.'


def generate_question():
    """
    Generate question.

    Returns:
        tuple
    """
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    return (number_one, number_two)


def generate_correct_answer(num_one, num_two):
    """
    Generate correct answer.

    Args:
        num_one: int
        num_two: int

    Returns:
        int
    """
    return math.gcd(num_one, num_two)


def generate_question_answer():
    """
    Generate question and answer.

    Returns:
        str, str
    """
    question = generate_question()
    answer = generate_correct_answer(*question)
    return '{0} {1}'.format(*question), str(answer)


def play_gcd():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.launch_game(RULES_GAME, generate_question_answer)
