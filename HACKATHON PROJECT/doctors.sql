-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: localhost    Database: doctors
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cardiology`
--

DROP TABLE IF EXISTS `cardiology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardiology` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardiology`
--

LOCK TABLES `cardiology` WRITE;
/*!40000 ALTER TABLE `cardiology` DISABLE KEYS */;
INSERT INTO `cardiology` VALUES (1,'Dr.Ravi','Sunshine Hospital','4'),(2,'Dr.Ankitha','KK Hospital','5'),(3,'Dr.Sarwal','Max Healthcare Hospital','4'),(4,'Dr.K K Pandey','Max Healthcare Hospital','3'),(5,'Dr.Suresh Joshi','Jaypee Hospital','4'),(6,'Dr.Ramu','Sunshine Hospital','4'),(7,'Dr.Mark Anthony','Aster Medicity','5'),(8,'Dr.Cassius','Sunshine Hospital','4'),(9,'Dr.Ramses','Aster Medcity','5');
/*!40000 ALTER TABLE `cardiology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `num` int DEFAULT NULL,
  `department` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Cardiology'),(2,'Neurology'),(3,'Radiology'),(4,'Dermatology'),(5,'Ophthalmology'),(6,'Urology'),(7,'ENT'),(8,'Gastroenterology'),(6,'Paediatrics'),(6,'Orthopaedics');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dermatology`
--

DROP TABLE IF EXISTS `dermatology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dermatology` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dermatology`
--

LOCK TABLES `dermatology` WRITE;
/*!40000 ALTER TABLE `dermatology` DISABLE KEYS */;
INSERT INTO `dermatology` VALUES (1,'Dr.Divya Nair','Enhance Clinics','5'),(2,'Dr.Vikram ','Shalby Hospital','5');
/*!40000 ALTER TABLE `dermatology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ent`
--

DROP TABLE IF EXISTS `ent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ent` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ent`
--

LOCK TABLES `ent` WRITE;
/*!40000 ALTER TABLE `ent` DISABLE KEYS */;
INSERT INTO `ent` VALUES (1,'Dr.Vineeth Vishwam','Aster Medicity','5'),(2,'Dr.Biswarup Mukherjee ','Amri Hospital','5'),(1,'Dr.Mohamed Rela','RIMC','5'),(2,'Dr.Sujit Chaudhary ','Amri Hospital','4'),(5,'Dr.Ravi Prasad','Aster Medicity','3'),(6,'Dr.Sarah','Aster Medcity','4'),(7,'Dr.Anjana','Aster Medcity','5');
/*!40000 ALTER TABLE `ent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gastroentology`
--

DROP TABLE IF EXISTS `gastroentology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gastroentology` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gastroentology`
--

LOCK TABLES `gastroentology` WRITE;
/*!40000 ALTER TABLE `gastroentology` DISABLE KEYS */;
INSERT INTO `gastroentology` VALUES (1,'Dr.Pranav','Aster','5');
/*!40000 ALTER TABLE `gastroentology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `neurology`
--

DROP TABLE IF EXISTS `neurology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `neurology` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `neurology`
--

LOCK TABLES `neurology` WRITE;
/*!40000 ALTER TABLE `neurology` DISABLE KEYS */;
INSERT INTO `neurology` VALUES (1,'Dr.Ramesh Kumar','Apollo Hospital','5'),(2,'Dr.Geetha Lakshmipathy','Max Superspeciality Hospital','3'),(3,'Dr.M.R Sivakumar','Nanavati Hospital','4'),(4,'Dr.Yogaraj','Aster Medicity','4');
/*!40000 ALTER TABLE `neurology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ophthalmology`
--

DROP TABLE IF EXISTS `ophthalmology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ophthalmology` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ophthalmology`
--

LOCK TABLES `ophthalmology` WRITE;
/*!40000 ALTER TABLE `ophthalmology` DISABLE KEYS */;
INSERT INTO `ophthalmology` VALUES (1,'Dr.Devi Prasad Shetty','Apollo Hospital','5'),(2,'Dr.Dhiren Shah','Artemis Hospital','5'),(1,'Dr.Sameer Kaushal','Artemis Hospital','5'),(2,'Dr.Varun Gogia','Medanta Medicity','5'),(3,'Dr.Svati Bansal','Medanta Medicity','4');
/*!40000 ALTER TABLE `ophthalmology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orthopaedics`
--

DROP TABLE IF EXISTS `orthopaedics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orthopaedics` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orthopaedics`
--

LOCK TABLES `orthopaedics` WRITE;
/*!40000 ALTER TABLE `orthopaedics` DISABLE KEYS */;
INSERT INTO `orthopaedics` VALUES (1,'Dr.Adeyanju','Artemis Hospital','5'),(2,'Dr.Ashok Rajgopal','Max Superspeciality Hospital','5'),(3,'Dr.B K Singh','Nanavati Hospital','5'),(4,'Dr.Pradeep Sharma','Global Hospital','4'),(5,'Dr.Gyan Sagar','Fortis Hospital','4'),(6,'Dr.Rakesh Mahajan','Wockhardt Hospital','3');
/*!40000 ALTER TABLE `orthopaedics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paediatrics`
--

DROP TABLE IF EXISTS `paediatrics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paediatrics` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paediatrics`
--

LOCK TABLES `paediatrics` WRITE;
/*!40000 ALTER TABLE `paediatrics` DISABLE KEYS */;
INSERT INTO `paediatrics` VALUES (1,'Dr.Nana C Joshi','Nanavati Hospital','5'),(2,'Dr.Rashid H Merchant','Nanavati Hospital','5'),(3,'Dr.V V Varadharajan','Rainbow Children Hospital','4'),(4,'Dr.BeNNY Benjamin','Fortis Hospital','4');
/*!40000 ALTER TABLE `paediatrics` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `radiology`
--

DROP TABLE IF EXISTS `radiology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `radiology` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `radiology`
--

LOCK TABLES `radiology` WRITE;
/*!40000 ALTER TABLE `radiology` DISABLE KEYS */;
INSERT INTO `radiology` VALUES (1,'Dr.Pulastya Sanyal','AMRI Hospital','5'),(2,'Dr.Sunil Shah','Jaslok Hospital','5'),(3,'Dr.Ravi Ramakantan','KDA Hospital','5'),(4,'Dr.Chander','Jaslok Hospital','4'),(5,'Dr.B Madhusudhan','Fortis Hospital','4'),(6,'Dr.Vimal Someshwar','Reliance Hospital','3');
/*!40000 ALTER TABLE `radiology` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `urology`
--

DROP TABLE IF EXISTS `urology`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `urology` (
  `sno` int DEFAULT NULL,
  `doc_name` varchar(200) DEFAULT NULL,
  `hospital` varchar(100) DEFAULT NULL,
  `rating` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `urology`
--

LOCK TABLES `urology` WRITE;
/*!40000 ALTER TABLE `urology` DISABLE KEYS */;
INSERT INTO `urology` VALUES (1,'Dr.Prasanna Kumar','AMRI Hospital','5'),(2,'Dr.Rajeev Sood ','Fortis  Hospital','4');
/*!40000 ALTER TABLE `urology` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-11-28 23:24:20
