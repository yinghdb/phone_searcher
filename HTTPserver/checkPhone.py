#coding=gbk

import re

def getPhoneMessage():
    fp = open('detail.xml')
    content = fp.read()
    brand = re.findall('<brand>(.+?)</brand>',content)
    price = re.findall('<price>(.+?)</price>',content)
    score = re.findall('<score>(.+?)</score>',content)
    contin = re.findall('<contin>(.+?)</contin>',content)
    scrnEfc = re.findall('<scrnEfc>(.+?)</scrnEfc>',content)
    photoEfc = re.findall('<photoEfc>(.+?)</photoEfc>',content)
    reaction = re.findall('<reaction>(.+?)</reaction>',content)
    perfm = re.findall('<perfm>(.+?)</perfm>',content)
    xinjia = re.findall('<xinjia>(.+?)</xinjia>',content)
    time = re.findall('<time>(.+?)</time>',content)
    scrnSize = re.findall('<scrnSize>(.+?)</scrnSize>',content)
    fenbian = re.findall('<fenbian>(.+?)</fenbian>',content)
    cpu = re.findall('<cpu>(.+?)</cpu>',content)
    battery = re.findall('<battery>(.+?)</battery>',content)
    quality = re.findall('<quality>(.+?)</quality>',content)
    front = re.findall('<front>(.+?)</front>',content)
    back = re.findall('<back>(.+?)</back>',content)
    size = re.findall('<size>(.+?)</size>',content)
    url = re.findall('<url>(.+?)</url>',content)
    return brand,price,score,contin,scrnEfc,photoEfc,reaction,perfm,xinjia,time,scrnSize,fenbian,cpu,battery,quality,front,back,size,url

def decodeXml():
    fp = open('choice.xml')
    content = fp.read()
    brand = re.findall('<brand>(.+?)</brand>',content)
    price = re.findall('<price>(.+?)</price>',content)
    size = re.findall('<size>(.+?)</size>',content)
    fashion = re.findall('<fashion>(.+?)</fashion>',content)
    thin = re.findall('<thin>(.+?)</thin>',content)
    battery = re.findall('<battery>(.+?)</battery>',content)
    bigScreen = re.findall('<bigScreen>(.+?)</bigScreen>',content)
    clrScreen = re.findall('<clrScreen>(.+?)</clrScreen>',content)
    photo = re.findall('<photo>(.+?)</photo>',content)
    self_photo = re.findall('<self-photo>(.+?)</self-photo>',content)
    easy_taken = re.findall('<easy-taken>(.+?)</easy-taken>',content)
    play = re.findall('<play(.+?)</play>',content)
    bussiness = re.findall('<bussiness>(.+?)</bussiness>',content)
    return brand,price,size,fashion,thin,battery,bigScreen,clrScreen,photo,self_photo,easy_taken,play,bussiness

def checkPhone(c_brand,c_price,c_size,c_fashion,c_thin,c_battery,c_bigScreen,c_clrScreen,c_photo,c_self_photo,c_easy_taken,c_play,c_bussiness):
    decodeXml()
    relatedPhone=[]
    (brand,price,size,fashion,thin,battery,bigScreen,clrScreen,photo,self_photo,easy_taken,play,bussiness)=decodeXml()
    dict = {'huawei':'华为','pingguo':'苹果','sanxin':'三星','meizu':'魅族','xiaomi':'小米','oppo':'OPPO','vivo':'VIVO','lianxiang':'联想','nuojiya':'诺基亚'}
    if(c_brand==[]):
        x=0
        for line in price:
            relatedPhone.append(x)
            x+=1
    else:
        x=0
        for line in brand:
            for c_line in c_brand:
                if(line.find(dict[c_line])!=-1):
                    relatedPhone.append(x)
            x+=1

    def comp(List,List2):
        if(List!=[]):
            lineNum = 0
            deleteNum = []
            for line in relatedPhone:
                flag = 0
                for c_line in List:
                    if(c_line==List2[line]):
                        flag = 1
                if(flag==0):
                    deleteNum.append(lineNum)
                lineNum+=1
            x=0
            for line in deleteNum:
                relatedPhone.pop(line-x)
                x+=1
    def comp2(Num,List2):
        lineNum = 0
        deleteNum = []
        for line in relatedPhone:
            if(Num == '1' and List2[line] == '0'):
                deleteNum.append(lineNum)
            lineNum+=1
        x=0
        for line in deleteNum:
            relatedPhone.pop(line-x)
            x+=1

    comp(c_price,price)
    comp(c_size,size)
    comp2(c_fashion,fashion)
    comp2(c_thin,thin)
    comp2(c_battery,battery)
    comp2(c_bigScreen,bigScreen)
    comp2(c_clrScreen,clrScreen)
    comp2(c_self_photo,self_photo)
    comp2(c_easy_taken,easy_taken)
    comp2(c_play,play)
    comp2(c_bussiness,bussiness)

    return relatedPhone