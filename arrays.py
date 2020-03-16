# Reverse a string

# str="Python"
# stringLength=len(str)
# slicedString=str[stringLength::-1]
# print (slicedString)

# # Check if Palindrome
#
# def isPalindrome(s):
#
#     # Reverse string
#     rev = ''.join(reversed(s))
#
#     # Check to see if strings are identical
#     if (s == rev):
#         return True
#     return False
#
# # main function
# s = "malayalam"
# ans = isPalindrome(s)
#
# if (ans):
#     print("Yes")
# else:
#     print("No")

# Reverse an integer

reverse = ''
num = input()
for i in range(len(num), 0, -1):
    reverse += num[i-1]
print(int(reverse))
