def sorted_array():
    numbers = []
    for i in range(5):
        num = int(input("Enter a value: "))
        numbers.append(num)
    print("Original:", numbers)
    print("Ascending:", sorted(numbers))
    print("Descending:", sorted(numbers, reverse=True))