-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 21, 2023 at 05:32 AM
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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
