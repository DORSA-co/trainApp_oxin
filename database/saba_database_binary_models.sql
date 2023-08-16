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
  `tuning_epochs` int NOT NULL DEFAULT '1',
  `batch_size` int NOT NULL DEFAULT '8',
  `lr` float NOT NULL DEFAULT '0',
  `split_ratio` float NOT NULL DEFAULT '25',
  `dataset_pathes` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `weights_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `date_` varchar(45) NOT NULL DEFAULT '0000/00/00',
  `accuracy` int NOT NULL DEFAULT '0',
  `loss` int NOT NULL DEFAULT '0',
  `precision_` int NOT NULL DEFAULT '0',
  `recall` int NOT NULL DEFAULT '0',
  `val_loss` int NOT NULL DEFAULT '0',
  `val_accuracy` int NOT NULL DEFAULT '0',
  `val_precision` int NOT NULL DEFAULT '0',
  `val_recall` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=134 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `binary_models`
--

LOCK TABLES `binary_models` WRITE;
/*!40000 ALTER TABLE `binary_models` DISABLE KEYS */;
INSERT INTO `binary_models` VALUES (85,1,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\', \'/home/reyhene/Desktop\', \'/home/reyhane/Dorsa\', \'/home/reyhane/pythonProjects/ trainApp_oxin_new\']','default_dataset/weights/binary/binarymodeltemp.h5','1401/10/22',1,0,0,0,0,1,0,0),(86,0,'(300,300)','splited',12,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-10-22-07-48-06','1401/10/22',1,0,1,0,0,1,0,0),(87,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-10-22-07-48-06','1401/10/22',1,0,0,0,0,1,0,0),(88,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-10-22-08-26-39','1401/10/22',1,0,1,0,0,1,0,0),(89,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-10-22-08-28-28','1401/10/22',1,0,0,0,0,1,0,0),(90,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-10-22-08-37-07','1401/10/22',1,0,1,0,0,1,0,0),(91,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-10-22-08-45-33','1401/10/22',1,0,0,0,0,1,0,0),(92,0,'(300,300)','splited',12,1,8,0.001,0.2,'[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']','default_dataset/weights/binary/1401-10-22-08-46-36','1401/10/22',1,0,1,0,0,1,0,0),(93,0,'(300,300)','splited',15,1,8,0.001,0.2,'[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']','default_dataset/weights/binary/1401-10-22-09-05-04','1401/10/22',1,0,1,0,0,1,0,0),(94,0,'(300,300)','splited',15,1,8,0.001,0.2,'[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']','default_dataset/weights/binary/1401-10-22-09-08-11','1401/10/22',1,0,1,0,0,1,0,0),(95,0,'(100,100)','splited',4,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-10-26-11-21-47','1401/10/26',1,0,1,0,0,1,0,0),(96,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-10-04-55','1401/11/01',1,0,1,0,0,1,0,0),(97,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-10-46-18','1401/11/01',1,0,0,0,0,1,0,0),(98,0,'(300,300)','splited',2,1,8,0.002,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-11-07-04','1401/11/01',1,0,1,0,0,1,0,0),(99,0,'(300,300)','splited',2,1,8,0,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-11-08-53','1401/11/01',0,0,0,1,0,0,0,0),(100,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-14-31-19','1401/11/01',1,0,1,0,0,1,0,0),(101,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-15-23-57','1401/11/01',1,0,1,0,0,1,0,0),(102,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-16-35-53','1401/11/01',1,0,1,0,0,1,0,0),(103,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-17-04-49','1401/11/01',1,0,0,0,0,1,0,0),(104,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-17-13-35','1401/11/01',1,0,1,0,0,1,0,0),(105,0,'(300,300)','splited',20,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-01-17-14-10','1401/11/01',1,0,0,0,0,1,0,0),(106,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-06-14-52-06','1401/11/06',1,0,1,0,0,1,0,0),(107,0,'(300,300)','splited',15,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-06-14-52-54','1401/11/06',1,0,0,0,0,1,0,0),(108,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-06-15-04-05','1401/11/06',0,0,0,0,0,0,0,0),(109,0,'(300,300)','splited',15,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-06-15-04-26','1401/11/06',1,0,1,1,0,1,1,1),(110,0,'(100,100)','splited',15,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-06-15-05-18','1401/11/06',1,0,1,0,0,0,0,1),(111,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-14-15-46-40','1401/11/14',1,0,0,0,0,1,0,0),(112,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/1401-11-16-19-05-51','1401/11/16',1,0,0,0,0,1,0,0),(113,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-10-15-02-25','2023/02/10',1,0,0,0,0,1,0,0),(114,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-14-19-20-28','2023/02/14',1,0,1,0,0,1,0,0),(115,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-14-19-24-38','2023/02/14',1,0,1,0,0,1,0,0),(116,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-14-20-34-49','2023/02/14',1,0,1,0,0,1,0,0),(117,0,'(300,300)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-14-22-33-26','2023/02/14',1,0,1,1,0,1,0,0),(118,0,'(256,256)','splited',2,1,4,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-17-36-12','2023/02/15',1,0,1,0,0,1,0,0),(119,0,'(256,256)','splited',20,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-18-40-00','2023/02/15',1,0,0,1,0,1,0,0),(120,0,'(256,256)','splited',20,1,4,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-18-54-59','2023/02/15',1,0,1,0,0,1,0,0),(121,0,'(256,256)','splited',20,1,1,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-19-09-21','2023/02/15',1,0,0,0,0,1,0,0),(122,0,'(256,256)','splited',20,1,1,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-19-11-02','2023/02/15',1,0,0,0,0,1,0,0),(123,0,'(256,256)','splited',20,1,1,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-21-13-49','2023/02/15',1,0,1,0,0,0,0,1),(124,0,'(256,256)','splited',20,1,2,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-21-36-05','2023/02/15',1,0,1,1,0,1,0,0),(125,0,'(256,256)','splited',5,1,2,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-21-38-33','2023/02/15',1,0,1,0,0,1,1,1),(126,0,'(256,256)','splited',2,1,4,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-15-21-44-11','2023/02/15',1,0,1,0,0,1,0,0),(127,0,'(256,256)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-18-14-33-18','2023/02/18',1,0,1,0,0,1,0,0),(128,0,'(256,256)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-18-14-35-10','2023/02/18',1,0,1,0,0,1,0,0),(129,0,'(256,256)','splited',2,0,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-18-14-48-05','2023/02/18',1,0,1,1,0,1,1,1),(130,0,'(256,256)','splited',2,1,8,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-18-16-17-01','2023/02/18',1,0,0,0,0,1,0,0),(131,0,'(256,256)','splited',2,1,2,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-18-16-43-08','2023/02/18',1,0,0,0,0,1,0,0),(132,0,'(256,256)','splited',2,1,2,0.001,0.2,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-18-16-45-37','2023/02/18',1,0,1,0,0,1,0,0),(133,0,'(256,256)','splited',2,1,2,0.001,0.5,'[\'default_dataset/binary\']','default_dataset/weights/binary/2023-02-19-09-13-29','2023/02/19',1,0,0,0,0,1,1,1);
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

-- Dump completed on 2023-08-15 10:21:00
