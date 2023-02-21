-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 21, 2023 at 05:31 AM
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
-- Table structure for table `localization_models`
--

CREATE TABLE `localization_models` (
  `id` int NOT NULL,
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
  `date_` varchar(45) NOT NULL DEFAULT '01/01/1401'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `localization_models`
--

INSERT INTO `localization_models` (`id`, `algo_name`, `pretrain_path`, `input_size`, `input_type`, `epochs`, `batch_size`, `lr`, `split_ratio`, `loss`, `accuracy`, `iou`, `fscore`, `val_loss`, `val_accuracy`, `val_iou`, `val_fscore`, `dataset_pathes`, `weights_path`, `date_`) VALUES
(10, '0', '', '(256,256)', '1', 2, 1, 0.001, 0.2, 0.764264, 0.586955, 0.310854, 0.449099, 1.02973, 0.968658, 0.000303313, 0.000606067, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-18-17-23-14', '2023/02/18'),
(11, '0', '', '(256,256)', '1', 5, 2, 0.01, 0.5, 0.787259, 0.510691, 0.134556, 0.210921, 1.77183, 0.808456, 0.000000000424284, 0.000000000424284, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-10-08-30', '2023/02/19'),
(12, '0', '', '(256,256)', '1', 10, 1, 0.001, 0.2, 0.857866, 0.486687, 0.205579, 0.295589, 2.08094, 0.726761, 0.00303876, 0.00604947, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-15-49-51', '2023/02/19'),
(13, '0', '', '(256,256)', '1', 2, 2, 0.001, 0.2, 0.838796, 0.590189, 0.150817, 0.249161, 1.43944, 0.716334, 0.00218703, 0.00436151, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-23-38-44', '2023/02/19'),
(14, '1', '/home/reyhane/PythonProjects/trainApp_oxin_new/default_dataset/weights/localization/2023-02-19-23-36-05/localization_model.h5', '(256,256)', '1', 2, 1, 0.001, 0.2, 0.809231, 0.760735, 0.0718374, 0.102411, 2.04686, 0.745753, 0.00174496, 0.00347174, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-23-40-50', '2023/02/19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `localization_models`
--
ALTER TABLE `localization_models`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `localization_models`
--
ALTER TABLE `localization_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
