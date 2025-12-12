"""
Find common items in 2 lists without duplicates. Sort the result list before output.
"""


def main():
    """Find common numbers."""
    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))
    print(list(set(li1) & set(li2)))


if __name__ == "__main__":
    main()
