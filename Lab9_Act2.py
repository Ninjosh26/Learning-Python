# Name: Josh Stafford
# Assignment: Lab 9 Activity 2
# Section: ENGR 102 - 206
# An aggie does not lie, cheat, or steal, nor tolerate those who do.

# Asks user to input values regarding the loan
amountLoan = float(input("What is the amount of the loan?"))
annualInterestRate = float(input("What is the annual interest rate (percent)?")) / 100
amountPaidMonthly = float(input("What is the amount paid monthly?"))
nameFile = input("What would you like to name the data file?")

totalInterest = 0

# Opens file to write
loanFile = open(nameFile + ".csv", "w")
# Specify the data
loanFile.write("month number, total interest, remaining loan\n")
# If the loan will not be paid off
if amountPaidMonthly <= (amountLoan * annualInterestRate / 12):
    # Iterate through months 0 - 30
    for i in range(31):
        # Prints starting data
        if i == 0:
            loanFile.write(str(i) + ", " + str(totalInterest) + ", " + str(amountLoan) +"\n")
        # Prints data for loan payment
        else:
            totalInterest += amountLoan * annualInterestRate / 12
            amountLoan += amountLoan * annualInterestRate / 12
            amountLoan -= amountPaidMonthly
            # Write loan data to file
            loanFile.write(str(i) + ", " + str(totalInterest) + ", " + str(amountLoan) + "\n")
# If the loan will be payed off
else:
    count = 0
    while True:
        # Print starting data
        if count == 0:
            loanFile.write(str(count) + ", 0, " + str(amountLoan) +"\n")
        # Print loan payment data
        else:
            totalInterest += amountLoan * annualInterestRate / 12
            amountLoan += amountLoan * annualInterestRate / 12
            amountLoan -= amountPaidMonthly
            # End the loop when the loan is payed off
            if amountLoan <= 0:
                loanFile.write(str(count) + ", " + str(totalInterest) + ", 0\n")
                break
            # Write data to file
            loanFile.write(str(count) + ", " + str(totalInterest) + ", " + str(amountLoan) + "\n")
        count += 1
loanFile.close()