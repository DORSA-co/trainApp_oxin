-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 21, 2023 at 05:31 AM
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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `plc_path`
--
ALTER TABLE `plc_path`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `plc_path`
--
ALTER TABLE `plc_path`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
