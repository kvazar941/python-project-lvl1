#!/usr/bin/env python3
"""Main script with entry point."""
from brain_games.games import gcd


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return '{0}'.format(gcd.main())


if __name__ == '__main__':
    main()
