# read number of elements
N = int(input("Enter N: "))

# read N numbers
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# read X and search
X = int(input("Enter X: "))

if X in numbers:
    print(numbers.index(X) + 1)
else:
    print(-1)
