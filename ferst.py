number1=input("напишите пожалуйста число: ")
number1=int(number1)
# print(number1)
# print(id(number1))
# print(type(number1))

number2=input("напиши второе число: ")
number2=int(number2)

sign=input("напишите знак (-,+,*,/): ")
if sign=="-":
    print("вы выбрали вычитание")
    result=(number1-number2)
    print(f"{number1}-{number2}={result}")
if sign=="+":
    print("вы выбрали сложение")
    result=(number1+number2)
    print(f"{number1}+{number2}={result}")