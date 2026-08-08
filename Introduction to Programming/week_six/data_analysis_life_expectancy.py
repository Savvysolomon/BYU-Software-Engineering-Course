"""
Program:                Life Expectancy Analyst

Author:                 Solomon Umoh


Description:            This program analyzes life expectancy data from a CSV file. 
                        It reads the data, processes it, and provides insights into 
                        life expectancy trends over time.     

                        
Creative Addition:      Allows user to type in country name of interest to discover
                        its average, minimum and maximum life expectancies.

"""

# open the file 
with open("life-expectancy.csv") as life_file:

    next(life_file)  # skip the header line

    # initialize variables to track overall minimum and maximum life expectancy
    overall_min_expectancy = float('inf')
    overall_max_expectancy = float('-inf')
    min_country = ""
    min_year = 0
    max_country = ""
    max_year = 0

    # initialize variables for average life expectancy
    year_min_expectancy = float('inf')
    year_max_expectancy = float('-inf')
    year_min_country = ""
    year_max_country = ""
    year_total_expectancy = 0
    year_count = 0

    # initialize variables for country
    country_total_expectancy = 0
    country_count = 0
    country_min_expectancy = float('inf')
    country_max_expectancy = float('-inf')
    country_min_year = 0
    country_max_year = 0



    # ask user for input they wish to analyze
    user_year = int(input("Enter the year of interest: "))

    user_country = input("Enter a country of interest: ").strip()



    # read the file line by line 
    for line in life_file:
        parts = line.split(",")  # split the line into parts

        # save each part in a separate variable
        country = parts[0].strip()
        year = int(parts[2].strip())
        life_expectancy = float(parts[3].strip())


        # check lowest and highest life expectancy
        if life_expectancy < overall_min_expectancy:
            overall_min_expectancy = life_expectancy
            min_country = country
            min_year = year


        if life_expectancy > overall_max_expectancy:
            overall_max_expectancy = life_expectancy
            max_country = country
            max_year = year


        # check for year specific life expectancy based on user input
        if year == user_year:
            year_total_expectancy = year_total_expectancy + life_expectancy
            year_count += 1

            # check for the minimum in the specific year
            if life_expectancy < year_min_expectancy:
                year_min_expectancy = life_expectancy
                year_min_country = country


            # check for the maximum in the specific year
            if life_expectancy > year_max_expectancy:
                year_max_expectancy = life_expectancy
                year_max_country = country



        # country specific min, max and average life expectancy
        if country.lower() == user_country.lower():
            country_total_expectancy += life_expectancy
            country_count += 1

            # check for the minimum in the specific country
            if life_expectancy < country_min_expectancy:
                country_min_expectancy = life_expectancy
                country_min_year = year

            # check for the maximum in the specific country
            if life_expectancy > country_max_expectancy:
                country_max_expectancy = life_expectancy
                country_max_year = year

    # check average year
    if year_count > 0:
        average_year = year_total_expectancy / year_count

    # check average country
    if country_count > 0:
        average_country = country_total_expectancy / country_count

    # print the results
    print("----------------------------------------------------------------")
    print(f"Overall minimum life expectancy: {overall_min_expectancy} in {min_country} ({min_year})")
    print(f"Overall maximum life expectancy: {overall_max_expectancy} in {max_country} ({max_year})")
    print("----------------------------------------------------------------")
   

    # print out year-specific details
    if year_count > 0:
        print(f"For the year {user_year}:")
        print(f"  The average life expectancy across all countries was {average_year:.2f}")
        print(f"  The max life expectancy was in {year_max_country} with {year_max_expectancy}")
        print(f"  The min life expectancy was in {year_min_country} with {year_min_expectancy}")
    else:
        print(f"No data found for the year {user_year}.")
    print("----------------------------------------------------------------")


    #print out country specific details
    if country_count > 0:
        print(f"For the country {user_country.title()}:")
        print(f"  The average life expectancy over time was {average_country:.2f}")
        print(f"  The historic max was {country_max_expectancy} in {country_max_year}")
        print(f"  The historic min was {country_min_expectancy} in {country_min_year}")
    else:
        print(f"No data found for the country '{user_country}'.")