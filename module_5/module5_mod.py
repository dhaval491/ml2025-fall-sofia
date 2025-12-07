class NumberList:
    def __init__(self):
        """Initialize an empty list to store numbers."""
        self.numbers = []

    def insert_number(self, num):
        """Insert a number into the list."""
        self.numbers.append(num)

    def search_number(self, x):
        """
        Search for number x in the list.
        Returns the 1-based index if found, otherwise -1.
        """
        for i, value in enumerate(self.numbers, start=1):
            if value == x:
                return i
        return -1

