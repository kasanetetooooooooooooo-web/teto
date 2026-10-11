import random
hello_words=["привет","салам","здраствуйте","hello","hi"]
bye=["пока пока","досвидание","пока"]
lol=["исккал медь сгорел медьведь","Действие при пожаре: git commit, git push,покинуть помещение"]

command=""
while command!="3": 
    command=input("\nВведите что то из команд: 1 расскажи шутку, 2 поздоровоться, 3 попрощаться\n выбор: ")
    if command=="1":
        print("искал медь, сгорел медьведь")
    elif command=="2":
        hello=random.choice(hello_words)
        print(hello)
    elif command=="3":
        bye_word=random.choice(bye)
        print(bye_word)
    else:   
        print("ошибка")