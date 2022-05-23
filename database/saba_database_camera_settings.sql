-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: saba_database
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `camera_settings`
--

DROP TABLE IF EXISTS `camera_settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `camera_settings` (
  `id` int NOT NULL,
  `gain_top` int NOT NULL DEFAULT '0',
  `gain_bottom` int NOT NULL DEFAULT '360',
  `gain_value` int NOT NULL DEFAULT '0',
  `expo_top` int NOT NULL DEFAULT '35',
  `expo_bottom` int NOT NULL DEFAULT '10000000',
  `expo_value` int NOT NULL DEFAULT '3000',
  `width` int NOT NULL DEFAULT '1920',
  `height` int NOT NULL DEFAULT '1200',
  `offsetx_top` int NOT NULL DEFAULT '16',
  `offsetx_bottom` int NOT NULL DEFAULT '0',
  `offsetx_value` int NOT NULL DEFAULT '0',
  `offsety_top` int NOT NULL DEFAULT '16',
  `offsety_bottom` int NOT NULL DEFAULT '0',
  `offsety_value` int NOT NULL DEFAULT '0',
  `interpacket_delay` int NOT NULL DEFAULT '0',
  `packet_size` int NOT NULL DEFAULT '0',
  `trigger_mode` tinyint NOT NULL DEFAULT '0',
  `max_buffer` int NOT NULL DEFAULT '0',
  `transmission_delay` int NOT NULL DEFAULT '0',
  `ip_address` varchar(45) NOT NULL,
  `rotation_value` float NOT NULL DEFAULT '0',
  `shifth_value` int NOT NULL DEFAULT '0',
  `shiftw_value` int NOT NULL DEFAULT '0',
  `serial_number` varchar(45) NOT NULL DEFAULT '0',
  `pxvalue_a` float NOT NULL DEFAULT '0',
  `pxvalue_b` float NOT NULL DEFAULT '0',
  `pxvalue_c` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `camera_settings`
--

LOCK TABLES `camera_settings` WRITE;
/*!40000 ALTER TABLE `camera_settings` DISABLE KEYS */;
INSERT INTO `camera_settings` VALUES (1,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'192.168.1.100',3.7,-39,2,'0',0,0,0),(2,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'192.168.1.2',0,0,0,'0',0,0,0),(3,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(4,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(5,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',2,21,50,'0',0,0,0),(6,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(7,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(8,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(9,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(10,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(11,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(12,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(13,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(14,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(15,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(16,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(17,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(18,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(19,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(20,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(21,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(22,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(23,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0),(24,0,360,0,35,10000000,500,1920,1200,16,0,0,16,0,0,10,10,0,10,10,'',0,0,0,'0',0,0,0);
/*!40000 ALTER TABLE `camera_settings` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-23  9:25:30
