-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: saba_database
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `sheets_info`
--

DROP TABLE IF EXISTS `sheets_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sheets_info` (
  `id` int NOT NULL AUTO_INCREMENT,
  `PLATE_ID` varchar(45) NOT NULL,
  `ORDER_ID` varchar(45) DEFAULT NULL,
  `HEAT_ID` varchar(45) DEFAULT NULL,
  `QC_STANDARD` varchar(45) DEFAULT NULL,
  `LENGHT` float DEFAULT NULL,
  `WIDTH` float DEFAULT NULL,
  `THICKNESS` float DEFAULT NULL,
  `LENGHT_ORDER` float DEFAULT NULL,
  `WIDTH_ORDER` float DEFAULT NULL,
  `THICKNESS_ORDER` float DEFAULT NULL,
  `user` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `main_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nframe` int DEFAULT '0',
  `cameras` varchar(45) DEFAULT '0-12',
  `image_format` varchar(10) DEFAULT '.png',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=72 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sheets_info`
--

LOCK TABLES `sheets_info` WRITE;
/*!40000 ALTER TABLE `sheets_info` DISABLE KEYS */;
INSERT INTO `sheets_info` VALUES (2,'14199ns','123456789','123456','ASTM450',6040,4200,25.23,6000,4200,25,'test','12:53:53','2023/07/23','oxin_image_grabber',97,'1-10','.png'),(63,'ABC12345A','123456789','123456','ASTM450',6040,5000,25.23,6000,5000,25,'test','12:53:53','2023/07/23','oxin_image_grabber',97,'1-12','.png'),(64,'AXK35508B','123456789','123456','ASTM450',6040,5000,25.23,6000,5000,25,'test','12:53:53','2023/07/23','oxin_image_grabber',71,'1-8','.png'),(65,'ABC12345A','123456789','123456','ASTM450',6040,2020,25.23,6000,2000,25,'root','16:44:40','2023/08/12','oxin_image_grabber',1,'1-12','.png'),(66,'ABC12345A','123456789','123456','ASTM450',6040,2020,25.23,6000,2000,25,'root','16:44:52','2023/08/12','oxin_image_grabber',1,'1-12','.png'),(67,'ABC12345A','123456789','123456','ASTM450',6040,2020,25.23,6000,2000,25,'root','16:45:04','2023/08/12','oxin_image_grabber',1,'1-12','.png'),(68,'ABC12345A','123456789','123456','ASTM450',6040,2020,25.23,6000,2000,25,'root','16:45:16','2023/08/12','oxin_image_grabber',1,'1-12','.png'),(69,'ABC12345A','123456789','123456','ASTM450',6040,2020,25.23,6000,2000,25,'root','16:45:28','2023/08/12','oxin_image_grabber',1,'1-12','.png'),(70,'2023-08-13_12-37-07','123456789','123456','ASTM450',6040,2020,25.23,6000,2000,25,'root','12:37:15','2023/08/13','oxin_image_grabber',1,'1-12','.png'),(71,'2023-08-13_12-37-19','123456789','123456','ASTM450',6040,2020,25.23,6000,2000,25,'root','12:37:27','2023/08/13','oxin_image_grabber',1,'1-12','.png');
/*!40000 ALTER TABLE `sheets_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-15 10:21:00
