#coding=utf-8
from flask import Flask
from flask import request
from flask import render_template
import jieba
import checkPhone
import DicRank

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    a=render_template('HTMLmodel.html',phoneList=[])
    return a

@app.route('/search', methods=['GET','POST'])
def search():
    isuse={'fashion':'0','thin':'0','battery':'0','bigScreen':'0','clrScreen':'0','photo':'0','self_photo':'0','easy_taken':'0','play':'0','bussiness':'0'}
    brand = request.form.getlist('brand')
    price = request.form.getlist('price')
    size = request.form.getlist('size')
    use = request.form.getlist('use')
    for line in use:
        isuse[line]='1'
    del keyword[:]
    keyword.extend(( ' '.join(jieba.cut(request.form['keyword']))).encode('gbk').split())
    del weightword[:]
    for line in keyword:
        weightword.append(1)
    del phoneListFirst[:]
    phoneListFirst.extend(checkPhone.checkPhone(brand,price,size,isuse['fashion'],isuse['thin'],isuse['battery'],isuse['bigScreen'],isuse['clrScreen'],isuse['photo'],isuse['self_photo'],isuse['easy_taken'],isuse['play'],isuse['bussiness']))
    phoneListSecond = DicRank.rank(postingList,postingListDis,indexDict,indexDictDis,keyword,weightword,phoneListFirst,d_score)
    phoneDetail = []
    for line in phoneListSecond:
        phoneDetail.append({'id':line,'brand':d_brand[line].decode('gbk'),'price':d_price[line].decode('gbk'),'score':d_score[line],'contin':d_contin[line],'scrnEfc':d_scrnEfc[line],'photoEfc':d_photoEfc[line],'reaction':d_reaction[line],'perfm':d_perfm[line],'xinjia':d_xinjia[line],'time':d_time[line].decode('gbk'),'scrnSize':d_scrnSize[line].decode('gbk'),'fenbian':d_fenbian[line].decode('gbk'),'cpu':d_cpu[line].decode('gbk'),'battery':d_battery[line].decode('gbk'),'quality':d_quality[line].decode('gbk'),'front':d_front[line].decode('gbk'),'back':d_back[line].decode('gbk'),'size':d_size[line].decode('gbk'),'url':d_url[line]})
    return render_template('HTMLmodel.html',phoneList = phoneDetail)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    delete_phone_id = request.form['id']
    diswords,disvalues = findDisWords(delete_phone_id)
    keyword.extend(diswords)
    weightword.extend(disvalues)
    phoneListFirst.remove(int(delete_phone_id))
    phoneListSecond = DicRank.rank(postingList,postingListDis,indexDict,indexDictDis,keyword,weightword,phoneListFirst,d_score)
    phoneDetail = []
    for line in phoneListSecond:
        phoneDetail.append({'id':line,'brand':d_brand[line].decode('gbk'),'price':d_price[line].decode('gbk'),'score':d_score[line],'contin':d_contin[line],'scrnEfc':d_scrnEfc[line],'photoEfc':d_photoEfc[line],'reaction':d_reaction[line],'perfm':d_perfm[line],'xinjia':d_xinjia[line],'time':d_time[line].decode('gbk'),'scrnSize':d_scrnSize[line].decode('gbk'),'fenbian':d_fenbian[line].decode('gbk'),'cpu':d_cpu[line].decode('gbk'),'battery':d_battery[line].decode('gbk'),'quality':d_quality[line].decode('gbk'),'front':d_front[line].decode('gbk'),'back':d_back[line].decode('gbk'),'size':d_size[line].decode('gbk'),'url':d_url[line]})
    return render_template('HTMLmodel.html',phoneList = phoneDetail)

@app.route('/bootstrap.css', methods=['GET', 'POST'])
def css():
    cssFile = open('bootstrap.css', 'rb')
    return cssFile.read()

@app.route('/banner.png', methods=['GET', 'POST'])
def banner():
    png = open('banner.png', 'rb')
    return png.read()

def findDisWords(phoneid):
    diswords = []
    disvalues = []
    K = 4
    Ka = 0.25
    if(float(d_contin[int(phoneid)])<4):
        diswords.append('电池'.decode('utf-8').encode('gbk'))
        diswords.append('续航'.decode('utf-8').encode('gbk'))
        disvalues.append(Ka*(K-float(d_contin[int(phoneid)])))
        disvalues.append(Ka*(K-float(d_contin[int(phoneid)])))
    if(float(d_scrnEfc[int(phoneid)])<4):
        diswords.append('屏幕'.decode('utf-8').encode('gbk'))
        disvalues.append(Ka*(K-float(d_scrnEfc[int(phoneid)])))
    if(float(d_photoEfc[int(phoneid)])<4):
        diswords.append('拍照'.decode('utf-8').encode('gbk'))
        disvalues.append(Ka*(K-float(d_photoEfc[int(phoneid)])))
    if(float(d_reaction[int(phoneid)])<4):
        diswords.append('影音'.decode('utf-8').encode('gbk'))
        diswords.append('娱乐'.decode('utf-8').encode('gbk'))
        disvalues.append(Ka*(K-float(d_reaction[int(phoneid)])))
        disvalues.append(Ka*(K-float(d_reaction[int(phoneid)])))
    if(float(d_perfm[int(phoneid)])<4):
        diswords.append('外观'.decode('utf-8').encode('gbk'))
        diswords.append('设计'.decode('utf-8').encode('gbk'))
        disvalues.append(Ka*(K-float(d_perfm[int(phoneid)])))
        disvalues.append(Ka*(K-float(d_perfm[int(phoneid)])))
    if(float(d_xinjia[int(phoneid)])<4):
        diswords.append('性价比'.decode('utf-8').encode('gbk'))
        disvalues.append(Ka*(K-float(d_xinjia[int(phoneid)])))
    return diswords,disvalues

if __name__ == '__main__':
    phoneListFirst = []
    keyword = []
    weightword = []
    (postingList,postingListDis,indexDict,indexDictDis) = DicRank.buildList()
    d_brand,d_price,d_score,d_contin,d_scrnEfc,d_photoEfc,d_reaction,d_perfm,d_xinjia,d_time,d_scrnSize,d_fenbian,d_cpu,d_battery,d_quality,d_front,d_back,d_size,d_url = checkPhone.getPhoneMessage()
    app.run()