---

#Training

####Training: Get Sourced

	Use View Sourcecode to get it
	在页面最下面找到key

####Training: ASCII

	In a computer, you can only work with numbers.
	In this challenge you have to decode the following message, which is in ASCII.

	84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 115, 103, 104, 109, 110, 97, 110, 111, 115, 109, 109, 112

	转换出ASCII

```python
List = [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115,58, 32, 115, 103, 104, 109, 110, 97, 110, 111, 115, 109, 109, 112]
for i in range(0,len(List),1):
print chr(List[i]),
```


####Training: WWW-Robots

	In this little training challenge, you are going to learn about the Robots_exclusion_standard.
	The robots.txt file is used by web crawlers to check if they are allowed to crawl and index your website or only parts of it.
	Sometimes these files reveal the directory structure instead protecting the content from being crawled.

	Enjoy!

	这是考察robots 看Wechall主域名后面加robots.txt出现

	http://www.wechall.net/robots.txt
	User-agent: *
	Disallow: /challenge/training/www/robots/T0PS3CR3T
	http://www.wechall.net/challenge/training/www/robots/T0PS3CR3T/

	提示了一个网址
	访问之 OK



####Training: Stegano I
	
	直接给了一个图片 下载

	文本打开 最后一句发现password

####Training: WWW-Basics
	
	在指定目录写内容即可,注意最后不要有换行

####Training: MySQL I
	
	This one is the classic mysql injection challenge.
	Your mission is easy: Login yourself as admin.
	Again you are given the sourcecode, also as highlighted version.

	Enjoy!

```php
<?php
/* TABLE STRUCTURE
CREATE TABLE IF NOT EXISTS users (
userid    INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
username  VARCHAR(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
password  CHAR(32) CHARACTER SET ascii COLLATE ascii_bin NOT NULL
) ENGINE=myISAM;
*/
 
# Username and Password sent?
if ( ('' !== ($username = Common::getPostString('username'))) &amp;&amp; (false !== ($password = Common::getPostString('password', false))) ) {
        auth1_onLogin($chall, $username, $password);
}
 
/**
 * Get the database for this challenge.
 * @return GDO_Database
 */
function auth1_db()
{
        if (false === ($db = gdo_db_instance('localhost', WCC_AUTH_BYPASS1_USER, WCC_AUTH_BYPASS1_PASS, WCC_AUTH_BYPASS1_DB))) {
                die('Database error 0815_1!');
        }
        $db-&gt;setLogging(false);
        $db-&gt;setEMailOnError(false);
        return $db;
}
 
/**
 * Exploit this!
 * @param WC_Challenge $chall
 * @param unknown_type $username
 * @param unknown_type $password
 * @return boolean
 */
function auth1_onLogin(WC_Challenge $chall, $username, $password)
{
        $db = auth1_db();
        
        $password = md5($password);
        
        $query = This one is the classic mysql injection challenge.
Your mission is easy: Login yourself as admin.
Again you are given the sourcecode, also as highlighted version.

Enjoy!

```php
<?php
/* TABLE STRUCTURE
CREATE TABLE IF NOT EXISTS users (
userid    INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
username  VARCHAR(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
password  CHAR(32) CHARACTER SET ascii COLLATE ascii_bin NOT NULL
) ENGINE=myISAM;
*/

# Username and Password sent?
if ( ('' !== ($username = Common::getPostString('username'))) && (false !== ($password = Common::getPostString('password', false))) ) {
	auth1_onLogin($chall, $username, $password);
}

/**
 * Get the database for this challenge.
 * @return GDO_Database
 */
function auth1_db()
{
	if (false === ($db = gdo_db_instance('localhost', WCC_AUTH_BYPASS1_USER, WCC_AUTH_BYPASS1_PASS, WCC_AUTH_BYPASS1_DB))) {
		die('Database error 0815_1!');
	}
	$db->setLogging(false);
	$db->setEMailOnError(false);
	return $db;
}

/**
 * Exploit this!
 * @param WC_Challenge $chall
 * @param unknown_type $username
 * @param unknown_type $password
 * @return boolean
 */
function auth1_onLogin(WC_Challenge $chall, $username, $password)
{
	$db = auth1_db();
	
	$password = md5($password);
	
	$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
	
	if (false === ($result = $db->queryFirst($query))) {
		echo GWF_HTML::error('Auth1', $chall->lang('err_unknown'), false); # Unknown user
		return false;
	}

	# Welcome back!
	echo GWF_HTML::message('Auth1', $chall->lang('msg_welcome_back', htmlspecialchars($result['username'])), false);
	
	# Challenge solved?
	if (strtolower($result['username']) === 'admin') {
		$chall->onChallengeSolved(GWF_Session::getUserID());
	}
	
	return true;
}
?>
<form action="index.php" method="post">
<table>
<tr>
	<td><?php echo $chall->lang('username'); ?>:</td>
	<td><input type="text" name="username" value="" /></td>
</tr>
<tr>
	<td><?php echo $chall->lang('password'); ?>:</td>
	<td><input type="password" name="password" value="" /></td>
</tr>
<tr>
	<td></td>
	<td><input type="submit" name="login" value="<?php echo $chall->lang('btn_login'); ?>" /></td>
</tr>
</table>
</form>
```
	直接找到验证 发现没有防止SQLI
	username输入 admin' AND 1=1;




####Training: Crypto - Transposition I

	错位，解密即可
```python
s='oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wa msmniaocam.d'
for i in range(0,len(s),2):
    print (s[i + 1] + s[i],end='')
#Wonderful. You can read the message way better when the letters are in correct order. I think you would like to see your password now: asmnmaicomad.
```




####Training: Register Globals
	这是一个全局变量注册，此处验证了login[0]是不是admin,在url后面添加?login[0]=admin即可
```php
if (isset($login))
{
        echo GWF_HTML::message('Register Globals', $chall->lang('msg_welcome_back', array(htmlspecialchars($login[0]), htmlspecialchars($login[1]))));
        if (strtolower($login[0]) === 'admin') {
                $chall->onChallengeSolved(GWF_Session::getUserID());
        }
}
```




- - -
























#Encodings


####Encodings: URL

	Your task is to decode the following:

	%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%61%72%63%62%73%68%73%6F%6D%67%6D%64%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21

	URL编码 直接转换

```python
import urllib
EncodedURL =  '%59%69%70%70%65%68%21%20%59%6F%75%72%20%55%52%4C%20%69%73%20%63%68%61%6C%6C%65%6E%67%65%2F%74%72%61%69%6E%69%6E%67%2F%65%6E%63%6F%64%69%6E%67%73%2F%75%72%6C%2F%73%61%77%5F%6C%6F%74%69%6F%6E%2E%70%68%70%3F%70%3D%61%72%63%62%73%68%73%6F%6D%67%6D%64%26%63%69%64%3D%35%32%23%70%61%73%73%77%6F%72%64%3D%66%69%62%72%65%5F%6F%70%74%69%63%73%20%56%65%72%79%20%77%65%6C%6C%20%64%6F%6E%65%21'
print urllib.unquote(EncodedURL).decode('utf-8','replace')
```




- - -



#Crypto


####Crypto - Caesar I

	As on most challenge sites, there are some beginner cryptos, and often you get started with the good old caesar cipher.
	I welcome you to the WeChall style of these training challenges :)

	Enjoy!

	KYV HLZTB SIFNE WFO ALDGJ FMVI KYV CRQP UFX FW TRVJRI REU PFLI LEZHLV JFCLKZFE ZJ CVSDZCEWJZXV

	提示是凯撒密码 猜测前面是THE 正确 移位为5 python输出

```python
KEY, CHARACTER_COUNT = 5, 26
str = "OCZ LPDXF WMJRI AJS EPHKN JQZM OCZ GVUT YJB JA XVZNVM VIY TJPM PIDLPZ NJGPODJI DN GZWHDGIANDBZ"
List = str.split(" ")
for character in List:
    for c in character:
        if c >= 'V':
            print (chr(ord(c)+KEY-CHARACTER_COUNT), end="")
        else:
            print (chr(ord(c)+KEY), end="")
    print (" ",end="")
```



- - -



#PHP

####PHP-0817

	I have written another include system for my dynamic webpages, but it seems to be vulnerable to LFI.
	Here is the code:
	GeSHi`ed PHP code

```php
<?php
if (isset($_GET['which']))
{
        $which = $_GET['which'];
        switch ($which)
        {
        case 0:
        case 1:
        case 2:
                require_once $which.'.php';
                break;
        default:
                echo GWF_HTML::error('PHP-0817', 'Hacker NoNoNo!', false);
                break;
        }
}
?>
```
	Your mission is to include solution.php.
	Here is the script in action: News, Forum, Guestbook.

	Good Luck!

	让访问solution.php
	直接在页面后面加参数 ?which=solution即可


- - -



#Stegano

####Stegano Attachment

	Hello challenger,

	You got mail and a nice attachment.
	Your unique solution which is bound to your session is in there too.

	Enjoy!

	下载文件 这是jpg和rar双文件头的文件(二进制合并) 直接改后缀名为.rar打开即可
	

- - -



#Others

####Prime Factory

	Your task is simple:
	Find the first two primes above 1 million, whose separate digit sums are also prime.
	As example take 23, which is a prime whose digit sum, 5, is also prime.
	The solution is the concatination of the two numbers,
	Example: If the first number is 1,234,567
	and the second is 8,765,432,
	your solution is 12345678765432

	找到符合规则的质数即可

```python
def isPrime(n):
    '''
    Is n a prime?
    '''
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        if i == 2:
            i += 1
        else:
            i += 2
    return True

def Sum(n):
    '''
    #calc the sum of digit number
    '''
    n_str = str(n)
    count = 0
    for t in n_str:
        count += ord(t)-ord('0')
    return count

for num in range(1000001,9999999,2):
    if isPrime(Sum(num)) and isPrime(num):
        print(num)
#10000331000037
```

####Zebra

	处理斑马身上的条形码得到answer
	The answer is saFFari
	

####hi (Math)
 	等差数列求和(17591026060782+2)*17591026060781/2，answer:154722098935564539692256152

- - -



#Warchall

####Warchall - Chapter I (Warchall begins)

	ssh登录,/home/level/0, solution0:bitwarrior
	/home/level/1 gray发现solution1:LameStartup
	第二关在隐藏文件中,solution2:HiddenIsConfig
	第3关看到了bash_history，solution3:RepeatingHistory
	第4-6关在home/user/USERNAME找，
	第4个在README.txt，需要改权限,
	solution4:AndIknowchown,
	第5关需要改level文件夹权限,然后等5mins,solution5:OhRightThePerms
	



- - -


#Tracks

####Tracks (HTTP)

	多次尝试cookie无果，本题大概分3步，注册，投票，不让投，在第二步的时候截获返回的Etag,修改后getflag，大概是HTTP缓存有关
