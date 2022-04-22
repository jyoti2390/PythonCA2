-- MySQL dump 10.13  Distrib 8.0.28, for Linux (x86_64)
--
-- Host: localhost    Database: wealthmanagement
-- ------------------------------------------------------
-- Server version	8.0.28-0ubuntu0.20.04.3

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
-- Table structure for table `fund_history`
--

DROP TABLE IF EXISTS `fund_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fund_history` (
  `fh_id` int NOT NULL,
  `fh1month` float NOT NULL,
  `fh1year` float NOT NULL,
  `fh_total` float NOT NULL,
  `fund_id` int DEFAULT NULL,
  PRIMARY KEY (`fh_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fund_history`
--

LOCK TABLES `fund_history` WRITE;
/*!40000 ALTER TABLE `fund_history` DISABLE KEYS */;
INSERT INTO `fund_history` VALUES (1,5.35,26.23,10.10,1),(2,45.1,10.29,29.00,2),(3,55.11,11.29,39.01,3),(4,21.11,5.29,42.1,4);
/*!40000 ALTER TABLE `fund_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funds`
--

DROP TABLE IF EXISTS `funds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funds` (
  `funds_id` int NOT NULL AUTO_INCREMENT,
  `fund_amc` varchar(255) DEFAULT NULL,
  `fund_aum` bigint NOT NULL,
  `fund_desc` varchar(255) DEFAULT NULL,
  `fund_mgr` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `fund_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `fund_nav` float NOT NULL,
  `fund_risk` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `fund_type` varchar(255) DEFAULT NULL,
  `img_src` varchar(255) DEFAULT NULL,
  `fund_id` int NOT NULL,
  PRIMARY KEY (`funds_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funds`
--

LOCK TABLES `funds` WRITE;
/*!40000 ALTER TABLE `funds` DISABLE KEYS */;
INSERT INTO `funds` VALUES (1,'HDFC',90000000,'HDFC BANK','HDFC','HDFC',23.66,'low','Equity','https://imageio.forbes.com/i-forbesimg/media/lists/companies/hdfc-bank_416x416.jpg?format=jpg&height=416&width=416&fit=bounds',1),(2,'BOI',190000000,'BOI Equity','BOI','BOI',23.99,'high','Equity','https://wexfordtoday.com/wp-content/uploads/2020/03/Bank-Of-Ireland.png',2),(3,'AIB',290000000,'AIB Equity','AIB','AIB',43.99,'high','Equity','https://upload.wikimedia.org/wikipedia/en/thumb/4/4b/Allied_Irish_Banks_logo.svg/1200px-Allied_Irish_Banks_logo.svg.png',3),(4,'AXIS Bank',390000000,'AXIZ Equity','AXIS','AXIS',9.99,'medium','Equity','https://www.cloudera.com/content/dam/www/marketing/images/logos/customers/axis-bank.png',4);
/*!40000 ALTER TABLE `funds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_fund`
--

DROP TABLE IF EXISTS `user_fund`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_fund` (
  `uf_id` int NOT NULL AUTO_INCREMENT,
  `fund_id` int DEFAULT NULL,
  `uf_amount` float NOT NULL,
  `uf_date` varchar(255) DEFAULT NULL,
  `uf_type` varchar(255) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  PRIMARY KEY (`uf_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_fund`
--

LOCK TABLES `user_fund` WRITE;
/*!40000 ALTER TABLE `user_fund` DISABLE KEYS */;
INSERT INTO `user_fund` VALUES (15,1,1000,'Tue Apr 19 2022','Equity',31),(16,3,20000,'Tue Apr 19 2022','Equity',31),(20,1,500,'Tue Apr 19 2022','Equity',34);
/*!40000 ALTER TABLE `user_fund` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `img_src` varchar(255) DEFAULT NULL,
  `user_age` int DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `user_password` varchar(255) DEFAULT NULL,
  `user_phone_number` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_email` (`user_email`,`user_password`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (16,'',81,'test5@xya.com','test5','test5','108497858'),(19,'',81,'test6@xya.com','test6','test6','108497858'),(22,'',81,'test7@xya.com','test7','test7','108497858'),(24,'',81,'test8@xya.com','test8','test8','108497858'),(26,'',81,'test9@xya.com','test9','test9','108497858'),(27,'',81,'test10@xya.com','test10','test10','108497858'),(28,'',81,'test11@xya.com','test11','test11','108497858'),(29,'',81,'test12@xya.com','test12','test12','108497858'),(30,'',81,'test13@xya.com','test13','test13','108497858'),(32,'',79,'testj@123.com','testj','jyoti@123','1234567890'),(34,'',23,'testjyoti@jyoti.com','testjyoti','jyoti@123','123456789'),(39,'',81,'testd13@xya.com','tes2t13','tesdst13','108497858'),(40,'',81,'testdb13@xya.com','tes2ts13','tevsdst13','108497858');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-22 17:33:34
