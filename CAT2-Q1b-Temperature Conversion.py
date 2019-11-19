# OOP2 CAT 2
'''c) Write a Python program to convert temperatures to and from celsius, fahrenheit. [
Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in
fahrenheit ] (5 marks)
Expected Output :
60°C is 140 in Fahrenheit; 45°F is 7 in Celsius'''

print("C: Input Temperature in Celsius ")
print("F: Input Temperature in Fahrenheit ")

choice=input("Press C or F: ")

if choice.upper()=="C": # User may press small c or Caps C
    #Accept Temperature in C and Convert to F
    t=float(input("Enter Temperature in Celsius "))
    c=(t/5*9)+32
    print("%s Degrees C is %s Degrees F" % (t,c))        

elif choice.upper()=="F": # User may press small f or Caps F
    #Accept Temperature in F and Convert to C
    t=float(input("Enter Temperature in Fahrenheit "))
    f=(t-32)/9*5
    print("%s Degrees F is %s Degrees C" % (t,f)) 
else:
    print("Invalid input. Only C or F is expected")    
