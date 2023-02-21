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

--
-- Indexes for dumped tables
--

--
-- Indexes for table `defect_groups`
--
ALTER TABLE `defect_groups`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `defect_groups`
--
ALTER TABLE `defect_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
