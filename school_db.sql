-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 05, 2022 at 01:16 PM
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

DROP TABLE IF EXISTS `attendance`;
CREATE TABLE IF NOT EXISTS `attendance` (
  `registration_number` varchar(20) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`registration_number`, `full_name`, `Class`, `date`) VALUES
('REG-15004', 'Ahortu Derrick', 'JHS 1', '03/10/2022'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', '03/02/2022');

-- --------------------------------------------------------

--
-- Table structure for table `feeding_fees`
--

DROP TABLE IF EXISTS `feeding_fees`;
CREATE TABLE IF NOT EXISTS `feeding_fees` (
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `type_of_fees` varchar(50) NOT NULL,
  `amount_paid` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feeding_fees`
--

INSERT INTO `feeding_fees` (`full_name`, `Class`, `type_of_fees`, `amount_paid`, `date`) VALUES
('ahortu', 'Class 6', 'Feeding Fees', '10', '12');

-- --------------------------------------------------------

--
-- Table structure for table `login_info`
--

DROP TABLE IF EXISTS `login_info`;
CREATE TABLE IF NOT EXISTS `login_info` (
  `username` varchar(20) NOT NULL,
  `fullname` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `confirm_password` varchar(100) NOT NULL,
  UNIQUE KEY `username` (`username`,`fullname`,`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login_info`
--

INSERT INTO `login_info` (`username`, `fullname`, `password`, `confirm_password`) VALUES
('as', 'ahortu', '12', '12');

-- --------------------------------------------------------

--
-- Table structure for table `mark`
--

DROP TABLE IF EXISTS `mark`;
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
-- Dumping data for table `mark`
--

INSERT INTO `mark` (`registration_number`, `full_name`, `Class`, `subjects`, `term`, `mark_type`, `date`, `grade`, `marks`) VALUES
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Enlish Language', 'Term 1', 'Exams', '03/10/2022', '1', '90'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Mathematics', 'Term 1', 'Exams', '03/10/2022', '1', '95'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Intergrated Science', 'Term 1', 'Exams', '03/10/2022', '1', '89'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Information Communication and Tech.', 'Term 1', 'Exams', '03/10/2022', '1', '98'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Social Studies', 'Term 1', 'Exams', '03/10/2022', '1', '95'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'History', 'Term 1', 'Exams', '03/10/2022', '1', '95'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'French', 'Term 1', 'Exams', '03/10/2022', '1', '70'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Basic Design and Tech.', 'Term 1', 'Exams', '03/10/2022', '3', '70'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Religious and Moral Education', 'Term 1', 'Exams', '03/10/2022', '2', '87'),
('REG-15004', 'Ahortu Derrick', 'JHS 1', 'Ghanaian Language', 'Term 1', 'Exams', '03/10/2022', '2', '87');

-- --------------------------------------------------------

--
-- Table structure for table `school_fees`
--

DROP TABLE IF EXISTS `school_fees`;
CREATE TABLE IF NOT EXISTS `school_fees` (
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(20) NOT NULL,
  `term` varchar(10) NOT NULL,
  `amount_paid` varchar(20) NOT NULL,
  `paid_by` varchar(100) NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `school_fees`
--

INSERT INTO `school_fees` (`full_name`, `Class`, `term`, `amount_paid`, `paid_by`, `date`) VALUES
('Ahortu', 'JHS 1', 'Term 1', '122', 'Derrick', '12th June,2022'),
('Kofi Ana', 'JHS 1', 'Term 1', '122', 'Derrick', '12th June,2022'),
('ahortu', 'JHS 3', 'Term 1', '400', 'ahortu', '13/09/2022'),
('ahortu', 'JHS 3', 'Term 2', '400', 'ahortu', '13/09/2022'),
('Ahortu Derrick', 'JHS 1', 'Term 1', '500', 'Derrick', '03/10/2022');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
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
-- Dumping data for table `students`
--

INSERT INTO `students` (`registration_number`, `full_name`, `date_of_birth`, `Class`, `gender`, `home_address`, `parent_full_name`, `phone_number`, `email_address`) VALUES
('REG-15004', 'Ahortu Derrick', '24/02/2022', 'JHS 1', 'Male', 'Ashiaman Lebanon Zone4, Accra, Ghana', 'Derrick', '0558039093', 'ahortuderrick0@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `studies_fees`
--

DROP TABLE IF EXISTS `studies_fees`;
CREATE TABLE IF NOT EXISTS `studies_fees` (
  `full_name` varchar(100) NOT NULL,
  `Class` varchar(50) NOT NULL,
  `type_of_fees` varchar(50) NOT NULL,
  `amount_paid` varchar(50) NOT NULL,
  `date` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `studies_fees`
--

INSERT INTO `studies_fees` (`full_name`, `Class`, `type_of_fees`, `amount_paid`, `date`) VALUES
('ahortu', 'Class 6', 'Studies Fees', '10', '12'),
('Ahortu Derrick', 'JHS 1', 'Studies Fees', '200', '13'),
('Ahortu Derrick', 'Class 1', 'Studies Fees', '100', '03/10/2022'),
('Ahortu Derrick', 'JHS 1', 'Studies Fees', '400', '03/10/2022'),
('Ahortu Derrick', 'JHS 1', 'Studies Fees', '100', '03/10/2022');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
