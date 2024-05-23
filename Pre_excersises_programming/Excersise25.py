numbers = [123, 345, 5, 3, 8, 87, 64, 95, 9, 10, 24, 54, 66]
sum = 0

for number in numbers:
    if number%2 == 1:
        sum = sum + number
        print(number)
print(f"The sum of all uneven number is: {sum}.")