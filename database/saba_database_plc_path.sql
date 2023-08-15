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
-- Table structure for table `plc_path`
--

DROP TABLE IF EXISTS `plc_path`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plc_path` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) NOT NULL,
  `path` varchar(500) NOT NULL DEFAULT '-',
  `value0` varchar(45) NOT NULL DEFAULT '-1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plc_path`
--

LOCK TABLES `plc_path` WRITE;
/*!40000 ALTER TABLE `plc_path` DISABLE KEYS */;
INSERT INTO `plc_path` VALUES (25,'ProjectorPulseTrig','ns=4;i=2','True'),(26,'NCamera','ns=4;i=3','2'),(27,'MemSoftwareStart','ns=4;i=4','False'),(28,'MemDownLimitSwitchIn','ns=4;i=5','False'),(29,'MemDownLimitSwitchOut','ns=4;i=6','False'),(30,'MemDownProjectorOnOff1','ns=4;i=7','False'),(31,'MemDownProjectorOnOff2','ns=4;i=8','False'),(32,'MemDownProjectorOnOff3','ns=4;i=9','False'),(33,'MemDownProjectorOnOff4','ns=4;i=10','False'),(34,'MemDownProjectorOnOff5','ns=4;i=11','False'),(35,'MemDownProjectorOnOff6','ns=4;i=12','False'),(36,'MemDownValve','ns=4;i=13','False'),(37,'DownTemperature','ns=4;i=23','134.55'),(38,'DownHighThreshold','ns=4;i=24','0.0'),(39,'DownLowThreshold','ns=4;i=25','0.0'),(40,'MemUpLimitSwitchIn','ns=4;i=26','False'),(41,'MemUpLimitSwitchOut','ns=4;i=27','False'),(42,'MemUpProjectorOnOff1','ns=4;i=28','False'),(43,'MemUpProjectorOnOff2','ns=4;i=29','False'),(44,'MemUpProjectorOnOff3','ns=4;i=30','False'),(45,'MemUpProjectorOnOff4','ns=4;i=31','False'),(46,'MemUpProjectorOnOff5','ns=4;i=32','False'),(47,'MemUpProjectorOnOff6','ns=4;i=33','False'),(48,'MemUpValve','ns=4;i=34','False'),(49,'UpTemperature','ns=4;i=35','27.6'),(50,'UpHighThreshold','ns=4;i=36','0.0'),(51,'UpLowThreshold','ns=4;i=37','0.0'),(52,'MemDistanceSensor','ns=4;i=38','False');
/*!40000 ALTER TABLE `plc_path` ENABLE KEYS */;
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
