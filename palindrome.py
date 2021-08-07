def isPalindrome(str):
    str_size = len(str)
    # Define the base case/stopping condition   
    if str_size == 0 or str_size == 1:
        return True
    
    # Do some work to shrink the problem space
    if str[0] == str[str_size - 1]:
        return isPalindrome(str[1:str_size - 1])

    # Additional base-case to handle non-palindromes
    return False


#word = "kayak", "racecar"
word = input("Type a word: ")
print(f"Is the word '{word}' a palindrome ? {isPalindrome(word)}")