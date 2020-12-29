class Student:
  
  def __init__(self, first, last, courses=None):
    self.first_name = first
    self.last_name = last
    if courses == None:
      self.courses = []
    else:
      self.courses = courses


  def add_course(self, course):
    if course not in self.courses:
      self.courses.append(course)
    else:
      print(f"{self.first_name} is already enrolled in the {course}")


  def remove_course(self, course):
    if course in self.courses:
      self.courses.remove(course)
    else:
      print(F"{course} not found.")



course_1 = ['python','rails','javascript']
course_2 = ['java','rails','c']

mashrur = Student("mashrur","hossain",course_1)
john = Student("john","doe",course_2)



print(mashrur.first_name, mashrur.last_name, mashrur.courses )
print(john.first_name, john.last_name, john.courses )

mashrur.add_course("rails")
print(mashrur.first_name, mashrur.last_name, mashrur.courses )
mashrur.add_course("java")
print(mashrur.first_name, mashrur.last_name, mashrur.courses )
john.remove_course("c")
print(john.first_name, john.last_name, john.courses )
john.remove_course("c")
print(john.first_name, john.last_name, john.courses )
john.remove_course("python")
print(john.first_name, john.last_name, john.courses )
