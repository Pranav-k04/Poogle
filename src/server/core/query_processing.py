import nltk,time
import json
from logging import getLogger

logger = getLogger("uvicorn.info")

logger.info("Loading assets!! This may take sometime!! Please wait patiently!")
start = time.perf_counter()
urls = json.load(open("./src/server/assets/urls.json", "r"))
titles = json.load(open("./src/server/assets/titles.json", "r"))
idf = json.load(open(f"./src/server/assets/IDF.json", "r"))
logger.info(f"Loaded all the assets in {time.perf_counter()-start}sec")

def process_query(query: str):
    lis = nltk.word_tokenize(query)
    score={}
    for x in lis:
        if not x.isalpha():
            continue
        x = x.lower()
        if idf.get(x) is not None:
            keys=idf[x].keys()
            for key in keys:
                if score.get(key) is None:
                    score[key]=idf[x][key]
                score[key]+=idf[x][key]
    sorted_Dict = sorted(score.items(),key=lambda x:x[1],reverse=True)
    k = 600 if len(sorted_Dict) else len(sorted_Dict)
    top_k =dict(sorted_Dict[:k])
    output = []
    for k in top_k.keys():
        output.append({
            "title": titles[k],
            "url": urls[k]
        })
    
    return output
