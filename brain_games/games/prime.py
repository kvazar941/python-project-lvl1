"""Prime module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question():
    """
    Generate question.

    Returns:
        int
    """
    return random.randint(1, 100)


def generate_correct_answer(checked_number):
    """
    Generate correct answer.

    Args:
        checked_number: int

    Returns:
        str
    """
    index = checked_number - 1
    while index > 1:
        if checked_number % index == 0:
            return 'no'
        index -= 1
    return 'yes'


def generate_question_answer():
    """
    Generate question and answer.

    Returns:
        int, str
    """
    question = generate_question()
    answer = generate_correct_answer(question)
    return '{0}'.format(question), answer


def play_prime():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.launch_game(RULES_GAME, generate_question_answer)


if __name__ == '__main__':
    play_prime()
