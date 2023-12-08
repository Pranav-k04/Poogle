import pandas as pd
import os, re
import json, time
import nltk
import math

#loading file paths
files = os.listdir("./full/")

#index contruction
IDF={}
doc_len={}
urls={}
titles={}
no_of_file=len(files)

start = time.perf_counter()
for x ,file in enumerate(files):
    fil = json.loads(open(f"./full/{file}", "r").read())
    if 'url' not in fil.keys():
        continue
    if 'unigramCount' not in fil.keys():
        continue
    flag = int(file.split('.')[0])
    urls[flag] = fil['url']
    doc_len[flag] = fil['wordCount']
    titles[flag] = fil['title']
    for key, value in fil["unigramCount"].items():
        if re.match('^[a-zA-Z]+$',key):
            key=key.lower()
            sub_key=int(file.split('.')[0])
            if(IDF.get(key)==None):

                IDF[key]={}
            if(IDF[key].get(sub_key) is  None):
                IDF[key][sub_key]=value
            IDF[key][sub_key]=+value
    if(x+1)%10000 ==0 :
        print(f'{x+1} files done')

for key in IDF.keys():
    doc_frq=len(IDF[key].keys())
    for sub_key in IDF[key].keys():
        if type(sub_key) is int:
            IDF[key][sub_key] = (1+math.log(IDF[key][sub_key],2))*math.log(len(doc_len)/doc_frq)/doc_len[sub_key]

print(f"TF-IDF of files in {time.perf_counter()-start} sec")
open("IDF.json", "w").write(re.sub("\n", "", json.dumps(IDF, indent=0)))
open("urls.json", "w").write(re.sub("\n", "", json.dumps(urls, indent=0)))
open("titles.json", "w").write(re.sub("\n", "", json.dumps(titles, indent=0)))