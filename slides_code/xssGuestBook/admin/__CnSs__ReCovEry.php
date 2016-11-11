<?php
session_start();
if (@!$_SESSION['admin']) 
{
    print "error";
    return false;
}


require '../config.php';
require '../mysql.class.php';



print 'delete';
$delete_sql = 'delete from guestbook where id>0';
$connect = mysql_connect(DB_HOST, DB_USER, DB_PWD);
$db = mysql_select_db(DB_NAME, $connect) or die ("error to database");
$query = mysql_query($delete_sql, $connect) or die("sql error");
header('location:_admin.php');
