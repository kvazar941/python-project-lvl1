"""progression module."""
import random

from brain_games.game_logic import games_logic

rules_game = 'What number is missing in the progression?'
expr = []
cor_answ = []
#  minimum and maximum sequence length
seq_len_min = 5
seq_len_max = 15


def progression_formation():
    """
    Implement the logic of the game.

    Returns:
        int
    """
    # 5, 15 - the numbers determined by the task
    leght_progr = random.SystemRandom().randint(seq_len_min, seq_len_max)
    init_num_progr = random.SystemRandom().randint(1, 100)
    step_progr = random.SystemRandom().randint(1, 10)
    pos_progr = 0
    quest = []
    while pos_progr < leght_progr:
        quest.append(str(init_num_progr + pos_progr * step_progr))
        pos_progr += 1
    return quest


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
        cor_answ.append(str(progr[quest_position]))
        progr[quest_position] = '..'
        expr.append(' '.join(progr))
        counter_question += 1
    return games_logic.main(rules_game, expr, cor_answ)


if __name__ == '__main__':
    main()
