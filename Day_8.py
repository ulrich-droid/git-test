   ## EXERCICE: Day 9
   ## 1
   ## empty dictionary
dog = {}
   ## 2
   ## add
dog["name"]="pacha"
dog["color"]="brown"
dog["breed"]="pit bul"
dog["legs"]="30 cm"
dog["age"]="2 years"
print("The dog information are:",dog)
   ## 3
   ## student dictionary
student_dictionary = {"firs_tname:":"AREGBA","last_name:":"ULRICH","gender:":"M","age:":23,"marital status:":"single","skills":["python","html","javascript"],"country:":"TOGO","city":"LOME","adresse:":"agoe"}
print("The student informations are:",student_dictionary)
   ## 4
   ## length
print("The length of student dictionary is:",len(student_dictionary))
   ## 5
   ## value of skills
print("the student skills are:",student_dictionary["skills"])
   ## 6
   ## modification of skills
student_dictionary["skills"]=["python","html","javascript","Node","MongoDB"]
print("student new information are:",student_dictionary)
   ## 7
   ## dictionnary keys as a list
print("dictionnary keys are:",student_dictionary.keys())
   ## 8
   ## dictionnary values as a list
print("dictionnary values are:",student_dictionary.values())
   ## 9
   ## dictionnary to a list of tuples
print("this dictionnary to list become:",student_dictionary.items())
   ## 10
   ## delete of one items in the dictionnary
print("delete of student adresse")
del student_dictionary["city"]
   ## 11
   ## delete of one dictionnary
print("delete of dog")
del dog 