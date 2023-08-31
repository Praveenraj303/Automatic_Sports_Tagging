-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 21, 2023 at 01:51 PM
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
-- Database: `addevent`
--

-- --------------------------------------------------------

--
-- Table structure for table `viewevent`
--

CREATE TABLE `viewevent` (
  `ename` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  `description` varchar(60) NOT NULL,
  `start_date` varchar(35) NOT NULL,
  `end_date` varchar(20) NOT NULL,
  `time` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `viewevent`
--

INSERT INTO `viewevent` (`ename`, `type`, `description`, `start_date`, `end_date`, `time`) VALUES
('Running Race', 'outdoor', 'Single player game 100 Meter race', '2023-04-05', '2023-04-05', '10:00'),
('Kho Kho', 'outdoor', 'Team Game need 12 players', '2023-04-15', '2023-04-17', '10:30'),
('Football', 'outdoor', 'Team Game need 11 players', '2023-04-20', '2023-04-22', '04.00'),
('Vollyball', 'outdoor', 'Team Game need 6 players', '2023-04-18', '2023-04-20', '12:00'),
('Kabadi', 'outdoor', 'Team Game need 7 players', '2023-04-20', '2023-04-22', '10:00'),
('Table Tennis', 'indoor', '3 Round selection', '2023-04-04', '2023-04-04', '10:30'),
('High Jump', 'outoor', 'Each member have 3 chances,scored based on height', '2023-04-13', '2023-04-13', '10:00');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
