-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 21, 2023 at 05:29 AM
-- Server version: 8.0.32-0ubuntu0.22.04.2
-- PHP Version: 8.1.2-1ubuntu2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `saba_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `classification_models`
--

CREATE TABLE `classification_models` (
  `id` int NOT NULL,
  `algo_name` varchar(45) NOT NULL DEFAULT '0',
  `input_size` varchar(45) NOT NULL DEFAULT '(100,100)',
  `input_type` varchar(45) NOT NULL DEFAULT '0',
  `epochs` int NOT NULL DEFAULT '10',
  `batch_size` int NOT NULL DEFAULT '8',
  `lr` float NOT NULL DEFAULT '0.001',
  `tuning_epochs` int NOT NULL DEFAULT '2',
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
  `date_` varchar(45) NOT NULL DEFAULT '01/01/1401'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `classification_models`
--
ALTER TABLE `classification_models`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `classification_models`
--
ALTER TABLE `classification_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
