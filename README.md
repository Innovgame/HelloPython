# FAQ
## Git Bash无法访问gist.github.com
1. 设置梯子
2. 设置windows里的host设置

``` recho
win+R 打开运行窗口
输入 C:\WINDOWS\system32\drivers\etc
以管理员身份用记事本打开 hosts文件
在文件末尾加入 192.30.253.118 gist.github.com 或者 192.30.253.119 gist.github.com
ping gist.github.com 通过
```