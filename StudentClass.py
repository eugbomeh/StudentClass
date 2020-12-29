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


  def __len__(self):
    return len(self.courses)


  def __str__(self):
    return f"First Name: {self.first_name.capitalize()}\nLast Name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"


file_name = "data.txt"
mashrur = Student("mashrur", "hossain", ["python", "ruby","javascript"])
print(mashrur.find_in_file(file_name))
print(mashrur.add_to_file(file_name))
joe = Student("joe", "schmo", ["python", "ruby", "javascript"])
print(joe.find_in_file(file_name))
print(joe.add_to_file(file_name))