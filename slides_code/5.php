<!DOCTYPE>
<html>
  <head>
    <title>
      sql test 5, union sqli
    </title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/bootstrap-theme.min.css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </head>

  <body>
  </body>
</html>



<?php
  if (@isset($_GET['id']))
  {
    $connect= mysql_connect("localhost","root","root");
    if (!$connect)
    {
      die('Could not connect: ' . mysql_error());
    }
    // one
    $sqlstr = "select content from news where id='" . $_GET['id'] . "';";
    $result = @mysql_db_query("data", $sqlstr, $connect);
    $row = @mysql_fetch_row($result);
    echo '<div class="col-sm-4 col-sm-offset-2">';
    if($row)
    {
      echo '<div class="alert alert-success" role="alert">success:'.$sqlstr.'</div>';
    }
    else
    {
      echo '<div class="alert alert-danger" role="alert">failed:'.$sqlstr.'</div>';
    }
    echo $row[0];
    mysql_close($connect);
  }
?>
