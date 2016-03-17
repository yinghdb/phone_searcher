#coding=utf-8
import math



def rank(postingList,postingListDis,indexDict,indexDictDis, keyWords, weightWords, phoneList,d_score):
    print(keyWords)
    print(weightWords)
    scoreAdv = {}
    scoreDis = {}
    Kadv = 1
    Kdis = 0.9
    Kd_score = 0.2
    for line in phoneList:
        scoreAdv[line]=0
        scoreDis[line]=0
    if(keyWords!=[]):
        num = 0
        for keyword in keyWords:
            if keyword in indexDict:
                pos = indexDict[keyword]
                phoneListNum = 0
                postingListNum = 0
                while(phoneListNum<len(phoneList) and postingListNum<len(postingList[pos])):
                    if(phoneList[phoneListNum]>postingList[pos][postingListNum]):
                        postingListNum+=1
                    elif(postingList[pos][postingListNum]>phoneList[phoneListNum]):
                        phoneListNum+=1
                    else:
                        scoreAdv[phoneList[phoneListNum]]+=weightWords[num]*postingList[pos+1][postingListNum]/math.sqrt(len(postingList[pos]))
                        postingListNum+=1
                        phoneListNum+=1
            num+=1
        num = 0
        for keyword in keyWords:
            if keyword in indexDictDis:
                pos = indexDictDis[keyword]
                phoneListNum = 0
                postingListNum = 0
                while(phoneListNum<len(phoneList) and postingListNum<len(postingListDis[pos])):
                    if(phoneList[phoneListNum]>postingListDis[pos][postingListNum]):
                        postingListNum+=1
                    elif(postingListDis[pos][postingListNum]>phoneList[phoneListNum]):
                        phoneListNum+=1
                    else:
                        scoreDis[phoneList[phoneListNum]]+=weightWords[num]*postingListDis[pos+1][postingListNum]/math.sqrt(len(postingListDis[pos]))
                        postingListNum+=1
                        phoneListNum+=1
    score = {}
    for phone in phoneList:
        if(float(d_score[phone])==5.0):
            d_score[phone]='2'
        score[phone]=Kadv*scoreAdv[phone]-Kdis*scoreDis[phone]+Kd_score*float(d_score[phone])
    i=0
    rankList=[]
    while i<20 and score != {}:
        for phone in score.keys():
            if(score[phone]==max(score.values())):
                rankList.append(phone)
                score.pop(phone)
                break
        i+=1
    return rankList

def buildList():
    advantageFile = open('advantageDic.dat', 'rb')
    disadvantageFile = open('disadvantageDic.dat','rb')
    indexDict={}
    indexDictDis={}
    termIndex = 0
    termIndexDis = 0
    postingList=[[]]
    postingListDis=[[]]
    for line in advantageFile:
        splitFirst = line.split(':')
        term = splitFirst[0]
        indexDict[term]=termIndex
        splitSecond = splitFirst[1].split(';')
        for s_line in splitSecond:
            splitThird = s_line.split(',')
            postingList.append([])
            postingList[termIndex].append(int(splitThird[0]))
            postingList[termIndex+1].append(int(splitThird[1]))
        termIndex+=2
    for line in disadvantageFile:
        splitFirst = line.split(':')
        term = splitFirst[0]
        indexDictDis[term]=termIndexDis
        splitSecond = splitFirst[1].split(';')
        for s_line in splitSecond:
            splitThird = s_line.split(',')
            postingListDis.append([])
            postingListDis[termIndexDis].append(int(splitThird[0]))
            postingListDis[termIndexDis+1].append(int(splitThird[1]))
        termIndexDis+=2
    return postingList,postingListDis,indexDict,indexDictDis





'''    for line in disadvantageFile:
        splitFirst = line.split(':')
        term = splitFirst[0]
        splitSecond = splitFirst[1].split(';')
        if(term in indexDict):
            index = indexDict[term]
            for s_line in splitSecond:
                splitThird = s_line.split(',')
                if(postingList[index].count(splitThird[0])):
                    pos = postingList[index].index(int(splitThird[0]))
                    postingList[index+1][pos]-=int(splitThird[1])
                else:
                    postingList[termIndex].append(int(splitThird[0]))
                    postingList[termIndex+1].append(int(splitThird[1]))
        else:
            indexDict[term]=termIndex
            for s_line in splitSecond:
                splitThird = s_line.split(',')
                postingList.append([])
                postingList[termIndex].append(int(splitThird[0]))
                postingList[termIndex+1].append(int(splitThird[1]))
            termIndex+=2
'''