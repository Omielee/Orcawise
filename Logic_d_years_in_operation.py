import csv
import math

def calculate_years_in_operation(revenue, profit):
    # Adjust weights to make the results more reasonable
    profit_stability_weight = 0.3
    profit_growth_weight = 0.7

    # Calculate profit growth rate
    profit_growth_rate = profit / revenue

    # Calculate years in operation using sigmoid function
    score = profit_stability_weight * profit_growth_rate - profit_growth_weight * profit_growth_rate
    years_in_operation = 30 / (1 + math.exp(-score))

    # Round the result to two decimal places
    return round(years_in_operation, 2)

# function for csv file
def fill_years_in_operation(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Header
        header = next(reader)
        header_index = header.index('Years in Operation')  
        writer.writerow(header)

        # calculate the years
        for row in reader:
            revenue = float(row[0])
            profit = float(row[1])
            years_in_operation = calculate_years_in_operation(revenue, profit)
            row[header_index] = years_in_operation  
            writer.writerow(row)


input_file = 'Business_Loan_Dataset - Business Loan Dataset.csv'
output_file = 'Change_Business_Loan_Dataset.csv'

fill_years_in_operation(input_file, output_file)

