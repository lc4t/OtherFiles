drop database if exists `xsser`;
CREATE DATABASE xsser DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
CREATE USER 'xss'@'localhost' IDENTIFIED BY 'xss@lc4t';
CREATE USER 'xss'@'127.0.0.1' IDENTIFIED BY 'xss@lc4t';
GRANT ALL ON xsser.* TO 'xss'@'127.0.0.1';
GRANT ALL ON xsser.* TO 'xss'@'localhost';
use xsser;
CREATE TABLE `guestbook` (
  `id` int(10) unsigned PRIMARY KEY AUTO_INCREMENT,
  `nickname` char(16) NOT NULL DEFAULT '',
  `email` varchar(60) DEFAULT NULL,
  `content` text NOT NULL,
  `createtime` int(10) unsigned NOT NULL DEFAULT '0',
  `reply` text DEFAULT NULL,
  `replytime` int(10) unsigned DEFAULT NULL,
  `status` tinyint(1) unsigned DEFAULT '0'
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;
CREATE TABLE User(
  `uid` INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `nickname` varchar(30) NOT NULL,
  `password` varchar(32) NOT NULL,
  `createtime` INT(10) unsigned NOT NULL,
  `level` TINYINT(1) unsigned DEFAULT '0'
)ENGINE=MyISAM CHARSET=utf8 AUTO_INCREMENT=1;
use xsser;
insert into User(nickname, password, createtime, level) values( 'admin', '21232f297a57a5a743894a0e4a801fc3', 1423018916, 9);
