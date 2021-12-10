#!/usr/bin/env python3
"""main module with entry point."""
from brain_games.games import parity_check


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return '{0}'.format(parity_check.main())


if __name__ == '__main__':
    main()
