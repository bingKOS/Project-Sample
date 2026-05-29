name = "John"
date = "2025-10-15"
date_of_birth = "2000-04-14"
age = 25
location = "London"
country = "UK"
weight = 70.5
year_of_study = 2025
student_id = "12345"
classes = ["Math", "Science", "English"]
marks = {"Math": 76, "Science": 45, "English": 22, "Geography": 89}
majors = ("Math", "Science", "English")
minors = (("History", "Geography"), ("Biology", "Chemistry"))

print("Name:", name, type(name))
print("Date:", date, type(date))
print("Age:", age, type(age))
print("Location:", location, type(location))
print("Country:", country, type(country))
print("Weight:", weight, type(weight))
print("Year of Study:", year_of_study, type(year_of_study))
print("Student ID:", student_id, type(student_id))
print("Classes:", classes, type(classes))
print("Marks:", marks, type(marks))
print("Majors:", majors, type(majors))
print("Minors:", minors, type(minors))

def getName(name):
    return (name)

def getProfile(name, age, location, country, date_of_birth):
    print (f"My name is {name}")
    print (f"My age is {age}")
    print(f"My location is {location}")
    print(f"My country is {country}")
    print(f"My date of birth is {date_of_birth}")

def getClasses(classes):
    for i in classes:
        print(f"My class is {i}", end =" , ")
def getMarks(marks):
    for key, value in marks.items():
        print(f"I got {value} in {key}")

def getGrades(marks):
    for key, value in marks.items():
        if value >= 90:
            print(f"I got {value} in {key} which is an A")
        elif value >= 80:
            print(f"I got {value} in {key} which is a B")
        elif value >= 70:
            print(f"I got {value} in {key} which is a C")
        elif value >= 60:
            print(f"I got {value} in {key} which is a D")
        else:
            print(f"I got {value} in {key} which is an F")

my_name = getName( "Marie")
getProfile(my_name, age, location, country, date_of_birth)
#'My name is Marie' instead of 'My name is John'
getClasses(classes)
getMarks(marks)
getGrades(marks)
text = f"My classes are { ', '.join(classes)}"
print(text)

  


