def main():
    s = input()
    words = s.split()
    reversed = [word[::-1] for word in words]
    print(" ".join(reversed))


if __name__ == "__main__":
    main()
