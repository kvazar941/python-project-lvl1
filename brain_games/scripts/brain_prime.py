#!/usr/bin/env python3
"""Main script with entry point."""
from brain_games.games import prime


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return prime.play_prime()


if __name__ == '__main__':
    main()
