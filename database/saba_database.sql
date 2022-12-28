-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 17, 2022 at 11:35 AM
-- Server version: 8.0.30-0ubuntu0.20.04.2
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
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
  `dataset_pathes` varchar(5000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `accuracy` int NOT NULL DEFAULT '0',
  `loss` int NOT NULL DEFAULT '0',
  `precision_` int NOT NULL DEFAULT '0',
  `recall` int NOT NULL DEFAULT '0',
  `val_loss` int NOT NULL DEFAULT '0',
  `val_accuracy` int NOT NULL DEFAULT '0',
  `val_precision` int NOT NULL DEFAULT '0',
  `val_recall` int NOT NULL DEFAULT '0',
  `weights_path` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `date_` varchar(45) NOT NULL DEFAULT 'null'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `binary_models`
--

INSERT INTO `binary_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `lr`, `tuning_epochs`, `split_ratio`, `dataset_pathes`, `accuracy`, `loss`, `precision_`, `recall`, `val_loss`, `val_accuracy`, `val_precision`, `val_recall`, `weights_path`, `date_`) VALUES
(1, 0, '(100,100)', 'resize', 10, 8, 0, 3, 25, 'dataset\\binary', 94, 10, 90, 89, 11, 90, 90, 88, 'weights', '7/2/1401'),
(3, 0, '(100,100)', '1', 10, 8, 0, 1, 0, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(4, 0, '(100,100)', '1', 10, 8, 0, 1, 0, '[\'dataset\\\\binary\']', 0, 0, 0, 0, 0, 0, 0, 0, 'weights\\binary', '24/02/1401'),
(5, 0, '(100,100)', '1', 10, 8, 0, 1, 0, '[\'dataset\\\\binary\']', 0, 0, 0, 0, 0, 0, 0, 0, 'weights\\binary', '24/02/1401'),
(6, 0, '(100,100)', '1', 10, 8, 0, 1, 0, '[\'dataset\\\\binary\']', 0, 0, 0, 0, 0, 0, 0, 0, 'weights\\binary\\24-2-1401-12-37-9', '24/01/1401'),
(7, 0, '(100,100)', '1', 4, 8, 0, 2, 0, '[\'dataset\\\\binary\']', 0, 0, 0, 0, 0, 0, 0, 0, 'weights\\binary\\24-2-1401-12-56-4', '24/02/1401'),
(8, 0, '(100,100)', '1', 10, 8, 0.001, 5, 0.25, '[\'dataset\\\\binary\']', 0, 0, 0, 0, 0, 0, 0, 0, 'weights\\binary\\24-2-1401-13-1-42', '24/02/1401'),
(9, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(10, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(11, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(12, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(13, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(14, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(15, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(16, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(17, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(18, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(19, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(20, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(21, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(22, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(23, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(24, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(25, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(26, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(27, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(28, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(29, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(30, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(31, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(32, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(33, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(34, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(35, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(36, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(37, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(38, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(39, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(40, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(41, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(42, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(43, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(44, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(45, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(46, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(47, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(48, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(49, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(50, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(51, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(52, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(53, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(54, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(55, 0, '(100,100)', 'null', 2, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(56, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(57, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(58, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(59, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(60, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(61, 0, '(100,100)', 'null', 10, 8, 0, 1, 25, 'null', 0, 0, 0, 0, 0, 0, 0, 0, 'null', 'null'),
(62, 0, '(100,100)', '1', 2, 8, 0.001, 1, 0.2, '[\'dataset/binary\']', 0, 0, 0, 0, 0, 0, 0, 0, 'dataset/weights/binary/3-3-1401-9-29-57', '03/03/1401'),
(63, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 1, 0, 1, 1, 1, 'MyDs/weights/binary/5-3-1401-11-6-38', '05/03/1401'),
(64, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'/home/reyhane/PycharmProjects/trainApp_oxin5/trainApp_oxin5/MyDs/binary\', \'/home/reyhane/PycharmProjects/trainApp_oxin5/trainApp_oxin5/MyDs1/binary\']', 0, 0, 0, 1, 0, 1, 1, 1, 'MyDs/weights/binary/5-3-1401-11-9-6', '05/03/1401'),
(65, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'TestDs/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, './TestDs/weights/binary/1401-5-3-9-3-19', '1401/5/3'),
(66, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-11-17-16-16', '1401/5/11'),
(67, 0, '(300,300)', '1', 10, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-11-17-18-23', '1401/5/11'),
(68, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-18-19-35-36', '1401/5/18'),
(69, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-18-19-39-28', '1401/5/18'),
(70, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-18-19-40-28', '1401/5/18'),
(71, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'TestDs/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-18-21-31-49', '1401/5/18'),
(72, 0, '(300,300)', '1', 20, 8, 0.001, 8, 0.2, '[\'default_dataset/binary\', \'TestDs/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-18-21-33-46', '1401/5/18'),
(73, 0, '(300,300)', '1', 10, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-9-24-2', '1401/5/19'),
(74, 0, '(300,300)', '1', 12, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-9-34-6', '1401/5/19'),
(75, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-9-42-0', '1401/5/19'),
(76, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-9-48-55', '1401/5/19'),
(77, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-9-54-28', '1401/5/19'),
(78, 0, '(300,300)', '1', 12, 8, 0.001, 5, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-10-9-23', '1401/5/19'),
(79, 0, '(300,300)', '1', 12, 8, 0.001, 5, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-10-13-9', '1401/5/19'),
(80, 0, '(300,300)', '1', 20, 8, 0.001, 10, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-10-18-49', '1401/5/19'),
(81, 0, '(400,200)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-13-0-12', '1401/5/19'),
(82, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-13-5-14', '1401/5/19'),
(83, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-13-10-39', '1401/5/19'),
(84, 0, '(400,100)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-19-13-11-19', '1401/5/19'),
(85, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'TestDs/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-20-15-35-58', '1401/5/20'),
(86, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-23-12-19-19', '1401/5/23'),
(87, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'TestDs/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-23-12-21-45', '1401/5/23'),
(88, 0, '(400,100)', '0', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\']', 1, 0, 1, 1, 0, 1, 1, 1, 'default_dataset/weights/binary/1401-5-23-12-23-52', '1401/5/23'),
(89, 0, '(300,300)', '1', 2, 8, 0.001, 1, 0.2, '[\'default_dataset/binary\', \'TestDs/binary\']', 0, 0, 0, 1, 0, 0, 0, 1, 'default_dataset/weights/binary/1401-5-26-11-36-22', '1401/5/26');

-- --------------------------------------------------------

--
-- Table structure for table `camera_settings`
--

CREATE TABLE `camera_settings` (
  `id` int NOT NULL,
  `gain_top` int NOT NULL DEFAULT '0',
  `gain_bottom` int NOT NULL DEFAULT '360',
  `gain_value` int NOT NULL DEFAULT '0',
  `expo_top` int NOT NULL DEFAULT '35',
  `expo_bottom` int NOT NULL DEFAULT '10000000',
  `expo_value` int NOT NULL DEFAULT '3000',
  `width` int NOT NULL DEFAULT '1920',
  `height` int NOT NULL DEFAULT '1200',
  `offsetx_top` int NOT NULL DEFAULT '16',
  `offsetx_bottom` int NOT NULL DEFAULT '0',
  `offsetx_value` int NOT NULL DEFAULT '0',
  `offsety_top` int NOT NULL DEFAULT '16',
  `offsety_bottom` int NOT NULL DEFAULT '0',
  `offsety_value` int NOT NULL DEFAULT '0',
  `interpacket_delay` int NOT NULL DEFAULT '0',
  `packet_size` int NOT NULL DEFAULT '0',
  `trigger_mode` tinyint NOT NULL DEFAULT '0',
  `max_buffer` int NOT NULL DEFAULT '0',
  `transmission_delay` int NOT NULL DEFAULT '0',
  `ip_address` varchar(45) NOT NULL,
  `rotation_value` float NOT NULL DEFAULT '0',
  `shifth_value` int NOT NULL DEFAULT '0',
  `shiftw_value` int NOT NULL DEFAULT '0',
  `serial_number` varchar(45) NOT NULL DEFAULT '0',
  `pxvalue_a` float NOT NULL DEFAULT '0',
  `pxvalue_b` float NOT NULL DEFAULT '0',
  `pxvalue_c` float NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `camera_settings`
--

INSERT INTO `camera_settings` (`id`, `gain_top`, `gain_bottom`, `gain_value`, `expo_top`, `expo_bottom`, `expo_value`, `width`, `height`, `offsetx_top`, `offsetx_bottom`, `offsetx_value`, `offsety_top`, `offsety_bottom`, `offsety_value`, `interpacket_delay`, `packet_size`, `trigger_mode`, `max_buffer`, `transmission_delay`, `ip_address`, `rotation_value`, `shifth_value`, `shiftw_value`, `serial_number`, `pxvalue_a`, `pxvalue_b`, `pxvalue_c`) VALUES
(1, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '192.168.1.100', 3.7, -39, 2, '0', 0, 0, 0),
(2, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '192.168.1.2', 0, 0, 0, '0', 0, 0, 0),
(3, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(4, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(5, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 2, 21, 50, '0', 0, 0, 0),
(6, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(7, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(8, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(9, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(10, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(11, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 6, '127.0.0.1', 0, 0, 0, '0', 0, 0, 0),
(12, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(13, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(14, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(15, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(16, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(17, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(18, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(19, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(20, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(21, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(22, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(23, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
(24, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0);

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
  `dataset_pathes` varchar(100) NOT NULL DEFAULT 'path',
  `weights_path` varchar(100) NOT NULL DEFAULT 'path',
  `date_` varchar(45) NOT NULL DEFAULT '01/01/1401'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `classification_models`
--

INSERT INTO `classification_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `lr`, `tuning_epochs`, `split_ratio`, `classes`, `loss`, `accuracy`, `precision_`, `recall`, `val_loss`, `val_accuracy`, `val_precision`, `val_recall`, `dataset_pathes`, `weights_path`, `date_`) VALUES
(1, '0', '(100,100)', '0', 10, 8, 0.001, 2, 0.25, ',4,2,', 1.5, 95, 95, 90, 2, 90, 90, 90, 'datsetpath', 'weightspath', '02/03/1401');

-- --------------------------------------------------------

--
-- Table structure for table `database_config`
--

CREATE TABLE `database_config` (
  `id` int NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `database_config`
--

INSERT INTO `database_config` (`id`, `user_name`, `password`) VALUES
(1, 'root', 'root');

-- --------------------------------------------------------

--
-- Table structure for table `datasets`
--

CREATE TABLE `datasets` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `user_own` varchar(45) NOT NULL,
  `path` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `datasets`
--

INSERT INTO `datasets` (`id`, `name`, `user_own`, `path`) VALUES
(0, 'default_dataset', 'root', 'default_dataset'),
(52, 'TestDs', 'ali', './TestDs');

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
  `groupp` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `level` varchar(45) DEFAULT NULL,
  `color` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT '-'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `defects_info`
--

INSERT INTO `defects_info` (`id`, `name`, `short_name`, `defect_ID`, `is_defect`, `groupp`, `level`, `color`, `date`) VALUES
(1, 'NO LABEL', 'LABEL', '0', 'No', '1', '0', '#FFFFFF', '7/2/1401'),
(47, 'd2', 'd2', '102', 'no', '1', '0', '#05d2d2', '7/2/1401'),
(55, 'd3', 'd3', '103', 'yes', '4', '1', '#05d2d2', '17/02/1401'),
(56, 'd1', 'd1', '101', 'yes', '4', '2', '#d20505', '7/2/1401'),
(57, 'd4', 'd4', '104', 'yes', '4', '2', '#980404', '7/2/1401');

-- --------------------------------------------------------

--
-- Table structure for table `defect_groups`
--

CREATE TABLE `defect_groups` (
  `id` int NOT NULL,
  `defect_group_name` varchar(45) DEFAULT NULL,
  `defect_group_id` varchar(45) DEFAULT NULL,
  `date_created` varchar(45) NOT NULL DEFAULT '-',
  `is_defect` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `defect_groups`
--

INSERT INTO `defect_groups` (`id`, `defect_group_name`, `defect_group_id`, `date_created`, `is_defect`) VALUES
(25, 'no_defect', '1', '7/2/1401', 'no'),
(28, 'gp2', '3', '7/2/1401', 'no'),
(29, 'gp4', '4', '7/2/1401', 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `image_processing`
--

CREATE TABLE `image_processing` (
  `id` int NOT NULL DEFAULT '0',
  `block_size` varchar(45) NOT NULL DEFAULT 'small',
  `defect` float NOT NULL DEFAULT '0',
  `noise` float NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `image_processing`
--

INSERT INTO `image_processing` (`id`, `block_size`, `defect`, `noise`) VALUES
(0, 'Medium', -0.8, 10);

-- --------------------------------------------------------

--
-- Table structure for table `localization_models`
--

CREATE TABLE `localization_models` (
  `id` int NOT NULL,
  `algo_name` int NOT NULL DEFAULT '-1',
  `input_size` varchar(45) NOT NULL DEFAULT '(100,100)',
  `input_type` varchar(45) NOT NULL DEFAULT 'null',
  `epochs` int NOT NULL DEFAULT '2',
  `batch_size` int NOT NULL DEFAULT '8',
  `lr` float NOT NULL DEFAULT '0',
  `split_ratio` float NOT NULL DEFAULT '25',
  `dataset_pathes` varchar(5000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `accuracy` int NOT NULL DEFAULT '0',
  `loss` int NOT NULL DEFAULT '0',
  `precision_` int NOT NULL DEFAULT '0',
  `recall` int NOT NULL DEFAULT '0',
  `val_loss` int NOT NULL DEFAULT '0',
  `val_accuracy` int NOT NULL DEFAULT '0',
  `val_precision` int NOT NULL DEFAULT '0',
  `val_recall` int NOT NULL DEFAULT '0',
  `weights_path` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `date_` varchar(45) NOT NULL DEFAULT 'null'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `localization_models`
--

INSERT INTO `localization_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `lr`, `split_ratio`, `dataset_pathes`, `accuracy`, `loss`, `precision_`, `recall`, `val_loss`, `val_accuracy`, `val_precision`, `val_recall`, `weights_path`, `date_`) VALUES
(1, 1, '(300,300)', '1', 60, 8, 0.001, 0.2, '[\'default_dataset/localization\']', 80, 1, 75, 79, 2, 78, 70, 74, 'default_dataset/weights/localization/1401-5-19-17-52-35', '1401/5/19'),
(2, 1, '(300,300)', '1', 60, 8, 0.001, 0.2, '[\'default_dataset/localization\']', 80, 1, 75, 79, 2, 78, 70, 74, 'default_dataset/weights/localization/1401-5-20-10-6-18', '1401/5/20'),
(3, 1, '(300,300)', '1', 60, 8, 0.001, 0.2, '[\'default_dataset/localization\', \'TestDs/localization\']', 80, 1, 75, 79, 2, 78, 70, 74, 'default_dataset/weights/localization/1401-5-20-11-6-0', '1401/5/20'),
(4, 1, '(300,300)', '1', 60, 8, 0.001, 0.2, '[\'default_dataset/localization\', \'TestDs/localization\']', 80, 1, 75, 79, 2, 78, 70, 74, 'default_dataset/weights/localization/1401-5-20-11-12-29', '1401/5/20'),
(5, 1, '(300,300)', '1', 60, 8, 0.001, 0.2, '[\'default_dataset/localization\', \'TestDs/localization\']', 80, 1, 75, 79, 2, 78, 70, 74, 'default_dataset/weights/localization/1401-5-20-11-15-9', '1401/5/20'),
(6, 1, '(304,304)', '1', 6, 1, 0.001, 0.2, '[\'default_dataset/localization\']', 1, 1, 0, 0, 2, 0, 0, 1, 'default_dataset/weights/localization/1401-5-25-11-52-16', '1401/5/25'),
(7, 1, '(304,304)', '1', 6, 1, 0.001, 0.2, '[\'default_dataset/localization\', \'TestDs/localization\']', 1, 2, 0, 0, 1, 1, 0, 0, 'default_dataset/weights/localization/1401-5-25-11-54-36', '1401/5/25'),
(8, 1, '(304,304)', '1', 10, 2, 0.001, 0.2, '[\'default_dataset/localization\']', 1, 2, 0, 0, 1, 1, 0, 0, 'default_dataset/weights/localization/1401-5-25-20-5-49', '1401/5/25'),
(9, 1, '(304,304)', '1', 10, 2, 0.001, 0.2, '[\'default_dataset/localization\', \'TestDs/localization\']', 1, 2, 0, 0, 1, 1, 0, 0, 'default_dataset/weights/localization/1401-5-26-11-55-48', '1401/5/26');

-- --------------------------------------------------------

--
-- Table structure for table `multi_tasking`
--

CREATE TABLE `multi_tasking` (
  `id` int NOT NULL,
  `camera_threads_value` int NOT NULL DEFAULT '4',
  `camera_threads_min` int NOT NULL DEFAULT '4',
  `camera_threads_max` int NOT NULL DEFAULT '24',
  `camera_process_value` int NOT NULL DEFAULT '2',
  `camera_process_min` int NOT NULL DEFAULT '2',
  `camera_process_max` int NOT NULL DEFAULT '8',
  `camera_refresh_rate_value` int NOT NULL DEFAULT '5',
  `camera_refresh_rate_min` int NOT NULL DEFAULT '5',
  `camera_refresh_rate_max` int NOT NULL DEFAULT '100',
  `writing_thread_value` int NOT NULL DEFAULT '4',
  `writing_thread_min` int NOT NULL DEFAULT '4',
  `writing_thread_max` int NOT NULL DEFAULT '24'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `multi_tasking`
--

INSERT INTO `multi_tasking` (`id`, `camera_threads_value`, `camera_threads_min`, `camera_threads_max`, `camera_process_value`, `camera_process_min`, `camera_process_max`, `camera_refresh_rate_value`, `camera_refresh_rate_min`, `camera_refresh_rate_max`, `writing_thread_value`, `writing_thread_min`, `writing_thread_max`) VALUES
(0, 5, 4, 24, 4, 2, 8, 2, 5, 100, 5, 4, 24);

-- --------------------------------------------------------

--
-- Table structure for table `plc_path`
--

CREATE TABLE `plc_path` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `path` varchar(500) NOT NULL DEFAULT '-',
  `value0` varchar(45) NOT NULL DEFAULT '-1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `plc_path`
--

INSERT INTO `plc_path` (`id`, `name`, `path`, `value0`) VALUES
(25, 'ProjectorPulseTrig', 'ns=4;i=2', 'True'),
(26, 'NCamera', 'ns=4;i=3', '2'),
(27, 'MemSoftwareStart', 'ns=4;i=4', 'False'),
(28, 'MemDownLimitSwitchIn', 'ns=4;i=5', 'False'),
(29, 'MemDownLimitSwitchOut', 'ns=4;i=6', 'False'),
(30, 'MemDownProjectorOnOff1', 'ns=4;i=7', 'False'),
(31, 'MemDownProjectorOnOff2', 'ns=4;i=8', 'False'),
(32, 'MemDownProjectorOnOff3', 'ns=4;i=9', 'False'),
(33, 'MemDownProjectorOnOff4', 'ns=4;i=10', 'False'),
(34, 'MemDownProjectorOnOff5', 'ns=4;i=11', 'False'),
(35, 'MemDownProjectorOnOff6', 'ns=4;i=12', 'False'),
(36, 'MemDownValve', 'ns=4;i=13', 'False'),
(37, 'DownTemperature', 'ns=4;i=23', '134.55'),
(38, 'DownHighThreshold', 'ns=4;i=24', '0.0'),
(39, 'DownLowThreshold', 'ns=4;i=25', '0.0'),
(40, 'MemUpLimitSwitchIn', 'ns=4;i=26', 'False'),
(41, 'MemUpLimitSwitchOut', 'ns=4;i=27', 'False'),
(42, 'MemUpProjectorOnOff1', 'ns=4;i=28', 'False'),
(43, 'MemUpProjectorOnOff2', 'ns=4;i=29', 'False'),
(44, 'MemUpProjectorOnOff3', 'ns=4;i=30', 'False'),
(45, 'MemUpProjectorOnOff4', 'ns=4;i=31', 'False'),
(46, 'MemUpProjectorOnOff5', 'ns=4;i=32', 'False'),
(47, 'MemUpProjectorOnOff6', 'ns=4;i=33', 'False'),
(48, 'MemUpValve', 'ns=4;i=34', 'False'),
(49, 'UpTemperature', 'ns=4;i=35', '27.6'),
(50, 'UpHighThreshold', 'ns=4;i=36', '0.0'),
(51, 'UpLowThreshold', 'ns=4;i=37', '0.0'),
(52, 'MemDistanceSensor', 'ns=4;i=38', 'False');

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` int NOT NULL,
  `parent_path` varchar(45) DEFAULT NULL,
  `path_dataset` varchar(45) DEFAULT NULL,
  `font_style` varchar(45) NOT NULL DEFAULT 'Arial',
  `font_size` int NOT NULL DEFAULT '10',
  `window_style` varchar(45) NOT NULL DEFAULT 'Windows',
  `window_color` varchar(45) NOT NULL DEFAULT 'blue',
  `language` varchar(45) NOT NULL DEFAULT 'English',
  `large_rect_area` int NOT NULL DEFAULT '0',
  `small_rect_area` int NOT NULL DEFAULT '0',
  `rect_accuracy` float NOT NULL DEFAULT '0.9',
  `split_size` varchar(45) NOT NULL DEFAULT '0',
  `n_defect_colors` int NOT NULL DEFAULT '1',
  `path_dataset_user` varchar(45) DEFAULT NULL,
  `path_weights` varchar(45) DEFAULT NULL,
  `camera_live_drive` varchar(45) DEFAULT NULL,
  `live_drive_max_used_ratio` int NOT NULL DEFAULT '80',
  `live_drive_remove_stop_ratio` int NOT NULL DEFAULT '60',
  `plc_ip` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `parent_path`, `path_dataset`, `font_style`, `font_size`, `window_style`, `window_color`, `language`, `large_rect_area`, `small_rect_area`, `rect_accuracy`, `split_size`, `n_defect_colors`, `path_dataset_user`, `path_weights`, `camera_live_drive`, `live_drive_max_used_ratio`, `live_drive_remove_stop_ratio`, `plc_ip`) VALUES
(0, 'oxin_image_grabber', 'dataset', 'Times New Roman', 11, 'Windows', '#144475', 'Persian', 2000, 1000, 0.9, '(100, 100)', 6, 'dataset', 'weights', 'D:', 63, 60, 'opc.tcp://127.0.0.1:8081');

-- --------------------------------------------------------

--
-- Table structure for table `sheets_info`
--

CREATE TABLE `sheets_info` (
  `id` int NOT NULL,
  `sheet_id` varchar(45) NOT NULL,
  `heat_number` varchar(45) DEFAULT NULL,
  `ps_number` varchar(45) DEFAULT NULL,
  `pdl_number` float DEFAULT NULL,
  `lenght` float DEFAULT NULL,
  `width` float DEFAULT NULL,
  `thickness` float DEFAULT NULL,
  `user` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `main_path` varchar(45) DEFAULT NULL,
  `nframe` int DEFAULT '0',
  `cameras` varchar(45) DEFAULT '0-12',
  `image_format` varchar(10) DEFAULT '.jpg'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sheets_info`
--

INSERT INTO `sheets_info` (`id`, `sheet_id`, `heat_number`, `ps_number`, `pdl_number`, `lenght`, `width`, `thickness`, `user`, `time`, `date`, `main_path`, `nframe`, `cameras`, `image_format`) VALUES
(1, '997', '0', '1111', 2222, 1500, 300, NULL, 'milad', '14:00:00', '1400/12/25', 'oxin_image_grabber', 25, '1-8', '.png'),
(2, '996', '0', '1111', 2222, 1000, 480, NULL, 'amir', '12:15:00', '1400/12/25', 'oxin_image_grabber', 20, '1-12', '.png');

-- --------------------------------------------------------

--
-- Table structure for table `sign_tables`
--

CREATE TABLE `sign_tables` (
  `id` int NOT NULL DEFAULT '0',
  `defects_info` int NOT NULL DEFAULT '0',
  `camera_settings` int NOT NULL DEFAULT '0',
  `sheets_info` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sign_tables`
--

INSERT INTO `sign_tables` (`id`, `defects_info`, `camera_settings`, `sheets_info`) VALUES
(0, 4, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int NOT NULL,
  `user_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `role` varchar(45) NOT NULL DEFAULT 'operator',
  `default_dataset` varchar(45) DEFAULT 'none',
  `date_created` varchar(45) DEFAULT '1-1-1401',
  `full_path` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `user_name`, `password`, `role`, `default_dataset`, `date_created`, `full_path`) VALUES
(4, 'test', 'test', 'operator', '0', '1-1-1401', NULL),
(5, 'ali', '1234', 'Operator', '52', '1-1-1401', NULL),
(18, 'alii', '1', 'Operator', '0', '1-1-1401', NULL),
(19, '1', '1', 'Operator', '0', '1-1-1401', NULL),
(20, '2', '2', 'Operator', '0', '1-1-1401', NULL),
(29, 'ali1', '1', 'Operator', '0', '1-1-1401', NULL),
(30, 'testt', '12', 'Operator', '0', '1-1-1401', NULL),
(31, 'te', 'te', 'Operator', '0', '1-1-1401', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `binary_models`
--
ALTER TABLE `binary_models`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `camera_settings`
--
ALTER TABLE `camera_settings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`);

--
-- Indexes for table `classification_models`
--
ALTER TABLE `classification_models`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `database_config`
--
ALTER TABLE `database_config`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `datasets`
--
ALTER TABLE `datasets`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `defects_info`
--
ALTER TABLE `defects_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `defect_groups`
--
ALTER TABLE `defect_groups`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `image_processing`
--
ALTER TABLE `image_processing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `localization_models`
--
ALTER TABLE `localization_models`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `multi_tasking`
--
ALTER TABLE `multi_tasking`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `plc_path`
--
ALTER TABLE `plc_path`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sheets_info`
--
ALTER TABLE `sheets_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sign_tables`
--
ALTER TABLE `sign_tables`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `binary_models`
--
ALTER TABLE `binary_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=90;

--
-- AUTO_INCREMENT for table `classification_models`
--
ALTER TABLE `classification_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=106;

--
-- AUTO_INCREMENT for table `database_config`
--
ALTER TABLE `database_config`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `datasets`
--
ALTER TABLE `datasets`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `defects_info`
--
ALTER TABLE `defects_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `defect_groups`
--
ALTER TABLE `defect_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `localization_models`
--
ALTER TABLE `localization_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `plc_path`
--
ALTER TABLE `plc_path`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `sheets_info`
--
ALTER TABLE `sheets_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=745;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
