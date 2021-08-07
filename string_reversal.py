def reverse_string(str):
    # What is the base case
    if str == "":
        return ""
    # What is the smallest amount of work I can do in each iteration
    return reverse_string(str[1:]) + str[0]

#word = "abcde"
word = input("Type a word: ")
print(f"The reverse of {word} is {reverse_string(word)}")