#此代码经过混淆，要源码请加qq
VERSION ='v2.2.1.8'#line:1
PULISH_TIME ='2021-11-07 16-37-00'#line:2
import time ,os #line:4
stime =time .strftime ('%Y-%m-%d %H-%M-%S')#line:5
if os .name =='nt':#line:6
    from colorama import init #line:7
    init (autoreset =True )#line:8
def __f_o_______________g (*OOOOOO0OO0OOO000O ,conf =[(1 ,36 ,48 )]):#line:10
    print (''.join (['\033[%s;%s;%sm%s\033[0m'%(conf [O00O00OOO000O0000 if O00O00OOO000O0000 <=len (conf )-1 else len (conf )-1 ][0 ],conf [O00O00OOO000O0000 if O00O00OOO000O0000 <=len (conf )-1 else len (conf )-1 ][1 ],conf [O00O00OOO000O0000 if O00O00OOO000O0000 <=len (conf )-1 else len (conf )-1 ][2 ],OOOOOO0OO0OOO000O [O00O00OOO000O0000 ])for O00O00OOO000O0000 in range (len (OOOOOO0OO0OOO000O ))]))#line:11
title ='╔══════════════════════════════════════╗\n'+'║  程序开始时间: %s%s║\n'%(stime ,((60 if os .name =='nt'else 22 )-len (stime ))*' ')+'╠══════════════════════════════════════╣\n'+'║  程序版本: %s%s║\n'%(VERSION ,((64 if os .name =='nt'else 26 )-len (VERSION ))*' ')+'╠══════════════════════════════════════╣\n'+'║  程序修改时间: %s%s║\n'%(PULISH_TIME ,((60 if os .name =='nt'else 22 )-len (PULISH_TIME ))*' ')+'╚══════════════════════════════════════╝'#line:13
__f_o_______________g (title ,conf =[(1 ,32 ,48 )])#line:14
import mitmproxy .http as mp #line:16
import re ,json #line:17
p =os .getcwd ().replace ('\\','/')+'/'#line:19
if not os .path .exists (p +'ark_history'):#line:20
    os .makedirs (p +'ark_history')#line:21
his =p +'ark_history/'+stime #line:22
with open (his ,'w',encoding ='utf-8')as f :#line:23
    f .write (title +'\n\n')#line:24
    f .close ()#line:25
try :#line:26
    f =open (p +'ark_data.json','r+',encoding ='utf-8')#line:27
    data =f .read ()#line:28
except Exception as e :#line:29
    print (e )#line:30
    f =open (p +'ark_data.json','w',encoding ='utf-8')#line:31
    data ='{}'#line:32
try :#line:33
    data =json .loads (data )#line:34
    f__o_____g =json .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False )#line:35
    f .seek (0 )#line:36
    f .truncate ()#line:37
    f .write (f__o_____g )#line:38
    f .close ()#line:39
except Exception as e :#line:40
    __f_o_______________g ('加载ark_data.json时出错:\r\n',e ,conf =[(1 ,33 ,48 ),(1 ,31 ,48 )])#line:41
    data ={}#line:42
    f__o_____g ='{}（加载出错，已将其作为空处理）'#line:43
__f_o_______________g ('data文件内容:\r\n',f__o_____g ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:44
del f #line:45
del f__o_____g #line:46
def ___ ():#line:48
    return True if time .localtime ().tm_hour ==20 else False #line:49
class _ :#line:51
    heartbeat ='http://line.*?realtime.*?api.biligame.net/app/v2/time/heartbeat'#line:52
    login_1 ='https://p.biligame.com/api/external/user.token.oauth.login/v3'#line:53
    login_2 ='https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/login/v3'#line:54
    login_3 ='https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/user.token.oauth.login/v3'#line:55
    login_4 ='https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/token.exchange/v3'#line:56
    get_token ='https://as.hypergryph.com/u8/user/v1/getToken'#line:57
    account_login ='https://.*?hypergryph.com/account/login'#line:58
    remote_config ='https://ak.*?conf.hypergryph.com/config/prod/.*?/remote_config'#line:59
    hyper ='https://.*?hypergryph.com'#line:60
    time_conf ='https://line.*?realtime.*?api.biligame.net/app/time/conf'#line:61
    gf_auth ='https://as.hypergryph.com/user/auth'#line:62
    gf_login ='https://as.hypergryph.com/user/login'#line:63
    ping ='https://.*?hypergryph.com/online/v1/ping'#line:64
    login_out ='https://.*?hypergryph.com/online/v1/loginout'#line:65
    hyper_host ='hypergryph'#line:66
    bili_host ='biligame'#line:67
    account_sync ='https://ak-gs-b.hypergryph.com/account/syncData'#line:68
    def umatch (O0OOOOOOO0000OO00 ,*OO0OOOOOO00O0O000 ):#line:70
        return False in (re .match (OO00OOO0000OO00O0 ,O0OOOOOOO0000OO00 )==None for OO00OOO0000OO00O0 in OO0OOOOOO00O0O000 )or True in (O0OO00OO000OOO00O in O0OOOOOOO0000OO00 for O0OO00OO000OOO00O in OO0OOOOOO00O0O000 )#line:71
class _f____o__g____ :#line:73
    def response (O000OOOOO00000O0O ,OOO0O000000OO0OO0 :mp .HTTPFlow ):#line:74
        if not _ .umatch (OOO0O000000OO0OO0 .request .url ,_ .hyper_host ,_ .bili_host ):#line:75
            return #line:76
        OOO00OOO00O000OOO ='\n\n\n=================='+time .strftime ('%Y-%m-%d %H:%M:%S')+'===============\n'#line:77
        OOO00OOO00O000OOO +='请求url: '+OOO0O000000OO0OO0 .request .url +'\n'#line:78
        OOO00OOO00O000OOO +='请求头'+str (OOO0O000000OO0OO0 .request .headers )+'\n'#line:79
        try :#line:80
            OOO00OOO00O000OOO +=('请求体: '+OOO0O000000OO0OO0 .request .get_text ()if OOO0O000000OO0OO0 .request .get_text ()!=None else '')+'\n'#line:81
        except :#line:82
            OOO00OOO00O000OOO +='请求体: '+'（decode失败或者为空）'#line:83
        OOO00OOO00O000OOO +='状态码: '+str (OOO0O000000OO0OO0 .response .status_code )+'\n'#line:84
        OOO00OOO00O000OOO +='返回头'+str (OOO0O000000OO0OO0 .response .headers )+'\n'#line:85
        try :#line:86
            OOO00OOO00O000OOO +='返回体: '+OOO0O000000OO0OO0 .response .text if OOO0O000000OO0OO0 .response .text !=None else ''#line:87
        except :#line:88
            OOO00OOO00O000OOO +='返回体: '+'（decode失败或者为空）'#line:89
        global his #line:90
        with open (his ,'a+',encoding ='utf-8')as O0O00OO00OO0000OO :#line:91
            O0O00OO00OO0000OO .write (OOO00OOO00O000OOO )#line:92
            O0O00OO00OO0000OO .close ()#line:93
class _f___o_______g_ :#line:95
    def request (OO000O0OO0O000OO0 ,OO00O000OO0000000 :mp .HTTPFlow ):#line:96
        OO0O00OOO0O0O0O0O =OO00O000OO0000000 .request .url #line:97
        if _ .umatch (OO0O00OOO0O0O0O0O ,_ .account_login )and not ___ ():#line:98
            __f_o_______________g ('当前为时间段外')#line:99
            O0O0O00OOO0OO0OOO =[O0O00O00OO00OO0O0 for O0O00O00OO00OO0O0 in data if data [O0O00O00OO00OO0O0 ]['uid']==int (json .loads (OO00O000OO0000000 .request .get_content ())['uid'])]#line:100
            O0000OOOOOO0OOOOO =O0O0O00OOO0OO0OOO [0 ]if len (O0O0O00OOO0OO0OOO )>=1 else None #line:101
            del O0O0O00OOO0OO0OOO #line:102
            if O0000OOOOOO0OOOOO :#line:103
                OO00O000OO0000000 .request .host ='none.com'#line:104
                OOO0O0OOO000OOOO0 =bytes (json .dumps ({'result':0 ,'uid':str (data [O0000OOOOOO0OOOOO ]['uid']),'secret':data [O0000OOOOOO0OOOOO ]['secret']if 'secret'in data [O0000OOOOOO0OOOOO ]else None ,'serviceLicenseVersion':0 }),encoding ='utf-8')#line:110
                OO00O000OO0000000 .response =mp .Response .make (status_code =200 ,content =OOO0O0OOO000OOOO0 ,headers ={'Cache-Control':'no-cache','Content-Length':bytes (len (OOO0O0OOO000OOOO0 )),'Content-Type':'application/json; charset=utf-8','Date':'Sat, 06 Nov 2021 13:41:52 GMT','seqnum':bytes (str (data [O0000OOOOOO0OOOOO ]['seqnum']),encoding ='utf-8')},)#line:121
                del OOO0O0OOO000OOOO0 #line:122
                __f_o_______________g ('已进行返回头和返回体修改:\r\n',str (OO00O000OO0000000 .response .headers )+'\r\n'+OO00O000OO0000000 .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:123
            else :#line:124
                __f_o_______________g ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:125
        elif _ .umatch (OO0O00OOO0O0O0O0O ,_ .login_out )and not ___ ():#line:126
            OO00O000OO0000000 .request .host ='none.com'#line:127
            OO00O000OO0000000 .response =mp .Response .make (status_code =200 ,content =b'{"result":0}',headers ={'Cache-Control':'no-cache','Content-Length':'12','Content-Type':'application/json; charset=utf-8','Date':'Sat, 06 Nov 2021 13:41:52 GMT','Vary':'origin'},)#line:138
    def response (OOOOO00O000OOOO0O ,OOOOO00OOO0000000 :mp .HTTPFlow ):#line:140
        global data #line:141
        O0OOO0OO00OOOOO00 =OOOOO00OOO0000000 .request .url #line:142
        O0OO00OOOO0000000 =False #line:143
        if _ .umatch (O0OOO0OO00OOOOO00 ,_ .remote_config ):#line:144
            OO00O0OOO0OO00OO0 =json .loads (OOOOO00OOO0000000 .response .content )#line:145
            OO00O0OOO0OO00OO0 ['enableBestHttp']=False #line:146
            OOOOO00OOO0000000 .response .set_text (json .dumps (OO00O0OOO0OO00OO0 ))#line:147
            __f_o_______________g ('修改完remote_config')#line:148
        elif _ .umatch (O0OOO0OO00OOOOO00 ,_ .time_conf ):#line:149
            OO00O0OOO0OO00OO0 =json .loads (OOOOO00OOO0000000 .response .content )#line:150
            OO00O0OOO0OO00OO0 ['recEnable']='false'#line:151
            OOOOO00OOO0000000 .response .set_text (json .dumps (OO00O0OOO0OO00OO0 ))#line:152
            __f_o_______________g ('对time-config完成修改')#line:153
        elif _ .umatch (O0OOO0OO00OOOOO00 ,_ .get_token ):#line:154
            __f_o_______________g ('getToken包内容:\r\n',OOOOO00OOO0000000 .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:155
            if OOOOO00OOO0000000 .response .status_code !=200 :#line:156
                O00OOOOOO0OOOOO00 =[OO0O0OO000O000OOO for OO0O0OO000O000OOO in data if data [OO0O0OO000O000OOO ]['login']['access_key']==json .loads (json .loads (OOOOO00OOO0000000 .request .get_content ())['extension'])['access_token']]#line:157
                O0000OOO0OO0O00OO =O00OOOOOO0OOOOO00 [0 ]if len (O00OOOOOO0OOOOO00 )>=1 else None #line:158
                del O00OOOOOO0OOOOO00 #line:159
                if O0000OOO0OO0O00OO :#line:160
                    OOOOO00OOO0000000 .response .status_code =200 #line:161
                    OO00O0OOO0OO00OO0 ={'result':0 ,'error':'','uid':str (data [O0000OOO0OO0O00OO ]['uid']),'channelUid':int (O0000OOO0OO0O00OO ),'token':data [O0000OOO0OO0O00OO ]['token'],'isGuest':0 ,'extension':'{\"nickName\":\"'+data [O0000OOO0OO0O00OO ]['login']['uname']+'\"}'if json .loads (OOOOO00OOO0000000 .request .text )['channelId']=='2'else '{\"isGuest\":false}'}#line:170
                    OOOOO00OOO0000000 .response .set_text (json .dumps (OO00O0OOO0OO00OO0 ))#line:171
                    __f_o_______________g ('密钥获取错误，已进行返回体修改:\r\n',OOOOO00OOO0000000 .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:172
                else :#line:173
                    __f_o_______________g ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:174
            else :#line:175
                OO00O0OOO0OO00OO0 =json .loads (OOOOO00OOO0000000 .response .content )#line:176
                O00OOOOOO0OOOOO00 =[OOOOOO0O0O0OOO0OO for OOOOOO0O0O0OOO0OO in data if int (OOOOOO0O0O0OOO0OO )==OO00O0OOO0OO00OO0 ['channelUid']]#line:177
                O0000OOO0OO0O00OO =O00OOOOOO0OOOOO00 [0 ]if len (O00OOOOOO0OOOOO00 )>=1 else None #line:178
                del O00OOOOOO0OOOOO00 #line:179
                OOO00OO0OOOOOO0O0 =json .loads (json .loads (OOOOO00OOO0000000 .request .get_content ())['extension'])['access_token']#line:180
                if O0000OOO0OO0O00OO :#line:181
                    data [O0000OOO0OO0O00OO ]['login']['access_key']=OOO00OO0OOOOOO0O0 #line:182
                    data [O0000OOO0OO0O00OO ]['uid']=int (OO00O0OOO0OO00OO0 ['uid'])#line:183
                    data [O0000OOO0OO0O00OO ]['token']=OO00O0OOO0OO00OO0 ['token']#line:184
                    O0OO00OOOO0000000 =True #line:185
                    __f_o_______________g ('正常获得token')#line:186
                elif json .loads (OOOOO00OOO0000000 .request .text )['channelId']=='1':#line:187
                    OOO0OOOO0000O0O0O =str (OO00O0OOO0OO00OO0 ['channelUid'])#line:188
                    if OOO0OOOO0000O0O0O in data :#line:189
                        data [OOO0OOOO0000O0O0O ]['login']['access_key']=OOO00OO0OOOOOO0O0 #line:190
                        data [OOO0OOOO0000O0O0O ]['uid']=int (OO00O0OOO0OO00OO0 ['uid'])#line:191
                        data [OOO0OOOO0000O0O0O ]['token']=OO00O0OOO0OO00OO0 ['token']#line:192
                        O0OO00OOOO0000000 =True #line:193
                        __f_o_______________g ('检测到官服账号成功登陆，已同步账号信息')#line:194
                    else :#line:195
                        data [str (OO00O0OOO0OO00OO0 ['channelUid'])]={'login':{'access_key':OOO00OO0OOOOOO0O0 ,},'uid':int (OO00O0OOO0OO00OO0 ['uid']),'seqnum':'1','token':OO00O0OOO0OO00OO0 ['token'],}#line:203
                        O0OO00OOOO0000000 =True #line:204
                        __f_o_______________g ('检测到官服新账号成功登陆，已建立账号信息')#line:205
                    del OOO0OOOO0000O0O0O #line:206
                else :#line:207
                    __f_o_______________g ('正常获得token，但未获得账号信息，','请在法定时间内重新登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:208
                del OOO00OO0OOOOOO0O0 #line:209
        elif _ .umatch (O0OOO0OO00OOOOO00 ,_ .account_login )and ___ ():#line:210
            __f_o_______________g ('account/login包内容:\r\n',OOOOO00OOO0000000 .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:211
            OO00O0OOO0OO00OO0 =json .loads (OOOOO00OOO0000000 .response .content )#line:212
            O00OOOOOO0OOOOO00 =[O0O000O000OO0OOO0 for O0O000O000OO0OOO0 in data if data [O0O000O000OO0OOO0 ]['uid']==int (json .loads (OOOOO00OOO0000000 .request .get_content ())['uid'])]#line:213
            O0000OOO0OO0O00OO =O00OOOOOO0OOOOO00 [0 ]if len (O00OOOOOO0OOOOO00 )>=1 else None #line:214
            del O00OOOOOO0OOOOO00 #line:215
            if O0000OOO0OO0O00OO :#line:216
                if OO00O0OOO0OO00OO0 ['result']==0 :#line:217
                    data [O0000OOO0OO0O00OO ]['secret']=OO00O0OOO0OO00OO0 ['secret']#line:218
                    O0OO00OOOO0000000 =True #line:219
                    __f_o_______________g ('正常获得secret，已保存')#line:220
                else :#line:221
                    __f_o_______________g ('法定时间段内登陆失败，原因未知')#line:222
            else :#line:223
                __f_o_______________g ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:224
        elif _ .umatch (O0OOO0OO00OOOOO00 ,_ .account_sync ):#line:225
            OO00O0OOO0OO00OO0 =json .loads (OOOOO00OOO0000000 .response .content )#line:226
            if (OO00O0OOO0OO00OO0 ['msg']=='stale sequence number'if 'msg'in OO00O0OOO0OO00OO0 else False ):#line:227
                try :#line:228
                    O00OOOOOO0OOOOO00 =[O00O000000000O00O for O00O000000000O00O in data if data [O00O000000000O00O ]['uid']==int (OOOOO00OOO0000000 .request .headers ['uid'])]#line:229
                    O0000OOO0OO0O00OO =O00OOOOOO0OOOOO00 [0 ]if len (O00OOOOOO0OOOOO00 )>=1 else None #line:230
                    del O00OOOOOO0OOOOO00 #line:231
                    if O0000OOO0OO0O00OO :#line:232
                        data [O0000OOO0OO0O00OO ]['seqnum']=str (int (data [O0000OOO0OO0O00OO ]['seqnum'])+2000 )#line:233
                        O0OO00OOOO0000000 =True #line:234
                        __f_o_______________g ('同步账号信息异常，已经尝试增加seqnum',conf =[(1 ,31 ,48 )])#line:235
                    else :#line:236
                        __f_o_______________g ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:237
                except Exception as OOOO00O0O0OOOO0OO :#line:238
                    __f_o_______________g ('同步账号信息异常，尝试增加seqnum失败：',OOOO00O0O0OOOO0OO ,conf =[(1 ,31 ,48 )])#line:239
            elif (OO00O0OOO0OO00OO0 ['message']=='invalid version'if 'message'in OO00O0OOO0OO00OO0 else False ):#line:240
                __f_o_______________g ('同步数据时服务器返回invalid version，官服未解决，若是b服可能是上一次登陆信息未保存或者闪断更新导致',conf =[(1 ,31 ,48 )])#line:241
            elif 'msg'in OO00O0OOO0OO00OO0 or 'message'in OO00O0OOO0OO00OO0 :#line:242
                __f_o_______________g ('未知错误',conf =[(1 ,31 ,48 )])#line:243
            else :#line:244
                __f_o_______________g ('同步账号信息正常')#line:245
        elif _ .umatch (O0OOO0OO00OOOOO00 ,_ .hyper ):#line:246
            __f_o_______________g ('[%s]游戏数据包url: '%time .strftime ('%H:%M:%S'),O0OOO0OO00OOOOO00 ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:247
            if not 'seqnum'in OOOOO00OOO0000000 .response .headers :#line:248
                return #line:249
            O00OOOOOO0OOOOO00 =[O0OO0OOO0OO0OO0O0 for O0OO0OOO0OO0OO0O0 in data if data [O0OO0OOO0OO0OO0O0 ]['uid']==int (OOOOO00OOO0000000 .request .headers ['uid'])]#line:250
            O0000OOO0OO0O00OO =O00OOOOOO0OOOOO00 [0 ]if len (O00OOOOOO0OOOOO00 )>=1 else None #line:251
            del O00OOOOOO0OOOOO00 #line:252
            if O0000OOO0OO0O00OO :#line:253
                if (OOOOO00OOO0000000 .response .headers ['seqnum']!='null'):#line:254
                    data [O0000OOO0OO0O00OO ]['seqnum']=OOOOO00OOO0000000 .response .headers ['seqnum']#line:255
                    O0OO00OOOO0000000 =True #line:256
                    __f_o_______________g ('已保存编号: '+str (OOOOO00OOO0000000 .response .headers ['seqnum']))#line:257
                else :#line:258
                    __f_o_______________g ('未检测到编号，可能是上一次登陆信息未保存或者闪断更新导致',conf =[(1 ,31 ,48 )])#line:259
            else :#line:260
                __f_o_______________g ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:261
        if O0OO00OOOO0000000 :#line:262
            with open (p +'ark_data.json','w',encoding ='utf-8')as OO0OOOO0OO00O0OOO :#line:263
                OO0OOOO0OO00O0OOO .write (json .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False ))#line:264
                OO0OOOO0OO00O0OOO .close ()#line:265
class __f__o________g_____ :#line:267
    ""#line:283
    def response (OO0OO000000O0O000 ,O00O0O00O00OOO00O :mp .HTTPFlow ):#line:284
        global data #line:285
        O0OO0OOOO0O0O0O00 =O00O0O00O00OOO00O .request .url #line:286
        OO0O0O000O00OO0O0 =False #line:287
        if _ .umatch (O0OO0OOOO0O0O0O00 ,_ .heartbeat ):#line:288
            OOO00OOO0000OO0O0 =json .loads (O00O0O00O00OOO00O .response .content )#line:289
            __f_o_______________g ('heartbeat包内容:\r\n',O00O0O00O00OOO00O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:290
            if (OOO00OOO0000OO0O0 ['data']['user_info']['adult_status']==0 ):#line:291
                OOO00OOO0000OO0O0 ['data']['trigger_status']=0 #line:292
                OOO00OOO0000OO0O0 ['data']['event_list']=[]#line:293
                O00O0O00O00OOO00O .response .set_text (json .dumps (OOO00OOO0000OO0O0 ))#line:294
                __f_o_______________g ('检测到未成年人，已进行返回体修改:\r\n',O00O0O00O00OOO00O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:295
            else :#line:296
                __f_o_______________g ('检测到已经成年，未进行修改')#line:297
        elif _ .umatch (O0OO0OOOO0O0O0O00 ,_ .login_1 ,_ .login_2 ,_ .login_3 ,_ .login_4 ):#line:298
            OOO00OOO0000OO0O0 =json .loads (O00O0O00O00OOO00O .response .content )#line:299
            __f_o_______________g ('向BililiGame SDK服务器登陆包内容:\r\n',O00O0O00O00OOO00O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:300
            O0O0OO00O000O00O0 =[OOO00O0O0OO00OOO0 for OOO00O0O0OO00OOO0 in data if data [OOO00O0O0OO00OOO0 ]['login']['access_key']==O00O0O00O00OOO00O .request .urlencoded_form ['access_key']or (str (data [OOO00O0O0OO00OOO0 ]['login']['uuid'])==O00O0O00O00OOO00O .request .urlencoded_form ['user_id']if 'user_id'in O00O0O00O00OOO00O .request .urlencoded_form else False )]#line:301
            OOO00OO00O00OO0O0 =O0O0OO00O000O00O0 [0 ]if len (O0O0OO00O000O00O0 )>=1 else None #line:302
            del O0O0OO00O000O00O0 #line:303
            if OOO00OOO0000OO0O0 ['code']!=0 :#line:304
                if OOO00OO00O00OO0O0 :#line:305
                    OOO00OOO0000OO0O0 ['code']=0 #line:306
                    OOO00OOO0000OO0O0 .pop ('message')#line:307
                    OOO00OOO0000OO0O0 ['access_key']=data [OOO00OO00O00OO0O0 ]['login']['access_key']#line:308
                    OOO00OOO0000OO0O0 ['uid']=int (OOO00OO00O00OO0O0 )#line:309
                    OOO00OOO0000OO0O0 ['face']=data [OOO00OO00O00OO0O0 ]['login']['face']#line:310
                    OOO00OOO0000OO0O0 ['s_face']=data [OOO00OO00O00OO0O0 ]['login']['s_face']#line:311
                    OOO00OOO0000OO0O0 ['uname']=data [OOO00OO00O00OO0O0 ]['login']['uname']#line:312
                    OOO00OOO0000OO0O0 ['expires']=int (time .time ()+3000000 )#line:313
                    O00O0O00O00OOO00O .response .set_text (json .dumps (OOO00OOO0000OO0O0 ))#line:314
                    __f_o_______________g ('检测到登陆code问题，已进行返回体修改:\r\n',O00O0O00O00OOO00O .response .text ,conf =[(1 ,36 ,48 ),(1 ,33 ,48 )])#line:315
                    if not 'uuid'in data [str (OOO00OOO0000OO0O0 ['uid'])]['login']or data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']==OOO00OOO0000OO0O0 ['uid']or data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']=='':#line:316
                        __f_o_______________g ('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：',conf =[(1 ,36 ,41 )])#line:317
                        data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']=str (input ())#line:318
                        OO0O0O000O00OO0O0 =True #line:319
                else :#line:320
                    __f_o_______________g ('查找不到此账号信息，','请在法定时间内登陆一次','以获得账号信息',conf =[(1 ,36 ,48 ),(1 ,31 ,48 ),(1 ,36 ,48 )])#line:321
            else :#line:322
                if OOO00OO00O00OO0O0 :#line:323
                    data [OOO00OO00O00OO0O0 ]['login']['face']=OOO00OOO0000OO0O0 ['face']#line:324
                    data [OOO00OO00O00OO0O0 ]['login']['s_face']=OOO00OOO0000OO0O0 ['s_face']#line:325
                    data [OOO00OO00O00OO0O0 ]['login']['uname']=OOO00OOO0000OO0O0 ['uname']#line:326
                    OO0O0O000O00OO0O0 =True #line:327
                    __f_o_______________g ('检测到b服成功登陆，已同步账号信息')#line:328
                    if not 'uuid'in data [str (OOO00OOO0000OO0O0 ['uid'])]['login']or data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']==OOO00OOO0000OO0O0 ['uid']or data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']=='':#line:329
                        __f_o_______________g ('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：',conf =[(1 ,36 ,41 )])#line:330
                        data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']=str (input ())#line:331
                else :#line:332
                    data [str (OOO00OOO0000OO0O0 ['uid'])]={'login':{'access_key':OOO00OOO0000OO0O0 ['access_key'],'face':OOO00OOO0000OO0O0 ['face'],'s_face':OOO00OOO0000OO0O0 ['s_face'],'uname':OOO00OOO0000OO0O0 ['uname'],'uuid':''},'uid':None ,'seqnum':1 ,'token':None ,'secret':None }#line:345
                    OO0O0O000O00OO0O0 =True #line:346
                    if len (O00O0O00O00OOO00O .request .urlencoded_form ['uid'])>=1 :#line:347
                        data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']=O00O0O00O00OOO00O .request .urlencoded_form ['uid']#line:348
                        __f_o_______________g ('检测到新账号成功登陆，已建立账号信息')#line:349
                    elif not 'uuid'in data [str (OOO00OOO0000OO0O0 ['uid'])]['login']or data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']==OOO00OOO0000OO0O0 ['uid']or data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']=='':#line:350
                        __f_o_______________g ('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：',conf =[(1 ,36 ,41 )])#line:351
                        data [str (OOO00OOO0000OO0O0 ['uid'])]['login']['uuid']=str (input ())#line:352
        if OO0O0O000O00OO0O0 :#line:353
            with open (p +'ark_data.json','w',encoding ='utf-8')as O0OOOO000O0OOO0OO :#line:354
                O0OOOO000O0OOO0OO .write (json .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False ))#line:355
                O0OOOO000O0OOO0OO .close ()#line:356
    '''
    def error(self, flow: mp.HTTPFlow):
        pass
    '''#line:360
class _______f____o________g__ :#line:362
    def response (O0O0O0O000OOO00OO ,O0000O00O000OO0O0 :mp .HTTPFlow ):#line:363
        OO0O0O00OOOOOOOO0 =O0000O00O000OO0O0 .request .url #line:364
        if _ .umatch (OO0O0O00OOOOOOOO0 ,_ .gf_login ,_ .gf_auth ):#line:365
            O00OOOO0OOOO00OOO =json .loads (O0000O00O000OO0O0 .response .content )#line:366
            O00OOOO0OOOO00OOO ['isMinor']=False #line:367
            O0000O00O000OO0O0 .response .set_text (json .dumps (O00OOOO0OOOO00OOO ))#line:368
        elif _ .umatch (OO0O0O00OOOOOOOO0 ,_ .ping ):#line:369
            O00OOOO0OOOO00OOO ={'result':0 ,'message':'OK','interval':5400 ,'timeLeft':-1 ,'alertTime':600 }#line:376
            O0000O00O000OO0O0 .response .set_text (json .dumps (O00OOOO0OOOO00OOO ))#line:377
addons =[_f____o__g____ (),_f___o_______g_ (),__f__o________g_____ (),_______f____o________g__ ()]#line:384
if __name__ =='__main__':#line:386
    from mitmproxy import options #line:387
    from mitmproxy .tools .dump import DumpMaster #line:388
    __f_o_______________g ('请输入数字设置抓包端口（尽量大于1000，必须小于等于65535）：')#line:389
    port =int (input ())#line:390
    opts =options .Options (listen_host ='127.0.0.1',listen_port =port )#line:391
    m =DumpMaster (options =opts )#line:392
    try :#line:393
        __f_o_______________g ('开始抓包，请确保wifi代理地址设置为127.0.0.1，端口为%d，如未下载证书可现在下载'%port )#line:394
        m .addons .add (*addons )#line:395
        m .run ()#line:396
    except :#line:397
        __f_o_______________g ('写入data文件内容:\r\n'+json .dumps (data ,indent =2 ,separators =(', ',': '),ensure_ascii =False ),conf =[(1 ,33 ,48 )])#line:398
        m .shutdown ()
