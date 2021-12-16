"""Game logic module."""
import prompt

number_of_rounds = 3  # 3 - the number of stages of the game


def main(rules, questions, correct_answers):
    """
    Implement the logic of the game.

    Args:
        rules: str
        questions: list
        correct_answers: list
    """
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421
    print(rules)  # noqa: WPS421
    counter_question = 0
    while counter_question < number_of_rounds:
        print(  # noqa: WPS4
            ("'Question: {0}'"
             ).format(questions[counter_question]),
        )
        answer_user = prompt.string('Your answer: ')
        if answer_user == correct_answers[counter_question]:
            print('Correct!')  # noqa: WPS421
            counter_question += 1
            if counter_question == number_of_rounds:
                print('Congratulations, {0}!'.format(name))  # noqa: WPS421
        else:
            print(  # noqa: WPS421
                ("'{0}' is wrong answer ;(. "
                 + "Correct answer was '{1}'.\n"  # noqa: W503
                 + "Let\'s try again, {2}!"  # noqa: W503
                 ).format(answer_user, correct_answers[counter_question], name),
            )
            counter_question = number_of_rounds


if __name__ == '__main__':
    main()
