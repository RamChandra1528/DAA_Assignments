def find_maximum(numbers):
    max_number = numbers[0]
    for number in numbers[1:]:
        if number > max_number:
            max_number = number
    return max_number


numbers = [3, 5, 7, 2, 8]
print(find_maximum(numbers))
