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
with open(r'twit.txt',encoding='utf-8') as filecontent:
    for line in filecontent:
        fcontent = []
        for i in line.split(','):
            fcontent.append(i[1:-1])
        nvs = zip(fieldsNames,fcontent)
        nvdic = dict((name,val) for name,val in nvs)
        twit_fields[nvdic.get('uid')] = nvdic
        print(twit_fields)
        break
