from working_on_csv.working_on_csv import build_list_csv, print_list_csv
from model.model import BasicModel, WordModel

def main():
    list_csv = build_list_csv("IMDB_validation.csv")

    mid = len(list_csv)//2
    first_part = list_csv[:mid]
    second_part = list_csv[mid:]
    
    basic = BasicModel()
    basic.train(first_part)
    accuracyBM = basic.predict(second_part)
    print(f"accuracy of BasicModel: {accuracyBM:.3%}") 


    word = WordModel()
    word.train(first_part)
    accuracyWM = word.predict(second_part)
    print(f"accuracy of WordModel: {accuracyWM:.3%}") 




























if __name__ == "__main__":
    main()
