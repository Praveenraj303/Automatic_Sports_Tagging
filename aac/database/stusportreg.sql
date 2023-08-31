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
-- Database: `stusportreg`
--

-- --------------------------------------------------------

--
-- Table structure for table `badminton`
--

CREATE TABLE `badminton` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` varchar(25) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `badminton`
--

INSERT INTO `badminton` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('20csc138', 'Devakrishnan', 'mathematics', 'deva@gmail.com', 'Badminton', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `basketball`
--

CREATE TABLE `basketball` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` text NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `basketball`
--

INSERT INTO `basketball` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('19mat120', 'rahul', 'Chemistry', 'rahul@gmail.com', 'Basketball', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `football`
--

CREATE TABLE `football` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` varchar(25) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `football`
--

INSERT INTO `football` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('20csc125', 'raj', 'English', 'raj@gmail.com', 'Football', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `handball`
--

CREATE TABLE `handball` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` varchar(25) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `handball`
--

INSERT INTO `handball` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('20mat160', 'Ajay', 'Tamil', 'ajay@gmail.com', 'Handball', 'male', 'Madurai', 'Tamil Nadu'),
('20csc138', 'Navaneethan.S', 'computer science', 'navan@gmail.com', 'Handball', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `hockey`
--

CREATE TABLE `hockey` (
  `rollno` varchar(10) NOT NULL,
  `name` text NOT NULL,
  `department` varchar(25) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hockey`
--

INSERT INTO `hockey` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('19mat120', 'Rahul', 'mathematics', 'rahul@gmail.com', 'Hockey', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `kabadi`
--

CREATE TABLE `kabadi` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` text NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kabadi`
--

INSERT INTO `kabadi` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('20che101', 'Vimal', 'physics', 'vimal@gmail.com', 'kabadi', 'male', 'Madurai', 'Tamil Nadu'),
('20csc145', 'Gokul', 'mathematics', 'gokul@gmail.com', 'kabadi', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `khokho`
--

CREATE TABLE `khokho` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` varchar(25) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `khokho`
--

INSERT INTO `khokho` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('21mat123', 'Aashik', 'English', 'aashik@gmail.com', 'KhoKho', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `runrace`
--

CREATE TABLE `runrace` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` varchar(100) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `district` varchar(40) NOT NULL,
  `state` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `runrace`
--

INSERT INTO `runrace` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('20csc145', 'praveenraj', 'computer science', 'praveenboomi303@gmail.com', 'Running race', 'male', 'Madurai', 'Tamil Nadu'),
('20mat123', 'Deva.S', 'Maths', 'deva@gmail.com', 'Running Race', 'male', 'Madurai', 'Tamil Nadu'),
('20phy123', 'Surya.S', 'Physics', 'surya@gmail.com', 'Running Race', 'male', 'Madurai', 'Tamil Nadu'),
('19mat120', 'Hari', 'English', 'hari@gmail.com', 'Running race', 'male', 'Madurai', 'Tamil Nadu'),
('20csc138', 'Venkatesh', 'English', 'vengatesh@gmail.com', 'Running race', 'male', 'Ariyalur', 'Andhra Pradesh');

-- --------------------------------------------------------

--
-- Table structure for table `tabletennis`
--

CREATE TABLE `tabletennis` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` varchar(25) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tabletennis`
--

INSERT INTO `tabletennis` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('20che101', 'praveenraj', 'mathematics', 'praveenboomi303@gmail.com', 'TableTennis', 'male', 'Madurai', 'Tamil Nadu');

-- --------------------------------------------------------

--
-- Table structure for table `vollyball`
--

CREATE TABLE `vollyball` (
  `rollno` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `department` varchar(25) NOT NULL,
  `email` varchar(35) NOT NULL,
  `event` text NOT NULL,
  `gender` text NOT NULL,
  `district` text NOT NULL,
  `state` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vollyball`
--

INSERT INTO `vollyball` (`rollno`, `name`, `department`, `email`, `event`, `gender`, `district`, `state`) VALUES
('20mat160', 'sharik', 'computer science', 'sharik@gmail.com', 'Vollyball', 'male', 'Madurai', 'Tamil Nadu');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
