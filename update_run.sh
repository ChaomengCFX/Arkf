# !/bin/bash
cd /root
curl -O https://gitee.com/jxr2006/ark-fatigue/raw/main/arknights.py
echo -e '\033[1;34;47m开始运行抓包程序\033[0m
\033[1;34m输入1并回车来确认，输入其他则终止进程（终止后可以输入python3 arknights.py来运行）:\033[0m'
read res
test $res = '1' && python3 /root/arknights.py || echo -e '取消运行程序'