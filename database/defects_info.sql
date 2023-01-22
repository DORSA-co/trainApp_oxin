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
(1, 'NO LABEL', 'LABEL', '0', 'No', '0', '0', '#FFFFFF', '7/2/1401'),
(2, 'd2', 'd2', '2', 'no', '1', '0', '#05d2d2', '7/2/1401'),
(3, 'd3', 'd3', '3', 'yes', '4', '1', '#05d2d2', '17/02/1401'),
(4, 'd1', 'd1', '1', 'yes', '4', '2', '#d20505', '7/2/1401'),
(5, 'd4', 'd4', '4', 'yes', '4', '2', '#980404', '7/2/1401'),
(62, 'defect101', 'd101', '101', 'no', '0', '0', '#a1afae', '07/10/2022'),
(63, 'defect102', 'd102', '102', 'yes', '4', '1', '#b0311d', '07/10/2022'),
(64, 'defect103', 'd103', '103', 'no', '0', '2', '#e2859e', '07/10/2022'),
(65, 'defect104', 'd104', '104', 'yes', '4', '0', '#e0c0f7', '07/10/2022'),
(66, 'defect105', 'd105', '105', 'yes', '4', '1', '#e7e610', '07/10/2022'),
(67, 'defect106', 'd106', '106', 'no', '0', '0', '#0c51b7', '07/10/2022'),
(68, 'defect107', 'd107', '107', 'no', '3', '2', '#64ffc4', '07/10/2022'),
(69, 'defect108', 'd108', '108', 'no', '0', '0', '#0cd2d0', '07/10/2022'),
(70, 'defect109', 'd109', '109', 'yes', '4', '1', '#a3bafa', '07/10/2022'),
(71, 'defect110', 'd110', '110', 'no', '3', '1', '#1e6c28', '07/10/2022'),
(72, 'defect111', 'd111', '111', 'no', '0', '1', '#91f638', '07/10/2022'),
(73, 'defect112', 'd112', '112', 'no', '0', '1', '#a76f1a', '07/10/2022'),
(74, 'defect113', 'd113', '113', 'no', '1', '1', '#ac2d10', '07/10/2022'),
(75, 'defect114', 'd114', '114', 'yes', '4', '2', '#698422', '07/10/2022'),
(76, 'defect115', 'd115', '115', 'no', '0', '1', '#b215d0', '07/10/2022'),
(77, 'defect116', 'd116', '116', 'no', '0', '0', '#c37f4c', '07/10/2022'),
(78, 'defect117', 'd117', '117', 'no', '3', '2', '#764deb', '07/10/2022'),
(79, 'defect118', 'd118', '118', 'yes', '4', '0', '#efa2ec', '07/10/2022'),
(80, 'defect119', 'd119', '119', 'yes', '4', '0', '#0ad04e', '07/10/2022'),
(81, 'defect120', 'd120', '120', 'no', '1', '2', '#be5ca7', '07/10/2022'),
(82, 'defect121', 'd121', '121', 'no', '0', '1', '#0c7cfd', '07/10/2022'),
(83, 'defect122', 'd122', '122', 'no', '1', '1', '#0d44a8', '07/10/2022'),
(84, 'defect123', 'd123', '123', 'no', '3', '0', '#0a1b9a', '07/10/2022'),
(85, 'defect124', 'd124', '124', 'no', '3', '2', '#f333db', '07/10/2022'),
(86, 'defect125', 'd125', '125', 'no', '1', '2', '#688aac', '07/10/2022'),
(87, 'defect126', 'd126', '126', 'no', '0', '1', '#2f4d70', '07/10/2022'),
(88, 'defect127', 'd127', '127', 'yes', '4', '2', '#9378eb', '07/10/2022'),
(89, 'defect128', 'd128', '128', 'yes', '4', '1', '#599e25', '07/10/2022'),
(90, 'defect129', 'd129', '129', 'yes', '4', '1', '#897a2b', '07/10/2022'),
(91, 'defect130', 'd130', '130', 'no', '3', '2', '#135447', '07/10/2022'),
(92, 'defect131', 'd131', '131', 'yes', '4', '2', '#f4cd7e', '07/10/2022'),
(93, 'defect132', 'd132', '132', 'yes', '4', '0', '#1f3aec', '07/10/2022'),
(94, 'defect133', 'd133', '133', 'no', '0', '2', '#754e64', '07/10/2022'),
(95, 'defect134', 'd134', '134', 'no', '3', '2', '#5f1c83', '07/10/2022'),
(96, 'defect135', 'd135', '135', 'no', '0', '1', '#3e301c', '07/10/2022'),
(97, 'defect136', 'd136', '136', 'yes', '4', '2', '#a1ce53', '07/10/2022'),
(98, 'defect137', 'd137', '137', 'no', '3', '1', '#fee0bc', '07/10/2022'),
(99, 'defect138', 'd138', '138', 'no', '1', '0', '#2df267', '07/10/2022'),
(100, 'defect139', 'd139', '139', 'yes', '4', '0', '#1659ca', '07/10/2022'),
(101, 'defect140', 'd140', '140', 'yes', '4', '2', '#4f77c0', '07/10/2022'),
(102, 'defect141', 'd141', '141', 'no', '1', '2', '#e0bcd1', '07/10/2022'),
(103, 'defect142', 'd142', '142', 'yes', '4', '2', '#099ef7', '07/10/2022'),
(104, 'defect143', 'd143', '143', 'no', '0', '2', '#8cb7a3', '07/10/2022'),
(105, 'defect144', 'd144', '144', 'no', '3', '1', '#5174cf', '07/10/2022'),
(106, 'defect145', 'd145', '145', 'no', '3', '0', '#ab3edf', '07/10/2022'),
(107, 'defect146', 'd146', '146', 'no', '1', '1', '#1d92b5', '07/10/2022'),
(108, 'defect147', 'd147', '147', 'no', '0', '0', '#b6d638', '07/10/2022'),
(109, 'defect148', 'd148', '148', 'no', '0', '0', '#dbd16b', '07/10/2022'),
(110, 'defect149', 'd149', '149', 'no', '3', '0', '#44286c', '07/10/2022'),
(111, 'defect150', 'd150', '150', 'no', '1', '2', '#cca5ba', '07/10/2022'),
(112, 'defect151', 'd151', '151', 'yes', '4', '1', '#1f2630', '07/10/2022'),
(113, 'defect152', 'd152', '152', 'no', '3', '0', '#ac50a7', '07/10/2022'),
(114, 'defect153', 'd153', '153', 'no', '1', '0', '#053543', '07/10/2022'),
(115, 'defect154', 'd154', '154', 'yes', '4', '0', '#533fe5', '07/10/2022'),
(116, 'defect155', 'd155', '155', 'no', '3', '1', '#ad4dae', '07/10/2022'),
(117, 'defect156', 'd156', '156', 'no', '0', '2', '#48634c', '07/10/2022'),
(118, 'defect157', 'd157', '157', 'no', '0', '2', '#43b6db', '07/10/2022'),
(119, 'defect158', 'd158', '158', 'no', '1', '0', '#0077fd', '07/10/2022'),
(120, 'defect159', 'd159', '159', 'no', '1', '2', '#9da9d4', '07/10/2022'),
(121, 'defect160', 'd160', '160', 'no', '0', '1', '#474031', '07/10/2022'),
(122, 'defect161', 'd161', '161', 'no', '3', '1', '#1ca29b', '07/10/2022'),
(123, 'defect162', 'd162', '162', 'no', '0', '1', '#38a6f4', '07/10/2022'),
(124, 'defect163', 'd163', '163', 'no', '0', '1', '#f7e42d', '07/10/2022'),
(125, 'defect164', 'd164', '164', 'no', '1', '2', '#bdad10', '07/10/2022'),
(126, 'defect165', 'd165', '165', 'no', '3', '1', '#743434', '07/10/2022'),
(127, 'defect166', 'd166', '166', 'no', '1', '0', '#bbc317', '07/10/2022'),
(128, 'defect167', 'd167', '167', 'no', '1', '2', '#04f725', '07/10/2022'),
(129, 'defect168', 'd168', '168', 'no', '0', '1', '#0b75aa', '07/10/2022'),
(130, 'defect169', 'd169', '169', 'no', '1', '2', '#a63da2', '07/10/2022'),
(131, 'defect170', 'd170', '170', 'no', '0', '1', '#42f0c8', '07/10/2022'),
(132, 'defect171', 'd171', '171', 'yes', '4', '2', '#eb97a2', '07/10/2022'),
(133, 'defect172', 'd172', '172', 'no', '0', '0', '#0feb26', '07/10/2022'),
(134, 'defect173', 'd173', '173', 'no', '0', '2', '#6f992c', '07/10/2022'),
(135, 'defect174', 'd174', '174', 'no', '3', '1', '#b08e73', '07/10/2022'),
(136, 'defect175', 'd175', '175', 'no', '1', '0', '#6af388', '07/10/2022'),
(137, 'defect176', 'd176', '176', 'no', '0', '1', '#ed3f84', '07/10/2022'),
(138, 'defect177', 'd177', '177', 'no', '0', '2', '#091644', '07/10/2022'),
(139, 'defect178', 'd178', '178', 'no', '0', '1', '#15cb96', '07/10/2022'),
(140, 'defect179', 'd179', '179', 'no', '0', '1', '#0f576e', '07/10/2022'),
(141, 'defect180', 'd180', '180', 'no', '0', '0', '#d3f777', '07/10/2022'),
(142, 'defect181', 'd181', '181', 'no', '0', '1', '#51d955', '07/10/2022'),
(143, 'defect182', 'd182', '182', 'no', '0', '2', '#7b401c', '07/10/2022'),
(144, 'defect183', 'd183', '183', 'no', '3', '1', '#5b827d', '07/10/2022'),
(145, 'defect184', 'd184', '184', 'yes', '4', '1', '#0975e1', '07/10/2022'),
(146, 'defect185', 'd185', '185', 'no', '0', '2', '#8e1ce1', '07/10/2022'),
(147, 'defect186', 'd186', '186', 'no', '3', '2', '#2c3b4a', '07/10/2022'),
(148, 'defect187', 'd187', '187', 'yes', '4', '2', '#2193cf', '07/10/2022'),
(149, 'defect188', 'd188', '188', 'no', '3', '2', '#3b62c4', '07/10/2022'),
(150, 'defect189', 'd189', '189', 'no', '0', '0', '#aeebf3', '07/10/2022'),
(151, 'defect190', 'd190', '190', 'no', '0', '2', '#37ae47', '07/10/2022'),
(152, 'defect191', 'd191', '191', 'no', '0', '0', '#a5d21a', '07/10/2022'),
(153, 'defect192', 'd192', '192', 'no', '3', '2', '#71b1fa', '07/10/2022'),
(154, 'defect193', 'd193', '193', 'yes', '4', '2', '#0414b0', '07/10/2022'),
(155, 'defect194', 'd194', '194', 'yes', '4', '2', '#188b67', '07/10/2022'),
(156, 'defect195', 'd195', '195', 'no', '1', '1', '#26fb63', '07/10/2022'),
(157, 'defect196', 'd196', '196', 'no', '1', '2', '#a6d650', '07/10/2022'),
(158, 'defect197', 'd197', '197', 'no', '1', '2', '#1c2d23', '07/10/2022'),
(159, 'defect198', 'd198', '198', 'no', '1', '2', '#cc383d', '07/10/2022'),
(160, 'defect199', 'd199', '199', 'yes', '4', '2', '#683f8f', '07/10/2022'),
(161, 'defect200', 'd200', '200', 'no', '0', '0', '#8ba4f7', '07/10/2022'),
(162, 'defect201', 'd201', '201', 'no', '3', '2', '#7d81d2', '07/10/2022');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `defects_info`
--
ALTER TABLE `defects_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `defects_info`
--
ALTER TABLE `defects_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=163;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;