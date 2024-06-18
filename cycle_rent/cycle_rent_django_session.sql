-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: cycle_rent
-- ------------------------------------------------------
-- Server version	8.0.29

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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('3k0cpuavpdu31aaiemzu5n9aw5dbl4pz','.eJxVjMsKwyAQAP_FcxEV46PH3vsNYXdda9qiEJNT6L8XIYf2OjPMIWbYtzLvndd5SeIqtLj8MgR6cR0iPaE-mqRWt3VBORJ52i7vLfH7drZ_gwK9jC0SKw6glDLJAKFCDEzWTVMGmnRmoJi9JhNIMVgX2EQMUXvLybEXny8QFjjk:1sIlAz:RvSAgsyIVpYpz9EL3wOnxNJWG4ueqrEQiCImc5tGxPg','2024-06-30 08:23:49.889561'),('s5fqr5voj9z5jvo7o0iahlbekensgx9k','e30:1sGPoo:PmF1f1Szk6aSTm2DL_tQMFTE7A-h99Wl72IEwGEsicI','2024-06-23 21:11:14.426210'),('x1govqzsteegma15ycacq0lsuk28hlf0','.eJxVjMsKwyAQAP_FcxEV46PH3vsNYXdda9qiEJNT6L8XIYf2OjPMIWbYtzLvndd5SeIqtLj8MgR6cR0iPaE-mqRWt3VBORJ52i7vLfH7drZ_gwK9jC0SKw6glDLJAKFCDEzWTVMGmnRmoJi9JhNIMVgX2EQMUXvLybEXny8QFjjk:1sIlR2:nc9sPRyFDk3GT468aazB6dFvCRWoypY3GHdGIsQiUE4','2024-06-30 08:40:24.429068');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-18 15:48:32
