def find_minimum(numbers):
    min_number = numbers[0]
    for number in numbers[1:]:
        if number < min_number:
            min_number = number
    return min_number


numbers = [3, 5, 7, 2, 8]
print(find_minimum(numbers))
