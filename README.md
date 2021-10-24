# 利用mitmproxy抓包绕过方舟防沉迷
***本教程仅供参考学习使用，严禁用于其他用途***
> 注: 暂时只实现了B服，官服晚些实现
## 步骤一 搭建服务端
> 服务端，相当于一个每时每刻都在监视或修改网络数据的工具，我们需要根据系统对它先进行搭建
### 安卓系统
1、服务端在安卓系统搭建是通过termux进行的，我们需要先下载termux  
[termux下载地址](https://f-droid.org/packages/com.termux/)
（进去找到最新版本点下载APK即可）  
[下载速度慢可以用网盘](https://pan.baidu.com/s/1L3P_Uq-1zngROkQYrXICuQ)
提取码:mrfz  
2、自行安装termux并打开  
3、复制下面这段命令到termux，并回车，按照指示安装即可（整个过程根据网络和配置在十分钟左右不等，期间会跳出一个存储空间请求，需要同意）  
```
rm -rf ark-fatigue; pkg install git -y && git clone https://gitee.com/jxr2006/ark-fatigue.git; bash ark-fatigue/a.sh
```  
*若不确保安装成功与否，此段可以再输入一次*
4、显示安装完成后，会出现运行核心程序的选项，输入y则运行，也可以暂时不运行，在下次打开软件时会出现运行的选项，另外，输入
```
python3 ~/ark-fatigue/arknights.py
```
也同样可以运行  
5、运行核心程序后，若输出显示*开始抓包*，恭喜你，服务端已经搭建完毕，可以进入客户端的配置
### Windows
l、去[mitmproxy官网](https://mitmproxy.org/#mitmproxy)选择windows版本下载，自行安装(如果是windows10以下版本需要下载[mitmproxy5.3.0](https://mitmproxy.org/downloads/)的mitmproxy-5.3.0-windows-installer.exe)  
![点击下载windows版本](https://images.gitee.com/uploads/images/2021/1023/174442_e05b8115_7638561.png "8%XI4@WA652P]RL{[LX67]7.png")  
![安装](https://images.gitee.com/uploads/images/2021/1023/174603_4fddf567_7638561.png "K{[0DZ1$H2RBA]24$5C48KU.png")  
2、下载这个项目的源代码，解压，记住路径，然后创建两个文件——ark_data.json，ark_history（注意第二个文件没有后缀，需要在菜单栏的查看打开显示拓展名）  
![设置完的文件夹](https://images.gitee.com/uploads/images/2021/1023/194835_d87d39b4_7638561.png "D7IB[7O2ASNFQY(0W1Y1UOF.png")  
![显示拓展名](https://images.gitee.com/uploads/images/2021/1023/203402_b94f7413_7638561.png "1MJTLRJD}8X`LGS47D1ZS}G.png")  
3、用代码编辑软件或者记事本打开arknights.py，将第一行单引号里面的内容修改为上一步解压的路径，记得最后要有一个/（图片里面是错误示范）  
![设置路径](https://images.gitee.com/uploads/images/2021/1023/195749_6642e1b8_7638561.png "WF6%SD~R14{)@5`4XJL$K@Q.png")  
4、接下来进行客户端（模拟器）的设置
## 步骤二 配置客户端
> 客户端，既运行游戏的系统，我们需要将其对服务端进行对接，使服务端能够监视或修改客户端的数据  
#### 以下所有步骤需要在服务端运行核心程序后进行
### 普通安卓系统
##### 由于系统问题，不再推荐直接使用安卓真机，建议使用虚拟机的方法  
1、设置->网络–>WLAN->选择连接的wifi长按(不同设备操作方式不同，有些是击旁边按钮)–>修改网络–>高级选项，将代理选项设置为手动，在代理服务器主机名中填写`127.0.0.1`，在端口上填写`8008`，完成设置后点击保存即可（不用的时候需要改回去，不然影响平时使用）
2、在浏览器打开`http://mitm.it`，点击安卓的第一个选项下载，随后打开会跳出证书安装器，随便起一个英文名字，确认即可
### 安卓虚拟机
由于直接在主机配置wifi网络需要来回切换，直接在真机上容易出自动登录证书问题，且流量党无法使用，这里介绍使用安卓虚拟机的办法  
*注意:termux服务端若安装在同一手机上，需要安装在真机，而不是虚拟机*  
1、下载虚拟机，这里推荐Vmos pro  
[下载地址](http://www.vmos.cn/product_center_vmospro.htm)  
2、添加虚拟机，选择安卓5.1 极客版  
3、把方舟导入虚拟机，并下载完文件  
4、重启虚拟机，打开xposed确认xposed框架启动  
5、下载JustTrustMe  
链接:https://pan.baidu.com/s/1vLdjOWM65Jt0EndqvC3Z0g  
提取码:mrfz  
将安装包导入虚拟机并安装  
6、安装完后会弹出启用xposed插件的提示，同意即可
7、设置->搜索WLAN->选择连接的VMOSwifi长按–>修改网络–>高级选项，将代理选项设置为手动，在代理服务器主机名中填写`127.0.0.1`，在端口上填写`8008`，完成设置后点击保存即可  
8、在虚拟机浏览器打开`http://mitm.it`，点击安卓的第一个选项下载，随后打开会跳出证书安装器，随便起一个英文名字，确认即可  
### 模拟器
1、用管理员权限打开cmd  
![打开cmd](https://images.gitee.com/uploads/images/2021/1023/195404_22b4d808_7638561.png "]_LNKLG~{~~A0EH0}VTTDDE.png")  
2、输入ipconfig查看自己的ip地址  
![查看ip](https://images.gitee.com/uploads/images/2021/1023/195606_47f602f1_7638561.png "QZ}5F329IO7M{3@MX%}FVOG.png")  
3、进入模拟器（我这里用的是mumu模拟器），设置WiFi代理为手动，地址为自己ip，端口为8008  
![设置代理](https://images.gitee.com/uploads/images/2021/1023/195942_49555077_7638561.png "OH2I)_LP%GSZPO5ZR1``ZEG.png")  
4、在管理员权限下的cmd输入，回车，程序开始运行，并会跳出抓包信息网页  
```
mitmweb -p 8008 -s 你解压源代码的文件夹路径/arknights.py
```
![运行](https://images.gitee.com/uploads/images/2021/1023/202312_0602a9f3_7638561.png "9JV5}2EF4(CYL%84W(]RDRB.png")  
然后在浏览器打开`http://mitm.it`，下载安卓证书并安装（期间会起一个名字，需要你记住，后面要找）  
![下载证书](https://images.gitee.com/uploads/images/2021/1023/200126_aa850b70_7638561.png "]5O5A1WM1VVH6%[ZQK0{D}6.png")  
5、打开模拟器root权限  
![设置root](https://images.gitee.com/uploads/images/2021/1023/200444_82fbb766_7638561.png "0~7(7}QA(M~H%1@95E}@WOS.png")  
6、打开模拟器的文件浏览器，打开超级用户模式  
![设置超级用户模式](https://images.gitee.com/uploads/images/2021/1023/200541_70e10cbb_7638561.png "7IW%{[EST7SU_%0[2RLT3@D.png")  
7、进入/data/misc/user/0/cacerts-added文件夹，选中你刚刚安装的证书（名字不是你刚刚设置的。如果没有安装过其他证书，应该只有一个文件）  
![选中证书](https://images.gitee.com/uploads/images/2021/1023/201059_1d928ee3_7638561.png "FOX}~RJ1U@MD71J31Q609%L.png")  
8、进入/etc/security/cacerts文件夹，粘贴选中的证书到系统证书目录  
![粘贴](https://images.gitee.com/uploads/images/2021/1023/201128_13686839_7638561.png "R1_K9]X`1~N6PKLS{U`~$$4.png")  
9、在设置->安全->信任的凭据->系统下面能找到你设置的证书名字，则说明安装成功  
![查看](https://images.gitee.com/uploads/images/2021/1023/201502_ee7e839a_7638561.png "4_)$HF6DD89M@75W6GLWIW5.png")  
10、以后要运行程序同样是在管理员权限下的cmd输入
```
mitmweb -p 8008 -s 你解压源代码的文件夹路径/arknights.py
```
![运行](https://images.gitee.com/uploads/images/2021/1023/202312_0602a9f3_7638561.png "9JV5}2EF4(CYL%84W(]RDRB.png")  
## 步骤三 在法定时间内登陆
由于要获取正常时段的用户信息来实现时段外登陆，你需要在时段内登陆一次
## 步骤四 完工！
你已经可以在时段外登陆了，不过要注意，闪断更新和大更新会刷新服务器数据导致登陆失效，需要下一次法定时间登陆来获得新的登陆信息  
**最后要说的是，不要过度的投入以影响到自己的学业哟~**
## 注意事项
**登录过程中一定需要打开程序来获得登录信息**
## 其他
手机端输入`bash upgit.sh`可以对代码进行更新  
此项目为我一人花了一周的研究成果，由于课业紧张，难免会有疏漏，反馈&交流加QQ: 2198818239  
请勿随意传播此教程
