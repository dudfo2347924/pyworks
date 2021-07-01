
import pickle

with open('datas.txt','wb') as f:
    li = ['개','소','닭']
    dic = {1:'개',2:'소',3:'닭'}
    pickle.dump(li, f)
    pickle.dump(dic, f)

with open('datas.txt','rb') as f:
    li = pickle.load(f)
    dic = pickle.load(f)
    print(li)
    print(dic)

