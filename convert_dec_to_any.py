## UPDATED 

'''
MACHINE ASSIGNMENT 2
Name: Gustavo Andia
Course: CS 517
Term: Summer 2024

'''
### Import Required Packages:
import sys

## Define Global Constant to restrict the number of digits:
MAX_DIGITS = 8

'''
Function 1: convert(base, rationalInput)
This function takes a rationalInput and base and returns is corresponding
conversion to the inputted base. 

'''
def convert(base, rationalInput):

    # Create/initialize a counter to process the input digit by digit
    digitCounter = 1

    # Create a variable to store the result of the conversion:
    conversion_result = "0."
    semicolon = ";"

    while (rationalInput != 0 and digitCounter <= MAX_DIGITS):
        
        prefix = ""

        # Re-assign prefix if length of base is larger
        if len(str(base)) > len(str(int(rationalInput*base))):
            prefix = "0"*(len(str(base)) - len(str(int(rationalInput*base))))
        
        # Append integer of base*number if base = 60
        if base == 60:
            conversion_result = conversion_result +  prefix + str(int(rationalInput*base))

        # If base is not 60, append integer of base*number and a ";"
        else:
            conversion_result = conversion_result  + prefix + str(int(rationalInput*base)) +  semicolon

        # Gather remaining fractional part of the inputted number:
        rationalInput = rationalInput*base - int(rationalInput*base)

        digitCounter = digitCounter + 1 # update the counter
    
    ## Return as flow if base is 60
    if base == 60:
        return float(conversion_result)
    
    ## Return as string if base is other than 60 to show ";"
    else:
        conversion_result = conversion_result[:-1] # drop last ";"
        return str(conversion_result)
    
    
'''
Function 2: showResultTable(base, finalAnswers)
This function takes the array of final conversions and base used as inputs and displays
them in a table. This function uses ".format()" only to format the table for
the output and NOT to perform any parts of the conversion.

'''
def showResultTable(base, finalAnswers):

    ## Create formatting for the final answer table:
    print("| {:<8}| {:<8}|".format("Base 10", "Base " + str(base)))
    print("| {:<8}| {:<8}|".format(":-------", ":-------"))


    ## Iterate through entries and print them
    if base == 60: ## If base is 60, print float with two digits after decimal point
        for answer in finalAnswers:
            print("| %-7s | %.2f    |"%(answer[0], answer[1]))
    
    else: ## If base is not 60, print resulting string with ";"
        for answer in finalAnswers:
            print("| %-7s | %-7s |"%(answer[0], answer[1]))


'''
Function: main():
The main function will gather user input, test any legalities regarding the
input, and then call the convert() and showResultTable() functions to convert
numbers to the given base and display them.

'''
def main():

    # Store the total number of decimal values passed via the command line:
    userEntryTotals = len(sys.argv)

    # Handle case in which no numbers are provided in the coommand line for conversion:
    if userEntryTotals < 3:
        print("Usage: ./convert_dec_to_any.py [base] [num1] [num2] [num3] ...")
        print("The program requires a base, [base], input and at least one decimal [numi] within [0, 1) to execute...")
        exit() # terminate the program

    userBase = int(sys.argv[1]) # store the entered base 

    # Create object to store results for the conversions:
    finalConversions = [{}]*(userEntryTotals - 2)

    # Process every input provided in the command line starting at sys.argv[2]
    # which corresponds to the first number to be converted
    for i in range(2, userEntryTotals):

        ## Gather i'th command line entry corresponding to decimal
        ## numbers being inputted by the user. Per instructions, it
        ## is assumed all input is valid:
        x = float(sys.argv[i])

        ## Restrict the input to input values of x within the interval[0, 1)
        if x < 0 or x >=1:
            print(str(x) + " is out of bounds! Inputs must be within [0, 1)")
            exit() # terminate program

        ## Call function to perform decimal to base conversion and store in array:
        finalConversions[i - 2] = [x, convert(userBase, x)]

    ## Call function to print the results to the screen:
    showResultTable(userBase, finalConversions)


if __name__ == '__main__':
    main()