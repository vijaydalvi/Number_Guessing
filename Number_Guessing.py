import random
random_num=random.randint(1,10)
guess=int(input("Guess The Number:-"))
chances=5
while guess!=random_num:
    if guess>random_num:
        chances=chances-1
        if chances==0:
            print("You Loss The Game")
            exit()
        print("Guess is High")
        print("You Have",chances,"chances")
        guess=int(input("Guess the Number:-"))
    elif guess<random_num:
        chances=chances-1
        if chances==0:
            
            print("You Loss The Game")
            exit()
        
        print("Guess is Low")
        print("You Have",chances,"chances")
        guess=int(input("Guess the Number:-"))
    
print(" Congratulations! You Have Won!")