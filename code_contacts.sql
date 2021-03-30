-- MySQL dump 10.13  Distrib 8.0.23, for Linux (x86_64)
--
-- Host: localhost    Database: code
-- ------------------------------------------------------
-- Server version	8.0.23-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `msg` varchar(50) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (1,'hello','test@gmail.com','5656565556','jo',NULL),(2,'testing','test@gmail.com','5656565556','hiii',NULL),(3,'test','test@gmail.com','7878787878','hi, this message for the testing purpose.',NULL),(4,'hello','hello@gmail.com','5568868654','hello.',NULL),(5,'testing','test@gmail.com','5656565556','hii, hello ',NULL),(6,'testing','test@gmail.com','5656565556','hii, hello ',NULL),(7,'testing','hello@gmail.com','5656565556','hii',NULL),(8,'sandip','sandip@gmail.com','9574585025','hi my name is sandip fachara.',NULL),(9,'hi','test@gmail.com','7878787878','hiiiiiiiiiiiiiiiiiiiii,',NULL),(10,NULL,'',NULL,NULL,NULL),(11,NULL,'test@gmail.com',NULL,NULL,NULL),(12,NULL,NULL,NULL,NULL,NULL),(13,NULL,NULL,NULL,NULL,NULL),(14,'testing','test@gmail.com','5656565556','hello',NULL),(15,NULL,NULL,NULL,NULL,NULL),(16,NULL,NULL,NULL,NULL,NULL),(17,NULL,NULL,NULL,NULL,NULL),(18,'hello','hello@gmail.com','5656565556','hiiiiii,',NULL);
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-30 12:36:48
