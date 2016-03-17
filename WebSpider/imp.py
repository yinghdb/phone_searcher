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


    score = re.findall('���� <strong>(.+?)</strong>',respHtml)
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
        text = text+"�ع�����"+User+'\n'
    else:
        return 0

    found = re.search('<span id="newPmVal_4">(<a href=.+?>)?(?P<User>.+?)(</a>)?</span>', respHtml);
    if(found):
        User = found.group("User");
        text = text+"�����ߴ�"+User+'\n'
    else:
        return 0

    found = re.search('<span>�����ֱ��ʣ�</span>(<a href=.+?>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"�ֱ���"+User+'\n'
    else:
        return 0

    found = re.search('CPUƵ��</span>\s+?<span id=".+?">(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"CPUƵ��"+User+'\n'
    else:
        return 0

    found = re.search('<span>���������</span>(<a href=.+?>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"�������"+User+'\n'
    else:
        return 0

    found = re.search('�ֻ�����</span>\s+?<span id=".+?">(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"����"+User+'\n'
    else:
        return 0

    found = re.search('<span>��������ͷ��</span>(<a href=.+?>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"������ͷ"+User+'\n'
    else:
        return 0

    found = re.search('<span>ǰ������ͷ��</span>(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</p>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"ǰ����ͷ"+User+'\n'
    else:
        return 0

    found = re.search('�ֻ��ߴ�</span>\s+?<span id=".+?">(<a href=("|\').+?("|\')>)?(?P<User>.+?)(</a>)?</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"�ֻ��ߴ�"+User+'\n'
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
        text = text+"Ʒ��"+User+'\n'
        print(User)
    else:
        return 0

    found = re.search('<b\s+?class="price-type price-retain".+?>(?P<User>.+?)<i class="icon">', respHtml);
    if(found):
        User = found.group("User");
        text = text+"�ο��۸�"+User+'\n'
    else:
        return 0

    found = re.search('</span>\s+?<span>(?P<User>.+?)</span>\s+?<span\s+?class="space">', respHtml)
    if(found):
        User = found.group("User");
        text = text+"����"+User+'\n'
    else:
        return 0

    found = re.search('<strong>�������</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"�������"+User+'\n'
    else:
        return 0

    found = re.search('<strong>��ĻЧ��</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"��ĻЧ��"+User+'\n'
    else:
        return 0

    found = re.search('<strong>����Ч��</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"����Ч��"+User+'\n'
    else:
        return 0

    found = re.search('<strong>Ӱ������</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"Ӱ������"+User+'\n'
    else:
        return 0

    found = re.search('<strong>������</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"������"+User+'\n'
    else:
        return 0

    found = re.search('<strong>�Լ۱�</strong>.+?<span class="text">(?P<User>.+?)</span>', respHtml)
    if(found):
        User = found.group("User");
        text = text+"�Լ۱�"+User+'\n'
    else:
        return 0

    found = re.search('<a href="(?P<User>.+?)" target="_self">����</a>', respHtml)
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