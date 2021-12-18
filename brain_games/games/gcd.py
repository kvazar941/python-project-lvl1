"""GCD module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Find the greatest common divisor of given numbers.'


def generating_question():
    """
    Generate question.

    Returns:
        tuple
    """
    number_one = random.SystemRandom().randint(1, 100)
    number_two = random.SystemRandom().randint(1, 100)
    return (number_one, number_two)


def generating_correct_answer(num_one, num_two):
    """
    Generate correct answer.

    Args:
        num_one: int
        num_two: int

    Returns:
        int
    """
    nod = min(num_one, num_two)
    while nod > 0:
        if num_one % nod == 0 and num_two % nod == 0:
            return nod
        nod -= 1


def generating_question_answer():
    """
    Generate question and answer.

    Yields:
        str, str
    """
    while True:  # noqa: WPS457
        questions = generating_question()
        answers = generating_correct_answer(*questions)
        yield '{0} {1}'.format(*questions), str(answers)


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.main(RULES_GAME, generating_question_answer())


if __name__ == '__main__':
    main()
