-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2023 at 01:53 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sportsscoreresult`
--

-- --------------------------------------------------------

--
-- Table structure for table `overchampion`
--

CREATE TABLE `overchampion` (
  `event` varchar(20) NOT NULL,
  `Category` varchar(30) NOT NULL,
  `name` varchar(70) NOT NULL,
  `Department` varchar(45) NOT NULL,
  `Position` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `overchampion`
--

INSERT INTO `overchampion` (`event`, `Category`, `name`, `Department`, `Position`) VALUES
('Sports Event', 'Over All Championship', '2016-2017 Won 17 Games over all the depa', 'Department of Mathematics', 'Winner'),
('Sports Event', 'Over All Championship', '2017-2018 Won 20 Games over all the depa', 'Department of Computer Science', 'Winner'),
('Sports Event', 'Over All Championship', '2018-2019 Won 16 Games over all the depa', 'Department of RDS', 'Winner'),
('Sports Event', 'Over All Championship', '2020-2021 Won 22 Games over all the depa', 'Department of Chemistry', 'Winner'),
('Sports Event', 'Over All Championship', '2021-2022 Won 20 Games over all the depa', 'Department of Mathematics', 'Winner'),
('Sports Event', 'Over All Championship', '2022-2023 Won 23 Games over all the depa', 'Department of Mathematics', 'Winner');

-- --------------------------------------------------------

--
-- Table structure for table `singleplayer`
--

CREATE TABLE `singleplayer` (
  `event` varchar(20) NOT NULL,
  `Category` varchar(30) NOT NULL,
  `name` varchar(25) NOT NULL,
  `Department` varchar(50) NOT NULL,
  `Position` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `singleplayer`
--

INSERT INTO `singleplayer` (`event`, `Category`, `name`, `Department`, `Position`) VALUES
('Running Race', 'Single Player', 'B.Praveenraj', 'Department of Computer Science', 'Winner'),
('Running race', 'Single Player', 'A.Ashok', 'Department of Mathematics', '1st Runnner Up'),
('Running race', 'Single Player', 'S.Subash', 'Department of English', '2nd Runner Up'),
('Shot Put', 'Single Player', 'S.Surya', 'Department of Chemistry', 'Winner'),
('Shot Put', 'Single Player', 'K.Raja', 'Department of Mathematics', '1st Runnner Up'),
('Shot Put', 'Single Player', 'T.Sundar', 'Department of Tamil', '2nd Runner Up'),
('Long  Jump', 'Single Player', 'P.Mohan', 'Department of RDS', 'Winner'),
('Long Jump', 'Single Player', 'H.Guna', 'Department of Physics', '1st Runnner Up'),
('Long Jump', 'Single Player', 'N.Mooventiran', 'Department of Computer Science', '2nd Runner Up'),
('Running race', 'Single player', 'praveenraj', 'COMPUTER', 'Winner'),
('Running race', 'Single player', 'Bharath', 'CHEMISTRY', '1st RunnerUp'),
('Running race', 'Single player', 'Deva', 'RURAL DEVELOPMENT SCIENCE', '2nd RunnerUp');

-- --------------------------------------------------------

--
-- Table structure for table `teamplayer`
--

CREATE TABLE `teamplayer` (
  `event` varchar(20) NOT NULL,
  `Category` varchar(30) NOT NULL,
  `name` varchar(30) NOT NULL,
  `Department` varchar(35) NOT NULL,
  `Position` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `teamplayer`
--

INSERT INTO `teamplayer` (`event`, `Category`, `name`, `Department`, `Position`) VALUES
('Football', 'Team Players', 'Team C', 'Department of Computer Science', 'Winner'),
('Football', 'Team Players', 'Team E', 'Department of Physics', '1st Runnner Up'),
('Football', 'Team Players', 'Team A', 'Department of Tamil', '2nd Runner Up'),
('Kabadi', 'Team Players', 'Team B', 'Department of Chemistry', 'Winner'),
('Kabadi', 'Team Players', 'Team A', 'Department of RDS', '1st Runnner Up'),
('Kabadi', 'Team Players', 'Team C', 'Department of English', '2nd Runnerup'),
('Volleyball', 'Team Players', 'Team D', 'Department of Tamil', 'Winner'),
('Volleyball', 'Team Players', 'Team C', 'Department of Computer Science', '1st Runnner Up'),
('Volleyball', 'Team Players', 'Team A', 'Department of English', '2nd Runnerup'),
('Hockey', 'Team Players', 'Team L', 'COMPUTER', 'Winner');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
