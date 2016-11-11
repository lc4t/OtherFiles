<?php
session_start();
if (!$_SESSION['admin']) {
	return false;
}

require '../config.php';
require '../mysql.class.php';

$id = $_POST['id'];
$reply = $_POST['reply'];

//!(empty($id) || empty($reply)) <=> (!empty($id) && !empty($reply))
if (!(empty($id) || empty($reply))) {
	$id = DB::cleanSql($id);
	$reply = DB::cleanSql($reply);

	$reply_sql = 'UPDATE ' . GB_TABLE_NAME . 'SET reply = ' . $reply . 'WHERE id = ' . $id;
	$reply_status = mysql_query($delete_sql);

	if ($delete_status) {
		echo '{"error":0, "msg":"reply success"}';
	} else {
		echo '{"error":1, "msg":"reply error"}';
	}
} else {
	echo '{"error":1, "msg":"id or reply not null"}';
}
