# 1. Есть у программистов одна очень популярная задача FizzBuzz: написать программу, которая спрашивает число у пользователя и :
# если число кратно 3, выводит Fizz;
# если число кратно 5, выводит Buzz;
# если число кратно 3 и 5, выводит FizzBuzz

number=input("нипишите число: ")
number=int(number)
print(f"ваше число {type (number)}")
if number %5==0 and number %3==0: 
    print("FizzBuzz")
elif number%3==0: 
    print("fizz")
elif number%5==0:
    print("buzz")
