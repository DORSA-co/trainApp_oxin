-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 22, 2023 at 07:09 AM
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
(52, '900Xg', '410', '266', 777, 6927, 2957, 26, 'root', '10:05:59', '1401/10/29', 'oxin_image_grabber', 17, '1-4', '.png'),
(53, '926Yt', '199', '666', 946, 9728, 3022, 14, 'root', '10:06:09', '1401/10/29', 'oxin_image_grabber', 17, '1-8', '.png'),
(54, '9500v', '588', '160', 742, 1354, 2955, 34, 'root', '10:06:19', '1401/10/29', 'oxin_image_grabber', 17, '1-4', '.png'),
(55, '9746S', '969', '735', 980, 1220, 2967, 18, 'root', '10:16:19', '1401/10/29', 'oxin_image_grabber', 13, '1-6', '.png'),
(56, '991LD', '552', '234', 297, 3453, 2979, 25, 'root', '10:16:29', '1401/10/29', 'oxin_image_grabber', 11, '1-8', '.png'),
(57, '1008nA', '925', '917', 778, 9565, 2974, 49, 'root', '10:18:09', '1401/10/29', 'oxin_image_grabber', 17, '1-12', '.png'),
(58, '1030yP', '907', '352', 272, 6906, 3008, 17, 'root', '10:18:19', '1401/10/29', 'oxin_image_grabber', 17, '1-10', '.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `sheets_info`
--
ALTER TABLE `sheets_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sheets_info`
--
ALTER TABLE `sheets_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=59;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
