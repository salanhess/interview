#coding=utf-8
from string import maketrans

#page: http://www.pythonchallenge.com/pc/def/map.html
#k ->  M  O->Q  E > G
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print str.replace('k','m').replace('o','q').replace('e','g')

intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = maketrans(intab, outtab)

print str.translate(trantab)

#http://www.pythonchallenge.com/pc/def/map.html
print 'http://www.pythonchallenge.com/pc/def/'+ 'map'.translate(trantab) + '.html'