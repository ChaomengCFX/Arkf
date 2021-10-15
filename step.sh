#! /bin/bash
cd ~
echo "\033[1;34m开始换termux清华大学源\033[0m"
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main@' $PREFIX/etc/apt/sources.list
sed -i 's@^\(deb.*games stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable@' $PREFIX/etc/apt/sources.list.d/game.list
sed -i 's@^\(deb.*science stable\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable@' $PREFIX/etc/apt/sources.list.d/science.list
echo "\033[1;5;33mupdata中若有选项需要选择请输入y——输入1来确认，输入2来跳过此步，输入其它将终止进程"
read i
case $i in
    1)
        echo -e "\033[1;33m开始update\033[0m"
;;
    2)
        echo -e "\033[1;33m已跳过update\033[0m"
;;
    *)
        echo -e "\033[1;33m终止进程\033[0m"
        exit
if pkg update; then
    echo -e "\033[1;33;41mupdate成功\033[0m"
else
    echo -e "\033[1;33;41mupdate失败，已终止进程\033[0m"
    exit
fi
echo -e "\033[1;33m开始upgrade\033[0m"

pkg upgrade || echo -e "\033[1;33;41mupgrade失败\033[0m"
echo -e "\033[1;33m开始安装python3\033[0m"
pkg install python3 || echo -e "\033[1;33;41mpython3安装失败\033[0m"
echo -e "\033[1;33m开始安装Rust编译器\033[0m"
pkg install rust || echo -e "\033[1;33;41mrust安装失败\033[0m"
echo -e "\033[1;33m开始换Rust中科大源\033[0m"
touch .cargo/config
echo '[source.crates-io]
registry = "https://github.com/rust-lang/crates.io-index"
replace-with = "ustc"
[source.ustc]
registry = "git://mirrors.ustc.edu.cn/crates.io-index"' > .cargo/config && echo -e "\033[1;33m开始安装mitmproxy库\033[0m" ; pip3 install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple && pip3 install mitmproxy -i https://pypi.tuna.tsinghua.edu.cn/simple || echo -e "\033[1;33;41mmitmproxy安装失败\033[0m" && echo -e "\033[1;33m开始下一步\033[0m"