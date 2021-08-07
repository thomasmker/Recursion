def sum(number):
    if number <= 1:
        return number
    return number + sum(number - 1)

num = int(input("Type a number: "))
print(sum(num))