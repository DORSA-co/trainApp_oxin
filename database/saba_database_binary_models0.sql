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
  `dataset_pathes` varchar(45) NOT NULL DEFAULT 'null',
  `accuracy` int NOT NULL DEFAULT '0',
  `loss` int NOT NULL DEFAULT '0',
  `precision_` int NOT NULL DEFAULT '0',
  `recall` int NOT NULL DEFAULT '0',
  `val_loss` int NOT NULL DEFAULT '0',
  `val_accuracy` int NOT NULL DEFAULT '0',
  `val_precision` int NOT NULL DEFAULT '0',
  `val_recall` int NOT NULL DEFAULT '0',
  `weights_path` varchar(45) NOT NULL DEFAULT 'null',
  `date_` varchar(45) NOT NULL DEFAULT '0000/00/00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=62 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `binary_models`
--

LOCK TABLES `binary_models` WRITE;
/*!40000 ALTER TABLE `binary_models` DISABLE KEYS */;
INSERT INTO `binary_models` VALUES (1,0,'(100,100)','resize',10,8,0,3,25,'dataset\\binary',94,10,90,89,11,90,90,88,'weights','1401/01/01'),(4,0,'(100,100)','1',10,8,0,1,0,'[\'dataset\\\\binary\']',0,0,0,0,0,0,0,0,'weights\\binary','1401/01/01'),(5,0,'(100,100)','1',10,8,0,1,0,'[\'dataset\\\\binary\']',0,0,0,0,0,0,0,0,'weights\\binary','1402/01/01'),(6,0,'(100,100)','1',10,8,0,1,0,'[\'dataset\\\\binary\']',0,0,0,0,0,0,0,0,'weights\\binary\\24-2-1401-12-37-9','1402/02/01'),(7,0,'(100,100)','1',4,8,0,2,0,'[\'dataset\\\\binary\']',0,0,0,0,0,0,0,0,'weights\\binary\\24-2-1401-12-56-4','1402/02/02'),(8,0,'(100,100)','1',10,8,0.001,5,0.25,'[\'dataset\\\\binary\']',0,0,0,0,0,0,0,0,'weights\\binary\\24-2-1401-13-1-42','1400/01/01');
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

-- Dump completed on 2022-08-03 15:07:06
