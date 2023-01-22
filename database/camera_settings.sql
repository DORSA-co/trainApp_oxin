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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `camera_settings`
--
ALTER TABLE `camera_settings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id_UNIQUE` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
