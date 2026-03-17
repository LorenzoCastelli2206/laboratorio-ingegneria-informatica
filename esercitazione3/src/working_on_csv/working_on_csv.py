import re

def clean_word(word):
    testo_min = word.lower()
    testo_min = testo_min.replace('<br', "")
    testo_pulito = re.sub(r'[^a-z\s]', '', testo_min) 
    return testo_pulito

def build_list_csv(file_csv):
    res = []

    with open(file_csv, "r", encoding="utf-8") as file:
        next(file)
        for row in file:
            text_label = row.strip().split('",')
            if (len(text_label) == 2):
                text = text_label[0]
                label = text_label[1]

                dict= {"text": text, "label": label}
                res.append(dict)
    return res

def print_list_csv(lista):
    for e in lista:
        print(e)

