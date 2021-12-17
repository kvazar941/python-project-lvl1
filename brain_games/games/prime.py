"""prime module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
question = []
correct_answer = []


def generating_question():
    """
    Generate question.

    Returns:
        int
    """
    return random.SystemRandom().randint(1, 100)


def generating_correct_answer(num):
    """
    Generate correct answer.

    Args:
        num: int

    Returns:
        str
    """
    index = num - 1
    while index > 1:
        if num % index == 0:
            return 'no'
        index -= 1
    return 'yes'


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        rand_num = generating_question()
        question.append('{0}'.format(rand_num))
        correct_answer.append(generating_correct_answer(rand_num))
        counter_question += 1
    return games_logic.main(RULES_GAME, question, correct_answer)


if __name__ == '__main__':
    main()
