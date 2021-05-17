import random

#set the limits to the card guessing
UPPERLIMIT = 10 
LOWERLIMIT = 0 
number = random.randint(LOWERLIMIT,UPPERLIMIT)

print("**********************************")
print("WELCOME TO THE NUMBER GUESSING GAME!")
print("**********************************")
print("PLEASE GUESS A NUMBER FROM 1 to 10! ")

#create the function called a 
def a():
    #setting the score as a counter for points to 0
    score = 0
    guess = int(input())
    
    if guess == number:
        score += 1
        print("GREAT JOB!")
    
    #checking if the user guesses the correct number
    while guess != number:
        if guess > number:
            print("TOO HIGH")
            score += 0
            
        elif guess < number:
            print("TOO LOW")
            score += 0
          
        if guess == number:
            print("YOU GOT IT CORRECT! ")
            score += 0
        print("PLEASE TRY AGAIN!")
        
        guess = int(input())
        
        if guess > number:
            score += 0
            
        elif guess < number:
            score += 0
            
        if guess == number:
            score += 0
            
            #breaks out of the while loop
            break
    
    #prints the total score 
    print("Your total score is: ", score) 
    return score
    
#calls the function
a()
