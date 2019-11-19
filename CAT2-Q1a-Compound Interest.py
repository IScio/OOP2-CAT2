# OOP2 CAT 2
'''b) Write a python program to calculate the compound interest. Use the formula A= P(1 + R/100)t (5 marks)'''

r=float(input("Enter the Rate of Interest: ")) # r is Interest Rate
p=float(input("Enter the Principal Amount: ")) # p is Principal
t=int(input("Enter Term Duration: ")) # t is time.

a=p*(1+r/100)**t    # ** This is an exponential operator
print(round(a,3))   # Print the result rounded to 2 decimal places
