# creating a main function where i can call all my functions under the main function
def main():
    # problem1()
    # problem2()
    # problem3()
    # problem4()


def problem1():
    print("The answer to problem 1")  #created two variables. 1 that is the start of my ssentence
    intro = "My name is"
    myName = "Melaati"
    print(intro, myName)

    # Create a function with two variables.
    # One should equal “My name is: “ and the other should equal your actual name.
    # Print the two variables in one print message.



def problem2():
    print("The answer to problem 2")   #this is asking the user to input their extra credit amount
    extraCredit = int(input("Enter the extra credit earned"))
    if(extraCredit < 5):
        print("Thats not enough extra credit")   #if its less that five it says its too little
    elif(extraCredit > 20):
        print("Thats too much extra credit")      #if its more than 20 it says its too much
    else:
        print("Thats perfect")
    # Create a function to ask the user to enter the extra credit they earned.
    # If they entered less than 5 print “That’s not enough extra credit.”
    # If they entered more than 20 print “That’s too much extra credit”.



def problem3():
    userPassword = input("Enter your passsword")      #compariing two inputs that the user put to make sure they match
    reEnterPassword = input("Re-enter your password")
    if(userPassword == reEnterPassword):
        print("Password match")     #if the password doesnt match its says it doesnt match
    else:
        print("Password did not match")



# Create a function to ask a user to enter a password.
# Enter a password. Ask user to reenter password.
# Check to see if they are correct.


def problem4():
    firstCard = int(input("Pick a card number "))
    secondCard = int(input("Pick another card number"))
    total = (firstCard + secondCard)     #its asking the user for two numbers and adding it to see if they got black jack or not
    print(total)
    if(total == 21):
        print("BLACKJACK!!")
    elif(total>21):
        print("BUST!")
    elif(total<21):
        print("The total is", str(total))




    # Create a function to ask for two card numbers.
    # If it equals 21 print BLACKJACK!,
    # if it’s greater than 21 print BUST!,
    # if it’s less than 21 print “The total is [THE TOTAL]”

























if __name__ == '__main__':
    main()

