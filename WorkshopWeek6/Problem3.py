S = input("Enter a string: ")

def isPalindrome(S):
    for i in range(0, len(S)):
        if S[0 + i] == S[len(S) - 1]:
            return "It is a palindrome!"
        else:
            return "It is not a palindrome!"
print(isPalindrome(S))