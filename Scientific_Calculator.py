import math

while True:

    print("\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to the power\n6 - Square Root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent")
    
    user_input = input("Please choose your choice from menu: ")     #Getting user input
    print("Your choice is: ", user_input)   #Displaying user input    

    #Here goes code for menu option 0 - Addition
    if user_input == "0":
        value1 = float(input("\nPlease enter first value to be added: "))   #getting first valur from user
        value2 = float(input("\nPlease enter second value to be added: "))  #getting 2nd valur from user
        
        summation = value1 + value2     #Getting result of addition
        print("\nResult of addition of %.1f and %.1f is: %.1f" % (value1, value2, summation))     #printing result
    
    #Here goes code for menu option 1 - Subtraction
    elif user_input == "1":
        subval1 = float(input("\nPlease enter first value for subtraction: "))    #getting first value from user
        subval2 = float(input("Please enter second value for subtraction: "))   #getting second value from user

        subtraction = subval1 - subval2     #getting result for subtraction
        print("\nResult of subtraction of %.1f from %.1f is: %.1f" % (subval2, subval1, subtraction ))    #printing result
    

    #Here goes code for menu optionn 2 - Multiplication
    elif user_input == "2":
        prodval1 = float(input("\nPlease enter first value for multiplication: "))      #getting first value from user
        prodval2 = float(input("Please enter second value for multiplication: "))       #getting secind value from user

        product = prodval1 * prodval2   #performing multiplication
        print("\nResult of multiplication of %.1f and %.1f is: %.1f" %(prodval1, prodval2, product))    #printing results

    
    #Here goes code for menu 3 - division
    elif user_input == "3":
        divval1 = float(input("\nPlease enter numerator: "))    #getting first value from user
        divval2 = float(input("Please enter denomenator: "))    #getting second value from user

        division = divval1 / divval2    #performing division operation
        print("\nResult of division of %.1f by %.1f is: %.1f" %(divval1, divval2, division))    #printing result

    
    #Here goes code for menu 4 - Modulo
    elif user_input == "4":
        modval1 = float(input("\nPlease enter numerator: "))    #getting first value from user
        modval2 = float(input("Please enter denomenator: "))    #getting secind value from user

        modulo = modval1 % modval2  #peerforming modulo operation
        print("\nResult of modulo on %.1f by %.1f is: %.1f" %(modval1, modval2, modulo))    #printing results
    

    #Here goes code for menu 5 - raising to the power
    elif user_input == "5":
        powval1 = float(input("\nPlease enter base value: "))   #getting first value from user
        powval2 = float(input("Please enter exponent value: ")) #getting second value from user

        powerop = pow(powval1, powval2)     #performing raising to power operation
        print("\nResult of rasing %.1f by %.1f is: %.1f" %(powval1, powval2, powerop))      #printing results
    
    #here gors code for menu 6 - square root
    elif user_input == "6":
        sqrootval1 = float(input("\nPlease enter the number to perform square root operation: "))

        sqroot = math.sqrt(sqrootval1)      #performing square root function
        print("\nSquare root of %.1f is: %.1f" %(sqrootval1, sqroot))
        
    
    #here goes code for menu 7 - logarithm
    elif user_input == "7":
        logval = float(input("\nPlease enter value to find logarithm of: "))    #getting value from user
        
        logbase10 =  math.log10(logval)     #finding logarithm base10
        natutrallog = math.log(logval)      #Finding natural logarithm
        print("\nNatural logarithm value for %.1f is: %.3f" %(logbase10, natutrallog))      #Printing results
        print("\nBase 10 logarithm for %.1f is: %.3f" %(logval, logbase10))         #Printing results

    #here goes code for menu 8 - Sine
    elif user_input == "8":
        sineval = float(input("\nPlease enter radiant to find its Sine value: "))      #Getting value from user
        
        sine = math.sin(math.radians(sineval))        #finding sine value 
        print("\nSine value for %.1f degree is: %.3f" %(sineval, sine))        #Printing results

    
    #Here goes code for menu 9 - Cosine
    elif user_input == "9":
        cosineval = float(input("\nPlease enter radiant to find its Cosine Value: "))
        
        cosine = math.cos(math.radians(cosineval))    #Finding Cos value
        print("\n Cosine value for %.1f degrees is: %.3f" %(cosineval, cosine))     #Printing results
    

    #Here goes code for menu 10 - Tangent
    elif user_input == "10":
        tanval = float(input("\nPlease enter radiant to find its Tangent value: "))
        
        tangent = math.tan(math.radians(tanval))
        print("\nTangent value for %.1f degrees is: %.3f" %(tanval, tangent))
    
    #Code for any other menu entry
    else:
        print("\nChosen menu entry is not valid. Please try again.")    #prompting user to re-choose menu
        continue        #restart while loop
          
    
    choice_input = input("\nMathematical operation was successful. Do you want to continue?   y/n\n")   #gettong user input
    
    if choice_input == "y":
        continue        #restart the while loop
    else:
        break           #stop execution
        
    

#Note to self: Implement exception handling to handle division exepetion when done working on this module.
