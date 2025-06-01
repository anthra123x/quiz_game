print("Welcome to my computer quiz game!") 

playing = input("Do you want to play? ") 

if playing.lower != "yes":
    quit()

print("Okay! Let's play!")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    print("The correct answer is central processing unit.") 

answer = input("What does GPU stand for? ")
if answer.lower == "graphics processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    print("The correct answer is graphics processing unit.")

print("You got " + str(score) + " questions correct!") 