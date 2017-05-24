#coding='utf-8'

import threading
import time
import random

#Target: multi-thread and random choice



def save_img(img_url):
    print u'Downloading http://'+ img_url + str(time.time())

#Use multi-thread to download
def start_save_img(imgurl_list):
    for i in imgurl_list:
        print threading.currentThread()
        th = threading.Thread(target=save_img,args=(i,))  # Don't forget , in i !!
        th.start()

def main():
    imgurl_list = ["a", "b", "c", "d"]
    start_save_img(imgurl_list)
    numList = [i for i in range(100)]
    delList = []
    print "\n"
    for i in range(10):
        thisTime = random.choice(numList)
        delList.append(thisTime)
        print "Index %s: This time choice is %s" % (i+1,thisTime)

if __name__ == '__main__':
    main()