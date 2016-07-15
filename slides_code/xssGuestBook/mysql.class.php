<?php
/**
*
*/
require 'config.php';
class DB {
	static $_connect = null;

	static function connect() {
		if (!self::$_connect) {
			$conn = mysql_connect(DB_HOST, DB_USER, DB_PWD);
			if ($conn) {
				mysql_select_db(DB_NAME, $conn);
				mysql_query("set names 'utf8'");	
				self::$_connect = $conn;
			} else {
				exit('database error');
			}
		}

		return self::$_connect;
	}

	static function cleanSql($sql) 
    {
		//$sql = mysql_real_escape_string($sql);
        //$sql = preg_replace("/\\/si",'.',$sql);
        // $sql = preg_replace("/script/si",'.',$sql);
        // $sql = preg_replace('/img/si','.',$sql);
        // $sql = preg_replace('/style/si','.',$sql);
        // $sql = preg_replace('/link/si','.',$sql);

        // $sql = preg_replace('/>/','.',$sql);
        // $sql = preg_replace('/open/si','.',$sql);
        // $sql = preg_replace('/&/si','.',$sql);
        // $sql = preg_replace('/#/si','.',$sql);
        // $sql = preg_replace('/java/si','.',$sql);
        // $sql = preg_replace('/%/si','.',$sql);
        // $sql = preg_replace('/\'/si','.',$sql);
        // $sql = preg_replace('/src/si','.',$sql);
        // $sql = preg_replace('/\[\]/si','.',$sql);
        // $sql = preg_replace('/_/si','.',$sql);

		return $sql;
	}

	static function close() {
		if (self::$_connect) {
			mysql_close(self::$_connect);
		}
	}
}


