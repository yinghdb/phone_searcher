#coding=GBK
import sys
import os
sys.path.append("../")
import jieba

def cuttest(test_sent):
    result = jieba.cut(test_sent, cut_all=True)
    resultList = ','.join(result)
    resultLine = resultList.split(',')
    return resultLine

advantageFile = open('advantageDic.dat','wb')
phoneID = 0
postingListNumber = 0
postingList = []
dict = {}
dictLast = []
while phoneID<605:
    openFile = 'phone/phone'+'%d' %phoneID+'/advantage'+'%d' %phoneID+'.txt'
    fp = open(openFile,'r')
    contentText = fp.read()
    contentLine = contentText.split()
    lineNumber = 0
    for line in contentLine:
        cutWord = cuttest(line)
        for keyWord in cutWord:
            if(keyWord in dict):
                pos = dict[keyWord]
                if(dictLast[pos] != '%d' %phoneID):
                    postingList[pos] = postingList[pos]+';'+'%d' %phoneID+','+'%d' %(len(contentLine)-lineNumber)
                    dictLast[pos]='%d' %phoneID
            else:
                dict[keyWord] = postingListNumber
                postingList.append(keyWord+':'+'%d' %phoneID+','+'%d' %(len(contentLine)-lineNumber))
                postingListNumber+=1
                dictLast.append('%d' %phoneID)
        lineNumber+=1
    phoneID+=1
for data in postingList:
    advantageFile.write(data.encode('gbk')+'\n')
