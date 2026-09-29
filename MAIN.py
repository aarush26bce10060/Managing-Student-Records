# Student Record Project
# Made by me
# Python program to store marks and write to file

# storing student details in lists
rolls = []
names = []
m1_list = []
m2_list = []
m3_list = []
totals = []
percents = []
grades = []
attendances = []

def calc_grade(p):
    # function to calculate grade
    if p >= 90:
        return "A+"
    if p >= 80 and p < 90:
        return "A"
    if p >= 70 and p < 80:
        return "B"
    if p >= 60 and p < 70:
        return "C"
    if p >= 50 and p < 60:
        return "D"
    if p < 50:
        return "Fail"

def load():
    try:
        f = open("students_data.txt", "r")
        lines = f.readlines()
        f.close()
        
        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                rolls.append(parts[0])
                names.append(parts[1])
                m1_list.append(float(parts[2]))
                m2_list.append(float(parts[3]))
                m3_list.append(float(parts[4]))
                totals.append(float(parts[5]))
                percents.append(float(parts[6]))
                grades.append(parts[7])
                attendances.append(float(parts[8]))
        print("Data loaded successfully!")
    except:
        # if file is not found
        print("No previous data file found, starting new.")

def save():
    f = open("students_data.txt", "w")
    for i in range(len(rolls)):
        # combining string with commas
        row = str(rolls[i]) + "," + str(names[i]) + "," + str(m1_list[i]) + "," + str(m2_list[i]) + "," + str(m3_list[i]) + "," + str(totals[i]) + "," + str(percents[i]) + "," + str(grades[i]) + "," + str(attendances[i]) + "\n"
        f.write(row)
    f.close()

def add_student():
    print("")
    print("--- ADD NEW STUDENT ---")
    r = input("Enter Roll No: ")
    n = input("Enter Name: ")
    
    # getting inputs
    m1 = float(input("Enter Mark 1: "))
    m2 = float(input("Enter Mark 2: "))
    m3 = float(input("Enter Mark 3: "))
    att = float(input("Enter Attendance %: "))
    
    tot = m1 + m2 + m3
    per = tot / 3
    grd = calc_grade(per)
    
    # append to lists
    rolls.append(r)
    names.append(n)
    m1_list.append(m1)
    m2_list.append(m2)
    m3_list.append(m3)
    totals.append(tot)
    percents.append(round(per, 2))
    grades.append(grd)
    attendances.append(att)
    
    save()
    print("Student added and saved!")

def show_all():
    print("")
    print("--- LIST OF ALL STUDENTS ---")
    if len(rolls) == 0:
        print("No records found.")
    else:
        print("Roll \t Name \t Total \t Percentage \t Grade \t Attendance")
        for i in range(len(rolls)):
            print(str(rolls[i]) + " \t " + str(names[i]) + " \t " + str(totals[i]) + " \t " + str(percents[i]) + "% \t\t " + str(grades[i]) + " \t " + str(attendances[i]) + "%")

def search():
    print("")
    print("--- SEARCH STUDENT ---")
    s_id = input("Enter Roll Number: ")
    found = 0
    
    for i in range(len(rolls)):
        if rolls[i] == s_id:
            found = 1
            print("Found!")
            print("Roll No    :", rolls[i])
            print("Name       :", names[i])
            print("Marks      :", m1_list[i], m2_list[i], m3_list[i])
            print("Total      :", totals[i])
            print("Percentage :", percents[i], "%")
            print("Grade      :", grades[i])
            print("Attendance :", attendances[i], "%")
            break
            
    if found == 0:
        print("Student not found!")

# main program execution starts here
load()

while True:
    print("\n***** MENU *****")
    print("1. Add Student")
    print("2. Display All")
    print("3. Search Student")
    print("4. Save")
    print("5. Exit")
    
    ch = input("Enter choice (1-5): ")
    
    if ch == "1":
        add_student()
    elif ch == "2":
        show_all()
    elif ch == "3":
        search()
    elif ch == "4":
        save()
        print("Saved successfully!")
    elif ch == "5":
        save()
        print("Goodbye!")
        break
    else:
        print("Wrong input, please try again!")