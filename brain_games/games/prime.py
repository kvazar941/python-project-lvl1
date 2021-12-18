"""Prime module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    #  We start the check with a number equal
    #  to half of the number being checked.
    index = checked_number // 2
    while index > 1:
        if checked_number % index == 0:
            return 'no'
        index -= 1
    return 'yes'


def generating_question_answer():
    """
    Generate question and answer.

    Yields:
        int, str
    """
    while True:  # noqa: WPS457
        questions = generating_question()
        answers = generating_correct_answer(questions)
        yield '{0}'.format(questions), answers


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.main(RULES_GAME, generating_question_answer())


if __name__ == '__main__':
    main()
