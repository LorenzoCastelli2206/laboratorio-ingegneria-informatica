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
    

good_words = [
    "good", "great", "excellent", "amazing", "wonderful", 
    "fantastic", "outstanding", "superb", "brilliant", "perfect", 
    "love", "loved", "best", "masterpiece", "beautiful", 
    "enjoyable", "entertaining", "fun", "thrilling", "exciting", 
    "engaging", "hilarious", "clever", "charming", "delightful", 
    "impressive", "incredible", "magnificent", "spectacular", "breathtaking", 
    "phenomenal", "awesome", "flawless", "fascinating", "gripping", 
    "captivating", "satisfying", "recommend", "pleasant", "solid", 
    "strong", "triumph", "classic", "uplifting", "fabulous", 
    "stunning", "exceptional", "marvelous", "glorious", "masterclass"
]
bad_words = [
    "bad", "terrible", "awful", "horrible", "worst", 
    "boring", "dull", "slow", "stupid", "dumb", 
    "predictable", "cliche", "disappointing", "disappointed", "garbage", 
    "trash", "waste", "fail", "failed", "poorly", 
    "weak", "messy", "confusing", "annoying", "irritating", 
    "painful", "dreadful", "abysmal", "unwatchable", "lame", 
    "flawed", "ridiculous", "nonsensical", "mediocre", "forgettable", 
    "disaster", "hate", "hated", "avoid", "skip", 
    "ruin", "ruined", "sadly", "unfortunately", "dragging", 
    "flat", "pointless", "tedious", "uninspired", "pathetic"
]

class WordModel(Model):
    def __init__(self):
        self.majority_class = None

    def train(self, reviews):
        gd = set()
        bd = set()
        texts = [r["text"] for r in reviews]
        labels = [l["label"] for l in reviews]
        
        contatore = 0
        for row in texts: 
            words = row.strip().split(' ')
            for w in words:
                if labels[contatore] == "1":
                    gd.add(clean_word(w))
                else:
                    bd.add(clean_word(w))
            contatore += 1
        
        print(bd)

 


    def predict(self, reviews):
        good = 0
        bad = 0
        good_review = 0
        bad_review = 0

        text = [r["text"] for r in reviews]
        for row in text: 
            words = row.strip().split(' ')
            #print(words)
            for word in words:
                if word in good_words:
                    good += 1
                elif word in bad_words:
                    bad += 1
            #print(f"ci sono {good} parole buone e {bad} parole cattive")
            if good > bad:
                good_review += 1
            elif bad >= good:
                bad_review += 1
            good = 0
            bad = 0
        
        res = "Errore"
        if good_review >= bad_review:
            res = "Positive"
            self.majority_class = 1
        else:
            res = "Negative"
            self.majority_class = 0

        avg = max(bad_review, good_review) / (good_review+bad_review)
        print(f"[WordModel] Majority class: '{res}', " 
              f"({max(bad_review, good_review)}/{(good_review+bad_review)}), "
              f"{avg:.3%}")  



        
        
