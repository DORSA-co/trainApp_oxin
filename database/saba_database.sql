-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 06, 2023 at 08:08 AM
-- Server version: 8.0.32-0ubuntu0.22.04.2
-- PHP Version: 8.1.2-1ubuntu2.11

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
  `algo_name` varchar(45) NOT NULL,
  `input_size` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `input_type` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `epochs` int NOT NULL,
  `batch_size` int NOT NULL,
  `lr` float NOT NULL,
  `tuning_epochs` int NOT NULL,
  `split_ratio` float NOT NULL,
  `dataset_pathes` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `accuracy` float NOT NULL,
  `loss` float NOT NULL,
  `precision_` float NOT NULL,
  `recall` float NOT NULL,
  `val_loss` float NOT NULL,
  `val_accuracy` float NOT NULL,
  `val_precision` float NOT NULL,
  `val_recall` float NOT NULL,
  `weights_path` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date_` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `binary_models`
--

INSERT INTO `binary_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `lr`, `tuning_epochs`, `split_ratio`, `dataset_pathes`, `accuracy`, `loss`, `precision_`, `recall`, `val_loss`, `val_accuracy`, `val_precision`, `val_recall`, `weights_path`, `date_`) VALUES
(145, '0', '(256,256)', '1', 5, 2, 0.001, 1, 0.2, '[\'default_dataset\']', 0.608696, 0, 0, 0, 0, 0.608696, 0, 0, 'default_dataset/weights/binary/2023-03-03-16-44-59', '2023/03/03'),
(146, '0', '(256,256)', '1', 5, 1, 0.001, 1, 0.2, '[\'default_dataset\']', 0.608696, 0, 0, 0, 0, 0.608696, 0, 0, 'default_dataset/weights/binary/2023-03-03-16-52-17', '2023/03/03'),
(147, '0', '(256,256)', '1', 5, 2, 0.001, 1, 0.2, '[\'default_dataset\']', 0.608696, 0, 0, 0, 0, 0.608696, 0, 0, 'default_dataset/weights/binary/2023-03-03-17-02-03', '2023/03/03');

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
(25, 'gp1', '1', '7/2/1401', 'yes'),
(28, 'gp2', '3', '7/2/1401', 'yes'),
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
  `algo_name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `pretrain_path` varchar(2000) NOT NULL,
  `input_size` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `input_type` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `epochs` int NOT NULL,
  `batch_size` int NOT NULL,
  `lr` float NOT NULL,
  `split_ratio` float NOT NULL,
  `loss` float NOT NULL,
  `accuracy` float NOT NULL,
  `iou` float NOT NULL,
  `fscore` float NOT NULL,
  `val_loss` float NOT NULL,
  `val_accuracy` float NOT NULL,
  `val_iou` float NOT NULL,
  `val_fscore` float NOT NULL,
  `dataset_pathes` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `weights_path` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date_` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
  `path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `binary_weight_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `localization_weight_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `classification_weight_path` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'null',
  `date_` varchar(45) NOT NULL DEFAULT '1/1/1401',
  `use_yolo` varchar(7) NOT NULL DEFAULT 'True'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `piplines`
--

INSERT INTO `piplines` (`id`, `name`, `user_own`, `path`, `binary_weight_path`, `localization_weight_path`, `classification_weight_path`, `date_`, `use_yolo`) VALUES
(1, 'pipline1', 'test', 'null', 'null', 'null', 'null', '1/1/1401', 'True'),
(2, 'pipline1', 'test', 'null', 'null', 'null', 'null', '1/1/1401', 'True'),
(12, 'milad2', 'test', 'Null', 'weights', 'weightspath', 'weightspath', '1/1/1401', 'True');

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
  `width_down_th` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `parent_path`, `path_dataset`, `font_style`, `font_size`, `window_style`, `window_color`, `language`, `large_rect_area`, `small_rect_area`, `rect_accuracy`, `split_size`, `n_defect_colors`, `path_dataset_user`, `path_weights`, `camera_live_drive`, `live_drive_max_used_ratio`, `live_drive_remove_stop_ratio`, `plc_ip`, `pipline_json_path`, `pipeline_json_path_o`, `result_path`, `manual_plc`, `plc_update_time`, `wind_duration`, `automatic_wind`, `auto_wind_intervals`, `manual_cameras`, `frame_rate`, `live_update_time`, `sound_warning`, `warning_alarm`, `nonallowed_frames`, `defect_percent`, `width_up_th`, `width_down_th`) VALUES
(0, 'oxin_image_grabber', 'dataset', 'Ubuntu', 11, 'Windows', '#144475', 'English', 2000, 1000, 0.9, '(100, 100)', 6, 'dataset', 'weights', 'D:', 63, 60, 'opc.tcp://127.0.0.1:8081', 'evaluated_jsons', 'pipelines', 'oxin_image_grabber', 'True', 2000, 5, 'True', 5000, 'True', 7, 130, 'False', '3.mp3', 5, 20, 50, 50);

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
(143, '900wB', '277', '550', 180, 4698, 3039, 15, 'root', '09:12:45', '2023/02/21', 'oxin_image_grabber', 17, '1-4', '.png');

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
(33, 'Dorsa_Admin', 'Dorsa1400@', 'DORSA', '0', '1401/05/26', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `yolo_models`
--

CREATE TABLE `yolo_models` (
  `id` int NOT NULL,
  `algo_name` varchar(45) NOT NULL,
  `input_size` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `input_type` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `epochs` int NOT NULL,
  `batch_size` int NOT NULL,
  `split_ratio` float NOT NULL,
  `box_loss` float NOT NULL,
  `obj_loss` float NOT NULL,
  `cls_loss` float NOT NULL,
  `val_precision` float NOT NULL,
  `val_recall` float NOT NULL,
  `val_mAP_50` float NOT NULL,
  `val_mAP_50_95` float NOT NULL,
  `val_box_loss` float NOT NULL,
  `val_obj_loss` float NOT NULL,
  `val_cls_loss` float NOT NULL,
  `dataset_pathes` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `weights_path` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date_` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `yolo_models`
--

INSERT INTO `yolo_models` (`id`, `algo_name`, `input_size`, `input_type`, `epochs`, `batch_size`, `split_ratio`, `box_loss`, `obj_loss`, `cls_loss`, `val_precision`, `val_recall`, `val_mAP_50`, `val_mAP_50_95`, `val_box_loss`, `val_obj_loss`, `val_cls_loss`, `dataset_pathes`, `weights_path`, `date_`) VALUES
(12, '0', '(256,256)', '1', 5, 16, 0.2, 0.123063, 0.0161485, 0.0536708, 0.000855065, 0.375, 0.0447805, 0.0186162, 0.118778, 0.00725914, 0.0523676, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-14-58-00', '2023/03/05'),
(13, '0', '(256,256)', '1', 20, 8, 0.2, 0.106677, 0.0185349, 0.0536978, 0.00436983, 0.916667, 0.187527, 0.0363611, 0.0941895, 0.00836772, 0.0544923, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-15-01-52', '2023/03/05'),
(14, '0', '(256,256)', '1', 2, 32, 0.2, 0.124175, 0.0183719, 0.0548606, 0.00156457, 0.583333, 0.00554461, 0.00244525, 0.129368, 0.00578719, 0.0485159, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-15-19-25', '2023/03/05'),
(15, '1', '(256,256)', '1', 5, 8, 0.3, 0.108646, 0.0220919, 0.051974, 0.00281771, 0.741667, 0.0171093, 0.00448128, 0.10548, 0.00926232, 0.0475607, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-15-21-30', '2023/03/05'),
(16, '2', '(256,256)', '0', 10, 4, 0.3, 0.12859, 0.0198422, 0.0507925, 0.00152672, 0.2, 0.04975, 0.024875, 0.127452, 0.0184363, 0.0503598, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-15-27-44', '2023/03/05'),
(17, '0', '(256,256)', '1', 1, 8, 0.2, 0.12585, 0.0189259, 0.053382, 0.00306098, 0.666667, 0.00574254, 0.0018457, 0.124571, 0.006136, 0.0474245, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-18-32', '2023/03/05'),
(18, '0', '(256,256)', '1', 1, 1, 0.2, 0.101614, 0.0158262, 0.0445821, 0.00317305, 0.75, 0.0329392, 0.00734397, 0.105507, 0.00623818, 0.0418865, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-22-09', '2023/03/05'),
(19, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(20, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(21, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(22, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(23, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(24, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(25, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(26, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(27, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(28, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(29, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(30, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(31, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(32, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05'),
(33, '0', '(256,256)', '1', 2, 2, 0.2, 0.122742, 0.0173663, 0.0537956, 0.001679, 0.458333, 0.0194206, 0.00238898, 0.110805, 0.00667135, 0.0445913, '[\'default_dataset\']', 'default_dataset/weights/localization_and_classification/2023-03-05-18-25-29', '2023/03/05');

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
-- Indexes for table `piplines`
--
ALTER TABLE `piplines`
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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=148;

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT for table `defects_info`
--
ALTER TABLE `defects_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=163;

--
-- AUTO_INCREMENT for table `defect_groups`
--
ALTER TABLE `defect_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `localization_models`
--
ALTER TABLE `localization_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `piplines`
--
ALTER TABLE `piplines`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `plc_path`
--
ALTER TABLE `plc_path`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT for table `sheets_info`
--
ALTER TABLE `sheets_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=144;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `yolo_models`
--
ALTER TABLE `yolo_models`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
