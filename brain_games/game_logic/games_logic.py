"""Game logic module."""
import logging

import prompt

# Configure the module logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
CONSOLEHANDLER = logging.StreamHandler()
CONSOLEHANDLER.setLevel(logging.INFO)
logger.addHandler(CONSOLEHANDLER)

number_of_rounds = 3  # 3 - the number of stages of the game


def main(rules, questions, correct_answers):
    """
    Implement the logic of the game.

    Args:
        rules: str
        questions: list
        correct_answers: list

    Returns:
        str
    """
    # Welcome the player and set the rules of the game
    logger.info('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    logger.info('Hello, {0}!'.format(name))
    logger.info(rules)
    counter_question = 0
    while counter_question < number_of_rounds:
        logger.info('Question: {0}'.format(questions[counter_question]))
        # Get the player's response
        answer = prompt.string('Your answer: ')
        # Compare the player's response
        # With the value of the 'parity' variable
        if answer == correct_answers[counter_question]:
            # Report the correct answer
            logger.info('Correct!')
        else:
            # report an incorrect answer and end the game
            return (
                "'{0}' is wrong answer ;(. "
                + "Correct answer was '{1}'.\n"  # noqa: W503
                + "Let\'s try again, {2}!"  # noqa: W503
            ).format(answer, correct_answers[counter_question], name)
        counter_question += 1
    # Report the successful completion of the game
    return 'Congratulation, {0}!'.format(name)


if __name__ == '__main__':
    main()
