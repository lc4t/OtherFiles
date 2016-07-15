 <?php
require '../config.php';
require '../mysql.class.php';
DB::connect();
$user = DB::cleanSql($_POST['uname']);
$pwd = DB::cleanSql($_POST['password']);

print  $_POST['uname'].$_POST['password'];

$sql_login = 'SELECT password FROM ' . ADMIN_TABLE_NAME . ' WHERE level=9 AND nickname = '. "'{$user}'" . ' LIMIT 1';


$insert_status = mysql_query($sql_login);
$password = mysql_fetch_array($insert_status);
$password = $password[0];
DB::close();

if ($user === "ddmin" && md5($pwd) === $password) {
	//save to session
	session_start();
	$_SESSION['admin'] = true;
	header('location:_admin.php');
} else {
	header('location:_index.html');
}

/**end of file**/