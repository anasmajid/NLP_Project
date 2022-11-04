from sarcasm import Sarcasm_Model
from joint import Joint
from subjectivity import Subjectivity_Model
from sentiment import Sentiment_Model

m=Sarcasm_Model('model/sarcasm.h5')
#remember to put in a list
result=m.score(['It is alright.'])
print(result)

m=Subjectivity_Model('model/subjectivity.h5')
result=m.score(['This is insane.'])
print(result)

m=Sentiment_Model('model/sentiment.h5')
result=m.score(['Dr Oz is terrible.', 'John Fetterman is the best'])
print(result)

m=Joint('model/joint.h5')
result=m.score(['John Fetterman is awesome.'])
print(result)