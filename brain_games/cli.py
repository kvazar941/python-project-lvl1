"""Communication module."""
import prompt


def welcome_user():
    """Request a name and greet a user by name."""
    print('Welcome to the Brain Games!')  # noqa: WPS421
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # noqa: WPS421


if __name__ == '__main__':
    welcome_user()
