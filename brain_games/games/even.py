"""Even module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    """
    Generate question for game even.

    Returns:
        int
    """
    return random.randint(1, 100)


def generate_correct_answer(checked_number):
    """
    Generate correct answer for game even.

    Args:
        checked_number: int

    Returns:
        str
    """
    return 'yes' if checked_number % 2 == 0 else 'no'


def generate_question_answer():
    """
    Generate question and answer for game even.

    Returns:
        str, str
    """
    question = generate_question()
    answer = generate_correct_answer(question)
    return str(question), answer


def play_even():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.launch_game(RULES_GAME, generate_question_answer)
