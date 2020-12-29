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

# this is the function that checks, add, or modify existing record in the file.
  def add_to_file(self, filename):
    # This will check if record exist or not
    if self.find_in_file(filename):
      # If record exist, this will ask if you want to edit the rocord or cancel
      print( f"Record already exists, do you want to update {self.first_name.capitalize()} {self.last_name.capitalize()}'s record?")
      with open(filename) as o:  
        for line in o:
          old_record = line
      u_response = input("Enter u to Update, c to Cancel -> ")
      record_to_update = Student.prep_to_write(self.first_name, self.last_name, self.courses)
      # If you choose to edit, this will perform the operation
      if u_response == "u":
        with open(filename, "w+") as to_update:
          to_update.write(record_to_update+"\n")
        return f"Record updated \nFrom: {old_record} \nTo: {record_to_update}"
      # If you choose to cancel, this will perform the operation
      else:
        return "No Changes made"
    # if record does not exist, this will add new rocord.
    else:
      record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
      with open(filename, "a+") as to_write:
        to_write.write(record_to_add+"\n")
      return f"New record added: {record_to_add}"

  @staticmethod
  def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details

  @staticmethod
  def prep_to_write(first_name, last_name, courses):
    full_name = first_name+','+last_name
    courses =",".join(courses)
    return full_name+':'+courses

  def __eq__(self, other):
    return self.first_name == other.first_name and self.last_name == other.last_name


  def __len__(self):
    return len(self.courses)


  def __str__(self):
    return f"First Name: {self.first_name.capitalize()}\nLast Name: {self.last_name.capitalize()}\nCourses: {', '.join(map(str.capitalize, self.courses))}"

# This is calling the file we will be working with
file_name = "data.txt"

# This are sample records to be added
mashrur = Student("mashrur", "hossain", ["python", "rubyon","javascript"])
print(mashrur.add_to_file(file_name))
# joe = Student("joe", "schmo", ["python", "rubyoo", "javascript"])
# print(joe.add_to_file(file_name))


# john,doe:java,c++,c
# evgeny,rahman:ruby,rails,javascript
# john,schmoe:python,ruby,javascript