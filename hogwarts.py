# demonstrates lists
students = ["Hermoine", "Harry", "Ran"]
""" print(students[0])
print(students[1])
print(students[2]) """


"""for i in range(len(students)):
    print(students[i])"""

for student in students:
    print(student)


# demonstrates dictionaries - map
students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
    }  

for student in students :
    print (student, students[student], sep=" - ")


# list of dictionaries
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronous": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronous": "stag"},
    {"name": "Draco", "house": "Slytherin", "patronous": None} # None is a keyword/special value that indicates no value
]

for student in students:
    print(student["name"], student["house"], student["patronous"], sep=", ")