import json
import difflib
#from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y for yes or N for no: " % get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word,data.keys())[0]];
        elif yn == 'N':
            return "Word does not exist !!"
        else:
            return "Dint understand the input..!"

    else:
        return  "Word does'nt exist..Please double check"

word = input("Enter value to search: ")
if(len(word)<10):
    output = translate(word)
    if type(output) == list:
        for items in output:
            print(items)
    else:
        print(output)
else:
    print("enter a WORD..!!")
