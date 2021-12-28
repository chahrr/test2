# Python program to find the largest number

def max_of_two( x, y ):
    if x > y:
        return x
    return y
def max_of_three( x, y, z ):
    return max_of_two( x, max_of_two( y, z ) )
print(max_of_three(9, 12, -8))

# among the three numbers using library function

def maximum(a, b, c):
	list = [a, b, c]
	return max(list)


a = 17
b = 50
c = 69
print(maximum(a, b, c))


# among the three numbers using library function

a = 1
b = 4
c = 6
print(max(a, b, c))
