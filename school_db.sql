-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 26, 2022 at 03:29 AM
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
-- Database: `school_db`
--
CREATE DATABASE IF NOT EXISTS `school_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `school_db`;

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE IF NOT EXISTS `attendance` (
  `registration_number` varchar(20) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Truncate table before insert `attendance`
--

TRUNCATE TABLE `attendance`;
-- --------------------------------------------------------

--
-- Table structure for table `feeding_fees`
--

CREATE TABLE IF NOT EXISTS `feeding_fees` (
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `amount_paid` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Truncate table before insert `feeding_fees`
--

TRUNCATE TABLE `feeding_fees`;
-- --------------------------------------------------------

--
-- Table structure for table `login_info`
--

CREATE TABLE IF NOT EXISTS `login_info` (
  `username` varchar(20) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `confirm_password` varchar(100) NOT NULL,
  UNIQUE KEY `username` (`username`,`fullname`,`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Truncate table before insert `login_info`
--

TRUNCATE TABLE `login_info`;
--
-- Dumping data for table `login_info`
--

INSERT DELAYED IGNORE INTO `login_info` (`username`, `fullname`, `password`, `confirm_password`) VALUES
('as', 'ahortu', '12', '12');

-- --------------------------------------------------------

--
-- Table structure for table `mark`
--

CREATE TABLE IF NOT EXISTS `mark` (
  `registration_number` varchar(20) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `subjects` varchar(100) NOT NULL,
  `term` varchar(20) NOT NULL,
  `mark_type` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `grade` varchar(50) NOT NULL,
  `marks` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Truncate table before insert `mark`
--

TRUNCATE TABLE `mark`;
-- --------------------------------------------------------

--
-- Table structure for table `school_fees`
--

CREATE TABLE IF NOT EXISTS `school_fees` (
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `term` varchar(10) NOT NULL,
  `amount_paid` varchar(20) NOT NULL,
  `paid_by` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Truncate table before insert `school_fees`
--

TRUNCATE TABLE `school_fees`;
--
-- Dumping data for table `school_fees`
--

INSERT DELAYED IGNORE INTO `school_fees` (`full_name`, `Class`, `term`, `amount_paid`, `paid_by`, `date`) VALUES
('Ahortu', 'JHS 1', 'Term 1', '122', 'Derrick', '12th June,2022'),
('Kofi Ana', 'JHS 1', 'Term 1', '122', 'Derrick', '12th June,2022'),
('Hellary Ama', 'JHS 2', 'Term 1', '1228', 'John Kuwasi', '13thJune');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE IF NOT EXISTS `students` (
  `registration_number` varchar(20) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `date_of_birth` varchar(20) NOT NULL,
  `Class` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `home_address` varchar(100) NOT NULL,
  `parent_full_name` varchar(100) NOT NULL,
  `phone_number` varchar(100) NOT NULL,
  `email_address` varchar(100) NOT NULL,
  UNIQUE KEY `registration_number` (`registration_number`),
  UNIQUE KEY `full_name` (`full_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Truncate table before insert `students`
--

TRUNCATE TABLE `students`;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
