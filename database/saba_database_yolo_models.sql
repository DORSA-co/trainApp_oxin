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
-- Table structure for table `yolo_models`
--

DROP TABLE IF EXISTS `yolo_models`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `yolo_models` (
  `id` int NOT NULL AUTO_INCREMENT,
  `algo_name` varchar(45) NOT NULL DEFAULT '1',
  `input_size` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '(224,224)',
  `input_type` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'resized',
  `epochs` int NOT NULL DEFAULT '10',
  `batch_size` int NOT NULL DEFAULT '4',
  `split_ratio` float NOT NULL DEFAULT '0.2',
  `dataset_pathes` varchar(2000) NOT NULL DEFAULT 'null',
  `weights_path` varchar(2000) NOT NULL DEFAULT 'default_datasetweightsyoloyolov5s.pt',
  `lr` float NOT NULL DEFAULT '0.001',
  `date_` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT '0000/00/00',
  `classes` varchar(200) NOT NULL DEFAULT ',4,2,1',
  `box_loss` float NOT NULL DEFAULT '0.01',
  `obj_loss` float NOT NULL DEFAULT '0.01',
  `cls_loss` float NOT NULL DEFAULT '0.01',
  `val_precision` float NOT NULL DEFAULT '0.01',
  `val_recall` float NOT NULL DEFAULT '0.01',
  `val_mAP_0.5` float NOT NULL DEFAULT '0.01',
  `val_mAP_0.5:0.95` float NOT NULL DEFAULT '0.01',
  `val_box_loss` float NOT NULL DEFAULT '0.01',
  `val_obj_loss` float NOT NULL DEFAULT '0.01',
  `val_cls_loss` float NOT NULL DEFAULT '0.01',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `yolo_models`
--

LOCK TABLES `yolo_models` WRITE;
/*!40000 ALTER TABLE `yolo_models` DISABLE KEYS */;
INSERT INTO `yolo_models` VALUES (1,'1','(224,224)','splited',10,1,0.2,'\'default_dataset\'','default_dataset/weights/yolo/yolov5s.pt',0.001,'\'2/4/1300\'',',2,5,6,',0.01,0.01,0.01,70,70,70,70,0.02,0.02,0.02),(2,'4','(224,224)','splited',10,1,0.2,'\'default_dataset\'','default_dataset/weights/yolo/yolov5x.pt',0.001,'\'2/4/1300\'',',2,5,6,',0.01,0.01,0.01,70,70,70,70,0.02,0.02,0.02);
/*!40000 ALTER TABLE `yolo_models` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-15 10:20:59
