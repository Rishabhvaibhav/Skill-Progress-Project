count = 1
while count < 5:
    
    fibo_input = int(input("enter the number count for fibonacchi sequence  : \n "))

    first_number = 0
    second_number = 1

    temp = 0
    print(first_number,second_number , end = " ")

    for i in range (0,fibo_input):
        temp = first_number + second_number
        print(temp,end = " ")
        first_number = second_number
        second_number = temp
        count += 1