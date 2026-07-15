#Expense Tracker Project

expenses = [] #list of all expenses

while True:
    print("===Calculation===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. EXIT")

    choice=int(input("Enter your choices:"))
    #1. Addition:
    if(choice==1):
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("Result: " ,a+b )
        

    #2. Subtraction
    elif(choice==2):
         a=int(input("Enter the first number: "))
         b=int(input("Enter the second number: "))
         print("Result: ",a-b)
       
        #3.Multiplication
    elif(choice==3):
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        print("Result: ",a*b)
 
        #4. Division
    elif(choice==4):
         a=int(input("Enter the first number: "))
         b=int(input("Enter the second number: "))
         print("Result: ",a/b)
    elif(choice==5):
        print("Thank You for using our calculator !\n")
        break
    else:
        print("Invalid choice. PLease try again !\n")
         