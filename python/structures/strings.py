"""
Check whether the input string is palindrome.
"""


def main():
    """Check palindrome."""
    s = input()
    n = round(len(s) / 2)
    for i in range(n):
        if s[i] != s[len(s) - i - 1]:
            print("no")
            return
    print("yes")


if __name__ == "__main__":
    main()
