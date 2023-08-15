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
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `settings` (
  `id` int NOT NULL,
  `parent_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `path_dataset` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `font_style` varchar(45) NOT NULL DEFAULT 'Arial',
  `font_size` int NOT NULL DEFAULT '10',
  `window_style` varchar(45) NOT NULL DEFAULT 'Windows',
  `window_color` varchar(45) NOT NULL DEFAULT 'blue',
  `language` varchar(45) NOT NULL DEFAULT 'English',
  `large_rect_area` int NOT NULL DEFAULT '0',
  `small_rect_area` int NOT NULL DEFAULT '0',
  `rect_accuracy` float NOT NULL DEFAULT '0.9',
  `split_size` varchar(500) NOT NULL DEFAULT '0',
  `n_defect_colors` int NOT NULL DEFAULT '1',
  `path_dataset_user` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `path_weights` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `camera_live_drive` varchar(500) DEFAULT NULL,
  `live_drive_max_used_ratio` int NOT NULL DEFAULT '80',
  `live_drive_remove_stop_ratio` int NOT NULL DEFAULT '60',
  `plc_ip` varchar(100) NOT NULL DEFAULT 'NULL',
  `pipline_json_path` varchar(500) NOT NULL DEFAULT 'NULL',
  `pipeline_json_path_o` varchar(500) NOT NULL DEFAULT 'NULL',
  `result_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `manual_plc` varchar(6) NOT NULL DEFAULT 'True',
  `plc_update_time` int NOT NULL DEFAULT '2000',
  `wind_duration` int NOT NULL DEFAULT '5',
  `automatic_wind` varchar(6) NOT NULL DEFAULT 'True',
  `auto_wind_intervals` int NOT NULL DEFAULT '5000',
  `manual_cameras` varchar(6) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'True',
  `frame_rate` int NOT NULL DEFAULT '7',
  `live_update_time` int NOT NULL DEFAULT '130',
  `sound_warning` varchar(6) NOT NULL DEFAULT 'True',
  `warning_alarm` varchar(100) NOT NULL,
  `nonallowed_frames` int NOT NULL DEFAULT '5',
  `defect_percent` int NOT NULL DEFAULT '20',
  `width_up_th` int NOT NULL,
  `width_down_th` int NOT NULL,
  `last_pipeline_name` varchar(45) DEFAULT NULL,
  `suggestions_path` varchar(2000) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `settings`
--

LOCK TABLES `settings` WRITE;
/*!40000 ALTER TABLE `settings` DISABLE KEYS */;
INSERT INTO `settings` VALUES (0,'oxin_image_grabber','dataset','Ubuntu',11,'Windows','#144475','Persian',6000,2800,90,'(100, 100)',21,'dataset','weights','/mnt/487CE64F7CE6377A/images',63,60,'opc.tcp://192.168.1.50:4840','evaluated_jsons','pipelines','oxin_image_grabber','True',500,3,'False',2000,'True',7,130,'False','3.mp3',90,20,50,50,'c','');
/*!40000 ALTER TABLE `settings` ENABLE KEYS */;
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
