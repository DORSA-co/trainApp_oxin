-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: May 27, 2023 at 05:57 AM
-- Server version: 8.0.33-0ubuntu0.20.04.2
-- PHP Version: 7.4.3-4ubuntu2.18

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
  `val_recall` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `binary_models`
--

INSERT INTO `binary_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `tuning_epochs`, `batch_size`, `lr`, `split_ratio`, `dataset_pathes`, `weights_path`, `date_`, `accuracy`, `loss`, `precision_`, `recall`, `val_loss`, `val_accuracy`, `val_precision`, `val_recall`) VALUES
(85, 1, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\', \'/home/reyhene/Desktop\', \'/home/reyhane/Dorsa\', \'/home/reyhane/pythonProjects/ trainApp_oxin_new\']', 'default_dataset/weights/binary/binarymodeltemp.h5', '1401/10/22', 1, 0, 0, 0, 0, 1, 0, 0),
(86, 0, '(300,300)', 'splited', 12, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-10-22-07-48-06', '1401/10/22', 1, 0, 1, 0, 0, 1, 0, 0),
(87, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-10-22-07-48-06', '1401/10/22', 1, 0, 0, 0, 0, 1, 0, 0),
(88, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-10-22-08-26-39', '1401/10/22', 1, 0, 1, 0, 0, 1, 0, 0),
(89, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-10-22-08-28-28', '1401/10/22', 1, 0, 0, 0, 0, 1, 0, 0),
(90, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-10-22-08-37-07', '1401/10/22', 1, 0, 1, 0, 0, 1, 0, 0),
(91, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-10-22-08-45-33', '1401/10/22', 1, 0, 0, 0, 0, 1, 0, 0),
(92, 0, '(300,300)', 'splited', 12, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']', 'default_dataset/weights/binary/1401-10-22-08-46-36', '1401/10/22', 1, 0, 1, 0, 0, 1, 0, 0),
(93, 0, '(300,300)', 'splited', 15, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']', 'default_dataset/weights/binary/1401-10-22-09-05-04', '1401/10/22', 1, 0, 1, 0, 0, 1, 0, 0),
(94, 0, '(300,300)', 'splited', 15, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\', \'/home/reyhane/PythonProjects/trainApp_oxin_new/Test_Dataset1/binary\']', 'default_dataset/weights/binary/1401-10-22-09-08-11', '1401/10/22', 1, 0, 1, 0, 0, 1, 0, 0),
(95, 0, '(100,100)', 'splited', 4, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-10-26-11-21-47', '1401/10/26', 1, 0, 1, 0, 0, 1, 0, 0),
(96, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-10-04-55', '1401/11/01', 1, 0, 1, 0, 0, 1, 0, 0),
(97, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-10-46-18', '1401/11/01', 1, 0, 0, 0, 0, 1, 0, 0),
(98, 0, '(300,300)', 'splited', 2, 1, 8, 0.002, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-11-07-04', '1401/11/01', 1, 0, 1, 0, 0, 1, 0, 0),
(99, 0, '(300,300)', 'splited', 2, 1, 8, 0, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-11-08-53', '1401/11/01', 0, 0, 0, 1, 0, 0, 0, 0),
(100, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-14-31-19', '1401/11/01', 1, 0, 1, 0, 0, 1, 0, 0),
(101, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-15-23-57', '1401/11/01', 1, 0, 1, 0, 0, 1, 0, 0),
(102, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-16-35-53', '1401/11/01', 1, 0, 1, 0, 0, 1, 0, 0),
(103, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-17-04-49', '1401/11/01', 1, 0, 0, 0, 0, 1, 0, 0),
(104, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-17-13-35', '1401/11/01', 1, 0, 1, 0, 0, 1, 0, 0),
(105, 0, '(300,300)', 'splited', 20, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-01-17-14-10', '1401/11/01', 1, 0, 0, 0, 0, 1, 0, 0),
(106, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-06-14-52-06', '1401/11/06', 1, 0, 1, 0, 0, 1, 0, 0),
(107, 0, '(300,300)', 'splited', 15, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-06-14-52-54', '1401/11/06', 1, 0, 0, 0, 0, 1, 0, 0),
(108, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-06-15-04-05', '1401/11/06', 0, 0, 0, 0, 0, 0, 0, 0),
(109, 0, '(300,300)', 'splited', 15, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-06-15-04-26', '1401/11/06', 1, 0, 1, 1, 0, 1, 1, 1),
(110, 0, '(100,100)', 'splited', 15, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-06-15-05-18', '1401/11/06', 1, 0, 1, 0, 0, 0, 0, 1),
(111, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-14-15-46-40', '1401/11/14', 1, 0, 0, 0, 0, 1, 0, 0),
(112, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/1401-11-16-19-05-51', '1401/11/16', 1, 0, 0, 0, 0, 1, 0, 0),
(113, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-10-15-02-25', '2023/02/10', 1, 0, 0, 0, 0, 1, 0, 0),
(114, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-14-19-20-28', '2023/02/14', 1, 0, 1, 0, 0, 1, 0, 0),
(115, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-14-19-24-38', '2023/02/14', 1, 0, 1, 0, 0, 1, 0, 0),
(116, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-14-20-34-49', '2023/02/14', 1, 0, 1, 0, 0, 1, 0, 0),
(117, 0, '(300,300)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-14-22-33-26', '2023/02/14', 1, 0, 1, 1, 0, 1, 0, 0),
(118, 0, '(256,256)', 'splited', 2, 1, 4, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-17-36-12', '2023/02/15', 1, 0, 1, 0, 0, 1, 0, 0),
(119, 0, '(256,256)', 'splited', 20, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-18-40-00', '2023/02/15', 1, 0, 0, 1, 0, 1, 0, 0),
(120, 0, '(256,256)', 'splited', 20, 1, 4, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-18-54-59', '2023/02/15', 1, 0, 1, 0, 0, 1, 0, 0),
(121, 0, '(256,256)', 'splited', 20, 1, 1, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-19-09-21', '2023/02/15', 1, 0, 0, 0, 0, 1, 0, 0),
(122, 0, '(256,256)', 'splited', 20, 1, 1, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-19-11-02', '2023/02/15', 1, 0, 0, 0, 0, 1, 0, 0),
(123, 0, '(256,256)', 'splited', 20, 1, 1, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-21-13-49', '2023/02/15', 1, 0, 1, 0, 0, 0, 0, 1),
(124, 0, '(256,256)', 'splited', 20, 1, 2, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-21-36-05', '2023/02/15', 1, 0, 1, 1, 0, 1, 0, 0),
(125, 0, '(256,256)', 'splited', 5, 1, 2, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-21-38-33', '2023/02/15', 1, 0, 1, 0, 0, 1, 1, 1),
(126, 0, '(256,256)', 'splited', 2, 1, 4, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-15-21-44-11', '2023/02/15', 1, 0, 1, 0, 0, 1, 0, 0),
(127, 0, '(256,256)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-18-14-33-18', '2023/02/18', 1, 0, 1, 0, 0, 1, 0, 0),
(128, 0, '(256,256)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-18-14-35-10', '2023/02/18', 1, 0, 1, 0, 0, 1, 0, 0),
(129, 0, '(256,256)', 'splited', 2, 0, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-18-14-48-05', '2023/02/18', 1, 0, 1, 1, 0, 1, 1, 1),
(130, 0, '(256,256)', 'splited', 2, 1, 8, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-18-16-17-01', '2023/02/18', 1, 0, 0, 0, 0, 1, 0, 0),
(131, 0, '(256,256)', 'splited', 2, 1, 2, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-18-16-43-08', '2023/02/18', 1, 0, 0, 0, 0, 1, 0, 0),
(132, 0, '(256,256)', 'splited', 2, 1, 2, 0.001, 0.2, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-18-16-45-37', '2023/02/18', 1, 0, 1, 0, 0, 1, 0, 0),
(133, 0, '(256,256)', 'splited', 2, 1, 2, 0.001, 0.5, '[\'default_dataset/binary\']', 'default_dataset/weights/binary/2023-02-19-09-13-29', '2023/02/19', 1, 0, 0, 0, 0, 1, 1, 1);

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
(11, 0, 360, 0, 35, 10000000, 500, 1920, 1200, 16, 0, 0, 16, 0, 0, 10, 10, 0, 10, 10, '', 0, 0, 0, '0', 0, 0, 0),
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
  `date_` varchar(45) NOT NULL DEFAULT '01/01/1401',
  `pretrain_path` varchar(1000) NOT NULL DEFAULT ''
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `classification_models`
--

INSERT INTO `classification_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `lr`, `split_ratio`, `classes`, `loss`, `accuracy`, `precision_`, `recall`, `val_loss`, `val_accuracy`, `val_precision`, `val_recall`, `dataset_pathes`, `weights_path`, `date_`, `pretrain_path`) VALUES
(1, '1', '(224,224)', 'splited', 50, 32, 0.001, 0.2, ',4,2,1,8,', 0.8, 34, 78, 45, 1, 12, 34, 10, '[\'default_dataset/binary\']', 'default_dataset/weights/classification/multiclassmodel.h5', '1401/11/01', 'default_dataset/weights/classification/1401-11-01-10-04-55'),
(106, '0', '(224,224)', 'splited', 30, 16, 0.01, 0.2, ',4,2,1,', 0.013, 45, 45, 23, 0.9, 45, 24, 22, '[\'default_dataset/binary\', \'/home/reyhene/Desktop\', \'/home/reyhane/Dorsa\', \'/home/reyhane/pythonProjects/ trainApp_oxin_new\']', 'default_dataset/weights/classification/1401-10-22-07-48-06', '1401/10/22', 'default_dataset/weights/classifiction/1401-10-22-08-45-33');

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
  `path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `split_size` varchar(20) NOT NULL DEFAULT '(300, 300)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `datasets`
--

INSERT INTO `datasets` (`id`, `name`, `user_own`, `path`, `split_size`) VALUES
(0, 'default_dataset', 'Default', 'default_dataset', '(300, 300)');

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

INSERT INTO `defects_info` (`id`, `name`, `short_name`, `defect_ID`, `is_defect`, `groupp`, `level`, `color`, `date`) VALUES
(1, 'NO LABEL', 'no lbl', '0', 'No', '0', '0', '#FFFFFF', '2023/02/22'),
(2, 'defect1', 'd1', '121', 'yes', '1', '0', '#05d2d2', '2023/02/22'),
(3, 'defect2', 'd2', '122', 'yes', '3', '1', '#99207b', '2023/02/22'),
(4, 'defect3', 'd3', '123', 'yes', '4', '2', '#d20505', '2023/02/22'),
(5, 'defect4', 'd4', '124', 'yes', '4', '2', '#8fab13', '2023/02/22');

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
(29, 'gp4', '4', '7/2/1401', 'yes'),
(30, 'No Defect', '0', '1401/05/26', 'no');

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
(10, '0', '', '(224,224)', '1', 2, 1, 0.001, 0.2, 0.764264, 0.586955, 0.310854, 0.449099, 1.02973, 0.968658, 0.000303313, 0.000606067, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/low_unet.h5', '2023/02/18'),
(11, '0', '', '(256,256)', '1', 5, 2, 0.01, 0.5, 0.787259, 0.510691, 0.134556, 0.210921, 1.77183, 0.808456, 0.000000000424284, 0.000000000424284, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-10-08-30', '2023/02/19'),
(12, '0', '', '(256,256)', '1', 10, 1, 0.001, 0.2, 0.857866, 0.486687, 0.205579, 0.295589, 2.08094, 0.726761, 0.00303876, 0.00604947, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-15-49-51', '2023/02/19'),
(13, '0', '', '(256,256)', '1', 2, 2, 0.001, 0.2, 0.838796, 0.590189, 0.150817, 0.249161, 1.43944, 0.716334, 0.00218703, 0.00436151, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-23-38-44', '2023/02/19'),
(14, '1', '/home/reyhane/PythonProjects/trainApp_oxin_new/default_dataset/weights/localization/2023-02-19-23-36-05/localization_model.h5', '(256,256)', '1', 2, 1, 0.001, 0.2, 0.809231, 0.760735, 0.0718374, 0.102411, 2.04686, 0.745753, 0.00174496, 0.00347174, '[\'default_dataset/localization\']', 'default_dataset/weights/localization/2023-02-19-23-40-50', '2023/02/19');

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
-- Table structure for table `piplines`
--

CREATE TABLE `piplines` (
  `id` int NOT NULL,
  `name` varchar(45) NOT NULL DEFAULT 'pipline1',
  `user_own` varchar(45) NOT NULL DEFAULT 'test',
  `binary_weight_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `localization_weight_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `classification_weight_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `yolo_weight_path` varchar(1000) NOT NULL DEFAULT 'null',
  `pipline_type` varchar(30) NOT NULL DEFAULT 'BY'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `piplines`
--

INSERT INTO `piplines` (`id`, `name`, `user_own`, `binary_weight_path`, `localization_weight_path`, `classification_weight_path`, `yolo_weight_path`, `pipline_type`) VALUES
(14, 'jj', 'test', 'default_dataset/weights/binary/binarymodeltemp.h5', '', '', 'default_dataset/weights/yolo/yolov5s.pt', 'BY'),
(15, 'test', 'test', 'default_dataset/weights/binary/binarymodeltemp.h5', 'default_dataset/weights/localization/low_unet.h5', 'default_dataset/weights/classification/multiclassmodel.h5', 'default_dataset/weights/yolo/yolov5s.pt', 'BSC'),
(16, 'test1', 'test', 'default_dataset/weights/binary/binarymodeltemp.h5', 'default_dataset/weights/localization/low_unet.h5', 'null', 'default_dataset/weights/yolo/yolov5s.pt', 'BSY'),
(17, 'test2', 'test', 'default_dataset/weights/binary/binarymodeltemp.h5', 'default_dataset/weights/localization/low_unet.h5', 'null', 'null', 'BS');

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
  `parent_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `suggestions_path` varchar(2000) DEFAULT NULL,
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
  `pipeline_json_path` varchar(500) NOT NULL DEFAULT 'NULL',
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
  `width_down_th` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `parent_path`, `suggestions_path`, `path_dataset`, `font_style`, `font_size`, `window_style`, `window_color`, `language`, `large_rect_area`, `small_rect_area`, `rect_accuracy`, `split_size`, `n_defect_colors`, `path_dataset_user`, `path_weights`, `camera_live_drive`, `live_drive_max_used_ratio`, `live_drive_remove_stop_ratio`, `plc_ip`, `pipeline_json_path`, `pipeline_json_path_o`, `result_path`, `manual_plc`, `plc_update_time`, `wind_duration`, `automatic_wind`, `auto_wind_intervals`, `manual_cameras`, `frame_rate`, `live_update_time`, `sound_warning`, `warning_alarm`, `nonallowed_frames`, `defect_percent`, `width_up_th`, `width_down_th`) VALUES
(0, 'oxin_image_grabber', 'oxin_image_grabber_suggestions', 'dataset', 'Ubuntu', 11, 'Windows', '#144475', 'English', 2000, 1000, 0.9, '(100, 100)', 6, 'dataset', 'weights', 'D:', 63, 60, 'opc.tcp://127.0.0.1:8081', 'evaluated_jsons', 'pipelines', 'oxin_image_grabber', 'True', 2000, 5, 'True', 5000, 'True', 7, 130, 'False', '3.mp3', 5, 20, 50, 50);

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
  `length` float DEFAULT NULL,
  `width` float DEFAULT NULL,
  `thickness` float DEFAULT NULL,
  `user` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `date` varchar(45) DEFAULT NULL,
  `main_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `nframe` int DEFAULT '0',
  `cameras` varchar(45) DEFAULT '0-12',
  `image_format` varchar(10) DEFAULT '.jpg'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sheets_info`
--

INSERT INTO `sheets_info` (`id`, `sheet_id`, `heat_number`, `ps_number`, `pdl_number`, `length`, `width`, `thickness`, `user`, `time`, `date`, `main_path`, `nframe`, `cameras`, `image_format`) VALUES
(149, '900AG', '347', '835', 944, 9312, 3041, 31, 'root', '07:25:09', '2023/05/27', '/media/reyhane/782F28BD242E495A/oxin_image_grabber', 37, '1-10', '.png'),
(150, '938ob', '439', '133', 462, 8967, 3046, 26, 'root', '07:25:22', '2023/05/27', '/media/reyhane/782F28BD242E495A/oxin_image_grabber', 31, '1-10', '.png'),
(151, '9708U', '823', '779', 335, 8089, 2970, 15, 'root', '07:25:33', '2023/05/27', '/media/reyhane/782F28BD242E495A/oxin_image_grabber', 28, '1-10', '.png'),
(152, '900mF', '477', '581', 917, 6017, 3029, 35, 'root', '08:11:00', '2023/05/27', '/media/reyhane/782F28BD242E495A/oxin_image_grabber', 27, '1-10', '.png'),
(153, '928G9', '274', '481', 388, 5696, 3036, 26, 'root', '08:11:13', '2023/05/27', '/media/reyhane/782F28BD242E495A/oxin_image_grabber', 23, '1-10', '.png'),
(154, '952Cb', '783', '502', 593, 9652, 2954, 13, 'root', '08:11:24', '2023/05/27', '/media/reyhane/782F28BD242E495A/oxin_image_grabber', 28, '1-10', '.png');

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
-- Table structure for table `storage_settings`
--

CREATE TABLE `storage_settings` (
  `id` int NOT NULL,
  `storage_upper_limit` int NOT NULL,
  `storage_lower_limit` int NOT NULL,
  `ssd_images_path` varchar(1000) NOT NULL,
  `ssd_datasets_path` varchar(1000) NOT NULL,
  `hdd_path` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `storage_settings`
--

INSERT INTO `storage_settings` (`id`, `storage_upper_limit`, `storage_lower_limit`, `ssd_images_path`, `ssd_datasets_path`, `hdd_path`) VALUES
(1, 15, 10, '/home/reyhane/PythonProjects/Oxin_Softwares/trainApp_oxin_new/oxin_image_grabber', '/home/reyhane/Desktop/default_dataset', '/media/reyhane/782F28BD242E495A/oxin_image_grabber');

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
(33, 'Dorsa_Admin', 'Dorsa1400@', 'DORSA', '0', '1401/05/26', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `yolo_models`
--

CREATE TABLE `yolo_models` (
  `id` int NOT NULL,
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
  `val_cls_loss` float NOT NULL DEFAULT '0.01'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `yolo_models`
--

INSERT INTO `yolo_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `split_ratio`, `dataset_pathes`, `weights_path`, `lr`, `date_`, `classes`, `box_loss`, `obj_loss`, `cls_loss`, `val_precision`, `val_recall`, `val_mAP_0.5`, `val_mAP_0.5:0.95`, `val_box_loss`, `val_obj_loss`, `val_cls_loss`) VALUES
(1, '1', '(224,224)', 'splited', 10, 1, 0.2, '\'default_dataset\'', 'default_dataset/weights/yolo/yolov5s.pt', 0.001, '\'2/4/1300\'', ',2,5,6,', 0.01, 0.01, 0.01, 70, 70, 70, 70, 0.02, 0.02, 0.02),
(2, '4', '(224,224)', 'splited', 10, 1, 0.2, '\'default_dataset\'', 'default_dataset/weights/yolo/yolov5x.pt', 0.001, '\'2/4/1300\'', ',2,5,6,', 0.01, 0.01, 0.01, 70, 70, 70, 70, 0.02, 0.02, 0.02);

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
-- Indexes for table `storage_settings`
--
ALTER TABLE `storage_settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `yolo_models`
--
ALTER TABLE `yolo_models`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `binary_models`
--
ALTER TABLE `binary_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=134;

--
-- AUTO_INCREMENT for table `classification_models`
--
ALTER TABLE `classification_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;

--
-- AUTO_INCREMENT for table `database_config`
--
ALTER TABLE `database_config`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `datasets`
--
ALTER TABLE `datasets`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `defect_groups`
--
ALTER TABLE `defect_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `localization_models`
--
ALTER TABLE `localization_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `plc_path`
--
ALTER TABLE `plc_path`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `sheets_info`
--
ALTER TABLE `sheets_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=155;

--
-- AUTO_INCREMENT for table `storage_settings`
--
ALTER TABLE `storage_settings`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `yolo_models`
--
ALTER TABLE `yolo_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
