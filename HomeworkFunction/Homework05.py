# Python code to reverse a string
# using recursion

def reverse(s):
	if len(s) == 0:
		return s
	else:
		return reverse(s[1:]) + s[0]

s = "GansforGans"

print ("The original string is : ",end="")
print (s)

print ("The reversed strig (using recursion) is : ",end="")
print (reverse(s))

# using extended slice syntax
def reverse(string):
	string = string[::-1]
	return string

s = "folksforfolks"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using extended) is : ",end="")
print (reverse(s))
