-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: day9
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `table_task1`
--

DROP TABLE IF EXISTS `table_task1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `table_task1` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `servtype` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'hosting',
  `subtype` varchar(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
  `user_id` bigint(10) NOT NULL,
  `referrer_user_id` int(9) NOT NULL,
  `state` enum('N','A','S','D','O') COLLATE utf8_unicode_ci DEFAULT 'N',
  `creation_date` date NOT NULL DEFAULT '0000-00-00',
  `creation_time` time NOT NULL DEFAULT '00:00:00',
  `creation_request_sent_date` datetime DEFAULT NULL,
  `notified_about_expiration` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`service_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table_task1`
--

LOCK TABLES `table_task1` WRITE;
/*!40000 ALTER TABLE `table_task1` DISABLE KEYS */;
INSERT INTO `table_task1` VALUES (1,'радоваться жизни','lite5',664082,664082,'S','2018-02-12','08:29:22','2012-07-12 12:40:00',55),(3,'srv_websitebuilder','start',208949,26532,'A','2018-02-11','21:51:38','2010-03-12 11:25:00',0),(4,'srv_google_apps','trial',382636,393221,'D','2017-11-03','09:02:42',NULL,1),(5,'srv_license_isp','lite5',45532,26532,'O','2017-08-18','16:04:41',NULL,0);
/*!40000 ALTER TABLE `table_task1` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-03 11:07:16
