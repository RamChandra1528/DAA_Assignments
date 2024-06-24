def count_even_digit_numbers(numbers):
    count = 0
    for number in numbers:
        if len(str(abs(number))) % 2 == 0:
            count += 1
    return count

numbers = [12, 345, 2, 6, 7896]
print(count_even_digit_numbers(numbers))
