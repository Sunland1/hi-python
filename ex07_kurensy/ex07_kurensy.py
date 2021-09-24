import tkinter as tk


def calcChange(change, nb_to_change2) : 
    return nb_to_change2/change


intro = """ 
 _   __                                ________   __
| | / /                                | ___ \ \ / /
| |/ / _   _ _ __ ___ _ __  ___ _   _  | |_/ /\ V / 
|    \| | | | '__/ _ \ '_ \/ __| | | | |  __/  \ /  
| |\  \ |_| | | |  __/ | | \__ \ |_| |_| |     | |  
\_| \_/\__,_|_|  \___|_| |_|___/\__, (_)_|     \_/  
                                 __/ |              
                                |___/          """


print(intro)
print("***********************************************************************")


algo = True
while algo : 
    symb1 = str(input("what is the symbole of money to convert : "))
    symb2 = str(input("what is the symbole of the target : "))
    nb_to_change2 = float(input("the value to convert : "))
    change = float(input("the current change for 1" + symb2 + " to " + symb1 + ": "))
    print(str(calcChange(change,nb_to_change2)) + " " + symb2)
    
    cmd = str(input("Again , y/n : "))
    if not cmd == "y" : 
        algo = False 