from pathlib import Path
import argparse




def tree(path,string="",nb_tab=0) :
    tab = "\t" * nb_tab
    for child in path.iterdir() :
        string += tab+"|__"+child.name+"\n" 
        if child.is_dir() :
            string = tree(child,string,nb_tab+1)
    
    return string


parser = argparse.ArgumentParser(description='Input your Path')
parser.add_argument('path', metavar='path', type=Path)
args = parser.parse_args()


print(tree(args.path))