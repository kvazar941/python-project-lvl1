#!/usr/bin/env python3
"""Main script with entry point."""
from brain_games.games import calc


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return calc.play_calc()


if __name__ == '__main__':
    main()
