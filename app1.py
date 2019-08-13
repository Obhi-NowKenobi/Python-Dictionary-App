import json
from difflib import get_close_matches

incorrect = "The word doesn't exist, please double check it."
data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == 'N':
            return incorrect
        else:
            return "We didn't understand your entry."

    else:
        return incorrect


word = input("Enter a word: ")

output = translate(word.lower())

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


