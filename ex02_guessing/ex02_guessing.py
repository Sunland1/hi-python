import random as rd 

def printClue(a,b,secrect_number) :
    midle = (a+b)//2
    if midle == secrect_number :
        print("It's close !")
        return a,b
    else : 
        if secrect_number > midle :
            print(str(midle+1) + "<secrect number<" + str(a))
            return a , midle + 1 
        else :
            print(str(b) + "<secrect number<" + str(midle-1)) 
            return midle - 1 , b  




intro = """
 _____                     _               _____   ___  ___  ___ _____ 
|  __ \                   (_)             |  __ \ / _ \ |  \/  ||  ___|
| |  \/_   _  ___  ___ ___ _ _ __   __ _  | |  \// /_\ \| .  . || |__  
| | __| | | |/ _ \/ __/ __| | '_ \ / _` | | | __ |  _  || |\/| ||  __| 
| |_\ \ |_| |  __/\__ \__ \ | | | | (_| | | |_\ \| | | || |  | || |___ 
 \____/\__,_|\___||___/___/_|_| |_|\__, |  \____/\_| |_/\_|  |_/\____/ 
                                    __/ |                              
                                   |___/                               """

print(intro+"\n")
rule = """
************************************************************************

RULE : Try to guess the number ! 

Option: write "start" to start the game 
        write "stop" to stop the game

************************************************************************
"""

print(rule)

###A améliorer => si l'utilisateur tape bien un chiffre 
game = True
while game :
    option = input("Start the game : ")
    if(option == "start") :
        a = int(input("Choose a range SUP : "))
        b = int(input("Choose a range INF : "))
        secrect_number = rd.randint(b,a)
        isLoose = True
        while isLoose :
            user_number = int(input("Choose a number : ")) 
            if user_number == secrect_number :
                print("You won the secret number is :" , secrect_number)
                isLoose = False
            else :
                a,b = printClue(a,b,secrect_number)
    else :
        game = False