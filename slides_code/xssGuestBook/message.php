<?php
$title = '留言本';
require 'config.php';
require './common/header.php';
require 'mysql.class.php';

$gb_count_sql = 'SELECT count(*) FROM ' . GB_TABLE_NAME;

DB::connect();
$gb_count_res = mysql_query($gb_count_sql);
$gb_count = mysql_fetch_array($gb_count_res);
$gb_count = $gb_count[0];

$page = isset($_GET['page']) ? intval($_GET['page']) : 1;

$pagenum = ceil($gb_count / PER_PAGE_GB);
if ($page > $pagenum || $page < 0) {
    $page = 1;
}

// 限制搜索结果
$offset = ($page - 1) * PER_PAGE_GB;

$pagedata_sql = 'SELECT  nickname,content,createtime,reply,replytime FROM ' . GB_TABLE_NAME . ' WHERE status = 0 ORDER BY createtime DESC LIMIT ' . $offset . ',' . PER_PAGE_GB;

$sql_page_result = mysql_query($pagedata_sql);
while($temp = mysql_fetch_array($sql_page_result))
{
    $sql_page_array[] = $temp;
}
DB::close();
echo '<html><head>';
echo '<meta http-equiv="content-type" content="text/html;charset=utf-8">';
echo '<script src="js/jquery.min.js"></script>';
echo '<link href="css/bootstrap.min.css" rel="stylesheet">';
echo '<script src="js/bootstrap.js"></script>';
echo '</head>';
//循环输出数据库中满足条件id留言内容
if (!empty($sql_page_array))
{
    foreach($sql_page_array as $key => $value)
    {

        echo '<div class="panel panel-default">';
        echo '<div class="panel-heading">';
        echo '留言者：' . $value['nickname'] . ' ';

        // echo '时间：' . date('Y-m-d H:i:s', $value['createtime']);
        echo '</div>';
        echo '<div class="panel-body">';
        echo $value['content'];
        echo '</div>';
        echo '</div>';


    }
}






echo '共 '.$gb_count.'&nbsp;&nbsp;条留言  ';
echo '<nav>';
echo '  <ul class="pagination">';
//echo '    <li>';
//echo '      <a href="#" aria-label="Previous">';
//echo '        <span aria-hidden="true">&laquo;</span>';
//echo '      </a>';
//echo '    </li>';


if ($pagenum > 1) 
{   
    for($i = 1; $i <= $pagenum; $i++)
    {
        echo '<li>';
        echo '<a href="?page=' .$i .'">' . $i;
        echo '</a>';
        echo '</li>';
    }
}

//if ($pagenum > 1) 
//{
//    for($i = 1; $i <= $pagenum; $i++) {
//        if($i == $page) {
//            echo '&nbsp;&nbsp;['.$i.']';
//        } else {
//            echo '<li><a href="#">' .$i .'</a></li>';
//        }
//    }
//}

//echo '    <li>';
//echo '      <a href="#" aria-label="Next">';
//echo '        <span aria-hidden="true">&raquo;</span>';
//echo '      </a>';
//echo '    </li>';
echo '  </ul>';
echo '</nav>';

require 'common/footer.php';


