#coding=utf-8
import re
#page= http://www.pythonchallenge.com/pc/def/equality.html
#Previous std answer: http://www.pythonchallenge.com/pcc/def/equality.html
#Current page is http://www.pythonchallenge.com/pcc/def/linkedlist.php

sampleStr='kAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbT \
MUKLECKdCthezSYBpIElRnZugFAxDRtQPpyeCBgBfaRVvvguRXLvkAdLOeCKxsDUvBBCwdpMMWmuELeG \
ENihrpCLhujoBqPRDPvfzcwadMMMbkmkzCCzoTPfbRlzBqMblmxTxNniNoCufprWXxgHZpldkoLCrHJq \
vYuyJFCZtqXLhWiYzOXeglkzhVJIWmeUySGuFVmLTCyMshQtvZpPwuIbOHNoBauwvuJYCmqznOBgByPw'

'''Hint: One small letter, surrounded by EXACTLY three big bodyguards on each of its sides. '''
#My method is NOT correct
#pattern = re.compile('[A-Z]{3}([a-z])[A-Z]{3}',re.S)

#Following is CORRECT
pattern = re.compile('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
#print pattern.findall(sampleStr)


with open('C3_info.txt') as f:
    codeList = pattern.findall(f.read())
    print ''.join(codeList)

