#coding=utf-8

#page= http://www.pythonchallenge.com/pc/def/ocr.html
#Best solution refer to http://www.pythonchallenge.com/pcc/def/equality.html

#str = r"%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{* \
#@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&"

def check_CharFrequence(str):
    decode = []
    for i in str:
        if str.count(i) < 5:
            decode.append(i)
    print ''.join(decode)
    #print sorted(char_freq.items(),key = lambda x: (x[1]))   #    aeilquty

with open('C2_info.txt') as f:
    #My method: it's very very not good, because of N^N complex
    #check_CharFrequence(f.read())
    #print f.read()

    #This method is good, because just translate as C1
    mess = f.read()
    print mess.translate(None, '%$()[]{}+_@^!*&#\n')

