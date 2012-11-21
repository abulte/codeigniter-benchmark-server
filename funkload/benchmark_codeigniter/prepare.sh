#!/bin/sh

MYSQL_USER='root'
MYSQL_PASSWD='root'

# drop database
mysql -u $MYSQL_USER -p$MYSQL_PASSWD -e "DROP DATABASE IF EXISTS benchmark"
# recreate
mysql -u $MYSQL_USER -p$MYSQL_PASSWD -e "CREATE DATABASE benchmark"
# schema
mysql -u $MYSQL_USER -p$MYSQL_PASSWD benchmark -e "CREATE TABLE news (
     id int(11) NOT NULL AUTO_INCREMENT,
     title varchar(128) NOT NULL,
     slug varchar(128) NOT NULL,
     text text NOT NULL,
     PRIMARY KEY (id),
     KEY slug (slug) 
     );"

