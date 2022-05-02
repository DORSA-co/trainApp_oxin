-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 30, 2022 at 03:19 PM
-- Server version: 8.0.28-0ubuntu0.20.04.3
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
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `id` int NOT NULL,
  `parent_path` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `path_dataset` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `font_style` varchar(45) NOT NULL DEFAULT 'Arial',
  `font_size` int NOT NULL DEFAULT '10',
  `window_style` varchar(45) NOT NULL DEFAULT 'Windows',
  `window_color` varchar(45) NOT NULL DEFAULT 'blue',
  `language` varchar(45) NOT NULL DEFAULT 'English',
  `split_size` varchar(45) DEFAULT NULL,
  `path_weights` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `path_dataset_user` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `parent_path`, `path_dataset`, `font_style`, `font_size`, `window_style`, `window_color`, `language`, `split_size`, `path_weights`, `path_dataset_user`) VALUES
(0, '/home/reyhane/oxin_image_grabber', '/home/reyhane/PycharmProjects/trainApp_oxin1/dataset/', 'Arial', 9, 'Windows', '#144475', 'English', '(300, 300)', '/home/reyhane/PycharmProjects/trainApp_oxin1/weights/', '/home/reyhane/PycharmProjects/trainApp_oxin1/dataset_user/');

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
