file = open("student_names.txt", "r")
lines = file.readlines()
last_lines = lines[-3:]

print(last_lines)
file.close()