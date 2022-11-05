import sys
sys.path.insert(1, '../backend')
from sarcasm import Sarcasm_Model
from joint import Joint
from subjectivity import Subjectivity_Model
from sentiment import Sentiment_Model

subj_m=Subjectivity_Model('../backend/model/subjectivity.h5')
senti_m=Sentiment_Model('../backend/model/sentiment.h5')
sarcas_m=Sarcasm_Model('../backend/model/sarcasm.h5')
joint_m=Joint('../backend/model/joint.h5')

def subjectivity_analysis(text):
    result=subj_m.score([text])
    print(result)
    result_dict = dict_builder("subj", result[0])
    return result_dict

def sentiment_analysis(text):
    result=senti_m.score([text])
    print(result)
    result_dict = dict_builder("senti", result[0])
    return result_dict

def sarcasm_analysis(text):
    result=sarcas_m.score([text])
    print(result)
    result_dict = dict_builder("sarcas", result[0])
    return result_dict

def joint_analysis(text):
    result=joint_m.score([text])
    print(result)
    result_dict = dict_builder("joint", result)
    return result_dict

def dict_builder(analysis_type, score):
    if analysis_type =="subj":
        neg_score = 1-score
        return {"opinionated" : float(score), "neutral" : float(neg_score)}
    elif analysis_type =="senti":
        neg_score = 1-score
        return {"positive" : float(score), "negative" : float(neg_score)}
    elif analysis_type =="sarcas":
        neg_score = 1-score
        return {"sarcastic" : float(score), "not sarcastic" : float(neg_score)}
    elif analysis_type =="joint":
        faction_score = float(score[0][0])
        senti_score = float(score[1][0])
        faction_neg_score = 1-faction_score
        senti_neg_score = 1-senti_score
        return [{"Democrats" : float(faction_score), "Republicans" : float(faction_neg_score)},
                {"positive" : float(senti_score), "negative" : float(senti_neg_score)}]
