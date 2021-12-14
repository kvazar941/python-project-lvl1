"""Communication module."""
import logging

import prompt

# Configure the module logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
CONSOLEHANDLER = logging.StreamHandler()
CONSOLEHANDLER.setLevel(logging.INFO)
logger.addHandler(CONSOLEHANDLER)


def welcome_user():
    """
    Request a name and greet a user by name.

    Returns:
        str
    """
    logger.info('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    return ('Hello, {0}!'.format(name))


if __name__ == '__main__':
    welcome_user()
