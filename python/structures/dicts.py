"""
Drop empty items from a dictionary.
"""

import json


def main():
    """Drop empty items from a dictionary."""
    d = json.loads(input())
    print({k: v for k, v in d.items() if v})


if __name__ == "__main__":
    main()
