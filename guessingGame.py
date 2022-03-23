import random 
print('Number guessing game')
number=random.randint(1,9)
chances=0
print('Guesss a number between 1 and 9')
while chances<5:
    guess=int(input('Enter your guess:-'))
    if guess==number:
        print ('Congo you won') 
        break
    elif guess<number :
     print ('Guess a higher number')
     break
    if not chances<5:
        print('YOU LOSE!!,The Number was:',number)
    
