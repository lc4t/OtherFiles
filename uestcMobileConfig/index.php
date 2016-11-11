<html>
<head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    <script src="//cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>
    <link rel="stylesheet" href="//cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">
    <script src="//cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
    <!--[if lt IE 9]>
    <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
    <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
</head>

<body>
<form role="form" action="uestc.php" method="post">
    <div class="form-group" >
        <lable for="username">username</lable>
        <input type="username" class="form-control" name="username" placeholder="201xxxxxxxxxx@local" style="width=11px">
    </div>

    <div class="form-group" >
        <label for="password">password</label>
        <input type="password" class="form-control" name="password" placeholder="PASSWORD" >
    </div>

    <button type="submit" class="btn btn-default">生成配置文件</button>
    <input type="reset" class="btn btn-reset" value="重置" id="reset">


</form>

</body>
</html>
