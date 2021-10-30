# !/bin/bash
# 换源
sed -i s@ports.ubuntu.com/ubuntu-ports@mirrors.tuna.tsinghua.edu.cn/ubuntu-ports@g /etc/apt/sources.list

#update&upgrade
echo -e '\033[1;33m开始安装update\033[0m'
apt-get update -y || echo -e '\033[1;33;41mupdate失败\033[0m'
echo -e '\033[1;33m开始安装upgrade\033[0m'
apt-get upgrade -y || echo -e '\033[1;33;41mupgrade失败\033[0m'
#安装python和pip
echo -e '\033[1;33m开始安装python\033[0m
\033[1;34;47m期间将进行时区设置，请先后输入6(Asia)，70，70(Shanghai)\033[0m
\033[1;34m输入1并回车来确认，输入其他则终止进程:\033[0m'
read res
test $res = '1' || echo -e '进程被手动终止'
apt-get install python3 -y || echo -e '\033[1;33;41mpython安装失败\033[0m'
echo -e '\033[1;33m开始安装python3-pip\033[0m'
apt-get install pip -y || echo -e '\033[1;33;41mpip安装失败\033[0m'
#安装mitmproxy
echo -e '\033[1;33m开始安装mitmproxy\033[0m'
pip install mitmproxy -i https://pypi.tuna.tsinghua.edu.cn/simple || echo -e '\033[1;33;41mpython3-pip安装失败\033[0m'

echo -e '\033[1;34;42mmitmproxy安装完毕\033[0m'