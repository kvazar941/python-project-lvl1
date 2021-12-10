"""Game logic module."""
import random

from brain_games.game_logic import games_logic


def main():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    rules_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    rand_num = []
    cor_answ = []
    counter_question = 0
    while counter_question < games_logic.number_of_rounds:
        random_number = random.SystemRandom().randint(1, 100)
        rand_num.append(random_number)
        if random_number % 2 == 0:
            cor_answ.append('yes')
        else:
            cor_answ.append('no')
        counter_question += 1
    return games_logic.main(rules_game, rand_num, cor_answ)


if __name__ == '__main__':
    main()
