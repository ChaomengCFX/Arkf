#此代码经过混淆，要源码请加qq
VERSION ='v2.2.1.8'#line:1
PULISH_TIME ='2021-11-07 16-37-00'#line:2
import time as O0000O0000Q0000 #line:4
import os as O00QQ0OO00O0 #line:5
Q00000QOOOOO00O =O0000O0000Q0000 .strftime ('%Y-%m-%d %H-%M-%S')#line:6
if O00QQ0OO00O0 .name =='nt':#line:7
    from colorama import init #line:8
    init (autoreset =True )#line:9
def O00OOO00000O00OO00000O (*OOOOOOOO0OO0O0OO0 ,conf =[(1 ,36 ,48 )]):#line:11
    print (''.join (['\033[%s;%s;%sm%s\033[0m'%(conf [OO0OO0000O00000OO if OO0OO0000O00000OO <=len (conf )-1 else len (conf )-1 ][0 ],conf [OO0OO0000O00000OO if OO0OO0000O00000OO <=len (conf )-1 else len (conf )-1 ][1 ],conf [OO0OO0000O00000OO if OO0OO0000O00000OO <=len (conf )-1 else len (conf )-1 ][2 ],OOOOOOOO0OO0O0OO0 [OO0OO0000O00000OO ])for OO0OO0000O00000OO in range (len (OOOOOOOO0OO0O0OO0 ))]))#line:12
OO00000OOQ000O ='╔══════════════════════════════════════╗\n'+'║  程序开始时间: %s%s║\n'%(Q00000QOOOOO00O ,((60 if O00QQ0OO00O0 .name =='nt'else 22 )-len (Q00000QOOOOO00O ))*' ')+'╠══════════════════════════════════════╣\n'+'║  程序版本: %s%s║\n'%(VERSION ,((64 if O00QQ0OO00O0 .name =='nt'else 26 )-len (VERSION ))*' ')+'╠══════════════════════════════════════╣\n'+'║  程序修改时间: %s%s║\n'%(PULISH_TIME ,((60 if O00QQ0OO00O0 .name =='nt'else 22 )-len (PULISH_TIME ))*' ')+'╚══════════════════════════════════════╝'#line:14
O00OOO00000O00OO00000O (OO00000OOQ000O ,conf =[(1 ,32 ,48 )])#line:15
import mitmproxy .http as mp #line:17
import re as O00000QQQ00 #line:18
import json as OQ00000000OO0QO #line:19
p =O00QQ0OO00O0 .getcwd ().replace ('\\','/')+'/'#line:21
if not O00QQ0OO00O0 .path .exists (p +'ark_history'):#line:22
    O00QQ0OO00O0 .makedirs (p +'ark_history')#line:23
his =p +'ark_history/'+Q00000QOOOOO00O #line:24
with open (his ,'w',encoding ='utf-8')as f :#line:25
    f .write (OO00000OOQ000O +'\n\n')#line:26
    f .close ()#line:27
try :#line:28
    f =open (p +'ark_data.json','r+',encoding ='utf-8')#line:29
    data =f .read ()#line:30
except Exception as e :#line:31
    print (e )#line:32
    f =open (p +'ark_data.json','w',encoding ='utf-8')#line:33
    data ='{}'#line:34
try :#line:35
    data =OQ00000000OO0QO .loads (data )#line:36
    O00OOOQ0000O0000O00OO0 =OQ00000000OO0QO .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False )#line:37
    f .seek (0 )#line:38
    f .truncate ()#line:39
    f .write (O00OOOQ0000O0000O00OO0 )#line:40
    f .close ()#line:41
except Exception as e :#line:42
    O00OOO00000O00OO00000O ('加载ark_data.json时出错:\r\n',e ,conf =[(1 ,33 ,48 ),(1 ,31 ,48 )])#line:43
    data ={}#line:44
    O00OOOQ0000O0000O00OO0 ='{}（加载出错，已将其作为空处理）'#line:45
O00OOO00000O00OO00000O ('data文件内容:\r\n',O00OOOQ0000O0000O00OO0 ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:46
del f #line:47
del O00OOOQ0000O0000O00OO0 #line:48
def O00OOO00000OO00O00OO0 ():#line:50
    return True if O0000O0000Q0000 .localtime ().tm_hour ==20 else False #line:51
class O00OOO00000O00OO0O0 :#line:53
    heartbeat ='http://line.*?realO0000O0000Q0000.*?api.biligame.net/app/v2/time/heartbeat'#line:54
    login_1 ='https://p.biligame.com/api/external/user.token.oauth.login/v3'#line:55
    login_2 ='https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/login/v3'#line:56
    login_3 ='https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/user.token.oauth.login/v3'#line:57
    login_4 ='https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/token.exchange/v3'#line:58
    get_token ='https://as.hypergryph.com/u8/user/v1/getToken'#line:59
    account_login ='https://.*?hypergryph.com/account/login'#line:60
    remote_config ='https://ak.*?conf.hypergryph.com/config/prod/.*?/remote_config'#line:61
    hyper ='https://.*?hypergryph.com'#line:62
    time_conf ='https://line.*?realO0000O0000Q0000.*?api.biligame.net/app/time/conf'#line:63
    gf_auth ='https://as.hypergryph.com/user/auth'#line:64
    gf_login ='https://as.hypergryph.com/user/login'#line:65
    ping ='https://.*?hypergryph.com/online/v1/ping'#line:66
    login_out ='https://.*?hypergryph.com/online/v1/loginout'#line:67
    hyper_host ='hypergryph'#line:68
    bili_host ='biligame'#line:69
    account_sync ='https://ak-gs-b.hypergryph.com/account/syncData'#line:70
    def umatch (OO000O0OOO0OOOOO0 ,*OO0O000O0OOOOO000 ):#line:72
        return False in (O00000QQQ00 .match (O00OO000000O0OOO0 ,OO000O0OOO0OOOOO0 )==None for O00OO000000O0OOO0 in OO0O000O0OOOOO000 )or True in (O00OOO00OO00OO0O0 in OO000O0OOO0OOOOO0 for O00OOO00OO00OO0O0 in OO0O000O0OOOOO000 )#line:73
class O00OOO00000OO000OO0 :#line:75
    def response (O00O0OO00000000OO ,O00OO0O00000000OO :mp .HTTPFlow ):#line:76
        if not O00OOO00000O00OO0O0 .umatch (O00OO0O00000000OO .request .url ,O00OOO00000O00OO0O0 .hyper_host ,O00OOO00000O00OO0O0 .bili_host ):#line:77
            return #line:78
        O0O000O0OO0O00O0O ='\n\n\n=================='+O0000O0000Q0000 .strftime ('%Y-%m-%d %H:%M:%S')+'===============\n'#line:79
        O0O000O0OO0O00O0O +='请求url: '+O00OO0O00000000OO .request .url +'\n'#line:80
        O0O000O0OO0O00O0O +='请求头'+str (O00OO0O00000000OO .request .headers )+'\n'#line:81
        try :#line:82
            O0O000O0OO0O00O0O +=('请求体: '+O00OO0O00000000OO .request .get_text ()if O00OO0O00000000OO .request .get_text ()!=None else '')+'\n'#line:83
        except :#line:84
            O0O000O0OO0O00O0O +='请求体: '+'（decode失败或者为空）'#line:85
        O0O000O0OO0O00O0O +='状态码: '+str (O00OO0O00000000OO .response .status_code )+'\n'#line:86
        O0O000O0OO0O00O0O +='返回头'+str (O00OO0O00000000OO .response .headers )+'\n'#line:87
        try :#line:88
            O0O000O0OO0O00O0O +='返回体: '+O00OO0O00000000OO .response .text if O00OO0O00000000OO .response .text !=None else ''#line:89
        except :#line:90
            O0O000O0OO0O00O0O +='返回体: '+'（decode失败或者为空）'#line:91
        global his #line:92
        with open (his ,'a+',encoding ='utf-8')as O0OO0OO000O0O0OO0 :#line:93
            O0OO0OO000O0O0OO0 .write (O0O000O0OO0O00O0O )#line:94
            O0OO0OO000O0O0OO0 .close ()#line:95
class O00OOO00000O00OO0000O0O :#line:97
    def request (O0OO00OO0OOO0O0O0 ,OO0OO00OOOO0O0O0O :mp .HTTPFlow ):#line:98
        O0O0O0OOO00OO000O =OO0OO00OOOO0O0O0O .request .url #line:99
        if O00OOO00000O00OO0O0 .umatch (O0O0O0OOO00OO000O ,O00OOO00000O00OO0O0 .account_login )and not O00OOO00000OO00O00OO0 ():#line:100
            O00OOO00000O00OO00000O ('当前为时间段外')#line:101
            OO0OOO0OOO0000O0O =[OO0OOO00O0O00O0O0 for OO0OOO00O0O00O0O0 in data if data [OO0OOO00O0O00O0O0 ]['uid']==int (OQ00000000OO0QO .loads (OO0OO00OOOO0O0O0O .request .get_content ())['uid'])]#line:102
            O000OOO0O00O0OOOO =OO0OOO0OOO0000O0O [0 ]if len (OO0OOO0OOO0000O0O )>=1 else None #line:103
            del OO0OOO0OOO0000O0O #line:104
            if O000OOO0O00O0OOOO :#line:105
                OO0OO00OOOO0O0O0O .request .host ='none.com'#line:106
                O000O0OO00OOOOO00 =bytes (OQ00000000OO0QO .dumps ({'result':0 ,'uid':str (data [O000OOO0O00O0OOOO ]['uid']),'secret':data [O000OOO0O00O0OOOO ]['secret']if 'secret'in data [O000OOO0O00O0OOOO ]else None ,'serviceLicenseVersion':0 }),encoding ='utf-8')#line:112
                OO0OO00OOOO0O0O0O .response =mp .Response .make (status_code =200 ,content =O000O0OO00OOOOO00 ,headers ={'Cache-Control':'no-cache','Content-Length':bytes (len (O000O0OO00OOOOO00 )),'Content-Type':'application/json; charset=utf-8','Date':'Sat, 06 Nov 2021 13:41:52 GMT','seqnum':bytes (str (data [O000OOO0O00O0OOOO ]['seqnum']),encoding ='utf-8')},)#line:123
                del O000O0OO00OOOOO00 #line:124
                O00OOO00000O00OO00000O ('已进行返回头和返回体修改:\r\n',str (OO0OO00OOOO0O0O0O .response .headers )+'\r\n'+OO0OO00OOOO0O0O0O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:125
            else :#line:126
                O00OOO00000O00OO00000O ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:127
        elif O00OOO00000O00OO0O0 .umatch (O0O0O0OOO00OO000O ,O00OOO00000O00OO0O0 .login_out )and not O00OOO00000OO00O00OO0 ():#line:128
            OO0OO00OOOO0O0O0O .request .host ='none.com'#line:129
            OO0OO00OOOO0O0O0O .response =mp .Response .make (status_code =200 ,content =b'{"result":0}',headers ={'Cache-Control':'no-cache','Content-Length':'12','Content-Type':'application/json; charset=utf-8','Date':'Sat, 06 Nov 2021 13:41:52 GMT','Vary':'origin'},)#line:140
    def response (OO0OO00OO0OO0OOOO ,OO0OO0O000O0000OO :mp .HTTPFlow ):#line:142
        global data #line:143
        OOOOOOOOO0O00O00O =OO0OO0O000O0000OO .request .url #line:144
        OO0O00O0O000000OO =False #line:145
        if O00OOO00000O00OO0O0 .umatch (OOOOOOOOO0O00O00O ,O00OOO00000O00OO0O0 .remote_config ):#line:146
            OO0OO00OO0OOOO000 =OQ00000000OO0QO .loads (OO0OO0O000O0000OO .response .content )#line:147
            OO0OO00OO0OOOO000 ['enableBestHttp']=False #line:148
            OO0OO0O000O0000OO .response .set_text (OQ00000000OO0QO .dumps (OO0OO00OO0OOOO000 ))#line:149
            O00OOO00000O00OO00000O ('修改完remote_config')#line:150
        elif O00OOO00000O00OO0O0 .umatch (OOOOOOOOO0O00O00O ,O00OOO00000O00OO0O0 .time_conf ):#line:151
            OO0OO00OO0OOOO000 =OQ00000000OO0QO .loads (OO0OO0O000O0000OO .response .content )#line:152
            OO0OO00OO0OOOO000 ['recEnable']='false'#line:153
            OO0OO0O000O0000OO .response .set_text (OQ00000000OO0QO .dumps (OO0OO00OO0OOOO000 ))#line:154
            O00OOO00000O00OO00000O ('对time-config完成修改')#line:155
        elif O00OOO00000O00OO0O0 .umatch (OOOOOOOOO0O00O00O ,O00OOO00000O00OO0O0 .get_token ):#line:156
            O00OOO00000O00OO00000O ('getToken包内容:\r\n',OO0OO0O000O0000OO .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:157
            if OO0OO0O000O0000OO .response .status_code !=200 :#line:158
                O00OOO0O00O0000O0 =[O0OO0OOO0O0O00OO0 for O0OO0OOO0O0O00OO0 in data if data [O0OO0OOO0O0O00OO0 ]['login']['access_key']==OQ00000000OO0QO .loads (OQ00000000OO0QO .loads (OO0OO0O000O0000OO .request .get_content ())['extension'])['access_token']]#line:159
                O00O0O0O00O0O0O0O =O00OOO0O00O0000O0 [0 ]if len (O00OOO0O00O0000O0 )>=1 else None #line:160
                del O00OOO0O00O0000O0 #line:161
                if O00O0O0O00O0O0O0O :#line:162
                    OO0OO0O000O0000OO .response .status_code =200 #line:163
                    OO0OO00OO0OOOO000 ={'result':0 ,'error':'','uid':str (data [O00O0O0O00O0O0O0O ]['uid']),'channelUid':int (O00O0O0O00O0O0O0O ),'token':data [O00O0O0O00O0O0O0O ]['token'],'isGuest':0 ,'extension':'{\"nickName\":\"'+data [O00O0O0O00O0O0O0O ]['login']['uname']+'\"}'if OQ00000000OO0QO .loads (OO0OO0O000O0000OO .request .text )['channelId']=='2'else '{\"isGuest\":false}'}#line:172
                    OO0OO0O000O0000OO .response .set_text (OQ00000000OO0QO .dumps (OO0OO00OO0OOOO000 ))#line:173
                    O00OOO00000O00OO00000O ('密钥获取错误，已进行返回体修改:\r\n',OO0OO0O000O0000OO .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:174
                else :#line:175
                    O00OOO00000O00OO00000O ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:176
            else :#line:177
                OO0OO00OO0OOOO000 =OQ00000000OO0QO .loads (OO0OO0O000O0000OO .response .content )#line:178
                O00OOO0O00O0000O0 =[OOO000O00O00000O0 for OOO000O00O00000O0 in data if int (OOO000O00O00000O0 )==OO0OO00OO0OOOO000 ['channelUid']]#line:179
                O00O0O0O00O0O0O0O =O00OOO0O00O0000O0 [0 ]if len (O00OOO0O00O0000O0 )>=1 else None #line:180
                del O00OOO0O00O0000O0 #line:181
                OOO0OOO00OO0O0O00 =OQ00000000OO0QO .loads (OQ00000000OO0QO .loads (OO0OO0O000O0000OO .request .get_content ())['extension'])['access_token']#line:182
                if O00O0O0O00O0O0O0O :#line:183
                    data [O00O0O0O00O0O0O0O ]['login']['access_key']=OOO0OOO00OO0O0O00 #line:184
                    data [O00O0O0O00O0O0O0O ]['uid']=int (OO0OO00OO0OOOO000 ['uid'])#line:185
                    data [O00O0O0O00O0O0O0O ]['token']=OO0OO00OO0OOOO000 ['token']#line:186
                    OO0O00O0O000000OO =True #line:187
                    O00OOO00000O00OO00000O ('正常获得token')#line:188
                elif OQ00000000OO0QO .loads (OO0OO0O000O0000OO .request .text )['channelId']=='1':#line:189
                    O00O00000O00OOOO0 =str (OO0OO00OO0OOOO000 ['channelUid'])#line:190
                    if O00O00000O00OOOO0 in data :#line:191
                        data [O00O00000O00OOOO0 ]['login']['access_key']=OOO0OOO00OO0O0O00 #line:192
                        data [O00O00000O00OOOO0 ]['uid']=int (OO0OO00OO0OOOO000 ['uid'])#line:193
                        data [O00O00000O00OOOO0 ]['token']=OO0OO00OO0OOOO000 ['token']#line:194
                        OO0O00O0O000000OO =True #line:195
                        O00OOO00000O00OO00000O ('检测到官服账号成功登陆，已同步账号信息')#line:196
                    else :#line:197
                        data [str (OO0OO00OO0OOOO000 ['channelUid'])]={'login':{'access_key':OOO0OOO00OO0O0O00 ,},'uid':int (OO0OO00OO0OOOO000 ['uid']),'seqnum':'1','token':OO0OO00OO0OOOO000 ['token'],}#line:205
                        OO0O00O0O000000OO =True #line:206
                        O00OOO00000O00OO00000O ('检测到官服新账号成功登陆，已建立账号信息')#line:207
                    del O00O00000O00OOOO0 #line:208
                else :#line:209
                    O00OOO00000O00OO00000O ('正常获得token，但未获得账号信息，','请在法定时间内重新登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:210
                del OOO0OOO00OO0O0O00 #line:211
        elif O00OOO00000O00OO0O0 .umatch (OOOOOOOOO0O00O00O ,O00OOO00000O00OO0O0 .account_login )and O00OOO00000OO00O00OO0 ():#line:212
            O00OOO00000O00OO00000O ('account/login包内容:\r\n',OO0OO0O000O0000OO .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:213
            OO0OO00OO0OOOO000 =OQ00000000OO0QO .loads (OO0OO0O000O0000OO .response .content )#line:214
            O00OOO0O00O0000O0 =[O000000000O0O0O0O for O000000000O0O0O0O in data if data [O000000000O0O0O0O ]['uid']==int (OQ00000000OO0QO .loads (OO0OO0O000O0000OO .request .get_content ())['uid'])]#line:215
            O00O0O0O00O0O0O0O =O00OOO0O00O0000O0 [0 ]if len (O00OOO0O00O0000O0 )>=1 else None #line:216
            del O00OOO0O00O0000O0 #line:217
            if O00O0O0O00O0O0O0O :#line:218
                if OO0OO00OO0OOOO000 ['result']==0 :#line:219
                    data [O00O0O0O00O0O0O0O ]['secret']=OO0OO00OO0OOOO000 ['secret']#line:220
                    OO0O00O0O000000OO =True #line:221
                    O00OOO00000O00OO00000O ('正常获得secret，已保存')#line:222
                else :#line:223
                    O00OOO00000O00OO00000O ('法定时间段内登陆失败，原因未知')#line:224
            else :#line:225
                O00OOO00000O00OO00000O ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:226
        elif O00OOO00000O00OO0O0 .umatch (OOOOOOOOO0O00O00O ,O00OOO00000O00OO0O0 .account_sync ):#line:227
            OO0OO00OO0OOOO000 =OQ00000000OO0QO .loads (OO0OO0O000O0000OO .response .content )#line:228
            if (OO0OO00OO0OOOO000 ['msg']=='stale sequence number'if 'msg'in OO0OO00OO0OOOO000 else False ):#line:229
                try :#line:230
                    O00OOO0O00O0000O0 =[O0O00O0O000O0O0OO for O0O00O0O000O0O0OO in data if data [O0O00O0O000O0O0OO ]['uid']==int (OO0OO0O000O0000OO .request .headers ['uid'])]#line:231
                    O00O0O0O00O0O0O0O =O00OOO0O00O0000O0 [0 ]if len (O00OOO0O00O0000O0 )>=1 else None #line:232
                    del O00OOO0O00O0000O0 #line:233
                    if O00O0O0O00O0O0O0O :#line:234
                        data [O00O0O0O00O0O0O0O ]['seqnum']=str (int (data [O00O0O0O00O0O0O0O ]['seqnum'])+2000 )#line:235
                        OO0O00O0O000000OO =True #line:236
                        O00OOO00000O00OO00000O ('同步账号信息异常，已经尝试增加seqnum',conf =[(1 ,31 ,48 )])#line:237
                    else :#line:238
                        O00OOO00000O00OO00000O ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:239
                except Exception as OOOO0O0OOO0000O00 :#line:240
                    O00OOO00000O00OO00000O ('同步账号信息异常，尝试增加seqnum失败：',OOOO0O0OOO0000O00 ,conf =[(1 ,31 ,48 )])#line:241
            elif (OO0OO00OO0OOOO000 ['message']=='invalid version'if 'message'in OO0OO00OO0OOOO000 else False ):#line:242
                O00OOO00000O00OO00000O ('同步数据时服务器返回invalid version，官服未解决，若是b服可能是上一次登陆信息未保存或者闪断更新导致',conf =[(1 ,31 ,48 )])#line:243
            elif 'msg'in OO0OO00OO0OOOO000 or 'message'in OO0OO00OO0OOOO000 :#line:244
                O00OOO00000O00OO00000O ('未知错误',conf =[(1 ,31 ,48 )])#line:245
            else :#line:246
                O00OOO00000O00OO00000O ('同步账号信息正常')#line:247
        elif O00OOO00000O00OO0O0 .umatch (OOOOOOOOO0O00O00O ,O00OOO00000O00OO0O0 .hyper ):#line:248
            O00OOO00000O00OO00000O ('[%s]游戏数据包url: '%O0000O0000Q0000 .strftime ('%H:%M:%S'),OOOOOOOOO0O00O00O ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:249
            if not 'seqnum'in OO0OO0O000O0000OO .response .headers :#line:250
                return #line:251
            O00OOO0O00O0000O0 =[OOO0OO00OO000OOO0 for OOO0OO00OO000OOO0 in data if data [OOO0OO00OO000OOO0 ]['uid']==int (OO0OO0O000O0000OO .request .headers ['uid'])]#line:252
            O00O0O0O00O0O0O0O =O00OOO0O00O0000O0 [0 ]if len (O00OOO0O00O0000O0 )>=1 else None #line:253
            del O00OOO0O00O0000O0 #line:254
            if O00O0O0O00O0O0O0O :#line:255
                if (OO0OO0O000O0000OO .response .headers ['seqnum']!='null'):#line:256
                    data [O00O0O0O00O0O0O0O ]['seqnum']=OO0OO0O000O0000OO .response .headers ['seqnum']#line:257
                    OO0O00O0O000000OO =True #line:258
                    O00OOO00000O00OO00000O ('已保存编号: '+str (OO0OO0O000O0000OO .response .headers ['seqnum']))#line:259
                else :#line:260
                    O00OOO00000O00OO00000O ('未检测到编号，可能是上一次登陆信息未保存或者闪断更新导致',conf =[(1 ,31 ,48 )])#line:261
            else :#line:262
                O00OOO00000O00OO00000O ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:263
        if OO0O00O0O000000OO :#line:264
            with open (p +'ark_data.json','w',encoding ='utf-8')as O00OO000O0O0O0OOO :#line:265
                O00OO000O0O0O0OOO .write (OQ00000000OO0QO .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False ))#line:266
                O00OO000O0O0O0OOO .close ()#line:267
class O00OOO00000OOO00000OO0 :#line:269
    ""#line:285
    def response (O00OO00000O0OO0OO ,O000OOOO00O00000O :mp .HTTPFlow ):#line:286
        global data #line:287
        OO0000OO00O00O00O =O000OOOO00O00000O .request .url #line:288
        OOO00OOO00OOO0O00 =False #line:289
        if O00OOO00000O00OO0O0 .umatch (OO0000OO00O00O00O ,O00OOO00000O00OO0O0 .heartbeat ):#line:290
            O00O0000OO00OOO0O =OQ00000000OO0QO .loads (O000OOOO00O00000O .response .content )#line:291
            O00OOO00000O00OO00000O ('heartbeat包内容:\r\n',O000OOOO00O00000O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:292
            if (O00O0000OO00OOO0O ['data']['user_info']['adult_status']==0 ):#line:293
                O00O0000OO00OOO0O ['data']['trigger_status']=0 #line:294
                O00O0000OO00OOO0O ['data']['event_list']=[]#line:295
                O000OOOO00O00000O .response .set_text (OQ00000000OO0QO .dumps (O00O0000OO00OOO0O ))#line:296
                O00OOO00000O00OO00000O ('检测到未成年人，已进行返回体修改:\r\n',O000OOOO00O00000O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:297
            else :#line:298
                O00OOO00000O00OO00000O ('检测到已经成年，未进行修改')#line:299
        elif O00OOO00000O00OO0O0 .umatch (OO0000OO00O00O00O ,O00OOO00000O00OO0O0 .login_1 ,O00OOO00000O00OO0O0 .login_2 ,O00OOO00000O00OO0O0 .login_3 ,O00OOO00000O00OO0O0 .login_4 ):#line:300
            O00O0000OO00OOO0O =OQ00000000OO0QO .loads (O000OOOO00O00000O .response .content )#line:301
            O00OOO00000O00OO00000O ('向BililiGame SDK服务器登陆包内容:\r\n',O000OOOO00O00000O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:302
            OOOOOO0OOO0OOO0O0 =[O0O00OOO0OO0O0OOO for O0O00OOO0OO0O0OOO in data if data [O0O00OOO0OO0O0OOO ]['login']['access_key']==O000OOOO00O00000O .request .urlencoded_form ['access_key']or (str (data [O0O00OOO0OO0O0OOO ]['login']['uuid'])==O000OOOO00O00000O .request .urlencoded_form ['user_id']if 'user_id'in O000OOOO00O00000O .request .urlencoded_form else False )]#line:303
            OOO0O00OOO0OOO0OO =OOOOOO0OOO0OOO0O0 [0 ]if len (OOOOOO0OOO0OOO0O0 )>=1 else None #line:304
            del OOOOOO0OOO0OOO0O0 #line:305
            if O00O0000OO00OOO0O ['code']!=0 :#line:306
                if OOO0O00OOO0OOO0OO :#line:307
                    O00O0000OO00OOO0O ['code']=0 #line:308
                    O00000QQQ00 .pop ('message')#line:309
                    O00O0000OO00OOO0O ['access_key']=data [OOO0O00OOO0OOO0OO ]['login']['access_key']#line:310
                    O00O0000OO00OOO0O ['uid']=int (OOO0O00OOO0OOO0OO )#line:311
                    O00O0000OO00OOO0O ['face']=data [OOO0O00OOO0OOO0OO ]['login']['face']#line:312
                    O00O0000OO00OOO0O ['s_face']=data [OOO0O00OOO0OOO0OO ]['login']['s_face']#line:313
                    O00O0000OO00OOO0O ['uname']=data [OOO0O00OOO0OOO0OO ]['login']['uname']#line:314
                    O00O0000OO00OOO0O ['expires']=int (O0000O0000Q0000 .time ()+3000000 )#line:315
                    O000OOOO00O00000O .response .set_text (OQ00000000OO0QO .dumps (O00O0000OO00OOO0O ))#line:316
                    O00OOO00000O00OO00000O ('检测到登陆code问题，已进行返回体修改:\r\n',O000OOOO00O00000O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:317
                    if not 'uuid'in data [str (O00O0000OO00OOO0O ['uid'])]['login']or data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']==O00O0000OO00OOO0O ['uid']or data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']=='':#line:318
                        O00OOO00000O00OO00000O ('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：',conf =[(1 ,36 ,41 )])#line:319
                        data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']=str (input ())#line:320
                        OOO00OOO00OOO0O00 =True #line:321
                else :#line:322
                    O00OOO00000O00OO00000O ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:323
            else :#line:324
                if OOO0O00OOO0OOO0OO :#line:325
                    data [OOO0O00OOO0OOO0OO ]['login']['face']=O00O0000OO00OOO0O ['face']#line:326
                    data [OOO0O00OOO0OOO0OO ]['login']['s_face']=O00O0000OO00OOO0O ['s_face']#line:327
                    data [OOO0O00OOO0OOO0OO ]['login']['uname']=O00O0000OO00OOO0O ['uname']#line:328
                    OOO00OOO00OOO0O00 =True #line:329
                    O00OOO00000O00OO00000O ('检测到b服成功登陆，已同步账号信息')#line:330
                    if not 'uuid'in data [str (O00O0000OO00OOO0O ['uid'])]['login']or data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']==O00O0000OO00OOO0O ['uid']or data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']=='':#line:331
                        O00OOO00000O00OO00000O ('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：',conf =[(1 ,36 ,41 )])#line:332
                        data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']=str (input ())#line:333
                else :#line:334
                    data [str (O00O0000OO00OOO0O ['uid'])]={'login':{'access_key':O00O0000OO00OOO0O ['access_key'],'face':O00O0000OO00OOO0O ['face'],'s_face':O00O0000OO00OOO0O ['s_face'],'uname':O00O0000OO00OOO0O ['uname'],'uuid':''},'uid':None ,'seqnum':1 ,'token':None ,'secret':None }#line:347
                    OOO00OOO00OOO0O00 =True #line:348
                    if len (O000OOOO00O00000O .request .urlencoded_form ['uid'])>=1 :#line:349
                        data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']=O000OOOO00O00000O .request .urlencoded_form ['uid']#line:350
                        O00OOO00000O00OO00000O ('检测到新账号成功登陆，已建立账号信息')#line:351
                    elif not 'uuid'in data [str (O00O0000OO00OOO0O ['uid'])]['login']or data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']==O00O0000OO00OOO0O ['uid']or data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']=='':#line:352
                        O00OOO00000O00OO00000O ('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：',conf =[(1 ,36 ,41 )])#line:353
                        data [str (O00O0000OO00OOO0O ['uid'])]['login']['uuid']=str (input ())#line:354
        if OOO00OOO00OOO0O00 :#line:355
            with open (p +'ark_data.json','w',encoding ='utf-8')as OOOOOO00O0OOO0O0O :#line:356
                OOOOOO00O0OOO0O0O .write (OQ00000000OO0QO .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False ))#line:357
                OOOOOO00O0OOO0O0O .close ()#line:358
    '''
    def error(self, flow: mp.HTTPFlow):
        pass
    '''#line:362
class O00OOO00000000O00OOOOOOOO000 :#line:364
    def response (O000O00000000OO0O ,OO0O00OO0O0OO00O0 :mp .HTTPFlow ):#line:365
        OO00O0000O000000O =OO0O00OO0O0OO00O0 .request .url #line:366
        if O00OOO00000O00OO0O0 .umatch (OO00O0000O000000O ,O00OOO00000O00OO0O0 .gf_login ,O00OOO00000O00OO0O0 .gf_auth ):#line:367
            O00OO0OO0O000O0OO =OQ00000000OO0QO .loads (OO0O00OO0O0OO00O0 .response .content )#line:368
            O00OO0OO0O000O0OO ['isMinor']=False #line:369
            OO0O00OO0O0OO00O0 .response .set_text (OQ00000000OO0QO .dumps (O00OO0OO0O000O0OO ))#line:370
        elif O00OOO00000O00OO0O0 .umatch (OO00O0000O000000O ,O00OOO00000O00OO0O0 .ping ):#line:371
            O00OO0OO0O000O0OO ={'result':0 ,'message':'OK','interval':5400 ,'timeLeft':-1 ,'alertTime':600 }#line:378
            OO0O00OO0O0OO00O0 .response .set_text (OQ00000000OO0QO .dumps (O00OO0OO0O000O0OO ))#line:379
addons =[O00OOO00000OO000OO0 (),O00OOO00000O00OO0000O0O (),O00OOO00000OOO00000OO0 (),O00OOO00000000O00OOOOOOOO000 ()]#line:386
if __name__ =='__main__':#line:388
    from mitmproxy import options #line:389
    from mitmproxy .tools .dump import DumpMaster #line:390
    O00OOO00000O00OO00000O ('请输入数字设置抓包端口（尽量大于1000，必须小于等于65535）：')#line:391
    port =int (input ())#line:392
    opts =options .Options (listen_host ='127.0.0.1',listen_port =port )#line:393
    m =DumpMaster (options =opts )#line:394
    try :#line:395
        O00OOO00000O00OO00000O ('开始抓包，请确保wifi代理地址设置为127.0.0.1，端口为%d，如未下载证书可现在下载'%port )#line:396
        m .addons .add (*addons )#line:397
        m .run ()#line:398
    except :#line:399
        O00OOO00000O00OO00000O ('写入data文件内容:\r\n'+OQ00000000OO0QO .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False ),conf =[(1 ,33 ,48 )])#line:400
        m .shutdown ()
