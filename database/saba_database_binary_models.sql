-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: saba_database
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `binary_models`
--

DROP TABLE IF EXISTS `binary_models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `binary_models` (
  `id` int NOT NULL AUTO_INCREMENT,
  `algo_name` int NOT NULL DEFAULT '-1',
  `input_size` varchar(45) NOT NULL DEFAULT '(100,100)',
  `input_type` varchar(45) NOT NULL DEFAULT 'null',
  `epochs` int NOT NULL DEFAULT '2',
  `batch_size` int NOT NULL DEFAULT '8',
  `lr` float NOT NULL DEFAULT '0',
  `tuning_epochs` int NOT NULL DEFAULT '1',
  `split_ratio` float NOT NULL DEFAULT '25',
  `loss` float NOT NULL DEFAULT '0',
  `accuracy` float NOT NULL DEFAULT '0',
  `precision_` float NOT NULL DEFAULT '0',
  `recall` float NOT NULL DEFAULT '0',
  `val_loss` float NOT NULL DEFAULT '0',
  `val_accuracy` float NOT NULL DEFAULT '0',
  `val_precision` float NOT NULL DEFAULT '0',
  `val_recall` float NOT NULL DEFAULT '0',
  `dataset_pathes` varchar(45) NOT NULL DEFAULT 'null',
  `weights_path` varchar(45) NOT NULL DEFAULT 'null',
  `date_` varchar(45) NOT NULL DEFAULT 'null',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `binary_models`
--

LOCK TABLES `binary_models` WRITE;
/*!40000 ALTER TABLE `binary_models` DISABLE KEYS */;
INSERT INTO `binary_models` VALUES (1,0,'(100,100)','resize',10,8,0,3,25,10,94,90,89,11,90,90,88,'dataset\\binary','weights','7/2/1401'),(3,0,'(100,100)','1',10,8,0,1,0,0,0,0,0,0,0,0,0,'null','null','null'),(4,0,'(100,100)','1',10,8,0,1,0,0,0,0,0,0,0,0,0,'[\'dataset\\\\binary\']','weights\\binary','24/02/1401'),(5,0,'(100,100)','1',10,8,0,1,0,0,0,0,0,0,0,0,0,'[\'dataset\\\\binary\']','weights\\binary','24/02/1401'),(6,0,'(100,100)','1',10,8,0,1,0,0,0,0,0,0,0,0,0,'[\'dataset\\\\binary\']','weights\\binary\\24-2-1401-12-37-9','24/01/1401'),(7,0,'(100,100)','1',4,8,0,2,0,0,0,0,0,0,0,0,0,'[\'dataset\\\\binary\']','weights\\binary\\24-2-1401-12-56-4','24/02/1401'),(8,0,'(100,100)','1',10,8,0.001,5,0.25,0,0,0,0,0,0,0,0,'[\'dataset\\\\binary\']','weights\\binary\\24-2-1401-13-1-42','24/02/1401'),(9,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(10,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(11,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(12,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(13,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(14,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(15,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(16,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(17,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(18,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(19,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(20,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(21,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(22,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(23,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(24,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(25,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(26,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(27,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(28,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(29,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(30,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(31,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(32,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(33,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(34,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(35,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(36,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(37,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(38,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(39,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(40,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(41,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(42,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(43,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(44,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(45,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(46,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(47,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(48,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(49,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(50,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(51,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(52,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(53,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(54,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(55,0,'(100,100)','null',2,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(56,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(57,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(58,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(59,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(60,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(61,0,'(100,100)','null',10,8,0,1,25,0,0,0,0,0,0,0,0,'null','null','null'),(62,0,'(100,100)','1',12,8,0.001,1,0.2,0,1,1,1,0,1,1,1,'[\'dataset\\\\binary\']','weights\\binary\\1-3-1401-16-27-27','01/03/1401'),(63,1,'(100,100)','1',12,8,0.001,1,0.2,0,1,1,1,0,1,1,1,'[\'dataset\\\\binary\']','weights\\binary\\1-3-1401-16-34-17','01/03/1401'),(64,0,'(100,100)','1',3,8,0.001,1,0.2,0,1,1,1,0,1,1,1,'[\'dataset\\\\binary\']','weights\\binary\\1-3-1401-17-20-36','01/03/1401');
/*!40000 ALTER TABLE `binary_models` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-23 13:10:13
