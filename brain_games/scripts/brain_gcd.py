#!/usr/bin/env python3
"""Main script with entry point."""
from brain_games.games import gcd


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return gcd.play_gcd()


if __name__ == '__main__':
    main()
