"""
Program:            Student Finder Program

Author:             Solomon Umoh

Description:        A program that uses a student’s ID Number 
                    to look up the student’s name.


"""

import csv 


def read_dictionary(filename, key_column_index):
    student_dictionary={}

    with open(filename, "rt") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            key_value = row[key_column_index]
            student_dictionary[key_value] = row
    return student_dictionary


def main():
    filename = r"c:\Users\Admin\BYU-Software-Engineering-Course\programming_with_functions\week05\students.csv"

    KEY_INDEX = 0
    NAME_INDEX = 1
    students = read_dictionary(filename, KEY_INDEX)

    inumber = input("Please enter an I-Number: ")

    inumber = inumber.replace("-","")

    if not inumber.isdigit():
            print("Invalid I-number")
    elif len(inumber) < 9:
        print("Invalid ID Number: too few digits")
    elif len(inumber) > 9:
            print("Invalid ID Number: too many digits")

    elif len(inumber) != 9:
        print("An I-number must be 9 digits long.")
    else:

        if inumber in students:
            student = students[inumber]
            name =  student[NAME_INDEX]
            print(f"The student's name is: {name}")
        else:
            print("No such student!")


if __name__ == "__main__":
    main()

