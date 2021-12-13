#!/usr/bin/env python3
"""main module with entry point."""
from brain_games import cli


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return cli.welcome_user()


if __name__ == '__main__':
    main()
