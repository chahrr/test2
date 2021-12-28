def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('student_names.txt',2)


#gfdfdbg
file = open("student_names.txt")

numberOflines = 1

for i in range(numberOflines):

    line = file.readline()
    print("the first n lines of the file is ",line)
