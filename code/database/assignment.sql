-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 07, 2020 at 02:01 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 5.6.40

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `assignment`
--

-- --------------------------------------------------------

--
-- Table structure for table `assets`
--

CREATE TABLE `assets` (
  `ID_asset` int(2) NOT NULL,
  `asset_name` varchar(50) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `assets`
--

INSERT INTO `assets` (`ID_asset`, `asset_name`) VALUES
(1, 'Afili Ask '),
(2, 'The blacklist');

-- --------------------------------------------------------

--
-- Table structure for table `extracted_video_source`
--

CREATE TABLE `extracted_video_source` (
  `ID_video_source` int(2) NOT NULL,
  `video_source_url` varchar(600) NOT NULL,
  `ID_asset` int(2) UNSIGNED NOT NULL,
  `extracted_from` int(2) NOT NULL,
  `screenshout_path` varchar(600) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `keywords`
--

CREATE TABLE `keywords` (
  `ID_keyword` int(2) NOT NULL,
  `ID_asset` int(2) NOT NULL,
  `keyword` varchar(50) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `keywords`
--

INSERT INTO `keywords` (`ID_keyword`, `ID_asset`, `keyword`) VALUES
(1, 1, 'Afili Ask '),
(2, 1, 'الحب ورطة'),
(3, 2, 'the blacklist');

-- --------------------------------------------------------

--
-- Table structure for table `website_name`
--

CREATE TABLE `website_name` (
  `ID_website` int(2) NOT NULL,
  `website_name` varchar(50) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `website_name`
--

INSERT INTO `website_name` (`ID_website`, `website_name`) VALUES
(1, 'https://www.cimaclub.io'),
(2, 'https://cimaflash.me');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `assets`
--
ALTER TABLE `assets`
  ADD PRIMARY KEY (`ID_asset`);

--
-- Indexes for table `extracted_video_source`
--
ALTER TABLE `extracted_video_source`
  ADD PRIMARY KEY (`ID_video_source`);

--
-- Indexes for table `keywords`
--
ALTER TABLE `keywords`
  ADD PRIMARY KEY (`ID_keyword`);

--
-- Indexes for table `website_name`
--
ALTER TABLE `website_name`
  ADD PRIMARY KEY (`ID_website`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `assets`
--
ALTER TABLE `assets`
  MODIFY `ID_asset` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `extracted_video_source`
--
ALTER TABLE `extracted_video_source`
  MODIFY `ID_video_source` int(2) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `keywords`
--
ALTER TABLE `keywords`
  MODIFY `ID_keyword` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `website_name`
--
ALTER TABLE `website_name`
  MODIFY `ID_website` int(2) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
