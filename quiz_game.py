print("Welcome to my computer quiz game!") 

playing = input("Do you want to play? ") 

if playing != "yes":
    quit()

print("Okay! Let's play!")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
else: 
    print("Incorrect!")
    print("The correct answer is central processing unit.") 

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print("Correct!")
else: 
    print("Incorrect!")
    print("The correct answer is graphics processing unit.")
