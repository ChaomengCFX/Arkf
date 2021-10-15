#!/data/data/com.termux/files/usr/bin/bash
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list
sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list
sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list
echo -e "\033[1;34;47m将开始安装，请确保网络通畅，从头下载需要2G左右数据，期间均为自动安装(除需要授权存储权限)\033[0m
\033[1;34m输入y并回车来确认，输入其他将退出:\033[0m"
read res
test $res = "y" || exit
echo -e "\033[1;33m开始update\033[0m"
pkg update -y || (echo -e "\033[1;33;41mupdate失败\033[0m"; exit)
echo -e "\033[1;33m开始upgrade\033[0m"
pkg upgrade -y || (echo -e "\033[1;33;41mupgrade失败\033[0m"; exit)
echo -e "\033[1;33m开始安装python3\033[0m"
pkg install python3 -y || (echo -e "\033[1;33;41mpython3安装失败\033[0m"; exit)
echo -e "\033[1;33m开始安装Rust编译器\033[0m"
pkg install rust -y || (echo -e "\033[1;33;41mrust安装失败\033[0m"; exit)
echo '[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = "ustc"
[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"' > ~/.cargo/config
echo -e "\033[1;33m开始安装mitmproxy库\033[0m"
pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install mitmproxy -i https://pypi.tuna.tsinghua.edu.cn/simple || (echo -e "\033[1;33;41mmitmproxy安装失败\033[0m"; exit)
echo -e "\033[1;34m获取读写权限，请同意\033[0m"
termux-setup-storage
touch /storage/emulated/0/ark_data.json
touch /storage/emulated/0/ark_history
echo '"\033[1;33m如果有代码更新，可输入bash upgit.sh来获得更新
输入python3 ~/ark-fatigue/arknights.py可运行核心程序\033[0m
\033[1;34m是否现在运行核心程序?
输入y并回车来确认，输入其他将退出:\033[0m"
read res
test $res = "y" && python3 ~/ark-fatigue/arknights.py' > ~/.bashrc
echo 'rm -rf ~/ark-fatigue
git clone https://github.com/jxr2006/ark-fatigue.git
echo -e "\033[1;33m克隆仓库完毕，是否运行核心程序?
输入y并回车来确认，输入其他将退出:\033[0m"
read res
test $res = "y" && python3 ~/ark-fatigue/arknights.py' > ~/upgit.sh
echo -e "\033[1;34;42m安装成功完毕，下一次重启程序后将运行核心程序\033[0m
\033[1;34m输入y来确认运行程序，或输入其他来结束安装:\033[0m"
read res
test $res = "y" && python3 ~/ark-fatigue/arknights.py