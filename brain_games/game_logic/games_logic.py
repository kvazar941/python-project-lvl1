"""Game logic module."""
import prompt

NUMBER_OF_ROUNDS = 3  # 3 - the number of stages of the game


def message(formation, formatting_message):
    """
    Output a formatted message.

    Args:
        formation: str
        formatting_message: str, int
    """
    print(formation.format(formatting_message))  # noqa: WPS421


def message_error(right_answer, wrong_answer):
    """
    Output a formatted message about the error.

    Args:
        right_answer: str, int
        wrong_answer: str, int
    """
    format_message = "'{0}' is wrong answer ;(. Correct answer was '{1}'."
    print(format_message.format(wrong_answer, right_answer))  # noqa: WPS421


def main(rules, question_answer):
    """
    Implement the logic of the game.

    Args:
        rules: str
        question_answer: function-generator
    """
    message('{0}', 'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    message('Hello, {0}!', name)
    message('{0}', rules)
    counter_question = 0
    while counter_question < NUMBER_OF_ROUNDS:
        question, answer = next(question_answer)
        message('Question: {0}', question)
        answer_user = prompt.string('Your answer: ')
        if answer_user == answer:
            message('{0}', 'Correct!')
            counter_question += 1
            if counter_question == NUMBER_OF_ROUNDS:
                message('Congratulations, {0}!', name)
        else:
            message_error(answer, answer_user)
            message("Let\'s try again, {0}!", name)
            counter_question = NUMBER_OF_ROUNDS


if __name__ == '__main__':
    main()
