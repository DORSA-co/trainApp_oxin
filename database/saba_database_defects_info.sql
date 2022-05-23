<<<<<<< HEAD
-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: saba_database
-- ------------------------------------------------------
-- Server version	8.0.28
=======
-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 21, 2022 at 09:42 AM
-- Server version: 8.0.29-0ubuntu0.20.04.3
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

>>>>>>> r_abtahi

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `saba_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `defects_info`
--

CREATE TABLE `defects_info` (
  `id` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `short_name` varchar(45) DEFAULT NULL,
  `defect_ID` varchar(45) DEFAULT NULL,
  `is_defect` varchar(45) DEFAULT 'Yes',
  `groupp` varchar(45) DEFAULT NULL,
  `level` varchar(45) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT '-'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `defects_info`
--

<<<<<<< HEAD
LOCK TABLES `defects_info` WRITE;
/*!40000 ALTER TABLE `defects_info` DISABLE KEYS */;
INSERT INTO `defects_info` VALUES (1,'NO LABEL','LABEL','0','No','0','0','#FFFFFF','7/2/1401'),(47,'d2','d2','2','no','1','0','#05d2d2','7/2/1401'),(55,'d3','d3','3','yes','4','1','#05d2d2','17/02/1401'),(56,'d1','d1','1','yes','4','2','#d20505','7/2/1401'),(57,'d4','d4','4','yes','4','2','#980404','7/2/1401');
/*!40000 ALTER TABLE `defects_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;
=======
INSERT INTO `defects_info` (`id`, `name`, `short_name`, `defect_ID`, `is_defect`, `groupp`, `level`, `color`, `date`) VALUES
(0, 'NO LABEL', 'NO LABEL', '0', 'No', '0', '0', '#FFFFFF', '7/2/1401'),
(47, 'd2', 'd2', '2', 'no', '1', '0', '#800080', '7/2/1401'),
(55, 'd3', 'd3', '3', 'yes', '4', '1', '#05d2d2', '17/02/1401'),
(56, 'd1', 'd1', '1', 'yes', '4', '2', '#d20505', '7/2/1401'),
(57, 'd4', 'd4', '4', 'yes', '4', '2', '#980404', '7/2/1401');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `defects_info`
--
ALTER TABLE `defects_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `defects_info`
--
ALTER TABLE `defects_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;
COMMIT;
>>>>>>> r_abtahi

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
<<<<<<< HEAD
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-21 15:24:05
=======
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
>>>>>>> r_abtahi
