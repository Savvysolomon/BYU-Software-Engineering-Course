# open the file 
with open("hr_system.txt") as hr_file:
    next(hr_file)


    # read the content of the file line by line 
    for line in hr_file:
        segments = line.split(" ")

        # save content data into variables 
        # headings =  ["Name", "Identity", "Job Title", "Pay Check"]

        name = segments[0]
        id = segments[1]
        job_title = segments[2]
        salary = int(segments[3])


        # assume the employees are paid twice a month
        paycheck_amount = salary / 24


        # add bonus to only employees with job title of engineer
        bonus = 1000


        if "engineer" in job_title.lower():
            paycheck_amount = paycheck_amount + bonus


        # print the content of the file 
        # print(f"{headings[0]:<15} {headings[1]:<15} {headings[2]:<15} {headings[3]}")
        print("-----------------------------------------------------------------------")
        print(f"{name:<15} (ID: {id})         {job_title:<15} - ${paycheck_amount:.2f}")

# filename = "hr-system.txt"

# # with open("hr_system.txt", "r+") as hr_file:
# #     hr_file.write("Solomon is a software developer")

# with open("hr_system.txt") as hr_file:
#     for line in hr_file:
#         print(line)

