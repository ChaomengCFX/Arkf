# !$PATH/bash
# 换termux源
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list
sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list
sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list

echo -e '\033[1;34;47m将开始安装ubuntu，请确保网络通畅，期间有些选项需要输入y\033[0m
\033[1;34m输入1并回车来确认，输入其他则终止进程:\033[0m'
read res
test $res = '1' || (echo -e '进程被手动终止'; exit)
# update
dpkg --configure -a
echo -e '\033[1;33m开始安装update\033[0m'
pkg update -y || (echo -e '\033[1;33;41mupdate失败\033[0m'; exit)
# 安装proot-distro
echo -e '\033[1;33m开始安装proot-distro\033[0m'
pkg install proot-distro -y || (echo -e '\033[1;33;41mproot-distro安装失败\033[0m'; exit)
# 安装ubuntu
echo -e '\033[1;33m开始安装ubuntu\033[0m'
sed -i 's@"https://github.com@"https://ghproxy.com/https://github.com@g' $ANDROID_DATA/data/com.termux/files/usr/etc/proot-distro/ubuntu.sh
proot-distro install ubuntu || (echo -e '\033[1;33;41mubuntu安装失败\033[0m'; exit)
echo 'proot-distro login ubuntu' > ~/.bashrc
# 登陆ubuntu
echo -e '\033[1;34m开始运行ubuntu\033[0m'
proot-distro login ubuntu || (echo -e '\033[1;33;41mubuntu运行失败\033[0m'; exit)