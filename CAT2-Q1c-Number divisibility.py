# OOP2 CAT 2
'''d) Write a Python function to check whether a number is divisible by another number.
Accept two integers values from the user (5 marks)
'''

num1=int(input("Input First Number: "))
num2=int(input("Input First Number: "))

if num2==0:      # Cannot Divide by 0
  print("Oops! Cannot Divide by 0")
else:
  print("Checking if %s is divisible by %s" % (num1,num2))
  if num1 % num2 == 0:   ## Is Divisible
    print("%s is Divisible by %s" % (num1,num2))
  else:
    print("%s is NOT Divisible by %s" % (num1,num2))
