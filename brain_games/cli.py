"""Communication module."""
import prompt


def welcome_user():
    """
    Request a name and greet a user by name.

    Returns:
        str
    """
    name = prompt.string('May I have your name? ')
    return 'Hello, {0}! '.format(name)
