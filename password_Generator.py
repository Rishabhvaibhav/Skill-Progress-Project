import random

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

count = 1
while count <= 5:
    try:
        input_number = int(input("Enter how many numbers you want: "))
        input_alphabet = int(input("Enter how many alphabets you want: "))
        input_symbols = int(input("Enter how many symbols you want: "))
        
        password = ""
        if input_alphabet or input_number or input_symbols == -1:
            break
        
        for _ in range(0, input_alphabet):
            password += random.choice(alphabet)
        
        for _ in range(0, input_number):
            password += random.choice(number)
        
        for _ in range(0, input_symbols):
            password += random.choice(symbols)
        
        print(password)
        count += 1
    except:
        print(NameError())
else:
    print("Loop Ended")
