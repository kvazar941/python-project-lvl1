"""gcd module."""
import random

from brain_games.game_logic import games_logic

rules_game = 'Find the greatest common divisor of given numbers.'
question = []
correct_answer = []


def generating_question(num_one, num_two):
    """
    Generate question.

    Args:
        num_one: int
        num_two: int

    Returns:
        str
    """
    return '{0} {1}'.format(num_one, num_two)


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


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        number_one = random.SystemRandom().randint(1, 100)
        number_two = random.SystemRandom().randint(1, 100)
        question.append(generating_question(number_one, number_two))
        corr_answ = generating_correct_answer(number_one, number_two)
        correct_answer.append(str(corr_answ))
        counter_question += 1
    return games_logic.main(rules_game, question, correct_answer)


if __name__ == '__main__':
    main()
