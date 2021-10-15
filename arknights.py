from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
import mitmproxy.http as mp
import re, json, time

class Urls:
    def __init__(self):
        self.heartbeat = 'http://line.*?-realtime-api.biligame.net/app/v2/time/heartbeat'
        self.login = 'https://p.biligame.com/api/external/user.token.oauth.login/v3'
        self.login_auto = 'https://line.*?-sdk.*?center-login-sh.biligame.net/api/external/login/v3'
        self.login_self = 'https://line.*?-sdk.*?center-login-sh.biligame.net/api/external/user.token.oauth.login/v3'
        self.get_token = 'https://as.hypergryph.com/u8/user/v1/getToken'
        self.account_login = 'https://ak-gs-b.hypergryph.com/account/login'
        #self.account_sync = 'https://ak-gs-b.hypergryph.com/account/syncData'
        self.hyper = 'https://ak-gs-b.hypergryph.com'

    def match(self, standard, url):
        global re
        if (re.match(standard, url) != None):
            return True
        else:
            return False

urls = Urls()
read = '===开始抓包===\r\n'
with open('/storage/emulated/0/data.json', 'r', encoding = 'utf-8') as f:
    try:
        data = json.loads(f.read())
        if (data == None):
            data = {}
    except:
        data = {}
    f.close()
print('\033[1;33mdata文件内容:\r\n' + str(data) + '\033[0m')

class Events:
    def __init__(self):
        pass

    def http_connect(self, flow: mp.HTTPFlow):
        pass
        
    def requestheaders(self, flow: mp.HTTPFlow):
        pass

    def request(self, flow: mp.HTTPFlow):
        global read
        read += '=================================\r\n'
        read += flow.request.url + '\r\n'
        read += flow.request.get_text() + '\r\n'
        
    def responseheaders(self, flow: mp.HTTPFlow):
        pass

    def response(self, flow: mp.HTTPFlow):
        global urls, read, data
        url = flow.request.url
        if (url.startswith(urls.hyper) and not urls.match(urls.account_login, url)):
            print('\033[1;36m检测到鹰角数据包\033[0m')
            i = False
            if (data != None):
                for key in data:
                    if (data[key]['uid'] == int(flow.request.headers['uid'])):
                        if (flow.response.headers['seqnum'] != 'null'):
                            data[key]['seqnum'] = flow.response.headers['seqnum']
                            print('\033[1;36m已保存seqnum: ' + str(flow.response.headers['seqnum']) + '\033[0m')
                        else:
                            print('\033[1;36m未保存seqnum，因为它为空值\033[0m')
                        i = True
            if (not i):
                print('\033[1;36m查找不到此账号信息，请在法定时间内登陆以获得账号信息\033[0m')
            del i
        if (urls.match(urls.heartbeat, url)):
            re = json.loads(flow.response.content)
            print('\033[1;36mheartbeat包内容:\r\n' + flow.response.text + '\033[0m')
            if (re['data']['user_info']['adult_status'] == 0):
                re['data']['trigger_status'] = 0
                re['data']['event_list'] = []
                flow.response.set_text(json.dumps(re))
                print('\033[1;36m检测到未成年人，已进行返回体修改:\r\n' + flow.response.text +'\033[0m')
            else:
                print('\033[1;36m检测到已经成年，未进行修改\033[0m')
        elif (urls.match(urls.login_self, url) or urls.match(urls.login, url)):
            re = json.loads(flow.response.content)
            print('\033[1;36m手动登陆包内容:\r\n' + flow.response.text + '\033[0m')
            if (re['code'] != 0):
                i = False
                if (data != None):
                    for key in data :
                        if (data[key]['login']['access_key'] == flow.request.urlencoded_form['access_key']):
                            re['code'] = 0
                            re.pop('message')
                            re['access_key'] = data[key]['login']['access_key']
                            re['uid'] = int(key)
                            re['face'] = data[key]['login']['face']
                            re['s_face'] = data[key]['login']['s_face']
                            re['uname'] = data[key]['login']['uname']
                            re['expires'] = int(time.time() + 3000000)
                            flow.response.set_text(json.dumps(re))
                            i = True
                            print('\033[1;36m检测到登陆code问题，已进行返回体修改:\r\n' + flow.response.text +'\033[0m')
                if (not i):
                    print('\033[1;36m查找不到此账号信息，请在法定时间内登陆一次以获得账号信息\033[0m')
            else:
                i = False
                if (data != None):
                    for key in data:
                        if (data[key]['login']['access_key'] == flow.request.urlencoded_form['access_key']):
                            data[key]['login']['face'] = re['face']
                            data[key]['login']['s_face'] = re['s_face']
                            data[key]['login']['uname'] = re['uname']
                            i = True
                            print('\033[1;36m检测到成功登陆，已同步账号信息\033[0m')
                if (not i):
                    data[str(re['uid'])] = {
                      'login': {
                     	  'access_key': re['access_key'],
                     	  'face': re['face'],
                     	  's_face': re['s_face'],
                     	  'uname': re['uname']
                     	 },
                     	 'uid': None,
                     	 'seqnum': 1,
                     	 'token': None,
                     	 'secret': None
                     }
                    print('\033[1;36m检测到新账号成功登陆，已建立账号信息\033[0m')
        elif (urls.match(urls.login_auto, url)):
            re = json.loads(flow.response.content)
            print('\033[1;36m自动登陆包内容:\r\n' + flow.response.text + '\033[0m')
            if (re['code'] != 0):
                i = False
                if (data != None):
                    for key in data :
                        if (data[key]['login']['access_key'] == flow.request.urlencoded_form['access_key']):
                            re['code'] = 0
                            re.pop('message')
                            re['access_key'] = data[key]['login']['access_key']
                            re['uid'] = int(key)
                            re['face'] = data[key]['login']['face']
                            re['s_face'] = data[key]['login']['s_face']
                            re['uname'] = data[key]['login']['uname']
                            re['expires'] = int(time.time() + 3000000)
                            flow.response.set_text(json.dumps(re))
                            i = True
                            print('\033[1;36m检测到登陆code问题，已进行返回体修改:\r\n' + flow.response.text +'\033[0m')
                if (not i):
                    print('\033[1;36m查找不到此账号信息，请在法定时间内登陆一次以获得账号信息\033[0m')
            else:
                i = False
                if (data != None):
                    for key in data:
                        if (data[key]['login']['access_key'] == flow.request.urlencoded_form['access_key']):
                            data[key]['login']['face'] = re['face']
                            data[key]['login']['s_face'] = re['s_face']
                            data[key]['login']['uname'] = re['uname']
                            i = True
                            print('\033[1;36m检测到成功登陆，已同步账号信息\033[0m')
                if (not i):
                    data[str(re['uid'])] = {
                      'login': {
                     	  'access_key': re['access_key'],
                     	  'face': re['face'],
                     	  's_face': re['s_face'],
                     	  'uname': re['uname']
                     	 },
                     	 'uid': None,
                     	 'seqnum': 1,
                     	 'token': None,
                     	 'secret': None
                     }
                    print('\033[1;36m检测到新账号成功登陆，已建立账号信息\033[0m')           
        elif (urls.match(urls.get_token, url)):
            re = json.loads(flow.response.content)
            print('\033[1;36mgetToken包内容:\r\n' + flow.response.text + '\033[0m')
            if (flow.response.status_code != 200):
                i = False
                if (data != None):
                    for key in data :
                        if (data[key]['login']['access_key'] == json.loads(json.loads(flow.request.get_content())['extension'])['access_token']):
                            flow.response.status_code = 200
                            re = {
                              'result': 0,
                              'error': '',
                              'uid': str(data[key]['uid']),
                              'channelUid': int(key),
                              'token': data[key]['token'],
                              'isGuest': 0,
                              'extension': '{\"nickName\":\"' + data[key]['login']['uname'] + '\"}'
                             }
                            flow.response.set_text(json.dumps(re))
                            i = True
                        print('\033[1;36m密钥获取错误，已进行返回体修改:\r\n' + flow.response.text +'\033[0m')
                if (not i):
                    print('\033[1;36m查找不到此账号信息，请在法定时间内登陆一次以获得账号信息\033[0m')
            else:
                i = False
                if (data != None):
                    for key in data:
                        if (int(key) == re['channelUid']):
                            data[key]['uid'] = int(re['uid'])
                            data[key]['token'] = re['token']
                            i = True
                            print('\033[1;36m正常获得token，已保存uid\033[0m')
                if (not i):
                    print('\033[1;36m正常获得token，但未获得账号信息，请在法定时间内完整登陆一次以获得账号信息\033[0m')
        elif (urls.match(urls.account_login, url)):
            re = json.loads(flow.response.content)
            print('\033[1;36maccount/login包内容:\r\n' + flow.response.text + '\033[0m')
            i = False
            if (data != None):
                for key in data:
                    if (data[key]['uid'] == int(json.loads(flow.request.get_content())['uid'])):
                        i = True
                        if (re['result'] != 0):
                            flow.response.status_code = 200
                            re = {
                              'result': 0,
                              'uid': str(data[key]['uid']),
                              'secret': data[key]['secret'],
                              'serviceLicenseVersion': 0
                             }
                            flow.response.set_text(json.dumps(re))
                            flow.response.headers['seqnum'] = data[key]['seqnum']
                            print('\033[1;36m检测到鹰角登陆错误，已进行返回头和返回体修改:\r\n' + str(flow.response.headers) + '\r\n' + flow.response.text +'\033[0m')
                        else:
                            data[key]['secret'] = re['secret']
                            print('\033[1;36m正常获得secret，已保存\033[0m')
            if (not i):
                print('\033[1;36m查找不到此账号信息，请在法定时间内完整登陆一次以获得账号信息\033[0m')
        read += 'response\r\n'
        read += str(flow.response.status_code) + '\r\n'
        read += flow.response.text + '\r\n'

    def error(self, flow: mp.HTTPFlow):
        global read
        read += 'error\r\n'
        
addons = [Events()]
opts = options.Options(listen_host = '127.0.0.1', listen_port = 9999)
m = DumpMaster(options=opts)

try:
    print('\033[1;36m====================开始抓包====================\033[0m')
    m.addons.add(*addons)
    m.run()
except KeyboardInterrupt:
    #print(read)
    with open('/storage/emulated/0/save', 'w', encoding = 'utf-8') as f:
        f.write(read)
        f.flush()
        f.close()
    with open('/storage/emulated/0/data.json', 'w', encoding = 'utf-8') as f:
        f.write(json.dumps(data))
        f.flush()
        f.close()
    print('\033[1;33m写入data文件内容:\r\n' + str(data) + '\033[0m')
    m.shutdown()