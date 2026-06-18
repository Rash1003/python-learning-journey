""" s = input("Enter a string: ")
char = input("Enter a character to count: ")

print(s.count(char))

s = input("Enter a string: ")
char = input("Enter a character to count: ")
  """


""" s = str(input("Enter a string: "))
char = str(input("Enter a character to delete: "))
print(s.replace(char, "")) """

s = str(input("Enter a string: "))

forward= s[0:]
backward = s[::-1]

if forward == backward:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")