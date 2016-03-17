x = 0
cf=open('commentAmount.txt','w')
for x in range(0,522):
    fp = open('phone/phone'+str(x)+'/score.txt','r').read()
    cf.write(fp+'\n')
    print fp
    print x
for x in range(522,605):
    cf.write('30\n')
    print(x)