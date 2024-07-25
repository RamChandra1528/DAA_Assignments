def LemonadeChange(bills: list[int]) -> bool:
    # If the first bill is not $5, we cannot provide change, return False
    if bills[0] != 5:
        return False

    # Initialize counters for $5 and $10 bills
    five, ten = 0, 0

    # Iterate through each bill in the list
    for bill in bills:
        if bill == 5:
            # If the bill is $5, just keep it (increment the count of $5 bills)
            five += 1
        elif bill == 10:
            # If the bill is $10, we need to give one $5 as change
            if five >= 1:
                five -= 1  # Give one $5 bill as change
                ten += 1  # Keep the $10 bill
            else:
                # If we don't have a $5 bill to give as change, return False
                return False
        else:
            # If the bill is $20, we prefer to give one $10 and one $5 as change
            if ten >= 1 and five >= 1:
                ten -= 1  # Give one $10 bill as change
                five -= 1  # Give one $5 bill as change
            elif five >= 3:
                # If we don't have a $10 bill, give three $5 bills as change
                five -= 3
            else:
                # If we can't provide the correct change, return False
                return False

    # If we've successfully processed all bills, return True
    return True

t = LemonadeChange([5, 5, 5, 10, 20])
print(t)