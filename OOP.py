
class student:
        
        
        def __init__(self, name, age, classes, progress):
            self.name = name
            self.age = age
            self.classe = classes
            self.progress = progress
            self.StillAllStudent = True 

        def isminor(self):
          return(self.age<18)


class PartTimeStudent(student): 
        def __init__(self, name, age, classes, progress):
            student.__init__(self, name, age, classes, progress)
            

class FullTimeStudent(student):
     
      pass


john = PartTimeStudent("John", 15, "[maths]", 70)

print("is John a minor", john.isminor())
