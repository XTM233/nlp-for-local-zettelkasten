import jieba
import jieba.analyse
import jieba.posseg as pseg
import re
import os
from random import randint

exclude_list = ["无法","时候","空空","赶紧","小时","部分","地方","有点","结果","基本","实际","利用","方面","原因","大家","大量"] # TODO 自动添加exclude list 如果对结果不满意
# for i in '，。！？：“”……（）':
#    txt=txt.replace(i,'')

def simple_split(content, exclude_list=exclude_list):
    txt = re.sub('\W*', '', content)
    words=list(jieba.cut(txt))
    words = [w for w in words if w not in exclude_list]
    return words

def simple_frequency(words, k=20, exclude_sigmoid=True):
 
    dic={}
    for i in words:
        if len(i)==1 or i in exclude_list:
            continue
        else:
            dic[i]=dic.get(i,0)+1
     
    wc=list(dic.items())
    wc.sort(key=lambda x:x[1],reverse=True)
    if exclude_sigmoid:
        wc = [(w[0], w[1]) for w in wc if w[1] > 1]
    return wc
    # for i in range(k):
    #     print(wc[i])

def tfidf_ana(content):
    content_s = "".join(content).strip()
    title_keys = jieba.analyse.extract_tags(content_s, topK=10, withWeight=False)  # topK is the number of keywords expected to be obtained
    title_keys = ','.join(title_keys)
    return title_keys

# data = tfidf_ana(f)

# print(data)

def noun_only(content):
    words =pseg.cut(content)
    nouns = [w.word for w in words if w.flag == "n"]
    return nouns

# result = simple_frequency(noun_only(f))
# for w in result:
#     print(w)

files = os.listdir("./")
exclude_files = [".git", ".stfolder", ".stversions"]

def detect_tags(files, exclude_files):
    dic = {}
    total_pc = {}
    count = 0
    for filename in files:
        count += 1
        if filename not in exclude_files:
            content = open(filename,'r',encoding='UTF-8').read()
            result = simple_frequency(noun_only(content), exclude_sigmoid=False)
            for word_tup in result:
                i = word_tup[0]
                dic[i] = dic.get(i,0) + word_tup[1]
                if total_pc.get(i):
                    total_pc[i].append(filename)
                else:
                    total_pc[i] = [filename]
        if count % 100 == 0:
            print(f"{count} files processed.")

    total_wc = list(dic.items())
    total_wc.sort(key=lambda x:x[1],reverse=True) # list.sort() doesn't return anything
    # total_wc = [w for w in total_wc if len(total_pc[w[0]]) >= 3]
    result = []
    for w in total_wc:
        i = w[0]
        if total_pc[i]:
            if len(total_pc[i]) >= 3:
                result.append(w)
    total_wc = result
    # for w in total_wc:
    #     print(w[0],w[1],total_pc[w[0]])
    random_tags(total_wc,total_pc)


def random_tags(total_wc,total_pc):
    ranran = len(total_wc)
    lst = [ ]
    for i in range(5):
        ing = randint(0, ranran-1)
        w = total_wc[ing]
        lst.append(w[0])
        print(i,w[0],w[1],total_pc[w[0]][:3])
    tmp = input("select the keyword you'd like to check: ")
    try: 
        for i in total_pc[lst[int(tmp)]]:
            print(i)
            if input("Y to confirm selection") == "Y":
                os.startfile(i) # TODO write a preview function，最好能直接显示包含关键词的那一行
        if input("Want more keywords?") != "N":
            random_tags(total_wc,total_pc)
    except TypeError:
        print("redraw the keywords")
        random_tags(total_wc,total_pc)
detect_tags(files,exclude_files)