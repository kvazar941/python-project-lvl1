"""Even module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'
question = []
correct_answer = []


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


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        random_number = generating_question()
        question.append(random_number)
        correct_answer.append(generating_correct_answer(random_number))
        counter_question += 1
    return games_logic.main(RULES_GAME, question, correct_answer)


if __name__ == '__main__':
    main()
