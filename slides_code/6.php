<!DOCTYPE>
<html>
  <head>
    <title>
      sql test 6, stack sqli
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

    $dbms = 'mysql';
    $dbName = 'data';
    $user = 'root';
    $pwd = 'root';
    $host = 'localhost';
    $dsn = "$dbms:host=$host;port=3306;dbname=$dbName";

    $pdo = new PDO($dsn,$user,$pwd);
    $sqlstr = "select content from news where id='" . $_GET['id'] . "';";
    $query = @$pdo->query($sqlstr);
    @$query->setFetchMode(PDO::FETCH_ASSOC);
    $ans = $query->fetchAll();
    print_r($ans);
    echo '<div class="col-sm-4 col-sm-offset-2">';
    if($ans)
    {
      echo '<div class="alert alert-success" role="alert">success:'.$sqlstr.'</div>';

    }
    else
    {
      echo '<div class="alert alert-danger" role="alert">failed:'.$sqlstr.'</div>';

    }


  }
?>
