#!/usr/bin/env python3
"""main module with entry point."""
from brain_games.games import progression


def main():
    """
    Execute the main code.

    Returns:
        str
    """
    return '{0}'.format(progression.main())


if __name__ == '__main__':
    main()
