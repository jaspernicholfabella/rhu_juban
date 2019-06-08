-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2019 at 05:24 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rhu_juban`
--

-- --------------------------------------------------------

--
-- Table structure for table `individual_records`
--

CREATE TABLE `individual_records` (
  `individual_id` int(255) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `address` varchar(200) NOT NULL,
  `age` int(255) NOT NULL,
  `bp` varchar(50) NOT NULL,
  `chief_complaints` varchar(1000) NOT NULL,
  `impression` varchar(500) NOT NULL,
  `management` varchar(500) NOT NULL,
  `entry_date` date NOT NULL,
  `doctor` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `individual_records`
--

INSERT INTO `individual_records` (`individual_id`, `full_name`, `address`, `age`, `bp`, `chief_complaints`, `impression`, `management`, `entry_date`, `doctor`) VALUES
(1, 'Jasper Nichol M Fabella', 'St Vincent Subdivision', 25, '12/240', 'cough', '', '', '2019-03-02', ''),
(1, 'Jasper Nichol M Fabella', 'St Vincent Subdivision', 25, '120/110', 'cough', 'malala na ubo', 'solmux', '2019-03-02', 'Jasper Fabella'),
(2, 'Nicolas G Fabella', 'St Vincent Subdivision, San Vicente', 40, '', '', '', '', '2019-03-03', ''),
(3, 'Juliana Nastassia M Fabella', 'St Vincent Subdivision', 17, '', '', '', '', '2019-03-03', ''),
(4, 'Janine  Corro', 'San Isidro Bulan Sorsogon', 20, '', '', '', '', '2019-03-03', ''),
(5, 'Corro  James', 'San Isidro Bulan Sorsogon', 15, '', '', '', '', '2019-03-03', ''),
(6, 'Evangeline Verano Moralde', 'St Vincent Subdivision, San Vicente', 50, '', '', '', '', '2019-03-03', ''),
(7, 'Jade Nicolas M Fabella', 'St Vincent Subdivision', 21, '', '', '', '', '2019-03-03', ''),
(8, 'Nathaniel  Esber', 'Zone 2 Bulan Sorsogon', 25, '', '', '', '', '2019-03-03', ''),
(9, 'Joeven  Geocada', 'Otavi Bulan Sorsogon', 25, '', '', '', '', '2019-03-03', ''),
(10, 'Jacinth Nicolas M Fabella', 'St Vincent Subdivision', 19, '', '', '', '', '2019-03-03', ''),
(11, 'Joeven  Bonifacio', 'Zone 4 Bulan Sorsogon', 25, '', '', '', '', '2019-03-03', '');

-- --------------------------------------------------------

--
-- Table structure for table `medicine`
--

CREATE TABLE `medicine` (
  `id` int(11) NOT NULL,
  `medicine_name` varchar(50) NOT NULL,
  `quantity` int(255) NOT NULL,
  `unit` varchar(5) NOT NULL,
  `description` varchar(100) NOT NULL,
  `batch` varchar(50) NOT NULL,
  `exp_date` date NOT NULL,
  `unit_price` int(255) NOT NULL,
  `amount` int(255) NOT NULL,
  `en_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `medicine`
--

INSERT INTO `medicine` (`id`, `medicine_name`, `quantity`, `unit`, `description`, `batch`, `exp_date`, `unit_price`, `amount`, `en_date`) VALUES
(3, 'antibiotic', 20, 'San V', 'diego', 'Y443', '2019-02-07', 1000, 10000, '2019-02-23'),
(5, 'antibiotic', 333, 'San V', 'diego', 'asdf', '2019-02-22', 1000, 1255, '2019-02-23'),
(6, 'antibiotic', 1, '55', 'diego', 'asdf', '2019-02-22', 2500, 100002111, '2019-02-23'),
(7, 'antibiotic', 227, 'San V', 'diego', 'asdf', '2020-04-01', 1000, 25, '2019-02-23'),
(8, 'aaaaaa', 2, 'San V', 'diego', 'asdf', '2019-01-02', 1200, 25, '2019-02-24');

-- --------------------------------------------------------

--
-- Table structure for table `med_release`
--

CREATE TABLE `med_release` (
  `id` int(11) NOT NULL,
  `medicine_name` varchar(50) NOT NULL,
  `quantity_released` int(11) NOT NULL,
  `batch` varchar(50) NOT NULL,
  `exp_date` varchar(50) NOT NULL,
  `date_released` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `med_release`
--

INSERT INTO `med_release` (`id`, `medicine_name`, `quantity_released`, `batch`, `exp_date`, `date_released`) VALUES
(2, 'antibiotic', 22, '', '2019-02-22', '2019-03-03'),
(3, 'antibiotic', 20, '', '2019-02-07', '2019-03-03'),
(4, 'antibiotic', 2, '', '2019-02-07', '2019-03-03'),
(5, 'antibiotic', 3, '', '2019-02-07', '2019-03-04'),
(6, 'antibiotic', 3, '', '2019-02-07', '2019-03-04'),
(7, 'antibiotic', 5, '', '2019-02-07', '2019-03-04'),
(8, 'antibiotic', 16, 'asdf', '2020-04-01', '2019-03-04');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `id` int(11) NOT NULL,
  `patient_code` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `age` int(100) NOT NULL,
  `sex` varchar(50) NOT NULL,
  `cs` varchar(50) NOT NULL,
  `phic` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `chief_complaints` varchar(100) NOT NULL,
  `weight` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `bp` varchar(50) NOT NULL,
  `t` varchar(50) NOT NULL,
  `pr` varchar(50) NOT NULL,
  `rr` varchar(50) NOT NULL,
  `patient_date` date NOT NULL,
  `birthday` varchar(50) NOT NULL,
  `management` varchar(100) NOT NULL,
  `treatment` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`id`, `patient_code`, `first_name`, `middle_name`, `last_name`, `age`, `sex`, `cs`, `phic`, `address`, `chief_complaints`, `weight`, `height`, `bp`, `t`, `pr`, `rr`, `patient_date`, `birthday`, `management`, `treatment`) VALUES
(1, '', 'Jasper Nichol', 'M', 'Fabella', 26, 'male', '12', '22222', 'St Vincent Subdivision', 'cough', 85, 167, '12/240', '3', '021s', '2e', '2019-03-02', '1993-04-04', 'malala na ubo', 'solmux'),
(2, '', 'Nicolas', 'G', 'Fabella', 40, 'male', '', '', 'St Vincent Subdivision, San Vicente', '', 0, 0, '', '', '', '', '2019-03-03', '1968-09-10', '', ''),
(3, '', 'Juliana Nastassia', 'M', 'Fabella', 17, 'female', '', '', 'St Vincent Subdivision', '', 0, 0, '', '', '', '', '2018-09-13', '', '', ''),
(4, '', 'Janine', '', 'Corro', 20, 'female', '', '', 'San Isidro Bulan Sorsogon', '', 0, 0, '', '', '', '', '2019-11-15', '1999-01-23', '', ''),
(5, '', 'James', '', 'Corro', 15, 'male', '', '', 'San Isidro Bulan Sorsogon', '', 0, 0, '', '', '', '', '2019-10-17', '', '', ''),
(6, '', 'Evangeline', 'Verano', 'Moralde', 50, 'female', '', '', 'St Vincent Subdivision, San Vicente', '', 0, 0, '', '', '', '', '2019-09-04', '1964-05-15', '', ''),
(7, '', 'Jade Nicolas', 'M', 'Fabella', 21, 'male', '', '', 'St Vincent Subdivision', '', 0, 0, '', '', '', '', '2019-07-13', '1996-01-20', '', ''),
(8, '', 'Nathaniel', '', 'Esber', 25, 'male', '', '', 'Zone 2 Bulan Sorsogon', '', 0, 0, '', '', '', '', '2019-06-20', '1993-01-01', '', ''),
(9, '', 'Joeven', '', 'Geocada', 25, 'male', '', '', 'Otavi Bulan Sorsogon', '', 0, 0, '', '', '', '', '2019-04-01', '1993-01-01', '', ''),
(10, '', 'Jacinth Nicolas', 'M', 'Fabella', 19, 'male', '', '', 'St Vincent Subdivision', '', 0, 0, '', '', '', '', '2019-03-03', '2000-12-19', '', ''),
(11, '', 'Joeven', '', 'Bonifacio', 25, 'male', '', '', 'Zone 4 Bulan Sorsogon', '', 0, 0, '', '', '', '', '2019-01-09', '1993-01-01', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `account_type` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `account_type`) VALUES
(2, 'admin', 'admin', 'admin'),
(3, 'nurse', 'nurse', 'nurse'),
(4, 'doctor', 'doctor', 'doctor'),
(5, 'pharmacist', 'pharmacist', 'pharmacist'),
(6, 'admin123', 'admin123', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `medicine`
--
ALTER TABLE `medicine`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `med_release`
--
ALTER TABLE `med_release`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `medicine`
--
ALTER TABLE `medicine`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `med_release`
--
ALTER TABLE `med_release`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `patient`
--
ALTER TABLE `patient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
