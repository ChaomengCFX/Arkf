# 利用mitmproxy实现时段外登陆
***本教程仅供参考学习使用，严禁用于其他用途***
## 步骤大纲：
1. **搭建代理服务器**
2. **配置客户端**
3. **B服需要在法定时间登陆一次**
4. **完成**
## 步骤一 搭建代理服务器
> 代理服务器，相当于一个每时每刻都在监视或修改网络数据的工具，我们需要根据系统对它先进行搭建  
**找到自己的系统按教程进行即可**
### 安卓系统
1. 服务端在安卓系统搭建是通过termux进行的，我们需要先下载termux  
[termux下载地址](https://f-droid.org/packages/com.termux/)
（进去找到最新版本点下载APK即可）  
[下载速度慢可以用网盘](https://pan.baidu.com/s/1L3P_Uq-1zngROkQYrXICuQ)
提取码:mrfz  
2. 自行安装termux并打开  
3. 进行liunx环境的安装，复制下面这段命令到termux，并回车，按照指示安装即可（整个过程请保持网络通畅，这是失败的主要原因）  
```
bash <(curl -s -S -L https://gitee.com/jxr2006/ark-fatigue/raw/main/install_ubuntu.sh)
```  
**注意：update的时候需要手动输入两次y**  
*这一步有时候会失败，大部分是网络问题，多试几遍即可*  
![安装](https://images.gitee.com/uploads/images/2021/1029/150552_e616577b_7638561.png "Screenshot_20211029-130639.png")  
▲安装  
![输入图片说明](https://images.gitee.com/uploads/images/2021/1029/151352_a8987044_7638561.png "Screenshot_20211029-130954.png")  
▲安装完成效果  
4. 显示`进入ubuntu`后，输入下面这行命令来安装mitmproxy
```
bash <(curl -s -S -L https://gitee.com/jxr2006/ark-fatigue/raw/main/setup_mitmproxy.sh)
```  
*注意：期间需要设置时区，请先后输入6（亚洲），70，70（上海）*  
![安装](https://images.gitee.com/uploads/images/2021/1029/150845_6a3ea038_7638561.png "Screenshot_20211029-131025.png")  
▲安装mitmproxy  
![设置大洲](https://images.gitee.com/uploads/images/2021/1029/150922_8390d541_7638561.png "Screenshot_20211028-180953.png")  
▲输入6  
![设置城市](https://images.gitee.com/uploads/images/2021/1029/150954_21fd196b_7638561.png "Screenshot_20211029-131316.png")
▲输入70，应该要输入两次  
5. 显示`mitmproxy`安装完成后，输入下面这行命令来导入并运行程序  
```
bash <(curl -s -S -L https://gitee.com/jxr2006/ark-fatigue/raw/main/init_script.sh)
```
![运行](https://images.gitee.com/uploads/images/2021/1029/152114_41ac3f3a_7638561.png "Screenshot_20211029-130149.png")
▲再次打开termux将自动更新并运行代码  
6. 设置完四位端口后，代理服务器已经搭建完毕，可以进入客户端的配置  
***之后每次登陆前请确保termux上的程序已经开始运行（启动termux默认运行，也可以输入`python3 arknights.py`来运行）***
### Windows
1. 去[mitmproxy官网](https://mitmproxy.org/#mitmproxy)选择windows版本下载，自行安装(如果是windows10以下版本需要下载[mitmproxy5.3.0](https://mitmproxy.org/downloads/)的mitmproxy-5.3.0-windows-installer.exe)  
![点击下载windows版本](https://images.gitee.com/uploads/images/2021/1023/174442_e05b8115_7638561.png "8%XI4@WA652P]RL{[LX67]7.png")  
![安装](https://images.gitee.com/uploads/images/2021/1023/174603_4fddf567_7638561.png "K{[0DZ1$H2RBA]24$5C48KU.png")  
2. 下载click_to_run.bat到一个新建的文件夹（下载最新版本的即可）  
![bat下载](https://images.gitee.com/uploads/images/2021/1031/183618_46bdefdc_7638561.png "3GS8R}@%6[~M@8}4`NY)F56.png")  
3. 运行click_to_run.bat，接下来进行客户端（模拟器）的设置  
## 步骤二 配置客户端
> 客户端，既运行游戏的系统，我们需要将其对服务端进行对接，使服务端能够监视或修改客户端的数据  
#### 以下所有步骤需要在代理服务器运行程序后进行
### 安卓系统
由于直接在主机配置wifi网络需要来回切换，直接在真机上容易出自动登录证书问题，且流量党无法使用，这里介绍使用安卓虚拟机的办法  
*注意:termux服务端若安装在同一手机上，需要安装在真机，而不是虚拟机*  
1. 下载Vmos pro破解版  
[网盘地址](https://pan.baidu.com/s/1MIis1SuL_Yvhm2bbj2jQLQ)  
提取码mrfz  
2. 添加虚拟机，选择安卓7.1 64位 精简版  
3. 通过浏览器下载方舟，或者打开文件传输，把方舟导入虚拟机，或者下载或导入b站及taptap，再下载方舟;请进入游戏下载完游戏文件  
4. 关闭虚拟机，打开root权限，此时推荐把竖屏模式关闭，如果以后想在后台刷关的话可以打开后台保活  
![打开root](https://images.gitee.com/uploads/images/2021/1029/235430_edafce17_7638561.png "Screenshot_20211029-234106.png")
▲打开右上角root开关  
![设置竖屏模式](https://images.gitee.com/uploads/images/2021/1029/235618_94df6e0b_7638561.png "Screenshot_20211029-234321.png")
▲关闭竖屏模式  
![后台保活](https://images.gitee.com/uploads/images/2021/1029/235647_3ea354bf_7638561.png "Screenshot_20211029-235607.png")
▲打开后台保活  
5. 设置->WLAN->选择连接的VMOSwifi长按–>修改网络–>高级选项，将代理选项设置为手动，在代理服务器主机名中填写`127.0.0.1`，在端口上填写你在搭建服务端时输入的端口，完成设置后点击保存即可  
![设置代理](https://images.gitee.com/uploads/images/2021/1029/235926_5eb1b7b9_7638561.png "Screenshot_20211029-234219.png")
▲设置wifi代理  
6. 在虚拟机浏览器打开`http://mitm.it`，点击安卓的第一个选项下载，随后打开，会需要设置锁屏密码，跳出证书安装器，起一个英文名字，确认即可  
![安装证书](https://images.gitee.com/uploads/images/2021/1030/000152_c3704100_7638561.png "Screenshot_20211029-234515.png")
▲安装安卓证书（绿色的第一个选项）  
***如果网站打开异常，请检查上一步代理服务器的程序是否运行，端口和地址设置是否无问题***  
7. 在文件传输中找到ES文件浏览器下载，运行  
![下载ES文件浏览器](https://images.gitee.com/uploads/images/2021/1030/000553_2658aad7_7638561.png "Screenshot_20211029-234403.png")
▲上图中的MT管理器暂时无法在虚拟机内使用  
8. 进入/data/misc/user/0/cacerts-added文件夹，剪切你刚刚安装的证书（名字不是你刚刚设置的。如果没有安装过其他证书，应该只有一个文件）  
9. 进入/etc/security/cacerts文件夹，粘贴证书到系统证书目录  
10. 在设置->安全->信任的凭据->系统下面能找到你设置的证书名字，则说明安装成功  
### 模拟器
1. 打开cmd  
![打开cmd](https://images.gitee.com/uploads/images/2021/1023/195404_22b4d808_7638561.png "]_LNKLG~{~~A0EH0}VTTDDE.png")  
2. 输入ipconfig查看自己的ip地址  
![查看ip](https://images.gitee.com/uploads/images/2021/1023/195606_47f602f1_7638561.png "QZ}5F329IO7M{3@MX%}FVOG.png")  
3. 进入模拟器（我这里用的是mumu模拟器），设置WiFi代理为手动，地址为自己ip，端口为8008  
![设置代理](https://images.gitee.com/uploads/images/2021/1023/195942_49555077_7638561.png "OH2I)_LP%GSZPO5ZR1``ZEG.png")  
4. 在浏览器打开`http://mitm.it`，下载安卓证书并安装（期间会设置锁屏密码，并起一个英文名字）  
![下载证书](https://images.gitee.com/uploads/images/2021/1023/200126_aa850b70_7638561.png "]5O5A1WM1VVH6%[ZQK0{D}6.png")  
5. 打开模拟器root权限  
![设置root](https://images.gitee.com/uploads/images/2021/1023/200444_82fbb766_7638561.png "0~7(7}QA(M~H%1@95E}@WOS.png")  
6. 打开模拟器的文件浏览器，打开超级用户模式  
![设置超级用户模式](https://images.gitee.com/uploads/images/2021/1023/200541_70e10cbb_7638561.png "7IW%{[EST7SU_%0[2RLT3@D.png")  
7. 进入/data/misc/user/0/cacerts-added文件夹，选中你刚刚安装的证书（名字不是你刚刚设置的。如果没有安装过其他证书，应该只有一个文件）  
![选中证书](https://images.gitee.com/uploads/images/2021/1023/201059_1d928ee3_7638561.png "FOX}~RJ1U@MD71J31Q609%L.png")  
8. 进入/etc/security/cacerts文件夹，粘贴选中的证书到系统证书目录  
![粘贴](https://images.gitee.com/uploads/images/2021/1023/201128_13686839_7638561.png "R1_K9]X`1~N6PKLS{U`~$$4.png")  
9. 在设置->安全->信任的凭据->系统下面能找到你设置的证书名字，则说明安装成功  
![查看](https://images.gitee.com/uploads/images/2021/1023/201502_ee7e839a_7638561.png "4_)$HF6DD89M@75W6GLWIW5.png")  
10. ***之后每次登陆前请确保click_to_run.bat已经开始运行（另外，如果更换了网络导致ip变化，请重新执行第2，3步）***
## 步骤三 \在法定时间内登陆
由于要获取正常时段的用户信息来实现时段外登陆，你需要在时段内登陆一次
## 步骤四 完工！
你已经可以在时段外登陆了，不过要注意，闪断更新和大更新会刷新服务器数据导致B服登陆数据失效，需要下一次法定时间登陆来获得新的登陆信息  
**最后要说的是，不要过度的投入以影响到自己的学业哟~**
## 注意事项
- **登录过程中一定需要打开代理服务器程序来获得登录信息**
- **输入命令的时候请确认输入法没有导致命令修改**
- **如果想将代理服务器和客户端用于不同设备，则客户端的地址需要设置为服务端ip地址，端口设置为服务端端口**
- **更新游戏的时候可以关闭代理，更新完再打开**
## 其他
- 手机端的代码在termux启动时代码会自动更新，电脑端运行click_to_run.bat时会下载新版本代码  
- *此项目为我一人花了一周的研究成果，由于课业紧张，难免会有疏忽
**请勿随意传播此教程(◍˃̶ᗜ˂̶◍)✩**
