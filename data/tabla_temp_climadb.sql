-- MariaDB dump 10.19  Distrib 10.6.4-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: climadb
-- ------------------------------------------------------
-- Server version	10.6.4-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tabla_temp`
--

DROP TABLE IF EXISTS `tabla_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tabla_temp` (
  `fecha` varchar(255) DEFAULT NULL,
  `temperatura` varchar(255) DEFAULT NULL,
  `temperaturaMinima` varchar(255) DEFAULT NULL,
  `temperaturaMaxima` varchar(255) DEFAULT NULL,
  `sensacionTermica` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tabla_temp`
--

/*!40000 ALTER TABLE `tabla_temp` DISABLE KEYS */;
INSERT INTO `tabla_temp` VALUES ('2021-11-04 03:00:00','18','18','18','19'),('2021-11-04 09:00:00','18','18','18','18'),('2021-11-04 15:00:00','24','24','24','24'),('2021-11-05 03:00:00','19','19','19','19'),('2021-11-05 09:00:00','18','18','18','18'),('2021-11-05 15:00:00','24','24','24','24'),('2021-11-05 21:00:00','24','24','24','25'),('2021-11-06 03:00:00','19','19','19','20'),('2021-11-06 09:00:00','19','19','19','19'),('2021-11-06 15:00:00','23','23','23','24'),('2021-11-06 21:00:00','22','22','22','23'),('2021-11-07 03:00:00','19','19','19','20'),('2021-11-07 09:00:00','18','18','18','19'),('2021-11-07 15:00:00','23','23','23','23'),('2021-11-07 21:00:00','25','25','25','25'),('2021-11-08 03:00:00','19','19','19','20'),('2021-11-08 09:00:00','18','18','18','19'),('2021-11-08 15:00:00','24','24','24','24');
/*!40000 ALTER TABLE `tabla_temp` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-04 11:17:39
