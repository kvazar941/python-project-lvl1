"""Game logic module."""
import prompt

NUMBER_OF_ROUNDS = 3  # 3 - the number of stages of the game
ERROR_MESSAGE = "'{0}' is wrong answer ;(. Correct answer was '{1}'."


def message(formation, formatting_message):
    """
    Output a formatted message.

    Args:
        formation: str
        formatting_message: str, int
    """
    print(formation.format(*formatting_message))


def launch_game(rules, question_answer):
    """
    Implement the logic of the module.

    Args:
        rules: str
        question_answer: function-generator
    """
    message('{0}', ('Welcome to the Brain Games!',))
    name = prompt.string('May I have your name? ')
    message('Hello, {0}!', (name,))
    message('{0}', (rules,))
    counter_question = 0
    while counter_question < NUMBER_OF_ROUNDS:
        question, answer = question_answer()
        message('Question: {0}', (question,))
        answer_user = prompt.string('Your answer: ')
        if answer_user == answer:
            message('{0}', ('Correct!',))
            counter_question += 1
        else:
            message(ERROR_MESSAGE, (answer_user, answer))
            message("Let\'s try again, {0}!", (name,))
            break
    if counter_question == NUMBER_OF_ROUNDS:
        message('Congratulations, {0}!', (name,))
