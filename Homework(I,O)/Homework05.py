file = open("student_names.txt")

print(file.read())
search_word = input("enter a word you want to search in file: ")
if(search_word in file.read()):
    print("word found")
else:
     print("word not found")