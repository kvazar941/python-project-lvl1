"""Game logic module."""
# flake8: noqa
import prompt

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
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(rules)
    counter_question = 0
    while counter_question < number_of_rounds:
        print('Question:', questions[counter_question])  # noqa: WPS421
        # Get the player's response
        answer = prompt.string('Your answer: ')
        # Compare the player's response
        # With the value of the 'parity' variable
        if answer == correct_answers[counter_question]:
            # Report the correct answer
            print('Correct!')
            counter_question += 1
            if counter_question == number_of_rounds:
                print('Congratulations, {0}!'.format(name))
        else:
            # report an incorrect answer and end the game
            print(
                ("'{0}' is wrong answer ;(. "
                + "Correct answer was '{1}'.\n"  # noqa: W503
                + "Let\'s try again, {2}!"  # noqa: W503
                ).format(answer, correct_answers[counter_question], name)
            )
            counter_question = number_of_rounds 


if __name__ == '__main__':
    main()
