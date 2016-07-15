 <?php
require 'config.php';
require 'mysql.class.php';
header("Content-Type: text/html;charset=utf-8");
DB::connect();
$author = DB::cleanSql($_POST['nickname']);
$content = DB::cleanSql($_POST['content']);
$email = DB::cleanSql($_POST['email']);
$create_time = time();

$sql_insert = 'insert into ' . GB_TABLE_NAME . '(nickname, content, createtime, email) values( ' . "'{$author}', '{$content}', {$create_time}, '{$email}')";


$insert_status = mysql_query($sql_insert);
DB::close();

if($insert_status) {
//	redirect to the index page
	header('location:message.php');
} else{
	echo '抱歉，留言失败！';
	echo '<a href='.'index.php>'.'首页</a>';	
}

?>
