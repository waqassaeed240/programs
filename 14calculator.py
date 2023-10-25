val1 = int(input("Enter the value 1 :- "))
val2 = int(input("Enter the value 2 :- "))
opr = input("Enter the Opr:- ")
if opr =='+':
    print(val1 + val2)
elif opr == '-':
    print(val1 - val2)
elif opr == '/':
    print(val1 / val2)
elif opr == '*':
    print (val1 * val2) 
else:
    print("Invilid Opr...")