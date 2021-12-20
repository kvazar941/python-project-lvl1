#!/usr/bin/env python3
"""Main script with entry point."""
from brain_games.games import even


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return even.play_even()


if __name__ == '__main__':
    main()
