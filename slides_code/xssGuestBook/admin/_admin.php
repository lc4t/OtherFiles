<?php

session_start();
// if (@!$_SESSION['admin']) {
// 	header('location:_index.html');
// }

setcookie('flag','CNSS{what_do_you_think_of_xss}');

$title = '留言本';

require '../config.php';
require '../common/admin_header.php';
require '../mysql.class.php';

$gb_count_sql = 'SELECT count(*) FROM ' . GB_TABLE_NAME;
//connect db
DB::connect();
$gb_count_res = mysql_query($gb_count_sql);
$gb_count = mysql_fetch_array($gb_count_res);
$gb_count = $gb_count[0];
$page = isset($_GET['page']) ? intval($_GET['page']) : 1;
//计算留言数，得出分页数
$pagenum = ceil($gb_count / PER_PAGE_GB);
if ($page > $pagenum || $page < 0) {
	$page = 1;
}
// 限制搜索结果
$offset = ($page - 1) * PER_PAGE_GB;

$pagedata_sql = 'SELECT id,nickname,content,email,createtime,reply,replytime FROM ' . GB_TABLE_NAME . ' ORDER BY createtime DESC LIMIT ' . $offset . ',' . PER_PAGE_GB;
$sql_page_result = mysql_query($pagedata_sql);
while($temp = mysql_fetch_array($sql_page_result)) {
	$sql_page_array[] = $temp;
}
DB::close();


if (!empty($sql_page_array))
{
    foreach($sql_page_array as $key => $value) {
        echo '<br /><div>';
        echo '<form action="delete.php" method="post">';
        echo '<input type="hidden" name="id"  value="' . $value['id'] . '" />';
        echo '留言者：'. $value['nickname'].'|';
        echo 'E-MAIL:' . $value['email'] . '<br />';
        echo '内容:' . $value['content'] . '<br />';

        // echo '时间：' . date('Y-m-d H:i:s', $value['createtime']) .'<br />';

        echo '<input type="submit" name="delete" value="delete"/></div>';
        echo '</form><hr />';
    }
}


echo '共 '.$gb_count.'&nbsp;&nbsp;条留言  ';
if ($pagenum > 1) {
	for($i = 1; $i <= $pagenum; $i++) {
		if($i == $page) {
			echo '&nbsp;&nbsp;['.$i.']';
		} else {
			echo '<a href="?page='. $i .'">&nbsp;' . $i . '&nbsp;</a>';
		}
	}
}

?>

<script src="../js/admin.js"></script>
<?php require '../common/footer.php';?>
