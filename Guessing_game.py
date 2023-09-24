import random

while True:
    try:
        guess_number = int(input("Enter Any number You guess between 0 to 10 : "))
        Computer_guess = random.randint(0,10)   
        if guess_number == Computer_guess:
            print("Your guess is Match ")
        else :
            print("Didn't Match ")
    except:
        print(TypeError)
    
