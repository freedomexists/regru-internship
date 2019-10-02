mysql -p
CREATE DATABASE day9;
USE day9;
SET sql_mode = '';
CREATE TABLE table_task1
(
service_id INT NOT NULL AUTO_INCREMENT,
servtype VARCHAR(20) DEFAULT 'hosting' NOT NULL,
subtype VARCHAR(32) DEFAULT '' NOT NULL,
user_id BIGINT(10) NOT NULL,
referrer_user_id INT(9) NOT NULL,
state ENUM('N','A','S','D','O') DEFAULT 'N',
creation_date DATE NOT NULL DEFAULT '0000-00-00',
creation_time TIME NOT NULL DEFAULT '00:00:00',
creation_request_sent_date DATETIME,
notified_about_expiration TINYINT DEFAULT 0,
PRIMARY KEY (service_id)
)
CHARACTER SET utf8 COLLATE utf8_unicode_ci;
DESCRIBE table_task1;
INSERT INTO table_task1
(servtype, subtype, user_id, referrer_user_id,
state, creation_date, creation_time, creation_request_sent_date,
notified_about_expiration)
VALUES
('srv_license_isp', 'lite5', 664082, 664082, 'S', '2018-02-12', '8:29:22', '2012-07-12 12:40', 55),
('srv_vps', 'SSD-VPS-2-0317', 664082, 664082, 'D', '2018-02-12', '8:31:24', NULL, -3),
('srv_websitebuilder', 'start', 208949,	26532, 'A', '2018-02-11', '21:51:38', '2010-03-12 11:25', 0),
('srv_google_apps', 'trial', 382636, 393221, 'D', '2017-11-03', '9:02:42', NULL, 1),
('srv_license_isp',	'lite5', 45532,	26532, 'O',	'2017-08-18', '16:04:41', NULL,	0)
;
SELECT * FROM table_task1;
DELETE FROM table_task1 WHERE service_id = 2;
UPDATE table_task1 SET servtype = 'радоваться жизни' WHERE service_id = 1;
exit
$ mysqldump -uroot -p day9 table_task1 > table_task1.sql
mysql -p
USE day9;
DROP TABLE mysql table_task1;
DROP DATABASE day9;
CREATE DATABASE day9;
source /some_path/day9/task1/table_task1.sql;
SELECT * FROM table_task1\G
