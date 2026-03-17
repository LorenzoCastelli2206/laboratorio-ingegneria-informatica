from abc import ABC, abstractmethod
from working_on_csv.working_on_csv import clean_word

class Model(ABC):
    @abstractmethod
    def train(self, reviews):
        pass

    @abstractmethod
    def predict(self, reviews):
        pass

    def predict_all(self, reviews):
        return [self.predict(r["text"]) for r in reviews]

class BasicModel(Model):
    def __init__(self):
        self.majority_class = None

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
        print(f"[BasicModel] Majority class: '{res}', " f"({counts[str(self.majority_class)]}/{len(labels)}), {avg:.3%}")

    def predict(self, reviews):
        return self.majority_class
    
min_freq = 5
ratio_min = 1.9 

class WordModel(Model):
    def __init__(self):
        self.majority_class = None
        self.good_words = {}
        self.bad_words = {}

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
        #print(good_words)


    def predict(self, reviews):
        good = 0
        bad = 0
        res = 0

        text = [r["text"] for r in reviews]
        labels = [l["label"] for l in reviews]
        count = 0
        for row in text: 
            words = row.strip().split(' ')
            #print(words)
            for word in words:
                if word in self.good_words:
                    good += self.good_words[word]
                elif word in self.bad_words:
                    bad += self.bad_words[word]
            #print(f"ci sono {good} parole buone e {bad} parole cattive")

            if (good > bad and labels[count] == "1") or (bad >= good and labels[count] == "0"):
                res += 1
                print(f"bene = {good}, male = {bad} DAJEEEE")
            else:
                print(f"bene = {good}, male = {bad} ...")

            good = 0
            bad = 0
            count += 1
            #print(res, count)
       

        acc = res / count
        print(f"accuracy : {acc:.3%}")  



        
        
