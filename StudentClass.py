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

  def find_in_file(self, filename):
    with open(filename) as f:  
      for line in f:
          first_name, last_name, course_details = Student.prep_record(line.strip())
          Student_read_in = Student(first_name, last_name, course_details)
          if self == Student_read_in:
            return True
      return False

  def add_to_file(self, filename):
    pass

  @staticmethod
  def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details

  def __eq__(self, other):
    return self.first_name == other.first_name and self.last_name == other.last_name


  def __len__(self):
    return len(self.courses)


  def __str__(self):
    return f"First Name: {self.first_name.capitalize()}\nLast Name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"


file_name = "data.txt"
mashrur = Student("mashrur", "hossain", ["python", "ruby","javascript"])
print(mashrur.find_in_file(file_name))
# print(mashrur.add_to_file(file_name))
# joe = Student("joe", "schmo", ["python", "ruby", "javascript"])
# print(joe.find_in_file(file_name))
# print(joe.add_to_file(file_name))


# john,doe:java,c++,c
# evgeny,rahman:ruby,rails,javascript
# john,schmoe:python,ruby,javascript