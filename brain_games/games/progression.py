"""progression module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'What number is missing in the progression?'
question = []
correct_answer = []
#  minimum and maximum sequence length
# 5, 15 - the numbers determined by the task
SEQ_LEN_MIN = 5
SEQ_LEN_MAX = 15


def progression_formation():
    """
    Implement the logic of the game.

    Returns:
        int
    """
    leght_progr = random.SystemRandom().randint(SEQ_LEN_MIN, SEQ_LEN_MAX)
    init_num_progr = random.SystemRandom().randint(1, 100)
    step_progr = random.SystemRandom().randint(1, 10)
    pos_progr = 0
    quest = []
    while pos_progr < leght_progr:
        quest.append(str(init_num_progr + pos_progr * step_progr))
        pos_progr += 1
    return quest


def generating_question(progression, position):
    """
    Generate question.

    Args:
        progression: list
        position: int

    Returns:
        str
    """
    progression[position] = '..'
    return progression


def generating_correct_answer(progression, position):
    """
    Generate correct answer.

    Args:
        progression: list
        position: int

    Returns:
        int
    """
    return progression[position]


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        progr = progression_formation()
        quest_position = random.SystemRandom().randint(0, (len(progr) - 1))
        corr_answ = generating_correct_answer(progr, quest_position)
        question.append(' '.join(generating_question(progr, quest_position)))
        correct_answer.append((str(corr_answ)))
        counter_question += 1
    return games_logic.main(RULES_GAME, question, correct_answer)


if __name__ == '__main__':
    main()
