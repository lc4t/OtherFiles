<?php
$title = '留言本';
//ddmin Xsser@lc4t
?>
<html>
  <head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script src="js/jquery.min.js"></script>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <script src="js/bootstrap.js"></script>
      <!--[if lt IE 9]>
         <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
         <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
      <![endif]-->
  </head>

<body>
  <form role="form" action="post.php" method="POST">
    <div class="form-group" >
    <lable for="nickname">Name</lable>
    <input type="name" class="form-control" name="nickname" placeholder="Name" style="width=11px">
    </div>

    <div class="form-group" >
      <label for="email">Email address</label>
      <input type="email" class="form-control" name="email" placeholder="Email" >
    </div>

    <div class="form-group" >
      <label for="content">content</label>
      <input type="text" class="form-control" name="content" placeholder="Content" >
    </div>

    <button type="submit" class="btn btn-default">留言</button>
    <input type="reset" class="btn btn-reset" value="重置" id="reset">


  </form>

</body>
<? require 'common/footer.php'; ?>