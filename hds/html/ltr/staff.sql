-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 22, 2024 at 07:40 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hds`
--

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `Firstname` varchar(15) NOT NULL,
  `Middlename` varchar(15) NOT NULL,
  `Lastname` varchar(15) NOT NULL,
  `Phone` int(10) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Address` varchar(30) NOT NULL,
  `Maritalstatus` varchar(15) NOT NULL,
  `Bloodgroup` varchar(5) NOT NULL,
  `Dob` date NOT NULL,
  `Adhar` int(12) NOT NULL,
  `Pan` varchar(10) NOT NULL,
  `Passport` varchar(15) NOT NULL,
  `Mobile` int(10) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `Mobile2` int(10) NOT NULL,
  `Email2` varchar(30) NOT NULL,
  `Country` varchar(15) NOT NULL,
  `State` varchar(20) NOT NULL,
  `City` varchar(15) NOT NULL,
  `Pincode` int(10) NOT NULL,
  `Address2` varchar(30) NOT NULL,
  `Education` varchar(20) NOT NULL,
  `Specilisation` varchar(20) NOT NULL,
  `Institute` varchar(20) NOT NULL,
  `Percentage` int(5) NOT NULL,
  `Year` int(5) NOT NULL,
  `Bankname` varchar(15) NOT NULL,
  `Accountno` int(20) NOT NULL,
  `Accountholder` varchar(30) NOT NULL,
  `Accountype` varchar(15) NOT NULL,
  `Ifsccode` varchar(20) NOT NULL,
  `Bankbranch` varchar(20) NOT NULL,
  `Department` varchar(20) NOT NULL,
  `Jobtitle` varchar(20) NOT NULL,
  `Employmentstatus` varchar(15) NOT NULL,
  `Staffid` varchar(15) NOT NULL,
  `Experience` int(3) NOT NULL,
  `Joiningdate` date NOT NULL,
  `Stime` varchar(6) NOT NULL,
  `Etime` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `Firstname`, `Middlename`, `Lastname`, `Phone`, `Gender`, `Address`, `Maritalstatus`, `Bloodgroup`, `Dob`, `Adhar`, `Pan`, `Passport`, `Mobile`, `Email`, `Mobile2`, `Email2`, `Country`, `State`, `City`, `Pincode`, `Address2`, `Education`, `Specilisation`, `Institute`, `Percentage`, `Year`, `Bankname`, `Accountno`, `Accountholder`, `Accountype`, `Ifsccode`, `Bankbranch`, `Department`, `Jobtitle`, `Employmentstatus`, `Staffid`, `Experience`, `Joiningdate`, `Stime`, `Etime`) VALUES
(1, 'None', 'None', 'None', 0, 'None', 'None', 'None', 'None', '0000-00-00', 0, 'None', 'None', 0, 'None', 0, 'None', 'None', 'None', 'None', 0, 'None', 'None', 'None', 'None', 0, 0, 'None', 0, 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 0, '0000-00-00', 'None', 'None'),
(2, 'j', 'c', 'd', 2147483647, 'Male', 's', 'Married', 'AB-', '2024-07-08', 2147483647, 'gh4567hu89', '1234567898', 2147483647, 's@gmail.com', 2147483647, 's@gmail.com', 'h', 'h', 'h', 567432, 'h', 'g', 'u', 'i', 67, 2022, 'h', 2147483647, 'h', 'Saving', 'gfhd6457', 'j', 'g', 'd', 'Full-Time', 'd3gh4', 8, '2024-07-16', '10:00', '18:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
