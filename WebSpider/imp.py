# coding=GBK
import urllib;
import urllib2;
import re;
import os;


def getComment(userMainUrl, number):
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();

    text = ''
    os.makedirs('E:/CODES/PYTHON/WebSpider/phone/phone'+'%d' %number)
    os.chdir('E:/CODES/PYTHON/WebSpider/phone/phone'+'%d' %number)

    advantage = re.findall('data-gd="1" title="(.+?)" onclick="return false">',respHtml)
    for line in advantage:
        text = text + line + '\n'
    advantageFile = open('advantage'+'%d' %number+'.txt','w')
    advantageFile.write(text)

    text = ''
    disadvantage = re.findall('data-gd="2" title="(.+?)" onclick="return false">',respHtml)
    for line in disadvantage:
        text = text + line + '\n'
    disadvantageFile = open('disadvantage'+'%d' %number+'.txt','w')
    disadvantageFile.write(text)

    text = ''
    comment = re.findall('<p><span>(.+?)</span>',respHtml)
    for line in comment:
        text = text + line + '\n'
    commentFile = open('comment'+'%d' %number+'.txt','w')
    commentFile.write(text)


    score = re.findall('概括 <strong>(.+?)</strong>',respHtml)
    if score==[]:
        score=['100']
    print(score)
    scoreFile = open('score.txt','w')
    scoreFile.write(score[0])

#------------------------------------------------------------------------------
def getPhoneInformMessage(userMainUrl):
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    text = ''



    found = re.search('<span id="newPmVal_1">(<a href=.+?>)?(?P<User>.+?)(</a>)?</span>', respHtml);
    if(found):
        User = found.group("User");
        text = text+"曝光日期"+User+'\n'
    else:
        return 0

    found = re.search('<span id="newPmVal_4">(<a href=.+?>)?(?P<User>.+?)(</a>)?</span>', respHtml);
    if(found):
        User = found.group("User");
        text = text+"主屏尺寸"+User+'\n'
    else:
        return 0

    found = re.search('<span>主屏分辨率：</span>(<a href=.+?>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"分辨率"+User+'\n'
    else:
        return 0

    found = re.search('CPU频率</span>\s+?<span id=".+?">(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"CPU频率"+User+'\n'
    else:
        return 0

    found = re.search('<span>电池容量：</span>(<a href=.+?>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"电池容量"+User+'\n'
    else:
        return 0

    found = re.search('手机重量</span>\s+?<span id=".+?">(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"重量"+User+'\n'
    else:
        return 0

    found = re.search('<span>后置摄像头：</span>(<a href=.+?>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"后摄像头"+User+'\n'
    else:
        return 0

    found = re.search('<span>前置摄像头：</span>(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"前摄像头"+User+'\n'
    else:
        return 0

    found = re.search('手机尺寸</span>\s+?<span id=".+?">(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"手机尺寸"+User+'\n'
    else:
        return 0

    return text

def getPhoneMainMessage(userMainUrl, number):
    req = urllib2.Request(userMainUrl);
    resp = urllib2.urlopen(req);
    respHtml = resp.read();
    text = ''

    found = re.search('<div class="page-title clearfix">\s+?<h1>(?P<User>.+?)</h1>', respHtml);
    if(found):
        User = found.group("User");
        text = text+"品名"+User+'\n'
        print(User)
    else:
        return 0

    found = re.search('<b\s+?class="price-type price-retain".+?>(?P<User>.+?)<i class="icon">', respHtml);
    if(found):
        User = found.group("User");
        text = text+"参考价格"+User+'\n'
    else:
        return 0

    found = re.search('</span>\s+?<span>(?P<User>.+?)</span>\s+?<span\s+?class="space">', respHtml)
    if(found):
        User = found.group("User");
        text = text+"评分"+User+'\n'
    else:
        return 0

    found = re.search('<strong>电池续航</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"电池续航"+User+'\n'
    else:
        return 0

    found = re.search('<strong>屏幕效果</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"屏幕效果"+User+'\n'
    else:
        return 0

    found = re.search('<strong>拍照效果</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"拍照效果"+User+'\n'
    else:
        return 0

    found = re.search('<strong>影音娱乐</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"影音娱乐"+User+'\n'
    else:
        return 0

    found = re.search('<strong>外观设计</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"外观设计"+User+'\n'
    else:
        return 0

    found = re.search('<strong>性价比</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"性价比"+User+'\n'
    else:
        return 0

    found = re.search('<a href="(?P<User>.+?)" target="_self">参数</a>', respHtml)
    if(found):
        User = found.group("User");
        informAddress = 'http://detail.zol.com.cn/'+User
    else:
        return 0

    commentAddress = informAddress[0:37]+'review.shtml'

    informMessage = getPhoneInformMessage(informAddress)
    if(informMessage):
        getComment(commentAddress, number)
        text = text + getPhoneInformMessage(informAddress) + userMainUrl
        return text
    else:
        return 0

def webSpider():
    productnum = 0
    listnumber = 1
    while listnumber<26:
        url = 'http://detail.zol.com.cn/cell_phone_index/subcate57_list_'+'%d' %listnumber+'.html'
        req = urllib2.Request(url);
        resp = urllib2.urlopen(req);
        resphtml = resp.read();

        subhtml = re.findall('<a href="/cell_phone/.+?" class="pic" target="_blank"><img width="220" height="165".+?" alt=""></a>\s+?.+?\s+?.+?\s+?.+?\s+?.+?</b>', resphtml)
        for line in subhtml:
            checkValid = re.findall('class="price-sign"',line)
            if (checkValid):
                subpageurl = re.findall('href="(.+?\.shtml)"',line)
                text = getPhoneMainMessage('http://detail.zol.com.cn'+subpageurl[0], productnum)
                if(text):
                    detailfile = open('phone'+'%d' %productnum+'.txt','w')
                    detailfile.write(text)

                    imgurl = re.findall('src="(.+?\.jpg)"',line)
                    urllib.urlretrieve(imgurl[0],'%s.jpg' % productnum)
                    productnum+=1
                else:
                    print 'not valid phone'
            else:
                print "not valid phone"
        print(listnumber)
        listnumber += 1

#    productNum = 0
#    phoneFile = 'phone' + '%d' %productNum
#    commentFile = 'comment'
#    os.makedirs('phone'+'/'+phoneFile+'/'+commentFile)
#    os.chdir('phone'+'/'+phoneFile)
#    detailFile = open(phoneFile+'.txt','w')
#    detailFile.write(getPhoneMainMessage('http://detail.zol.com.cn/cell_phone/index392236.shtml'))



###############################################################################
if __name__=="__main__":
    webSpider()