import json

students = []
# add student
def add_student():
    name = input("Enter Name : ")
    mark = float(input("Enter Mark : "))
    students.append({"Name": name, "Marks": mark})
    print("Student Added...✔️")

# show student
def show_student():
    if not students:
        print("Student not available")
    else:
        print("Student List:")
        for i, student in enumerate(students):
            print(f"{i+1}. {student['Name']} - {student['Marks']}")


# delete student
def delete_student():
    show_student()
    while True:
        try:
            index = int(input("Enter Student Number to Delete: ")) - 1
            if 0 <= index < len(students):
                removed = students.pop(index)
                print("Removed Student :", removed['Name'])
                break
            else:
                print("InValid Index")
        except:
            print("Enter Valid Index")


# search student
def search_student():
    name = input("Enter Student Name : ")
    found = False
    for s in students:
        if s["Name"].lower() == name.lower():
            print(f"Found : {s['Name']} - {s['Marks']}")
            found = True

    if not found:
        print("Student not found...😓")

# save student
def save_student():
    with open("students.json", "w") as file:
        json.dump(students, file)

# load studendt
def load_student():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
        students.extend(data)
    except:
        pass

# load student data
load_student()

# main loop
while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Enter Your Choice : ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        save_student()
        print("Data saved, Exiting...")
        break
    else:
        print("Invalid Choice 🥺")