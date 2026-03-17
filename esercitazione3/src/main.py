from working_on_csv.working_on_csv import build_list_csv, print_list_csv
from model.model import BasicModel, WordModel

def main():
    list_csv = build_list_csv("IMDB_validation.csv")
    # print_list_csv(list_csv)

    mid = len(list_csv)//2
    first_part = list_csv[:mid]
    second_part = list_csv[mid:]
    
    basic = BasicModel()
    basic.train(list_csv)

    word = WordModel()
    word.train(first_part)
    word.predict(second_part)



























if __name__ == "__main__":
    main()
