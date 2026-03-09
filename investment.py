"""
Program: investment.py
2/18/2026 Nancy
Chapter 3 case study

Application that provides investment report. User provides details about investment. Output is calculations for each year individually and some final summaries.
"""
# Input phase
print()
startBalance=float(input("Please, enter the investment amount>> "))
years= int(input("Next, enter the number of years for the investment>> "))
rate=float(input("Finally, enter the interest as a percent>> "))


# Processing phase

rate=rate/100

# initalize the accumulator variable for the interest
totalInterest=0.0

#Display header for table in tabular format
print() # this will create line break on its own


# Compute and display the results for each year usig a FOR LOOP.

for year in range(1,years+1):
	interest=(startBalance*rate)
	endBalance=startBalance+interest 
	print("%4d%18.2f%10.2f%16.2f" % (year,startBalance, interest, endBalance))
	startBalance=endBalance
	totalInterest+=interest
	# end of loop

#output phase displaying the totals

print ("-" * 50)
print ("Final Balance: $%0.2f" % endBalance)
print ("Total Interest Earned: $%0.2f" % totalInterest)

input ("\nPress ENTER TO exit.")

