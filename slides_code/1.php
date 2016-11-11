<!DOCTYPE>
<html>
  <head>
    <title>
      sql test 1 ,no filter
    </title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="css/bootstrap-theme.min.css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
  </head>

  <body>
    <form class="form-horizontal" method="POST" action="/1.php">
      <div class="form-group center-block">
        <label for="user-input" class="col-sm-2 control-label">User</label>
        <div class="col-sm-4">
          <input type="text" name="username" class="form-control" id="user-input" placeholder="username">
        </div>
      </div>
      <div class="form-group center-block">
        <label for="pass-input" class="col-sm-2 control-label">Password</label>
        <div class="col-sm-4">
          <input type="password" name="password" class="form-control" id="pass-input" placeholder="Password">
        </div>
      </div>
      <div class="form-group center-block">
        <div class="col-sm-offset-2 col-sm-10">
          <button type="submit" class="btn btn-success">Sign in</button>
        </div>
      </div>
    </form>
  </body>
</html>



<?php
  if (@isset($_POST['username']) && @isset($_POST['password']))
  {
    $connect= mysql_connect("localhost","root","root");
    if (!$connect)
    {
      die('Could not connect: ' . mysql_error());
    }
    // one
    $sqlstr = "select 1 from users where username='" . $_POST['username'] . "' and password='".md5($_POST['password'])."';";
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
    mysql_close($connect);
  }
?>
