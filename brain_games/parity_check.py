"""Communication module."""
import prompt
import logging
from random import randint


def game_parity_check():
    """
    Request a name and greet a user by name.

    Returns:
        str
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    logger.addHandler(consoleHandler)
    formatter = logging.Formatter('%(message)s')
    consoleHandler.setFormatter(formatter)
    logger.info('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    logger.info('Hello, {0}!'.format(name))
    logger.info('Answer "yes" if the number is even, otherwise answer "no".')
    counter_question = 1
    number_question = 3
    while counter_question <= number_question:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            parity = 'yes'
        else:
            parity = 'no'
        logger.info('Question: {0}'.format(random_number))
        answer = prompt.string('Your answer: ')
        if answer == parity:
            logger.info('Correct!')
        else:
            return "'{0}' is wrong answer ;(. Correct answer was '{1}'.\nLet,s try again, {2}!".format (answer, parity, name)
        counter_question += 1

    return 'Congratulation, {0}!'.format(name)

