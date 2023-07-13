-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: myportfoliodb
-- ------------------------------------------------------
-- Server version       8.0.33

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
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `description` text NOT NULL,
  `link` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES (1,'Cocktail Please','../static/projects/Cocktail_Please.png','Do you love to try out new Cocktails? This is the perfect app for you. It will recommend you a random cocktail every week. Check it out at:','https://cocktail-please.vercel.app/','2023-07-13 11:08:46'),(2,'Ye Quotes','../static/projects/Ye_Quotes.png','Ever thought of what Kanye has said on social media? No? Neither did I, but you can use it when you don\'t have anything to tweet, or maybe for your Instagram post\'s description, enjoy it! Check it out at:','https://yeyom.github.io/kanye_quotes/','2023-07-13 11:09:41'),(3,'Portfolio vol. 1','../static/projects/Past_Portfolio.png','This was my past portfolio I built with React, it features a brutalist design I personally love. Check it out at: ','https://yeyom.github.io/yeyo_portfolio/','2023-07-13 11:13:28'),(4,'Maze Solver','../static/projects/MazeSolver.png','Maze Solver built with python. This project uses various techniques such as DFS, BFS, Dijkstra and A* Star to generate and solve a maze. Browse the code ','https://github.com/YeyoM/mazeSolver','2023-07-13 11:14:16'),(5,'Lofi Terminal','../static/projects/Lofi_terminal.png','This lofi player will make every developer feel like home, use it for those long coding sessions, built with NextJs and react-terminal. Check it out at: ','https://lofi-terminal.vercel.app/','2023-07-13 11:14:56');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-13 13:25:27