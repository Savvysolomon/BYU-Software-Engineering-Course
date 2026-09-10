"""
Program:            Result Checker

Author:             Solomon Umoh

Description:        An application that help mentors to add scores of students,
                    view students result and remove student from record. 

"""

# Initialize the variables
mentor_database = ["solomon umoh", "nathaniel blake", "blessing wilson"]
student_records = []



print("================= ALBERT EINSTEIN'S SCHOOL PORTAL ===================\n")

# with open("school_database.csv") as school_file: 
#     next(school_file)

print("Welcome! Login to gain access to the Result Checker Environment.\n")


print("========= Login Area =========== \n")


# =================== LOGIN PHASE ========================
while True: 
    user_login = input("Enter your username: ").strip()

    # action for user login
    if user_login in mentor_database:
        print("You're logged in successfully.\n")


        print("========== MENU ==============")
        print("-------------------------------")
        print("1. Add to Score Register (+)")
        print("-------------------------------")
        print("2. View Score Board <0>")
        print("-------------------------------")
        print("3. Logout of the Portal (x)")
        print("-------------------------------\n")
        break
    else:
        print("Invalid login details. Try again.")


# ==================  MENU PHASE =========================
while True:
    user_choice = input("Enter a menu number: ") 

    # action for menu 1
    if user_choice == "1":
        print("-----------------------------------------------------")
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_score = input("Enter student's score: ")

        # append student data to the record
        record = {
            "id": student_id, 
            "name": student_name,
            "score": student_score 
        }
        student_records.append(record)
        print("-----------------------------------------------------")
        print(f"The record for {student_name} has been added successfully!\n")

    # action for menu 2
    elif user_choice == "2":
        print("\n============================ STUDENT RECORDS =================================\n")
        if not student_records:
            print("No records found")

        for record in student_records:
            
            print(f"Student ID: {record['id']}    |   Student Name: {record['name']}    |   Student Score: {record['score']} ")
            print("------------------------------------------------------------------------------")
        print("\n==============================================================================")

    # action for menu 3
    elif user_choice == "3":
        print("Logging out of the portal. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, or 3.\n")


