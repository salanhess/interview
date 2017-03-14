#coding=utf-8

#twit_fields = {'field':{'bid':'','uid':'','username':'','v_class':'',content,img,time,source,rt_num,cm_num,rt_uid,rt_username,rt_v_class,rt_content,rt_img,src_rt_num,src_cm_num,gender,rt_mid,location,rt_mid,mid,lat,lon,lbs_type,lbs_title,poiid,links,hashtags,ats,rt_links,rt_hashtags,rt_ats,v_url,rt_v_url

fieldsNames = ['bid','uid','username','v_class','content','img','time', \
                                        'source','rt_num','cm_num','rt_uid','rt_username','rt_v_class', \
                                        'rt_content','rt_img','src_rt_num','src_cm_num','gender','rt_mid',\
                                        'location','rt_mid','mid','lat','lon','lbs_type','lbs_title','poiid',\
                                        'links','hashtags','ats','rt_links','rt_hashtags','rt_ats','v_url','rt_v_url']

twit_fields = {}
#use with encoding=utf-8 open file
#use zip and dic convert to generate nvdic
fpath = r'twit.txt'
#fpath = r'twitter数据挖掘片段.txt'

'''11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。'''
def MaxUid(*uidGroup):
    Flag,Muid = 0,''
    for i in set(uidGroup):
        if Flag < uidGroup.count(i):
            Flag = uidGroup.count(i)
            Muid = i
    return(Muid,Flag)

Ltest = [1,2,1,1]
print(MaxUid(*Ltest))

def analysis_twit(fpath):
    with open(fpath,encoding='utf-8') as filecontent:
        Flag = 0
        for line in filecontent:
            fcontent = []
            for i in line.split(','):
                fcontent.append(i[1:-1])
            nvs = zip(fieldsNames,fcontent)
            nvdic = dict((name,val) for name,val in nvs)
            twit_fields[nvdic.get('bid')] = nvdic
            if Flag < 1:
                print("Sample twit_fields{uid,usrdic{}}: " + str(twit_fields))
                Flag+=1
            #break
    #How may users and user related names: user_dict = {uid1:name1,uid2:name2 ...}
    user_dict = {}
    for i in twit_fields.keys():
        #get uid, username in twit_fields dictionary
        user_dict[twit_fields[i]['uid']] = twit_fields[i]['username']
    #print(user_dict.keys(),user_dict.values())

    import time
    date_dict = {}
    FlagDate = 0
    DetailDate = []
    TimeFrequency = []
    FlagHour = 0
    DetailHour = 0
    L20121103 = []
    info_Original_source = []
    Flag_rt_v_url = 0
    Flag_573638104 = 0
    UidList = []
    UidContext = ''
    UidContextFlag = 0
    UidContext_ID = ''
    Uid_rt_v_url = []
    Uid_eleven = []
    Uid_v_url = []
    for i in twit_fields.keys():
        #{bid:(uid,date)} 由于字典是无序的，所以需要用元组来控制
        date_dict[twit_fields[i]['bid']] = (twit_fields[i]['username'],twit_fields[i]['time'])
        #print(twit_fields[i]['time'],time.strftime('%Y-%m',time.strptime(twit_fields[i]['time'],'%Y-%m-%d %X')))
        # 3.有多少个2012年11月发布的tweets，采用strptime来分解字符串成标准元组，然后用strftime来拼接
        if time.strftime('%Y-%m',time.strptime(twit_fields[i]['time'],'%Y-%m-%d %X')) == '2012-11':
            FlagDate+=1
        #4.有哪几天的数据？
        Ddate = time.strftime('%Y-%m-%d',time.strptime(twit_fields[i]['time'],'%Y-%m-%d %X'))
        if Ddate not in DetailDate:
            DetailDate.append(Ddate)
        #5.在哪个小时发布的数据最多？
        TimeFrequency.append(time.strftime('%H',time.strptime(twit_fields[i]['time'],'%Y-%m-%d %X')))
        '''7. 请按照时间顺序输出 2012-11-03 每个小时的发布tweets的频率（要求：输出为一个list [(1,20),(2,30)] 代表1点发了20个tweets，2点发了30个tweets） '''
        if time.strftime('%Y-%m-%d', time.strptime(twit_fields[i]['time'], '%Y-%m-%d %X')) == '2012-11-03':
            L20121103.append(time.strftime('%H', time.strptime(twit_fields[i]['time'], '%Y-%m-%d %X')))
        '''8. 统计该文本里，来源的相关信息和次数，比如（输出一个list。例如[('Twitter for Android',1),('TweetList!',1)]）'''
        info_Original_source.append(twit_fields[i]['source'])
        '''9. 计算转发URL中：以："https://twitter.com/umiushi_no_uta"开头的有几个。(要求，输出一个整数。)'''
        if "https://twitter.com/umiushi_no_uta" in twit_fields[i]['rt_v_url']:
            Flag_rt_v_url+=1
        '''10. UID为573638104的用户 发了多少个微博 （要求：输出一个整数）'''
        if '573638104' == twit_fields[i]['uid']:
            Flag_573638104+=1
        UidList.append(twit_fields[i]['uid'])
        '''12. 该文本里，谁发的微博内容长度最长 （要求：输出用户的uid，字符串格式。）'''
        if len(twit_fields[i]['content']) > UidContextFlag:
            UidContext = twit_fields[i]['content']
            UidContextFlag = len(twit_fields[i]['content'])
            UidContext_ID = twit_fields[i]['uid']
        '''13. 该文本里，谁转发的URL最多 '''
        if len(twit_fields[i]['rt_v_url']) > 0:
            Uid_rt_v_url.append(twit_fields[i]['uid'])
        if time.strftime('%H',time.strptime(twit_fields[i]['time'],'%Y-%m-%d %X')) == '11':
            Uid_eleven.append(twit_fields[i]['uid'])
        '''15. 该文本里，哪个用户的源微博URL次数最多。'''
        if len(twit_fields[i]['v_url']) > 0:
            Uid_v_url.append(twit_fields[i]['uid'])
    print("15. 该文本里，Uid 用户 %s 发的源微博URL次数最多,为 %d次" % (MaxUid(*Uid_v_url)[0], MaxUid(*Uid_v_url)[1]))
    print("14. 该文本里，11点钟Uid 用户 %s 发的微博次数最多,为 %d次"  % (MaxUid(*Uid_eleven)[0], MaxUid(*Uid_eleven)[1]))
    print("===13. 该文本里 Uid %s 用户转发的URL最多,为 %d次 ===" % (MaxUid(*Uid_rt_v_url)[0], MaxUid(*Uid_rt_v_url)[1]))
    print("12. 该文本里，%s 发的微博内容长度最长,有 %d 字符，内容是 %s" % (UidContext_ID,UidContextFlag,UidContext))
    '''11. 定义一个函数，该函数可放入任意多的用户uid参数（如果不存在则返回null），函数返回发微薄数最多的用户uid。'''
    print("====Uid %s 用户发布了 %s 条微博，成为冠军===" %  (MaxUid(*UidList)[0],MaxUid(*UidList)[1]))
    print("10.UID为573638104的用户发了 %d 个微博 " % Flag_573638104)
    print("9.转发URL中：以：\"https://twitter.com/umiushi_no_uta\"开头的有 %d个" % Flag_rt_v_url)
    #8.Iterater according set(To remove duplicate element,and then count use list internal func)
    info_source = []
    for i in set(info_Original_source):
        info_source.append((i,info_Original_source.count(i)))
    print("======8.信息来源以及次数=====" + str(sorted(info_source)))
    #7. Get draft list and the format according requirement
    L20121103_detail = []
    for i in set(L20121103):
        L20121103_detail.append((i,L20121103.count(i)))
    print("======7.2012-11-03 每个小时的发布tweets的频率======" + str(sorted(L20121103_detail)))
    #6.该文本里，输出在每一天发表tweets最多的用户,{ date1:[user1..userN],date2:[user1.. userN] }
    #First convert to string EveryDaydic[(date1:user1),(date1:user2).. (dateN:userN)]
    EveryDaydic = []
    for i in date_dict.keys():
        Ddate = time.strftime('%Y-%m-%d', time.strptime(date_dict[i][1], '%Y-%m-%d %X'))
        EveryDaydic.append((Ddate,date_dict[i][0]))
    #Then double loop in this List according date,then save the largest user with Bestdict
    FlagBestEveryday = 0
    FlagBestUserEveryday = ''
    Bestdict = {}
    for eachday in DetailDate:
        for i in EveryDaydic:
            if eachday == i[0]:
                if FlagBestEveryday < EveryDaydic.count(i):
                    FlagBestEveryday = EveryDaydic.count(i)
                    FlagBestUserEveryday = i[1]
                    Bestdict[eachday]=(FlagBestUserEveryday,FlagBestEveryday)
    #Output 6
    print("========每一天发表tweets最多的用户=====: " + str(Bestdict))
    #print(TimeFrequency)
    for i in TimeFrequency:
        if TimeFrequency.count(i) > FlagHour:
            FlagHour = TimeFrequency.count(i)
            DetailHour = i
    print("在%s点，发布的数据最多with %s times" % (DetailHour,FlagHour))
    print("Contain '2012-11 tweets: %s,User dict is %s" % (FlagDate,date_dict))
    print(DetailDate)


    #striptime: strip time string according format; strftime: format time tuple according required format.
    # t = "2012-11-02 12:35:37"
    # new_timeFormat = time.strftime('%Y-%m',time.strptime(t,'%Y-%m-%d %X'))
    # print(new_timeFormat)

analysis_twit(fpath)
