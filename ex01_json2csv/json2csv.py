import pandas as pd 

def json2csv(json_path,output_path) :
    df = pd.read_json (json_path)
    df.to_csv (output_path, index = None)



json2csv("../asset/exemple_001.json" , "../output/test.csv")