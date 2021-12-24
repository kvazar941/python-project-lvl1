"""Progression module."""
import random

from brain_games.game_logic import games_logic

RULES_GAME = 'What number is missing in the progression?'
#  minimum and maximum sequence length
# 5, 15 - the numbers determined by the task
SEQ_LEN_MIN = 5
SEQ_LEN_MAX = 15


def create_progression():
    """
    Implement the logic of the game.

    Returns:
        list
    """
    leght = random.randint(SEQ_LEN_MIN, SEQ_LEN_MAX)
    init_number = random.randint(1, 100)
    step = random.randint(1, 10)
    position = 0
    init_progression = []
    while position < leght:
        init_progression.append(str(init_number + position * step))
        position += 1
    return init_progression


def generate_question(progression, position):
    """
    Generate question.

    Args:
        progression: list
        position: int

    Returns:
        list
    """
    progression[position] = '..'
    return progression


def generate_correct_answer(progression, position):
    """
    Generate correct answer.

    Args:
        progression: list
        position: int

    Returns:
        str
    """
    return progression[position]


def generate_question_answer():
    """
    Generate question and answer.

    Returns:
        str, str
    """
    progression = create_progression()
    question_position = random.randint(0, (len(progression) - 1))
    answer = str(generate_correct_answer(progression, question_position))
    question = ' '.join(generate_question(progression, question_position))
    return question, answer


def play_progression():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    return games_logic.launch_game(RULES_GAME, generate_question_answer)
