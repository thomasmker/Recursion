def findBinary(number, result):
    if number == 0:
        return result
    
    result = str(number % 2) + result
    return findBinary(int(number / 2), result)

number = int(input("Type a number: "))
print(findBinary(number,""))