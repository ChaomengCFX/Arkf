powershell (new-object System.Net.WebClient).DownloadFile('https://gitee.com/jxr2006/ark-fatigue/raw/main/arknights.py','%~dp0arknights.py')
mitmweb -p 8008 -s %~dp0arknights.py