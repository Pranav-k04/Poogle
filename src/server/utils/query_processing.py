import nltk,time,json

IDF = json.loads(open(f"IDF1.json", "r").read())
urls = json.loads(open(f"urls.json",'r').read())
titles = json.loads(open(f"titles.json",'r').read())

query = "human brain"

lis= nltk.word_tokenize(query)
score={}
start = time.perf_counter()
for x in lis:
    x = x.lower() 
    if IDF.get(x) is not None:
        keys=IDF[x].keys()
        for key in keys:
            if score.get(key) is None:
                score[key]=IDF[x][key]
            score[key]+=IDF[x][key]
sorted_Dict = sorted(score.items(),key=lambda x:x[1],reverse=True)
print(f"sorted files in {time.perf_counter()-start} sec")
k=600
top_k =dict(sorted_Dict[:k])
url_list=[]
title_list=[]
for k in top_k.keys():
    url_list.append(urls[k])
    title_list.append(titles[k])
print(top_k.keys())
print(url_list)
print(title_list)
