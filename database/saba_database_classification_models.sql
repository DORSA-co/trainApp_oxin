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
-- Table structure for table `classification_models`
--

DROP TABLE IF EXISTS `classification_models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `classification_models` (
  `id` int NOT NULL AUTO_INCREMENT,
  `algo_name` varchar(45) NOT NULL DEFAULT '0',
  `input_size` varchar(45) NOT NULL DEFAULT '(100,100)',
  `input_type` varchar(45) NOT NULL DEFAULT '0',
  `epochs` int NOT NULL DEFAULT '10',
  `batch_size` int NOT NULL DEFAULT '8',
  `lr` float NOT NULL DEFAULT '0.001',
  `split_ratio` float NOT NULL DEFAULT '0.25',
  `classes` varchar(100) NOT NULL,
  `loss` float NOT NULL DEFAULT '0',
  `accuracy` float NOT NULL DEFAULT '0',
  `precision_` float NOT NULL DEFAULT '0',
  `recall` float NOT NULL DEFAULT '0',
  `val_loss` float NOT NULL DEFAULT '0',
  `val_accuracy` float NOT NULL DEFAULT '0',
  `val_precision` float NOT NULL DEFAULT '0',
  `val_recall` float NOT NULL DEFAULT '0',
  `dataset_pathes` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'path',
  `weights_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'path',
  `date_` varchar(45) NOT NULL DEFAULT '01/01/1401',
  `pretrain_path` varchar(1000) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classification_models`
--

LOCK TABLES `classification_models` WRITE;
/*!40000 ALTER TABLE `classification_models` DISABLE KEYS */;
INSERT INTO `classification_models` VALUES (1,'1','(224,224)','splited',50,32,0.001,0.2,',4,2,1,8,',0.8,34,78,45,1,12,34,10,'[\'default_dataset/binary\']','default_dataset/weights/classification/multiclassmodel.h5','1401/11/01','default_dataset/weights/classification/1401-11-01-10-04-55'),(106,'0','(224,224)','splited',30,16,0.01,0.2,',4,2,1,',0.013,45,45,23,0.9,45,24,22,'[\'default_dataset/binary\', \'/home/reyhene/Desktop\', \'/home/reyhane/Dorsa\', \'/home/reyhane/pythonProjects/ trainApp_oxin_new\']','default_dataset/weights/classification/1401-10-22-07-48-06','1401/10/22','default_dataset/weights/classifiction/1401-10-22-08-45-33');
/*!40000 ALTER TABLE `classification_models` ENABLE KEYS */;
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
