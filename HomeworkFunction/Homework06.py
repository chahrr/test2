list  = [42, 45, 78, 20, 20]

total = sum(list)   
    
print("Sum of all elements in the list = ",total)

# Using for loop 
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total  

numbers = (8, 5, 1,6)
print(sum(numbers()))
