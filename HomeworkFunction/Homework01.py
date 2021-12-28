
#check palindrome
n = input("Enter the word and see if it is palindrome: ") 
if n == n[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")

# function which return reverse of a string

def isPalindrome(m):
	return m == m[::-1]



m = "madam"
word = isPalindrome(m)

if word:
	print("Yes")
else:
	print("No")
