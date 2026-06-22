print("----------TO-DO LIST MENU----------\n")

num1,num2 = map(int,input("Enter two numbers: ").split())

print(" 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
ch = int(input("Enter choice number: "))

match ch:
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        print(num1/num2)
    case _:
        print("Invalid Choice")
