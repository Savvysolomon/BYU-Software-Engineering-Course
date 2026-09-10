# open the file

file_path = "Introduction to Programming\\week_six\\web_traffic.csv"

with open(file_path) as web_file:


    total_time = 0
    total_referrals = 0
    total_pages = 0
    # read through the file line by line 
    for line in web_file:

        # split the line into parts
        parts = line.split(",")

        # store each parts in a separate variable
        page = parts[0].strip()
        time = float(parts[1].strip())
        referring_page = parts[2].strip()

        total_time += time
        total_referrals += 1
        total_pages += 1

        # print the file 
        print("-------------------------------------------------------------------------------")
        print(f"Page '{page}' was referred from '{referring_page}' for '{time}' seconds.")
    print("-------------------------------------------------------------------------------")
    print(f"Total time spent on the page was: {total_time} seconds.")
    print(f"Total number of referrals: {total_referrals}")
    print(f"Total number of pages: {total_pages}")  
    print("================================================================================")


