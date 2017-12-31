import nltk
import random
import pickle
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC,NuSVC
from sklearn.linear_model import LogisticRegression
from statistics import mode
from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
class voteClassifier(ClassifierI):

    def __init__(self,*classifiers):
        self._classifier=classifiers

    def classify(self, feature):
        vote=[]
        for c in self._classifier:
            v=c.classify(feature)
            vote.append(v)

        return mode(vote)
    def confidence(self,feature):
        vote=[]
        for c in self._classifier:
            v=c.classify(feature)
            vote.append(v)
        choice_count=vote.count(mode(vote))
        return choice_count/len(vote)



##unpickle document
file_in=open("document.pickle","rb")
document=pickle.load(file_in)
file_in.close()


    
##unpickle all_words  
file_in=open("all_words.pickle","rb")
all_words=pickle.load(file_in)
file_in.close()

all_words=nltk.FreqDist(all_words)
word_feature=list(all_words.keys())[:1000]

def find_feature(string):
    
   w=word_tokenize(string)
   feature={}
   for i in word_feature:
       feature[i]=(i in w)

   return feature


feature_set=[(find_feature(rev),cat) for rev,cat in document]
random.shuffle(feature_set)

##pickle feature_set
##file_out=open("feature_set.pickle","wb")
##pickle.dump(feature_set,file_out)
##file_out.close()

train_set=feature_set[:10000]
test_set=feature_set[10000:]




##unpickle naivebayes
file_in=open("nbc.pickle","rb")
classifier=pickle.load(file_in)
file_in.close()


##unpickle linearsvc
file_in=open("lsvc.pickle","rb")
Lsvc_classifier=pickle.load(file_in)
file_in.close()

##unpickle nusvc
file_in=open("nusvc.pickle","rb")
Nusvc_classifier=pickle.load(file_in)
file_in.close()


##unpickle LR
file_in=open("LR.pickle","rb")
LR_classifier=pickle.load(file_in)
file_in.close()


vote_classifier=voteClassifier(Lsvc_classifier,Nusvc_classifier,LR_classifier)
##print("Accuracy percentage of VC:",(nltk.classify.accuracy(vote_classifier,test_set))*100)
##
##print("classify:", vote_classifier.classify(test_set[6][0]) ,"confidence %",vote_classifier.confidence(test_set[6][0])*100)




def sentiment(text):
    feats=find_feature(text)
    return vote_classifier.classify(feats),vote_classifier.confidence(feats)*100



