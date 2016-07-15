CREATE DATABASE data;
use data;
CREATE TABLE users(username varchar(255), password varchar(255), admin int(2));
CREATE TABLE news(id varchar(255), content text);
insert into users values('admin', '21232f297a57a5a743894a0e4a801fc3', 1);
insert into news values('1', 'this is content 1');
insert into news values('2', 'this is content 2');
insert into news values('3', 'this is content 3');
