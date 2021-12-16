"""Game logic module."""
import prompt

number_of_rounds = 3  # 3 - the number of stages of the game


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


def main(rules, questions, correct_answers):
    """
    Implement the logic of the game.

    Args:
        rules: str
        questions: list
        correct_answers: list
    """
    message('{0}', 'Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    message('Hello, {0}!', name)
    message('{0}', rules)
    counter_question = 0
    while counter_question < number_of_rounds:
        message('Question: {0}', questions[counter_question])
        answer_user = prompt.string('Your answer: ')
        if answer_user == correct_answers[counter_question]:
            message('{0}', 'Correct!')
            counter_question += 1
            if counter_question == number_of_rounds:
                message('Congratulations, {0}!', name)
        else:
            message_error(correct_answers[counter_question], answer_user)
            message("Let\'s try again, {0}!", name)
            counter_question = number_of_rounds


if __name__ == '__main__':
    main()
