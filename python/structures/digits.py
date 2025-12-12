"""
Find sum of n-integer digits. n >= 0.
"""


def main():
    """Sum of number digits."""
    n = input()
    print(sum(int(d) for d in str(n)))


if __name__ == "__main__":
    main()
