from module5_mod import NumberList


def main():
    # Read N
    N = int(input("Enter a positive integer N: "))

    # Create NumberList object
    num_list = NumberList()

    # Read N numbers
    print(f"Enter {N} numbers:")
    for _ in range(N):
        number = int(input())
        num_list.insert_number(number)

    # Read X
    X = int(input("Enter X to search for: "))

    # Search for X
    result = num_list.search_number(X)

    # Output result (just the index or -1)
    print(result)


if __name__ == "__main__":
    main()

