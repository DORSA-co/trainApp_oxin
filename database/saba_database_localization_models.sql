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
-- Table structure for table `localization_models`
--

DROP TABLE IF EXISTS `localization_models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `localization_models` (
  `id` int NOT NULL AUTO_INCREMENT,
  `algo_name` varchar(45) NOT NULL DEFAULT '0',
  `pretrain_path` varchar(2000) NOT NULL,
  `input_size` varchar(45) NOT NULL DEFAULT '(100,100)',
  `input_type` varchar(45) NOT NULL DEFAULT '0',
  `epochs` int NOT NULL DEFAULT '10',
  `batch_size` int NOT NULL DEFAULT '8',
  `lr` float NOT NULL DEFAULT '0.001',
  `split_ratio` float NOT NULL DEFAULT '0.25',
  `loss` float NOT NULL DEFAULT '0',
  `accuracy` float NOT NULL DEFAULT '0',
  `iou` float NOT NULL DEFAULT '0',
  `fscore` float NOT NULL DEFAULT '0',
  `val_loss` float NOT NULL DEFAULT '0',
  `val_accuracy` float NOT NULL DEFAULT '0',
  `val_iou` float NOT NULL DEFAULT '0',
  `val_fscore` float NOT NULL DEFAULT '0',
  `dataset_pathes` varchar(100) NOT NULL DEFAULT 'path',
  `weights_path` varchar(100) NOT NULL DEFAULT 'path',
  `date_` varchar(45) NOT NULL DEFAULT '01/01/1401',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `localization_models`
--

LOCK TABLES `localization_models` WRITE;
/*!40000 ALTER TABLE `localization_models` DISABLE KEYS */;
INSERT INTO `localization_models` VALUES (10,'0','','(224,224)','1',2,1,0.001,0.2,0.764264,0.586955,0.310854,0.449099,1.02973,0.968658,0.000303313,0.000606067,'[\'default_dataset/localization\']','default_dataset/weights/localization/low_unet.h5','2023/02/18'),(11,'0','','(256,256)','1',5,2,0.01,0.5,0.787259,0.510691,0.134556,0.210921,1.77183,0.808456,0.000000000424284,0.000000000424284,'[\'default_dataset/localization\']','default_dataset/weights/localization/2023-02-19-10-08-30','2023/02/19'),(12,'0','','(256,256)','1',10,1,0.001,0.2,0.857866,0.486687,0.205579,0.295589,2.08094,0.726761,0.00303876,0.00604947,'[\'default_dataset/localization\']','default_dataset/weights/localization/2023-02-19-15-49-51','2023/02/19'),(13,'0','','(256,256)','1',2,2,0.001,0.2,0.838796,0.590189,0.150817,0.249161,1.43944,0.716334,0.00218703,0.00436151,'[\'default_dataset/localization\']','default_dataset/weights/localization/2023-02-19-23-38-44','2023/02/19'),(14,'1','/home/reyhane/PythonProjects/trainApp_oxin_new/default_dataset/weights/localization/2023-02-19-23-36-05/localization_model.h5','(256,256)','1',2,1,0.001,0.2,0.809231,0.760735,0.0718374,0.102411,2.04686,0.745753,0.00174496,0.00347174,'[\'default_dataset/localization\']','default_dataset/weights/localization/2023-02-19-23-40-50','2023/02/19');
/*!40000 ALTER TABLE `localization_models` ENABLE KEYS */;
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
