### web狗的writeup id:l4t0_0

## 能看到吗？

	查看源代码得到flag{a2714506-b3e2-417d-bac9-e8d078ed4d96}
   
## 加密的地址
	
	注释里面 flag{455ec542-5f3e-4cd6-beb0-26a5e67338fe}
    
## 看仔细了

	base64
	pass=MWMzNmNkNTI= ==> 1c36cd52
	pass1=NDFiNzczNWVlZmRj ==> 41b7735eefdc
    输入得到 flag{dd97563d-e256-4b08-b5cb-a86ea77ade4f}
   
## 外表可是具有欺骗性的

	源代码最后是unicode编码，转换后flag{52bab258-a1a6-46c3-b621-f6e251484a1f}

## 洞察力是你取胜的关键

	源码里面有一个5.js,发现是js混淆后，反混淆得到	    				32:64:39:30:61:39:30:38:31:63:62:38:64:61:63:38:61:64:65:65:61:34:63:33:61:66:30:33:34:39:32:61
    hex2sring后得到2d90a9081cb8dac8adeea4c3af03492a，转md5得到zf651q

## 统计

	s=1+2*3+4*5···98*99+100
```python
s = ''
for i in range(1, 100, 1):
    s += str(i)
    if (i % 2):
        s += '+'
    else:
        s += '*'
s += '100'
print (eval(s))
```
	得到164251
	提交得到flag

## 找到它！

	字符串不变，直接看答案是9Vevi，然后brup爆破提交得到flag
	
## 神奇数

```
for i in range(31622, 99999, 1):
    t = str(i * i)
    if ('0' in t and '1' in t and '2' in t and '3' in t and '4' in t and '5' in t and '6' in t and '7' in t and '8' in t and '9' in t):
        print (t)
        print (i)
        break
```
	得到1026753849根是32043

## ASCII与二进制

	7位

## 算算二进制

	1048575，直接看20个1的二进制是多少

## 你会吗？

	中断字

## 残缺的base64

```python
	s = '6ZWc6Iqx5_C05pyI'
import base64
for i in range(ord('a'), ord('z') + 1, 1):
    try:
        print (base64.b64decode(s.replace('_', chr(i))).decode())
    except Exception as e:
        # print (e)
        pass

for i in range(ord('A'), ord('Z') + 1, 1):
    try:
        print (base64.b64decode(s.replace('_', chr(i))).decode())
    except Exception as e:
        pass

for i in range(ord('0'), ord('9') + 1, 1):
    try:
        print (base64.b64decode(s.replace('_', chr(i))).decode())
    except Exception as e:
        pass
```
得到一堆
```
镜花場月
镜花尴月
镜花怴月
镜花搴月
镜花栴月
镜花水月
镜花䀴月
镜花䐴月
镜花䠴月
镜花䰴月
镜花倴月
镜花吴月
镜花瀴月
镜花琴月
镜花破月
镜花簴月
```
	镜花水月正确，6ZWc6Iqx5rC05pyI

## 错误的md5
	
    把l改成1，得到企鹅
    
## 就差一步

	直接rot13，flag{91b19e02-4fb7-45b6-a59b-4edac2b1d2ad}
    
## 这句话有点意思！

	培根，看是否斜体ABAAB AABAA ABBAA ABBAA AAAAA BAAAA AAABB
    第二种方式解密得到：kennard

## 有选择吗？

	B

## flag呢

	wireshark打开看到No.9里面有flag,flag{\304\343\327\324\274\272\277\264\327\305\260\354}
    '\304\343\327\324\274\272\277\264\327\305\260\354'.decode('gbk')
    flag{你自己看着办}

## 万中有一

	过滤http,在No.218也就是最后一个包的stream中找到flag{6c0d68b0-c638-4fb5-a8f5-fdc756daf7e0}qjbjq}

## 大黑阔

	打开看到一片聊天记录，然后扣出来一个map
    各种隐写分析无果
    看聊天记录，提到了王思聪100，百度一下发现是王思聪出席第100个万达广场，在昆明，然后这个map的网址也是昆明，往地图上昆明看，发现白色的flag，简直了
    
##  Findpass
apktool反编译，然后dex2jar看到源码后，对着源码写脚本
```python
char1 = [i for i in 'Tr43Fla92Ch4n93']
char2 = (list(open('src.jpg', 'r').read()))
for i in range(0, len(char1)):
    k = ord(char2[ord(char1[i])]) % ord('\n')
    if (i % 2 == 1):
        char1[i] = chr(ord(char1[i]) + k)
    else:
        char1[i] = chr(ord(char1[i]) - k)
print (''.join(char1))
```
得到Qv49AmZB2Df4jB-，但是并不是flag
对着[http://drops.wooyun.org/papers/6045](http://drops.wooyun.org/papers/6045)插桩后，得到Qv49CmZB2Df4jB-




## 整站我也能看到

	gift.rar得到flag,这个脑洞0.0
    
## 登录
	
    没连数据库，试了sql注入果然没反应，最后找到备份文件sql.sql，这个脑洞给34分

## flag在哪里?

	直接把小写的php改成大写的PHP过，这个脑洞给ssctf2014的出题人

## 执行!

	root' # 绕过后直接进入flag目录cat查看flag
    flag{76c78577-6e75-420d-8837-a44613bb5f3a}

## 弹弹弹

	输入<script>alert(1);</script>就给了flag,这是我见过最简单的xss

##　就在其中

	brup爆破xxxx.php，找到1234.php，直接访问没内容，首页file=1234.php也不行
    用http://106.75.8.230:12866/?file=php://filter/convert.base64-encode/resource=1234.php
    得到base64，flag{3b456e00-954b-4290-92eb-966e38750477}

## 瞒天过海

	登陆得到token，ad0234829205b9033196ba818f7a872b
    解密之test2
    改cookie为test的md5不行，test1不行
    admin不行，admin1可以 e00cf25ad42683b3df678c61f42c6bda
    

## 摄影师的家
	
    （题目已经关了，回忆一下）
    看网站信息，去下载源码秋潮v1.5，找到默认数据库路径为/db/bear.asp,下载，里面直接找到admin的md5，解密之进入后台
    之后在图片管理的地方上传一句话木马，改为jpg即可，然后数据库备份把1.jpg改为shell.asp即可连接
    c盘找到flag



