-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 22, 2023 at 07:08 AM
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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `multi_tasking`
--
ALTER TABLE `multi_tasking`
  ADD PRIMARY KEY (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
