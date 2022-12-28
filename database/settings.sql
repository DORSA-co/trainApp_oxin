-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 17, 2022 at 06:58 AM
-- Server version: 8.0.29-0ubuntu0.20.04.3
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
  `parent_path` varchar(45) DEFAULT NULL,
  `font_style` varchar(45) NOT NULL DEFAULT 'Arial',
  `font_size` int NOT NULL DEFAULT '10',
  `window_style` varchar(45) NOT NULL DEFAULT 'Windows',
  `window_color` varchar(45) NOT NULL DEFAULT 'blue',
  `language` varchar(45) NOT NULL DEFAULT 'English',
  `large_rect_area` int NOT NULL DEFAULT '0',
  `small_rect_area` int NOT NULL DEFAULT '0',
  `rect_accuracy` float NOT NULL DEFAULT '0.9',
  `n_defect_colors` int NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`id`, `parent_path`, `font_style`, `font_size`, `window_style`, `window_color`, `language`, `large_rect_area`, `small_rect_area`, `rect_accuracy`, `n_defect_colors`) VALUES
(0, 'oxin_image_grabber', 'Times New Roman', 11, 'Windows', '#144475', 'Persian', 2000, 1000, 0.9, 6);

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
