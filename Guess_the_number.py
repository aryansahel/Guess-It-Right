#START OF CODE
#Guess_the_number.py ©

#This is a game where a number is randomly generated and the goal is for the user to guess that number. The number lies between 1 and 20.
#The user is asked to enter a valid number between 1 & 20.
#As the game proceeds, they are given chances to enter new numbers and operators that will change their original number.
#To win the game, the user must guess the randomly generated number in 3 tries or less. 

import msvcrt as m
import random

#Function imported from Microsoft Visual C/C++ library that waits for user to hit enter before executing the rest of the code. 
def wait():
    m.getch()

#Function to do the math depending upon user inputs.
def math_calculator(operator, num_1, num_2):
    if(operator == "+"):
        result = int(num_1) + int(num_2)
    elif(operator == "-"):
        result = int(num_1) - int(num_2)
    elif(operator == "*"):
        result = int(num_1)*int(num_2)
    elif(operator == "/"):
        result = int(num_1)/int(num_2)
    return result
    

name = input("Please enter your name: ")      #Prompts the user for their name.
age = input("Please enter your age: ")        #Prompts the user for their age.

#THIS IS THE ANSWER TO THE GAME. 
#This function returns a randomly generated number within the range of 1 & 20.
answer = random.randint(1, 20) 

print()

#Here we check if the user is fit to play this game given their age.
if(int(age) >= 30):
    print("OOPS! You are too old to play this game :(")
elif(int(age) <= 5):
        print("OOPS! You are too young to play this game :(")

#If the user's age is between 5 and 30 years, the rest of the game will proceed. 
else: 
    #Print statements explaining the game to the user and adding a personal touch.
    print("Welcome", name + "! My name is Michael Scott and I am the regional manager of Dunder Mifflin's Scranton branch.")
    print("As a part of Dunder Mifflin's new initiative, we are offering our customers a discount of 10% on all our products for 6 months!")
    print("There is one condition, however - YOU MUST PASS THE CHALLENGE THAT LIES AHEAD!")
    wait()
    print()

    print("Our team of hardworking employees (and Pam) have devised a special game.")
    print("The object of the game is simple - you have to guess the number I am thinking of in 3 tries or less. Have fun playing!")
    wait()
    print()
    
    #Prompts the user to enter a value between 1 and 20 (both inclusive).
    user_value = input("Please enter a number between 1 and 20: ") 
    
    #If the user enters an invalid value then they are prompted to enter new values
    #until an acceptable value is enterred. 
    while(int(user_value) < 1 or int(user_value) > 20):
        user_value = input("Please re-enter a number between 1 and 20: ")

    #Variable to keep track of the number of tries taken by the user.
    tries = 0

    #In case the user enters the correct value in the first try itself.
    if(int(user_value) == answer):
        print("WHOA! You've hit jackpot! Correct guess in the first try! This calls for a 15% discount!")
    
    #But if that is not the case, then the game proceeds as it is supposed to.
    else: 
        print("The game is ready for you", name + ". Your starting position is", user_value +".")
        print("Henceforth, you'll be given chances to update your existing number.")

        #The loop to run the logic of the game.
        while(int(user_value) <= 20 and user_value != answer and tries <= 3):

            #Prompts user for an operator and value to update the existing number
            operator = input("What operator would you like to use (+, -, *, /)? ")
            while (operator != "+" and operator != "-" and operator != "*" and operator != "/"):
                operator = input("Please enter a valid operator (+, -, *, /): ")
            
            number = input("What number would you like to use your operator on? ")
            while (number.isdigit() == False):                     #Makes sure a valid input is provided by user. 
                number = input("Please enter a valid number: ")
        
            #Updates the user_vaue depending upon the operator and number enterred by the user and then prints out the updated value.       
            user_value = math_calculator(operator, user_value, number)
            print("Your new value is", str(user_value) + ".")
        
            #Increments the number of tries by one.
            tries += 1

        #DECIDING FACTORS FOR THE OUTCOME OF THE GAME ARE LISTED BELOW.
        if(user_value == answer and tries <= 3):
            print("Congratulations! You have won the game and are entitled to our discount!")
        elif(int(user_value) > answer):
            print("OOPS! Your final value is bigger than the answer! The answer was", str(answer) + ". Better luck next time!")
        elif(int(user_value) < answer):
            print("OOPS! Your final value is smaller than the answer! The answer was", str(answer) + ". Better luck next time! ")

#END OF CODE
