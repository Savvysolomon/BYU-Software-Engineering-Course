"""

Program:                Receipt Generator
Author:                 Solomon Umoh
Description:            This program prints a receipt for a customer based on the items 
                        they purchased and their prices. It calculates the total cost, 
                        applies any discounts, and formats the output to look like 
                        a receipt.

Enhancement:            Added the feature for calculating and printing a "return by" date and time - 
                        30 days in the future at 9:00 PM at the bottom of the receipt.

"""

import csv  # import the csv module to read the csv file
import os   # import os module to handle file paths dynamically
from datetime import datetime, timedelta  # timedelta for the future date calculation

def read_dictionary(filename, key_column_index):
    """
    Reads a CSV file and returns a dictionary 
    where the keys are from the specified column index.
    """
    # initialize an empty dictionary
    dictionary = {}

    # open the CSV file for reading
    with open(filename, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        
        # skip header row
        next(reader)

        # loop through each row in the CSV file and add it to the dictionary
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row
            
    # return the completed dictionary
    return dictionary
            


def main():
    # start the try block
    try:
        # get the folder path where receipt.py is currently located
        current_directory = os.path.dirname(os.path.abspath(__file__))
        
        # join the folder path to the CSV file names
        products_path = os.path.join(current_directory, "products.csv")
        request_path = os.path.join(current_directory, "request.csv")

        # read the products.csv file dynamically and store it in a dictionary
        products_dict = read_dictionary(products_path, 0) 

        print("Savvy Grocery Store")
        print()
        print("==================== Requested Items ====================")

        # initialize counters to zero before loop starts
        total_items = 0
        subtotal = 0

        # open the request.csv file dynamically
        with open(request_path, mode='r') as request_file:
            reader = csv.reader(request_file)
            
            # skip header row
            next(reader)

            # loop through each row in order
            for row in reader:
                # grab product ID and quantity from row
                product_id = row[0]
                quantity = row[1]
                
                # look up product ID in catalog dictionary
                product_info = products_dict[product_id]
                
                # extract name and price from catalog information
                product_name = product_info[1]
                price = product_info[2]
                
                # print line item
                print(f"{product_name}: {quantity} @ {price}")
        
                # convert string values to numbers 
                total_items += int(quantity)
                subtotal += (int(quantity) * float(price))

        
        print("---------------------------------------------------------")
        
        # calculate tax and total
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total_due = subtotal + sales_tax

        # print the totals
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")
        print()

        # print closure statement and current time stamp
        print("Thank you for shopping at the Savvy Grocery Store!")
        current_date_time = datetime.now()
        print(f"{current_date_time:%a %b %e %H:%M:%S %Y}")

        # addition: calculate and print the 30-day return policy date at 9:00 PM
        return_date = current_date_time + timedelta(days=30)
        return_date_fixed_time = return_date.replace(hour=21, minute=0, second=0)
        print(f"Return Policy: Items can be returned by 9:00 PM on {return_date_fixed_time:%A, %b %d, %Y}")

    # match the except blocks directly with main try statement
    except FileNotFoundError as file_err:
        print("\nError: missing file")
        print(file_err)

    except PermissionError as perm_err:
        print("\nError: You do not have permission to access this file.")
        print(perm_err)

    except KeyError as key_err:
        print("\nError: unknown product ID in the request.csv file")
        print(key_err)


if __name__ == "__main__":
    main()
