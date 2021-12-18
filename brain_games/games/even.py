"""Even module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generating_question():
    """
    Generate question.

    Returns:
        int
    """
    return random.SystemRandom().randint(1, 100)


def generating_correct_answer(checked_number):
    """
    Generate correct answer.

    Args:
        checked_number: int

    Returns:
        str
    """
    return 'yes' if checked_number % 2 == 0 else 'no'


def generating_question_answer():
    """
    Generate question and answer.

    Yields:
        str, str
    """
    while True:  # noqa: WPS457
        questions = generating_question()
        answers = generating_correct_answer(questions)
        yield str(questions), answers


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.main(RULES_GAME, generating_question_answer())


if __name__ == '__main__':
    main()
