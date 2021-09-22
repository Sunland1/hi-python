import random as rd


def checkRule(number_c , number_u) : 
    if number_c == number_u :
        print("computer choose the same thing")
        return None

    if number_c == 1 :
        if number_u == 3 :
            print("computer choose scissors and you chosse : paper")
            return False
        else :
            print("computer choose scissors and you chosse : stone")
            return True

    if number_c == 2 :
        if number_u == 1 :
            print("computer choose stone and you chosse : scissors")
            return False
        else :
            print("computer choose stone and you chosse : paper")
            return True

    if number_c == 3 :
        if number_u == 2 :
            print("computer choose paper and you chosse : stone")
            return False
        else :
            print("computer choose paper and you chosse : scissors")
            return True





intro = """
_     _  _______  ___      _______  _______  __   __  _______   _______  _______   ______    _______  _______ 
| | _ | ||       ||   |    |       ||       ||  |_|  ||       | |       ||       | |    _ |  |       ||       |
| || || ||    ___||   |    |       ||   _   ||       ||    ___| |_     _||   _   | |   | ||  |    _  ||       |
|       ||   |___ |   |    |       ||  | |  ||       ||   |___    |   |  |  | |  | |   |_||_ |   |_| ||       |
|       ||    ___||   |___ |      _||  |_|  ||       ||    ___|   |   |  |  |_|  | |    __  ||    ___||      _|
|   _   ||   |___ |       ||     |_ |       || ||_|| ||   |___    |   |  |       | |   |  | ||   |    |     |_ 
|__| |__||_______||_______||_______||_______||_|   |_||_______|   |___|  |_______| |___|  |_||___|    |_______|

"""


commande = """
-----------------------------------------------------------------------------

    press 1 for scissors
    press 2 for stone
    press 3 for paper

-----------------------------------------------------------------------------

    write "exit" to exit the game
    write "start" to start a party 

-----------------------------------------------------------------------------

"""


print(intro)
print(commande)

game = True
while game :
    input_user = input("start a party ?\n")
    if input_user == "start" : 
        print("let's go !")
        print("---------------------------")
        print("the computer has chosen something ! ")
        ramdom_nb = rd.randint(1,3)
        user_action = int(input("Choose an action :\n"))
        isWin = checkRule(ramdom_nb,user_action)
        if isWin : 
            print("GG you won ! ")
        elif isWin != None : 
            print("You loose !")
        else :
            print("EQUAL")
    if input_user == "exit" : 
        print("Good by ! :)")
        game = False









