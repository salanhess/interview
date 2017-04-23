#coding = utf-8

#http://www.pythonchallenge.com/pc/def/peak.html

import pickle


pkl_file = open('C5_banner.p', 'rb')
selfref_list= pickle.load(pkl_file)

with open('C5_info.txt','wb') as f:
    pickle.dump(selfref_list,f)

with open('C5_info.txt') as f:
    print(pickle.load(f).encode('utf-8'))


