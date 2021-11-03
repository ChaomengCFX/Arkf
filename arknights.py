import mitmproxy.http as mp
import os, re, json, time

if os.name == 'nt':
    from colorama import init
    init(autoreset = True)

def printc(*string, conf = [(1, 36, 48)]):
    print(''.join(['\033[%s;%s;%sm%s\033[0m' % (conf[n if n <= len(conf) - 1 else len(conf) - 1][0], conf[n if n <= len(conf) - 1 else len(conf) - 1][1], conf[n if n <= len(conf) - 1 else len(conf) - 1][2], string[n]) for n in range(len(string))]))

p = os.getcwd().replace('\\', '/') + '/'
if not os.path.exists(p + 'ark_history'):
    os.makedirs(p + 'ark_history')
his = p + 'ark_history/' + time.strftime('%Y_%m_%d %H-%M-%S')
with open(his, 'w', encoding = 'utf-8') as f:
    f.write('……………………………………………………………………\n' + '…………………………………程序开端…………………………………\n' + '……………………………………………………………………\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
    f.close()
try:
    with open(p + 'ark_data.json', 'r', encoding = 'utf-8') as f:
        data = json.loads(f.read())
        if (data == None):
            data = {}
        f.close()
except:
    data = {}
printc('data文件内容:\r\n', str(data), conf = [(1, 36, 48), (1, 33, 48)])

class Urls:
    heartbeat = 'http://line.*?realtime.*?api.biligame.net/app/v2/time/heartbeat'
    login_1 = 'https://p.biligame.com/api/external/user.token.oauth.login/v3'
    login_2 = 'https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/login/v3'
    login_3 = 'https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/user.token.oauth.login/v3'
    login_4 = 'https://line.*?sdk.*?center.*?login.*?biligame.*?/api/external/token.exchange/v3'
    get_token = 'https://as.hypergryph.com/u8/user/v1/getToken'
    account_login = 'https://.*?hypergryph.com/account/login'
    remote_config = 'https://ak.*?conf.hypergryph.com/config/prod/.*?/remote_config'
    hyper = 'https://.*?hypergryph.com'
    time_conf = 'https://line.*?realtime.*?api.biligame.net/app/time/conf'
    gf_auth = 'https://as.hypergryph.com/user/auth'
    gf_login = 'https://as.hypergryph.com/user/login'
    ping = 'https://.*?hypergryph.com/online/v1/ping'
    hyper_host = 'hypergryph'
    bili_host = 'biligame'
    #account_sync = 'https://ak-gs-b.hypergryph.com/account/syncData'

    def umatch(url, *standard):
        return False in (re.match(s, url) == None for s in standard) or True in (s in url for s in standard)

class History_recorder:
    def response(self, flow: mp.HTTPFlow):
        if not Urls.umatch(flow.request.url, Urls.hyper_host, Urls.bili_host):
            return
        read = '\n\n\n==================' + time.strftime('%Y-%m-%d %H:%M:%S') + '===============\n'
        read += '请求url: ' + flow.request.url + '\n'
        read += '请求头' + str(flow.request.headers) + '\n'
        try:
            read += ('请求体: ' + flow.request.get_text() if flow.request.get_text() != None else '') + '\n'
        except:
            read += '请求体: ' + '（decode失败或者为空）'
        read += '状态码: ' + str(flow.response.status_code) + '\n'
        read += '返回头' + str(flow.response.headers) + '\n'
        try:
            read += '返回体: ' + flow.response.text if flow.response.text != None else ''
        except:
            read += '返回体: ' + '（decode失败或者为空）'
        global his
        with open(his, 'a+', encoding = 'utf-8') as f:
            f.write(read)
            f.close()

class Based:
    def response(self, flow: mp.HTTPFlow):
        global data
        url = flow.request.url
        c = False
        if Urls.umatch(url, Urls.remote_config):
            re = json.loads(flow.response.content)
            re['enableBestHttp'] = False
            flow.response.set_text(json.dumps(re))
            printc('修改完remote_config')
        elif Urls.umatch(url, Urls.time_conf):
            re = json.loads(flow.response.content)
            re['recEnable'] = 'false'
            flow.response.set_text(json.dumps(re))
            printc('对time-config完成修改')
        elif Urls.umatch(url, Urls.hyper):
            if not 'seqnum' in flow.response.headers:
                return
            printc('检测到鹰角数据包')
            i = [k for k in data if data[k]['uid'] == int(flow.request.headers['uid'])]
            key = i[0] if len(i) >= 1 else None
            del i
            if key:
                if (flow.response.headers['seqnum'] != 'null'):
                    data[key]['seqnum'] = flow.response.headers['seqnum']
                    printc('已保存seqnum: ' + str(flow.response.headers['seqnum']))
                else:
                    printc('未保存seqnum，因为它为空值，可能是上一次登陆信息未保存或者闪断更新导致')
            else:
                printc('查找不到此账号信息，', '请在法定时间内登陆一次', '以获得账号信息', conf = [(1, 36, 48), (1, 31, 48), (1, 36, 48)])
        elif Urls.umatch(url, Urls.get_token):
            re = json.loads(flow.response.content)
            printc('getToken包内容:\r\n', flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
            if flow.response.status_code != 200:
                i = [k for k in data if data[k]['login']['access_key'] == json.loads(json.loads(flow.request.get_content())['extension'])['access_token']]
                key = i[0] if len(i) >= 1 else None
                del i
                if key:
                    flow.response.status_code = 200
                    re = {
                      'result': 0,
                      'error': '',
                      'uid': str(data[key]['uid']),
                      'channelUid': int(key),
                      'token': data[key]['token'],
                      'isGuest': 0,
                      'extension': '{\"nickName\":\"' + data[key]['login']['uname'] + '\"}' if json.loads(flow.request.text)['channelId'] == '2' else '{\"isGuest\":false}'
                     }
                    flow.response.set_text(json.dumps(re))
                    printc('密钥获取错误，已进行返回体修改:\r\n', flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
                else:
                    printc('查找不到此账号信息，', '请在法定时间内登陆一次', '以获得账号信息', conf = [(1, 36, 48), (1, 31, 48), (1, 36, 48)])
            else:
                i = [k for k in data if int(k) == re['channelUid']]
                key = i[0] if len(i) >= 1 else None
                del i
                if key:
                    data[key]['login']['access_key'] = json.loads(json.loads(flow.request.get_content())['extension'])['access_token']
                    data[key]['uid'] = int(re['uid'])
                    data[key]['token'] = re['token']
                    c = True
                    printc('正常获得token')
                elif json.loads(flow.request.text)['channelId'] == '1':
                    data[str(re['channelUid'])] = {
                      'login': {
                     	  'access_key': json.loads(json.loads(flow.request.get_content())['extension'])['access_token'],
                     	 },
                     	 'uid': re['uid'],
                     	 'seqnum': 1,
                     	 'token': re['token'],
                     	 'secret': None
                     }
                    c = True
                    printc('检测到官服新账号成功登陆，已建立账号信息')
                else:
                    printc('正常获得token，但未获得账号信息，', '请在法定时间内重新登陆一次', '以获得账号信息', conf = [(1, 36, 48), (1, 31, 48), (1, 36, 48)])
        elif Urls.umatch(url, Urls.account_login):
            re = json.loads(flow.response.content)
            printc('account/login包内容:\r\n', flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
            i = [k for k in data if data[k]['uid'] == int(json.loads(flow.request.get_content())['uid'])]
            key = i[0] if len(i) >= 1 else None
            del i
            if key:
                if re['result'] != 0:
                    flow.response.status_code = 200
                    re = {
                      'result': 0,
                      'uid': str(data[key]['uid']),
                      'secret': data[key]['secret'],
                      'serviceLicenseVersion': 0
                     }
                    flow.response.set_text(json.dumps(re))
                    flow.response.headers['seqnum'] = str(data[key]['seqnum'])
                    printc('检测到鹰角登陆错误，已进行返回头和返回体修改:\r\n', str(flow.response.headers) + '\r\n' + flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
                else:
                    data[key]['secret'] = re['secret']
                    c = True
                    printc('正常获得secret，已保存')
            else:
                printc('查找不到此账号信息，', '请在法定时间内登陆一次', '以获得账号信息', conf = [(1, 36, 48), (1, 31, 48), (1, 36, 48)])
        if c:
            with open(p + 'ark_data.json', 'w', encoding = 'utf-8') as f:
                f.write(json.dumps(data))
                f.close()

class Bilibili_listener:
    '''
    def __init__(self):
        pass

    def http_connect(self, flow: mp.HTTPFlow):
        pass
        
    def requestheaders(self, flow: mp.HTTPFlow):
        pass

    def request(self, flow: mp.HTTPFlow):
        pass
        
    def responseheaders(self, flow: mp.HTTPFlow):
        pass
    '''
    def response(self, flow: mp.HTTPFlow):
        global data
        url = flow.request.url
        c = False
        if Urls.umatch(url, Urls.heartbeat):
            re = json.loads(flow.response.content)
            printc('heartbeat包内容:\r\n', flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
            if (re['data']['user_info']['adult_status'] == 0):
                re['data']['trigger_status'] = 0
                re['data']['event_list'] = []
                flow.response.set_text(json.dumps(re))
                printc('检测到未成年人，已进行返回体修改:\r\n', flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
            else:
                printc('检测到已经成年，未进行修改')
        elif Urls.umatch(url, Urls.login_1, Urls.login_2, Urls.login_3, Urls.login_4):
            re = json.loads(flow.response.content)
            printc('向BililiGame SDK服务器登陆包内容:\r\n', flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
            i = [k for k in data if data[k]['login']['access_key'] == flow.request.urlencoded_form['access_key'] or (str(data[k]['login']['uuid']) == flow.request.urlencoded_form['user_id'] if 'user_id' in flow.request.urlencoded_form else False)]
            key = i[0] if len(i) >= 1 else None
            del i
            if re['code'] != 0:
                if key:
                    re['code'] = 0
                    re.pop('message')
                    re['access_key'] = data[key]['login']['access_key']
                    re['uid'] = int(key)
                    re['face'] = data[key]['login']['face']
                    re['s_face'] = data[key]['login']['s_face']
                    re['uname'] = data[key]['login']['uname']
                    re['expires'] = int(time.time() + 3000000)
                    flow.response.set_text(json.dumps(re))
                    printc('检测到登陆code问题，已进行返回体修改:\r\n', flow.response.text, conf = [(1, 36, 48), (1, 33, 48)])
                    if not 'uuid' in data[str(re['uid'])]['login'] or data[str(re['uid'])]['login']['uuid'] == re['uid'] or data[str(re['uid'])]['login']['uuid'] == '':
                        printc('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：', conf = [(1, 36, 41)])
                        data[str(re['uid'])]['login']['uuid'] = str(input())
                        c = True
                else:
                    printc('查找不到此账号信息，', '请在法定时间内登陆一次', '以获得账号信息', conf = [(1, 36, 48), (1, 31, 48), (1, 36, 48)])
            else:
                if key:
                    data[key]['login']['face'] = re['face']
                    data[key]['login']['s_face'] = re['s_face']
                    data[key]['login']['uname'] = re['uname']
                    c = True
                    printc('检测到b服成功登陆，已同步账号信息')
                    if not 'uuid' in data[str(re['uid'])]['login'] or data[str(re['uid'])]['login']['uuid'] == re['uid'] or data[str(re['uid'])]['login']['uuid'] == '':
                        printc('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：', conf = [(1, 36, 41)])
                        data[str(re['uid'])]['login']['uuid'] = str(input())
                else:
                    data[str(re['uid'])] = {
                      'login': {
                     	  'access_key': re['access_key'],
                     	  'face': re['face'],
                     	  's_face': re['s_face'],
                     	  'uname': re['uname'],
                          'uuid': ''
                     	 },
                     	 'uid': None,
                     	 'seqnum': 1,
                     	 'token': None,
                     	 'secret': None
                     }
                    c = True
                    if len(flow.request.urlencoded_form['uid']) >= 1:
                        data[str(re['uid'])]['login']['uuid'] = flow.request.urlencoded_form['uid']
                        printc('检测到新账号成功登陆，已建立账号信息')
                    elif not 'uuid' in data[str(re['uid'])]['login'] or data[str(re['uid'])]['login']['uuid'] == re['uid'] or data[str(re['uid'])]['login']['uuid'] == '':
                        printc('检测到此账号登录时的账号、手机号码或邮箱未保存，请自行输入登录时的账号，只有一次机会，注意不要输错：', conf = [(1, 36, 41)])
                        data[str(re['uid'])]['login']['uuid'] = str(input())
        if c:
            with open(p + 'ark_data.json', 'w', encoding = 'utf-8') as f:
                f.write(json.dumps(data))
                f.close()
    '''
    def error(self, flow: mp.HTTPFlow):
        pass
    '''

class Official_listener:
    def response(self, flow: mp.HTTPFlow):
        url = flow.request.url
        if Urls.umatch(url, Urls.gf_login, Urls.gf_auth):
            te = json.loads(flow.response.content)
            te['isMinor'] = False
            flow.response.set_text(json.dumps(te))
        elif Urls.umatch(url, Urls.ping):
            te = {
              'result': 0,
              'message': 'OK',
              'interval': 5400,
              'timeLeft': -1,
              'alertTime': 600
             }
            flow.response.set_text(json.dumps(te))

addons = [
    History_recorder(),
    Based(),
    Bilibili_listener(),
    Official_listener()
 ]

if __name__ == '__main__':
    from mitmproxy import options
    from mitmproxy.tools.dump import DumpMaster
    printc('请输入数字设置抓包端口（尽量大于1000，必须小于等于65535）：')
    port = int(input())
    opts = options.Options(listen_host = '127.0.0.1', listen_port = port)
    m = DumpMaster(options = opts)
    try:
        printc('====================开始抓包，请确保wifi代理地址设置为127.0.0.1，端口为%d，如未下载证书可现在下载====================' % port)
        m.addons.add(*addons)
        m.run()
    except:
        printc('写入data文件内容:\r\n' + str(data), conf = [(1, 33, 48)])
        m.shutdown()
