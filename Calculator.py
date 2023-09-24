def Calculator():
    show_operator = ("Addition = +" , 
                    "Subtract = -" ,
                    "Multiply = *", 
                    "Divide =   /" , 
                    "Power =   **" )
    print(show_operator)
    print()
    operator = input("Enter the operators you want : ")
        
    user_input_1 = int(input("Enter the First Number   : "))

    user_input_2 = int(input("Enter the second Number  : "))

    try:
        if operator == "+" : 
            print(user_input_1 + user_input_2)
        elif operator == "-":
            print(user_input_1 - user_input_2)
        elif operator == "*":
            print(user_input_1 * user_input_2)
        elif operator == "/":
            print(user_input_1 / user_input_2)
        elif operator == "**":
            print(user_input_1 ** user_input_2)
        else:
            print("Invalid Entry ")
    except:
        print(TypeError)

Calculator()