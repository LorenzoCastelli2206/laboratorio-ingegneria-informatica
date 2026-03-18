from abc import ABC, abstractmethod
from working_on_csv.working_on_csv import clean_word
import csv

class Model(ABC):
    @abstractmethod
    def train(self, reviews):
        pass

    @abstractmethod
    def predict(self, reviews):
        pass

    def predict_all(self, reviews):
        return [self.predict(r["text"]) for r in reviews]



    ################################## BASICMODEL  ################################## 
class BasicModel(Model):
    def __init__(self):
        self.majority_class = None

    ################################## BASICMODEL TRAIN ################################## 
    def train(self, reviews):
        labels = [r["label"] for r in reviews]
        counts = {}
        for r in reviews :
            l = r["label"]
            if l not in counts:
                counts[l] = 0
            counts[l] += 1
        self.majority_class = int(max(counts, key=counts.get))

        res = "Errore"
        if self.majority_class == 1:
            res = "Positive"
        else:
             res = "Negative"

        avg = counts[str(self.majority_class)]/len(labels)
        #print(f"[BasicModel] Majority class: '{res}', " f"({counts[str(self.majority_class)]}/{len(labels)}), {avg:.3%}")

    ################################## BASICMODEL PREDICT ################################## 
    def predict(self, reviews):
        file_name = "predict_BM.csv"

        labels = [r["label"] for r in reviews]
        texts = [t["text"] for t in reviews]
        count = 0
        res = 0
        for r in reviews : 
            if (labels[count] == "0" and self.majority_class == 0) or (labels[count] == "1" and self.majority_class == 1):
                res += 1

            with open(file_name, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter= ',')
                writer.writerow([texts[count], labels[count], str(self.majority_class)])
            
            count += 1
        
        print(f"Prediction saved on {file_name}")

        acc = res/count
        return acc



    ################################## WORDMODEL ################################## 
min_freq = 5
ratio_min = 1.9 

class WordModel(Model):
    def __init__(self):
        self.majority_class = None
        self.good_words = {}
        self.bad_words = {}

    ################################## WORDMODEL TRAIN ##################################
    def train(self, reviews):
        gd = {}
        bd = {}
        texts = [r["text"] for r in reviews]
        labels = [l["label"] for l in reviews]
        
        contatore = 0
        for row in texts: 
            words = row.strip().split(' ')
            for w in words:
                parola_pulita = clean_word(w)
                if labels[contatore] == "1":
                    if parola_pulita in gd:
                        gd[parola_pulita] += 1
                    else:
                        gd[parola_pulita] = 1
                    
                else:
                    if parola_pulita in bd:
                        bd[parola_pulita] += 1
                    else:
                        bd[parola_pulita] = 1
            contatore += 1

        for w, count in bd.items():
            if count > min_freq:
                if w in gd and (count/gd[w] > ratio_min) :
                    self.bad_words[w] = count/gd[w]
                    #print(f"'{w}' -> Negative: {count} | Positive: {gd[w]}")
                if w not in gd:
                    self.bad_words[w] = count
                    #print(f"'{w}' -> Negative: {count} | Positive: 0") 
        for w, count in gd.items():
            if count > min_freq:
                if w in bd and (count/bd[w] > ratio_min):
                    self.good_words[w] = count/bd[w]
                    #print(f"'{w}' -> Positive: {count} | Negative: {bd[w]}")
                if w not in bd:
                    #print(f"'{w}' -> Positive: {count} | Negative: 0")
                    self.good_words[w] = count

    ################################## WORDMODEL PREDICT ##################################
    def predict(self, reviews):
        file_name = "predict_WM.csv"

        good = 0
        bad = 0
        res = 0

        texts = [r["text"] for r in reviews]
        labels = [l["label"] for l in reviews]
        count = 0
        for row in texts: 
            words = row.strip().split(' ')
            for word in words:
                if word in self.good_words:
                    good += self.good_words[word]
                elif word in self.bad_words:
                    bad += self.bad_words[word]

            if (good > bad and labels[count] == "1") or (bad >= good and labels[count] == "0"):
                res += 1

            char_csv = ''
            if good>bad:
                char_csv = "1"
            else:
                char_csv = "0"
            good = 0
            bad = 0

            with open(file_name, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter= ',')
                writer.writerow([texts[count], labels[count], char_csv])

            count += 1
       
        print(f"Prediction saved on {file_name}")

        acc = res / count
        return acc



        
        
