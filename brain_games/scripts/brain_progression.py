#!/usr/bin/env python3
"""Main script with entry point."""
from brain_games.games import progression


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return progression.play_progression()


if __name__ == '__main__':
    main()
