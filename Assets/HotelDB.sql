-- MySQL dump 10.13  Distrib 5.1.33, for Win32 (ia32)
--
-- Host: localhost    Database: Hotel
-- ------------------------------------------------------
-- Server version	5.1.33-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `Username` varchar(67) DEFAULT NULL,
  `Password` varchar(67) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('Aathish','securepwd'),('Ajay Ghale','verysecurepwd'),('Anushka','pwd'),('Jaspreet','bumrah'),('Ishaan Kishan','reallysecurepwd');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guest`
--

DROP TABLE IF EXISTS `guest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guest` (
  `GuestID` int(4) DEFAULT NULL,
  `GuestName` varchar(30) DEFAULT NULL,
  `RoomType` varchar(15) DEFAULT NULL,
  `CheckinDate` date DEFAULT NULL,
  `CheckoutDate` date DEFAULT NULL,
  `RoomNo` int(4) DEFAULT NULL,
  `BookingSource` varchar(10) DEFAULT NULL,
  `NetPayment` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guest`
--

LOCK TABLES `guest` WRITE;
/*!40000 ALTER TABLE `guest` DISABLE KEYS */;
INSERT INTO `guest` VALUES (101,'Aarav','Single','2022-09-01','2022-09-04',281,'Online',15000),(102,'Basanti','Single','2022-08-28','2022-09-07',282,'Online',20000),(103,'Kavita','Double','2022-09-08','2022-09-18',302,'Offline',30000),(104,'Shiva','Double','2022-09-13','2022-09-15',139,'Online',25000),(105,'Reshmi','Single','2022-09-13','2022-09-16',285,'Offline',17500),(106,'Raj','Single','2022-09-21','2022-10-03',114,'Online',18000),(107,'Suman','Single','2022-10-06','2022-10-13',298,'Online',16750),(108,'Kiran','Double','2022-10-07','2022-10-09',175,'Offline',22000),(109,'Kumar','Double','2022-10-06','2022-10-13',308,'Online',27500),(110,'Radha','Single','2022-10-13','2022-10-17',148,'Offline',18000);
/*!40000 ALTER TABLE `guest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `login`
--

DROP TABLE IF EXISTS `login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `login` (
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `login`
--

LOCK TABLES `login` WRITE;
/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` VALUES ('Aathish','randompassword'),('Ajay Ghale','reallysecurepassword'),('Ben','123789'),('Aditi','somepwd');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staff`
--

DROP TABLE IF EXISTS `staff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staff` (
  `StaffID` varchar(7) DEFAULT NULL,
  `Name` varchar(49) DEFAULT NULL,
  `DateOfBirth` date DEFAULT NULL,
  `Designation` varchar(25) DEFAULT NULL,
  `Salary` int(10) DEFAULT NULL,
  `DateOfHire` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staff`
--

LOCK TABLES `staff` WRITE;
/*!40000 ALTER TABLE `staff` DISABLE KEYS */;
INSERT INTO `staff` VALUES ('R6900','Ajay Ghale','1990-07-24','Assistant Hotel Manager',60000,'2005-08-01'),('R6901','Anushka','1999-06-08','Receptionist',40000,'2006-06-06'),('R6902','Ashwin','2000-06-09','Sales Marketing Manager',50000,'2017-01-07'),('R6903','Dhanush','1999-04-01','Night Auditor',42650,'2008-09-10'),('R6904','Divya','1999-10-10','Room Attendant',20000,'2008-09-21'),('R6905','Gordon','1997-03-19','Chef',30000,'2011-09-22'),('R6906','Hari','2002-06-23','Waiter',20000,'2019-12-02'),('R6907','Ishaan Kishan','1991-01-26','Hotel Manager',58000,'2001-02-28'),('R6908','Jaspreet','2001-04-28','Receptionist ',40000,'2015-04-28'),('R6909','Manish','1997-09-21','Waiter',20000,'2012-01-01'),('R6910','Rohit','1998-06-06','Procurement specialist',56570,'2002-11-18'),('R6911','Vikas','1997-05-26','Chef',30000,'2012-08-15');
/*!40000 ALTER TABLE `staff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-09  5:08:31
