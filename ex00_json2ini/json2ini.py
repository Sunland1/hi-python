import json 

def json2ini(object_variable,string="",string_key="") :
    if(object_variable == None) :
        return string
    for key in object_variable :
        if not type(object_variable[key]) == dict :
            if type(object_variable[key]) == list :
                for tab_value in object_variable[key] : 
                    string += key + "[]=" + str(tab_value) + "\n" 
            else : 
                string += key + "=" + str(object_variable[key]) + "\n"
    string+="\n"
    for key in object_variable :
        if type(object_variable[key]) == dict :
            string_key += "." + key
            string += "["+string_key.replace("." , "" , 1)+"]\n"
            return json2ini(object_variable[key],string,string_key)

    return json2ini(None,string,string_key)
 


#opening json file
with open("../asset/exemple_001.json" , "r") as file : 
    data = json.load(file)


with open("../output/exemple_001.ini" , "w") as output_file : 
    output_file.write(json2ini(data))