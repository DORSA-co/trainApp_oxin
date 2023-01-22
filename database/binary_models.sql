-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 22, 2023 at 07:07 AM
-- Server version: 8.0.31-0ubuntu0.22.04.1
-- PHP Version: 8.1.2-1ubuntu2.8

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
-- Table structure for table `binary_models`
--

CREATE TABLE `binary_models` (
  `id` int NOT NULL,
  `algo_name` int NOT NULL DEFAULT '-1',
  `input_size` varchar(45) NOT NULL DEFAULT '(100,100)',
  `input_type` varchar(45) NOT NULL DEFAULT 'null',
  `epochs` int NOT NULL DEFAULT '2',
  `batch_size` int NOT NULL DEFAULT '8',
  `lr` float NOT NULL DEFAULT '0',
  `tuning_epochs` int NOT NULL DEFAULT '1',
  `split_ratio` float NOT NULL DEFAULT '25',
  `dataset_pathes` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `accuracy` int NOT NULL DEFAULT '0',
  `loss` int NOT NULL DEFAULT '0',
  `precision_` int NOT NULL DEFAULT '0',
  `recall` int NOT NULL DEFAULT '0',
  `val_loss` int NOT NULL DEFAULT '0',
  `val_accuracy` int NOT NULL DEFAULT '0',
  `val_precision` int NOT NULL DEFAULT '0',
  `val_recall` int NOT NULL DEFAULT '0',
  `weights_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `date_` varchar(45) NOT NULL DEFAULT '0000/00/00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `binary_models`
--

INSERT INTO `binary_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `lr`, `tuning_epochs`, `split_ratio`, `dataset_pathes`, `accuracy`, `loss`, `precision_`, `recall`, `val_loss`, `val_accuracy`, `val_precision`, `val_recall`, `weights_path`, `date_`) VALUES
(85, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-07-41-28', '1401/10/22'),
(86, 0, '(300,300)', '1', 12, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-07-42-46', '1401/10/22'),
(87, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-07-48-06', '1401/10/22'),
(88, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-08-26-39', '1401/10/22'),
(89, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-08-28-28', '1401/10/22'),
(90, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-08-37-07', '1401/10/22'),
(91, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-08-45-33', '1401/10/22'),
(92, 0, '(300,300)', '0', 12, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-08-46-36', '1401/10/22'),
(93, 0, '(300,300)', '0', 15, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-09-05-04', '1401/10/22'),
(94, 0, '(300,300)', '0', 15, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-09-08-11', '1401/10/22'),
(95, 0, '(100,100)', '1', 4, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-26-11-21-47', '1401/10/26'),
(96, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-10-04-55', '1401/11/01'),
(97, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-10-46-18', '1401/11/01'),
(98, 0, '(300,300)', '1', 2, 8, 0.002, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-11-07-04', '1401/11/01'),
(99, 0, '(300,300)', '1', 2, 8, 0, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 0, 'default_dataset/weights/binary/1401-11-01-11-08-53', '1401/11/01'),
(100, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-14-31-19', '1401/11/01'),
(101, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-15-23-57', '1401/11/01'),
(102, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-16-35-53', '1401/11/01'),
(103, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-17-04-49', '1401/11/01'),
(104, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-17-13-35', '1401/11/01'),
(105, 0, '(300,300)', '1', 20, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-17-14-10', '1401/11/01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `binary_models`
--
ALTER TABLE `binary_models`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `binary_models`
--
ALTER TABLE `binary_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
