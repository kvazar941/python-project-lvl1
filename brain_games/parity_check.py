"""Game logic module."""
import logging
import random

import prompt

# Configure the module logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
CONSOLEHANDLER = logging.StreamHandler()
CONSOLEHANDLER.setLevel(logging.INFO)
logger.addHandler(CONSOLEHANDLER)


def game_parity_check():
    """
    Implement the logic of the game.

    Returns:
        str
    """
    # Welcome the player and set the rules of the game
    logger.info('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    logger.info('Hello, {0}!'.format(name))
    logger.info('Answer "yes" if the number is even, otherwise answer "no".')
    counter_question = 1
    while counter_question <= 3:  # 3 - the number of stages of the game
        # Choose a random number from 1 to 100
        random_number = random.SystemRandom().randint(1, 100)
        # Check a random number for parity
        # and assign the result to the variable 'parity'
        if random_number % 2 == 0:
            parity = 'yes'
        else:
            parity = 'no'
        logger.info('Question: {0}'.format(random_number))
        # Get the player's response
        answer = prompt.string('Your answer: ')
        # Compare the player's response
        # With the value of the 'parity' variable
        if answer == parity:
            # Report the correct answer
            logger.info('Correct!')
        else:
            # report an incorrect answer and end the game
            return (
                '{0} is wrong answer ;(.' +
                + 'Correct answer was {1}\n' +
                + 'Let,s try again, {2}!'
            ).format(answer, parity, name)
        counter_question += 1
    # Report the successful completion of the game
    return 'Congratulation, {0}!'.format(name)
