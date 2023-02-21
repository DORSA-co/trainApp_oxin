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
(85, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'/home/reyhene/Desktop\', \'/home/reyhane/Dorsa\', \'/home/reyhane/pythonProjects/ trainApp_oxin_new\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-10-22-07-41-28', '1401/10/22'),
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
(105, 0, '(300,300)', '1', 20, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-01-17-14-10', '1401/11/01'),
(106, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-06-14-52-06', '1401/11/06'),
(107, 0, '(300,300)', '1', 15, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-06-14-52-54', '1401/11/06'),
(108, 0, '(300,300)', '0', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 0, 0, 0, 0, 0, 'default_dataset/weights/binary/1401-11-06-15-04-05', '1401/11/06'),
(109, 0, '(300,300)', '0', 15, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 1, 0, 1, 1, 1, 'default_dataset/weights/binary/1401-11-06-15-04-26', '1401/11/06'),
(110, 0, '(100,100)', '1', 15, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-11-06-15-05-18', '1401/11/06'),
(111, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-14-15-46-40', '1401/11/14'),
(112, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/1401-11-16-19-05-51', '1401/11/16'),
(113, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-10-15-02-25', '2023/02/10'),
(114, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-14-19-20-28', '2023/02/14'),
(115, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-14-19-24-38', '2023/02/14'),
(116, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-14-20-34-49', '2023/02/14'),
(117, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 1, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-14-22-33-26', '2023/02/14'),
(118, 0, '(256,256)', '1', 2, 4, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-15-17-36-12', '2023/02/15'),
(119, 0, '(256,256)', '1', 20, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 1, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-15-18-40-00', '2023/02/15'),
(120, 0, '(256,256)', '1', 20, 4, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-15-18-54-59', '2023/02/15'),
(121, 0, '(256,256)', '1', 20, 1, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-15-19-09-21', '2023/02/15'),
(122, 0, '(256,256)', '1', 20, 1, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-15-19-11-02', '2023/02/15'),
(123, 0, '(256,256)', '1', 20, 1, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 0, 0, 1, 'default_dataset/weights/binary/2023-02-15-21-13-49', '2023/02/15'),
(124, 0, '(256,256)', '1', 20, 2, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 1, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-15-21-36-05', '2023/02/15'),
(125, 0, '(256,256)', '1', 5, 2, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 1, 1, 'default_dataset/weights/binary/2023-02-15-21-38-33', '2023/02/15'),
(126, 0, '(256,256)', '1', 2, 4, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-15-21-44-11', '2023/02/15'),
(127, 0, '(256,256)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-18-14-33-18', '2023/02/18'),
(128, 0, '(256,256)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-18-14-35-10', '2023/02/18'),
(129, 0, '(256,256)', '1', 2, 8, 0.001, 0, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 1, 0, 1, 1, 1, 'default_dataset/weights/binary/2023-02-18-14-48-05', '2023/02/18'),
(130, 0, '(256,256)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-18-16-17-01', '2023/02/18'),
(131, 0, '(256,256)', '1', 2, 2, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-18-16-43-08', '2023/02/18'),
(132, 0, '(256,256)', '1', 2, 2, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 0, 0, 1, 0, 0, 'default_dataset/weights/binary/2023-02-18-16-45-37', '2023/02/18'),
(133, 0, '(256,256)', '0', 2, 2, 0.001, 1, 0.5, '[\'default_dataset/binary\']', 1, 0, 0, 0, 0, 1, 1, 1, 'default_dataset/weights/binary/2023-02-19-09-13-29', '2023/02/19');

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=134;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
