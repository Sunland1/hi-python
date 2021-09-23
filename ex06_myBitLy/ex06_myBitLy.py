import json
import string
import random

def bitlyURL() :
    letters = string.ascii_lowercase + string.ascii_uppercase
    random_letter = ''.join(random.choice(letters) for i in range(5))
    return "https://bit.ly/"+random_letter

def resolveURL(bitly_url,store) :
    url = "" 
    for key,value in store.items() : 
        if(value == bitly_url) :
            url = key
            break
    return url

def isInStore(url,store) :
    bitly_url = ""
    isIn = False 
    for key,value in store.items() : 
        if(key == url) :
            bitly_url = value
            isIn = True
            break
    return  isIn,bitly_url


def storeURL(url,bitly_url,store) :
    store[url] = bitly_url
    with open("./store.json" , "w") as file : 
        file.write(json.dumps(store , sort_keys=True, indent=4))
    return store



def getStore() :
    with open("./store.json" , "r") as file : 
        return  json.load(file)



def printStore(store) : 
    print(json.dumps(store , sort_keys=True, indent=4))



intro = """ 
                 _     _ _   _   _        ________   __
                | |   (_) | | | | |       | ___ \ \ / /
 _ __ ___  _   _| |__  _| |_| |_| |_   _  | |_/ /\ V / 
| '_ ` _ \| | | | '_ \| | __| __| | | | | |  __/  \ /  
| | | | | | |_| | |_) | | |_| |_| | |_| | | |     | |  
|_| |_| |_|\__, |_.__/|_|\__|\__|_|\__, | \_|     \_/  
            __/ |                   __/ |              
           |___/                   |___/               """




rule = """

****************************************************************************

    CMD : 
        show : show the current store of url shortly 
        bitly : bitly your url ! (exp : bitly myurl )
        resolve: resolve a bitly url  ! (exp: resolve mybitly_url)
        exit : exit the program !


***************************************************************************
"""

print(intro)
print(rule)

store = getStore()
isOn = True
bitly_url = ""
while isOn : 
    cmd = str(input("type your commande here : ")).split(" ")

    if cmd[0] == "show" :
        print("******************** Store ***********************") 
        printStore(store)
        print("**************************************************")


    elif cmd[0] == "bitly" : 
        url = cmd[1]
        isIn,bitly_url = isInStore(url,store)
        if isIn : 
            print("oops.. this url are in the store :" , bitly_url)
        else : 
            bitly_url = bitlyURL()
            print("Your bitly URL is : " , bitly_url)
            store = storeURL(url,bitly_url,store) 

    elif cmd[0] == "resolve" :

        bitly_url = cmd [1]
        url = resolveURL(bitly_url,store)
        if url == "" : 
            print("NOT IN THE STORE URL")
        else : 
            print("Your resolve this url : " , url)


    elif cmd[0] == "exit" :
        print("Good Bye ! :) ") 
        isOn = False
    

    else : 
        print("Wrong commande")



