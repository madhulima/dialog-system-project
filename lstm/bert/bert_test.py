#Test bert serving server
from bert_serving.client import BertClient
bc = BertClient()
a = bc.encode(['First do it', 'then do it right', 'then do it better'])
b = bc.encode(['First do it ||| hello me'])
print(a,b)





