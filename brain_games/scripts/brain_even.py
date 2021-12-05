#!/usr/bin/env python3
"""main module with entry point."""
from brain_games import parity_check


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return '{0}'.format(parity_check.game_parity_check())


if __name__ == '__main__':
    main()
