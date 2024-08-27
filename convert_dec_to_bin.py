'''
MACHINE ASSIGNMENT 1
Name: Gustavo Andia
Course: CS 517
Term: Summer 2024

'''
### Import Required Packages:
import sys

## Define Global Constant to restrict the number of digits:
MAX_DIGITS = 8

'''
Function 1: convertToBinary(rationalInput)
This function takes a rationalInput and returns is corresponding
conversion to binary. This function implements the algorithm from
chapter 1 to perform the conversion.

'''
def convertToBinary(rationalInput):

    # Create/initialize a counter to process the input digit by digit
    digitCounter = 1

    # Create a variable to store the result of the conversion:
    binary_result = str()

    # Given that the input is not 0, process it digit by digit
    # until the counter is equal to the MAX_DIGITS = 8
    while (rationalInput != 0 and digitCounter <= MAX_DIGITS):
        
        # Multiply by 2 and re-assign this value to number being
        # Processed
        rationalInput = rationalInput * 2

        # CASE 1: After multiplying by 2, if input is greater than or equal
        # to 1 (we are not always going to run into the exactly 1 case)
        if rationalInput >= 1:
            binary_result = binary_result + '1' # append 1 digit to result
            rationalInput = rationalInput - 1 # subtract 1 from input input

        # CASE 2: After multiplying by 2, if input is less than 1 ...
        else:
            binary_result = binary_result + '0' # append 0 to result

        digitCounter = digitCounter + 1 # update the counter

    ## return converted value with ".0" appended in front:
    return "0." + binary_result


'''
Function 2: showResultTable(finalAnswers)
This function takes the array of final conversions as an input and displays
them in a table. This function uses ".format()" only to format the table for
the output and NOT to perform any parts of the conversion.

'''
def showResultTable(finalAnswers):

    ## Create formatting for the final answer table:
    print("| {:<8}| {:<8}|".format("Base 10", "Base 2"))
    print("| {:<8}| {:<8}|".format(":-------", ":-------"))

    ## Iterate through entries and print them
    for answer in finalAnswers:
        print("| {:<8}| {:<8}|".format(answer[0], answer[1]))
        

'''
Function: main():
The main function will gather user input, test any legalities regarding the
input, and then call the convertToBinary() and showResultTable() to convert
numbers to binary and display them.

'''
def main():

    # Store the total number of decimal values passed via the command line:
    userEntryTotals = len(sys.argv)

    # Handle case in which no numbers are provided in the coommand line for conversion:
    if userEntryTotals <= 1:
        print("Usage: ./convert_dec_to_bin.py [num1] [num2] [num3] ...")
        print("The program requires at least one input [numi] within [0, 1) to execute...")
        exit() # terminate the program

    # Create object to store results for the conversions:
    finalConversions = [{}]*(userEntryTotals - 1)

    # Process every input provided in the command line starting at sys.argv[1]
    # which corresponds to the first number to be converted
    for i in range(1, userEntryTotals):

        ## Gather i'th command line entry corresponding to decimal
        ## numbers being inputted by the user. Per instructions, it
        ## is assumed all input is valid:
        x = float(sys.argv[i])

        ## Restrict the input to input values of x within the interval[0, 1)
        if x < 0 or x >=1:
            print(str(x) + " is out of bounds! Inputs must be within [0, 1)")
            exit() # terminate program

        ## Call function to perform decimal to binary conversion and store in array:
        finalConversions[i - 1] = [x, convertToBinary(x)]

    ## Call function to print the results to the screen:
    showResultTable(finalConversions)


if __name__ == '__main__':
    main()