<?php

error_reporting(0);
error_reporting(E_ALL^E_NOTICE);
define('DEBUG', 'false');
define('DB_HOST', 'localhost');
define('DB_USER', 'xss');
define('DB_PWD', 'xss@lc4t');
define('DB_NAME', 'xsser');
define('GB_TABLE_NAME', 'guestbook');
define('ADMIN_TABLE_NAME', 'User');
define('PER_PAGE_GB', 5);

if (DEBUG) {
	ini_set("display_errors", 1);
	error_reporting(E_ALL);
}
/**end of file**/