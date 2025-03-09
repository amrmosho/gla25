-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 05, 2025 at 09:55 PM
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
-- Database: `py_insya_2`
--

-- --------------------------------------------------------

--
-- Table structure for table `gla_address`
--

CREATE TABLE `gla_address` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `whatsapp` varchar(50) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL,
  `kit_lang` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_address`
--

INSERT INTO `gla_address` (`id`, `title`, `address`, `email`, `phone`, `whatsapp`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(1, 'El Moez Le Din Allah St', '60 El Moez Le Din Allah St., El Gamalia, Cairo', 'info@elgallagold.com', '17153', '01009539999', 0, 0, '2025-02-18 11:49:12', '2025-02-18 11:49:12', ''),
(2, 'Palm Hills', 'Street 88 , Palm Hills , 6th of October, Giza', 'info@elgallagold.com', '17153', '01009539999', 0, 0, '2025-02-18 11:49:12', '2025-02-18 11:49:12', '');

-- --------------------------------------------------------

--
-- Table structure for table `gla_blog`
--

CREATE TABLE `gla_blog` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `link` text DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `fk_blog_category_id` int(11) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL,
  `_order` int(11) DEFAULT NULL,
  `home` int(11) DEFAULT NULL,
  `kit_lang` text DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_blog`
--

INSERT INTO `gla_blog` (`id`, `title`, `content`, `image`, `link`, `city`, `state`, `fk_blog_category_id`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `_order`, `home`, `kit_lang`) VALUES
(1, 'El Galla Gold receives export orders from three Arab countries and aims to open its third branch in 2025.', 'El Galla Gold receives export orders from three Arab countries and aims to open its third branch in 2025.', 'images/20250212121821__000_057.png', 'https://almalnews.com/%d8%a7%d9%84%d8%ac%d9%84%d8%a7-%d8%ac%d9%88%d9%84%d8%af-%d8%aa%d8%aa%d9%84%d9%82%d9%89-%d8%b7%d9%84%d8%a8%d8%a7%d8%aa-%d8%aa%d8%b5%d8%af%d9%8a%d8%b1%d9%8a%d8%a9-%d9%84%d9%803-%d8%af%d9%88/', '', '', 0, 0, 0, '2025-02-12 12:06:34', '2024-12-12 09:29:26', 1, 1, '{\"ar\": {\"title\": \"\\u00ab\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\u00bb \\u062a\\u062a\\u0644\\u0642\\u0649 \\u0637\\u0644\\u0628\\u0627\\u062a \\u062a\\u0635\\u062f\\u064a\\u0631\\u064a\\u0629 \\u0644\\u06403 \\u062f\\u0648\\u0644 \\u0639\\u0631\\u0628\\u064a\\u0629 \\u0648\\u062a\\u0633\\u062a\\u0647\\u062f\\u0641 \\u0641\\u062a\\u062d \\u062b\\u0627\\u0644\\u062b \\u0641\\u0631\\u0648\\u0639\\u0647\\u0627 \\u062e\\u0644\\u0627\\u0644 2025\"}}'),
(2, 'El Galla Gold\'s participation in the prestigious Istanbul Jewelry Show in October 2024.', 'El Galla Gold\'s enthusiastic participation in the prestigious Istanbul Jewelry Show in October 2024.\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n', 'images/20250212132044__33.png', 'https://www.youtube.com/watch?v=j8A2M3w0nDM', '', '', 0, 0, 0, '2025-02-12 12:06:51', '2024-12-12 09:29:26', 2, 1, '{\"ar\": {\"title\": \"\\u0645\\u0634\\u0627\\u0631\\u0643\\u0629 \\u0634\\u0631\\u0643\\u0629 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f \\u0641\\u064a \\u0645\\u0639\\u0631\\u0636 \\u0627\\u0633\\u0637\\u0646\\u0628\\u0648\\u0644 \\u0644\\u0644\\u0645\\u062c\\u0648\\u0647\\u0631\\u0627\\u062a \\u0641\\u064a \\u0623\\u0643\\u062a\\u0648\\u0628\\u0631 2024\"}}'),
(3, 'El Galla Gold proudly showcases a stunning collection of gold coins under the title \'Egyptian Tales of Gold.\'', 'El Galla Gold proudly showcases a stunning collection of gold coins under the title \'Egyptian Tales of Gold.\'', 'images/20250212132057__44.png', 'https://www.osoulmisrmagazine.com/397053', '', '', 0, 0, 0, '2025-02-12 12:07:07', '2024-12-12 09:29:26', 3, 1, '{\"ar\": {\"title\": \"\\u00ab\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\u00bb \\u062a\\u0633\\u062a\\u0639\\u0631\\u0636 \\u0645\\u062c\\u0645\\u0648\\u0639\\u0629 \\u0645\\u0646 \\u062c\\u0646\\u064a\\u0647\\u0627\\u062a \\u0627\\u0644\\u0630\\u0647\\u0628 \\u062a\\u062d\\u062a \\u0639\\u0646\\u0648\\u0627\\u0646 \\u00ab\\u062d\\u0643\\u0627\\u064a\\u0627\\u062a \\u0645\\u0635\\u0631\\u064a\\u0629 \\u0645\\u0646 \\u0630\\u0647\\u0628\\u00bb\\r\\n\"}}'),
(4, 'El Galla Gold\'s participation in the fourth edition of the Nebu Expo for Gold & Jewelry', 'El Galla Gold\'s participation in the fourth edition of the Nebu Expo for Gold & Jewelry', 'images/20250212124819__000_0441.png', 'https://www.youtube.com/watch?v=Vpi3I1SwcDg', '', '', 0, 0, 0, '2025-02-12 12:07:21', '2024-12-12 09:29:26', 4, 1, '{\"ar\": {\"title\": \"\\u0645\\u0634\\u0627\\u0631\\u0643\\u0629 \\u0634\\u0631\\u0643\\u0629 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f \\u0641\\u064a \\u0627\\u0644\\u0646\\u0633\\u062e\\u0629 \\u0627\\u0644\\u0631\\u0627\\u0628\\u0639\\u0629 \\u0645\\u0646 \\u0645\\u0639\\u0631\\u0636 \\u0646\\u0628\\u064a\\u0648 \\u0644\\u0644\\u0630\\u0647\\u0628 \\u0648 \\u0627\\u0644\\u0645\\u062c\\u0648\\u0647\\u0631\\u0627\\u062a\\r\\n\"}}'),
(5, 'Foreign attendance at the \'Nebu\' exhibition supports Egyptian companies\' exports.', 'Foreign attendance at the \'Nebu\' exhibition supports Egyptian companies\' exports.', 'images/20250212124946__000_0462.png', 'https://www.alborsaanews.com/2024/12/17/1854208', '', '', 0, 0, 0, '2025-02-12 12:07:34', '2024-12-12 09:29:26', 5, 1, '{\"ar\": {\"title\": \"\\u0625\\u0642\\u0628\\u0627\\u0644 \\u0627\\u0644\\u0623\\u062c\\u0627\\u0646\\u0628 \\u0639\\u0644\\u0649 \\u0645\\u0639\\u0631\\u0636 \\u201c\\u0646\\u064a\\u0628\\u0648\\u201d \\u064a\\u062f\\u0639\\u0645 \\u0635\\u0627\\u062f\\u0631\\u0627\\u062a \\u0627\\u0644\\u0634\\u0631\\u0643\\u0627\\u062a \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\\u0629\\r\\n\"}}'),
(9, 'Dahab Masr', 'Dahab Masr', 'images/20250209185545__Copy_of_Dahab_Masr_Signature_-_lookup_2.png', NULL, '', '', 18, 0, 0, '2025-02-16 13:52:21', '2025-02-13 12:58:59', NULL, NULL, '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0630\\u0647\\u0628 \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\", \"content\": \"\\u0627\\u0644\\u0630\\u0647\\u0628 \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\"}}'),
(10, 'Kamalo', 'Kamalo', 'images/20250209185636__images.png', NULL, '', '', 18, 0, 0, '2025-02-16 13:52:55', '2025-02-13 12:58:59', NULL, NULL, '{\"ar\": {\"title\": \"\\u0643\\u0645\\u0627\\u0644\\u0648\", \"content\": \"\\u0643\\u0645\\u0627\\u0644\\u0648\"}}'),
(11, 'El Galla Jewellery', 'El Galla Jewellery', 'images/20250209191250__elgallajewel.jpg', NULL, '', '', 18, 0, 0, '2025-02-16 13:53:17', '2025-02-13 12:58:59', NULL, NULL, '{\"ar\": {\"title\": \"\\u0645\\u062c\\u0648\\u0647\\u0631\\u0627\\u062a \\u0627\\u0644\\u062c\\u0644\\u0627\", \"content\": \"\\u0645\\u062c\\u0648\\u0647\\u0631\\u0627\\u062a \\u0627\\u0644\\u062c\\u0644\\u0627\"}}'),
(12, 'EL KADY', 'EL KADY', 'images/20250209191614__El_Kady_K_logo-1.png', 'None', 'cairo', 'maadi', 18, 0, 0, '0000-00-00 00:00:00', '2025-02-13 12:58:59', 0, 0, '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0642\\u0627\\u0636\\u064a\", \"content\": \"\\u0627\\u0644\\u0642\\u0627\\u0636\\u064a\"}}'),
(13, 'GOLD SOUQ', 'GOLD SOUQ', 'images/20250209191705__gold_souq_logo_final_241112_140149-1.png', 'None', 'alexandria', '-', 18, 0, 0, '2025-03-03 09:08:18', '2025-02-13 12:58:59', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0648\\u0642 \\u0627\\u0644\\u0630\\u0647\\u0628\", \"content\": \"\\u0633\\u0648\\u0642 \\u0627\\u0644\\u0630\\u0647\\u0628\"}}'),
(14, 'ALZAHRAA', 'ALZAHRAA', 'images/20250209191832__Logo_Alzahraa-1.png', 'None', 'cairo', 'october', 18, 0, 0, '2025-03-03 09:08:07', '2025-02-13 12:58:59', 0, 0, '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0632\\u0647\\u0631\\u0627\\u0621\", \"content\": \"\\u0627\\u0644\\u0632\\u0647\\u0631\\u0627\\u0621\"}}');

-- --------------------------------------------------------

--
-- Table structure for table `gla_blog_category`
--

CREATE TABLE `gla_blog_category` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `des` text DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL,
  `kit_lang` text DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_blog_category`
--

INSERT INTO `gla_blog_category` (`id`, `title`, `des`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(18, 'partner', 'partner', 0, 0, '2025-02-13 13:01:43', '2025-02-13 13:01:43', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `gla_login_temp`
--

CREATE TABLE `gla_login_temp` (
  `id` int(11) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `otp` varchar(10) DEFAULT NULL,
  `expiry` datetime NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_login_temp`
--

INSERT INTO `gla_login_temp` (`id`, `mobile`, `otp`, `expiry`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(32, '01555256285', '4002', '2025-03-04 22:16:01', 0, 0, '2025-03-04 20:11:01', '2025-02-16 15:38:02'),
(33, '01123881630', '9538', '2025-03-04 22:34:28', 0, 0, '2025-03-04 20:29:28', '2025-03-03 13:57:18');

-- --------------------------------------------------------

--
-- Table structure for table `gla_order`
--

CREATE TABLE `gla_order` (
  `id` int(11) NOT NULL,
  `fk_user_id` int(11) NOT NULL DEFAULT 0,
  `total` int(11) NOT NULL,
  `shipping` double NOT NULL,
  `payment_method` varchar(55) NOT NULL,
  `payment_status` varchar(55) NOT NULL,
  `order_status` varchar(55) NOT NULL,
  `delivery_type` varchar(100) NOT NULL,
  `fk_address_id` int(11) NOT NULL,
  `document` text NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_order`
--

INSERT INTO `gla_order` (`id`, `fk_user_id`, `total`, `shipping`, `payment_method`, `payment_status`, `order_status`, `delivery_type`, `fk_address_id`, `document`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(20, 1, 335700, 200, '8', 'pending', 'pending', 'store', 2, '', 0, 0, '2025-03-03 11:44:34', '2025-03-03 11:44:34');

-- --------------------------------------------------------

--
-- Table structure for table `gla_order_item`
--

CREATE TABLE `gla_order_item` (
  `id` int(11) NOT NULL,
  `fk_order_id` int(11) NOT NULL,
  `fk_product_id` int(11) NOT NULL,
  `subtype` varchar(50) NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `gram_price` double NOT NULL,
  `quantity` int(11) NOT NULL,
  `charges` decimal(10,0) NOT NULL,
  `gift_card` tinyint(4) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_order_item`
--

INSERT INTO `gla_order_item` (`id`, `fk_order_id`, `fk_product_id`, `subtype`, `price`, `gram_price`, `quantity`, `charges`, `gift_card`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(21, 20, 1, 'george', 8415, 4140, 4, 0, 0, 0, 0, '0000-00-00 00:00:00', '2025-03-03 11:44:34'),
(22, 20, 4, 'countryside', 33560, 4140, 3, 0, 1, 0, 0, '0000-00-00 00:00:00', '2025-03-03 11:44:34'),
(23, 20, 4, 'mawled_nabawy', 33560, 4140, 6, 0, 0, 0, 0, '0000-00-00 00:00:00', '2025-03-03 11:44:34');

-- --------------------------------------------------------

--
-- Table structure for table `gla_payment_methods`
--

CREATE TABLE `gla_payment_methods` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `des` text DEFAULT NULL,
  `logo` varchar(255) NOT NULL,
  `charges` varchar(10) DEFAULT NULL,
  `charges_type` varchar(10) DEFAULT NULL,
  `paymob_id` text NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL,
  `kit_lang` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_payment_methods`
--

INSERT INTO `gla_payment_methods` (`id`, `title`, `des`, `logo`, `charges`, `charges_type`, `paymob_id`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(1, 'Cash', 'Pay with cash upon delivery. Please ensure you have the exact amount ready as our delivery personnel may not have change.', '', '', '', '', 0, 0, '2025-02-18 12:52:57', '2025-02-18 12:52:33', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u062f\\u0641\\u0639 \\u0639\\u0646\\u062f \\u0627\\u0644\\u062a\\u0633\\u0644\\u064a\\u0645\", \"des\": \"\\u0627\\u062f\\u0641\\u0639 \\u0646\\u0642\\u062f\\u064b\\u0627 \\u0639\\u0646\\u062f \\u0627\\u0644\\u0627\\u0633\\u062a\\u0644\\u0627\\u0645. \\u064a\\u0631\\u062c\\u0649 \\u0627\\u0644\\u062a\\u0623\\u0643\\u062f \\u0645\\u0646 \\u0623\\u0646 \\u0644\\u062f\\u064a\\u0643 \\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u0645\\u062d\\u062f\\u062f \\u062c\\u0627\\u0647\\u0632\\u064b\\u0627 \\u0644\\u0623\\u0646 \\u0645\\u0648\\u0638\\u0641\\u064a \\u0627\\u0644\\u062a\\u0648\\u0635\\u064a\\u0644 \\u0644\\u062f\\u064a\\u0646\\u0627 \\u0642\\u062f \\u0644\\u0627 \\u064a\\u0643\\u0648\\u0646 \\u0644\\u062f\\u064a\\u0647\\u0645 \\u0623\\u064a \\u0646\\u0642\\u0648\\u062f.\"}}'),
(2, 'Aman', 'Pay securely using Aman service', 'images/payment/20250218150813__aman_logo.png', '20', 'fixed', '4919279', 0, 0, '2025-02-18 13:08:14', '2025-02-18 12:55:42', '{\"ar\": {\"title\": \"\\u0623\\u0645\\u0627\\u0646\", \"des\": \"\\u0627\\u0644\\u062f\\u0641\\u0639 \\u0639\\u0628\\u0631 \\u062e\\u062f\\u0645\\u0629 \\u0623\\u0645\\u0627\\u0646 \\u0628\\u0633\\u0647\\u0648\\u0644\\u0629 \\u0648\\u0623\\u0645\\u0627\\u0646\"}}'),
(3, 'Contact', 'Pay via Contact for fast financial solutions', 'images/payment/20250218150758__contact_logo.png', '20', 'fixed', '4919279', 0, 0, '2025-02-18 13:08:00', '2025-02-18 12:56:24', '{\"ar\": {\"title\": \"\\u0643\\u0648\\u0646\\u062a\\u0627\\u0643\\u062a\", \"des\": \"\\u0627\\u0644\\u062f\\u0641\\u0639 \\u0645\\u0646 \\u062e\\u0644\\u0627\\u0644 \\u0643\\u0648\\u0646\\u062a\\u0627\\u0643\\u062a \\u0644\\u0644\\u062d\\u0644\\u0648\\u0644 \\u0627\\u0644\\u0645\\u0627\\u0644\\u064a\\u0629 \\u0627\\u0644\\u0633\\u0631\\u064a\\u0639\\u0629\"}}'),
(4, 'Mogo', ' Mogo service for easy purchase financing', 'images/payment/20250218150734__mogo_logo.png', '20', 'fixed', '4919279', 0, 0, '2025-02-18 13:07:36', '2025-02-18 12:57:17', '{\"ar\": {\"title\": \"\\u0645\\u0648\\u062c\\u0648\", \"des\": \"\\u062e\\u062f\\u0645\\u0629 \\u0645\\u0648\\u062c\\u0648 \\u0644\\u062a\\u0645\\u0648\\u064a\\u0644 \\u0627\\u0644\\u0645\\u0634\\u062a\\u0631\\u064a\\u0627\\u062a \\u0628\\u0633\\u0647\\u0648\\u0644\\u0629\"}}'),
(5, 'Souhoola', 'Install your purchases with Souhoola hassle-free', 'images/payment/20250218150910__Souhoola_logo.png', '20', 'fixed', '4919279', 0, 0, '2025-02-18 13:09:12', '2025-02-18 12:58:16', '{\"ar\": {\"title\": \"\\u0633\\u0647\\u0648\\u0644\\u0629\", \"des\": \"\\u0642\\u0633\\u0651\\u0637 \\u0645\\u0634\\u062a\\u0631\\u064a\\u0627\\u062a\\u0643 \\u0645\\u0639 \\u0633\\u0647\\u0648\\u0644\\u0629 \\u0628\\u062f\\u0648\\u0646 \\u062a\\u0639\\u0642\\u064a\\u062f\\u0627\\u062a\"}}'),
(6, 'Forsa', 'Quick and easy financing through Forsa', 'images/payment/20250218151034__forsa_logo.png', '20', 'fixed', '4919279', 0, 0, '2025-02-18 13:10:36', '2025-02-18 12:59:03', '{\"ar\": {\"title\": \"\\u0641\\u0631\\u0635\\u0629\", \"des\": \"\\u062a\\u0645\\u0648\\u064a\\u0644 \\u0633\\u0647\\u0644 \\u0648\\u0633\\u0631\\u064a\\u0639 \\u0639\\u0628\\u0631 \\u0641\\u0631\\u0635\\u0629\"}}'),
(7, 'Cards', 'Pay using credit and debit cards', 'images/payment/20250218151458__visa_logo.png', '2', 'percent', '4919279', 0, 0, '2025-02-18 13:14:59', '2025-02-18 12:59:59', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0628\\u0637\\u0627\\u0642\\u0627\\u062a\", \"des\": \"\\u0627\\u0644\\u062f\\u0641\\u0639 \\u0628\\u0628\\u0637\\u0627\\u0642\\u0627\\u062a \\u0627\\u0644\\u0627\\u0626\\u062a\\u0645\\u0627\\u0646 \\u0648\\u0627\\u0644\\u062e\\u0635\\u0645 \\u0627\\u0644\\u0645\\u0628\\u0627\\u0634\\u0631\"}}'),
(8, 'Bank Transfer', 'Secure payment via bank transfer', '', '', '', '', 0, 0, '2025-03-02 09:10:48', '2025-02-18 13:00:45', '{\"ar\": {\"title\": \"\\u062a\\u062d\\u0648\\u064a\\u0644 \\u0628\\u0646\\u0643\\u064a\", \"des\": \"\\u062a\\u062d\\u0648\\u064a\\u0644 \\u0628\\u0646\\u0643\\u064a \\u0645\\u0628\\u0627\\u0634\\u0631 \\u0644\\u0644\\u062f\\u0641\\u0639 \\u0628\\u0623\\u0645\\u0627\\u0646\"}}');

-- --------------------------------------------------------

--
-- Table structure for table `gla_price`
--

CREATE TABLE `gla_price` (
  `id` int(11) NOT NULL,
  `buy` varchar(255) DEFAULT NULL,
  `sell` varchar(255) DEFAULT NULL,
  `buy_24` varchar(50) NOT NULL,
  `sell_24` varchar(50) NOT NULL,
  `kit_deleted` tinyint(4) DEFAULT 0,
  `kit_disabled` tinyint(4) DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `kit_lang` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `gla_price`
--

INSERT INTO `gla_price` (`id`, `buy`, `sell`, `buy_24`, `sell_24`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(8, '4040', '4005', '4617', '4577', 0, 0, NULL, '0000-00-00 00:00:00', ''),
(7, '4005', '4045', '4577', '4622', 0, 0, NULL, '2025-03-02 08:49:22', ''),
(9, '4070', '4050', '4651', '4628', 0, 0, NULL, '2025-03-02 09:28:26', ''),
(10, '4005', '4045', '4577', '4622', 0, 0, NULL, '2025-03-02 10:39:39', ''),
(11, '4050', '4090', '4628', '4674', 0, 0, NULL, '2025-03-02 10:45:36', ''),
(12, '4050', '4050', '4628', '4628', 0, 0, NULL, '2025-03-02 10:46:01', ''),
(13, '4005', '4045', '4577', '4622', 0, 0, NULL, '2025-03-02 10:46:25', ''),
(14, '4100', '4140', '4685', '4731', 0, 0, NULL, '2025-03-02 11:51:16', '');

-- --------------------------------------------------------

--
-- Table structure for table `gla_product`
--

CREATE TABLE `gla_product` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `des` text DEFAULT NULL,
  `th_main` varchar(255) DEFAULT NULL,
  `th_overlay` varchar(255) DEFAULT NULL,
  `price` double NOT NULL DEFAULT 0,
  `buy_price` double DEFAULT NULL,
  `weight` varchar(45) DEFAULT NULL,
  `kart` varchar(45) DEFAULT NULL,
  `stamp` double DEFAULT NULL,
  `vat` double DEFAULT NULL,
  `gram` int(11) DEFAULT NULL,
  `cashback_gram` int(11) DEFAULT NULL,
  `cashback` double DEFAULT NULL,
  `fk_product_category_id` int(11) DEFAULT 0,
  `types_data` text DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `display_home` tinyint(4) DEFAULT NULL,
  `kit_order` int(11) DEFAULT NULL,
  `kit_lang` text DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_product`
--

INSERT INTO `gla_product` (`id`, `title`, `des`, `th_main`, `th_overlay`, `price`, `buy_price`, `weight`, `kart`, `stamp`, `vat`, `gram`, `cashback_gram`, `cashback`, `fk_product_category_id`, `types_data`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `display_home`, `kit_order`, `kit_lang`) VALUES
(1, 'Quarter Gold Coin', 'Quarter Gold Coin', '/images/products/_1/quarter George gold coin front.png', '/images/products/_1/quarter George gold coin back.png', 8415, 8245, '2', '21', 59.55, 7.45, 1, 1, 22.5, 2, '{\n  \"royal\": {\n    \"title\": \"Royal\",\n    \"alias\": \"royal\",\n    \"id\": 15,\n    \"des\": \"\",\n    \"data\": {\n      \"george\": {\n        \"title\": \"George\",\n        \"alias\": \"george\",\n        \"id\": 5,\n        \"des\": \"\",\n        \"fk_parent_id\": 15,\n        \"uid\": \"b718b8f0a5d64287a4c301ed2dce152a\",\n        \"images\": \"images/products/250a8bc6386741199b7162a4b676c3f5__quarter_George_gold_coin_front.png,images/products/dcb6d832d8bd41c4b88e337d70e05f2e__quarter_George_gold_coin_back.png\",\n        \"order\": \"1\",\n        \"label\": \"\"\n      }\n    }\n  }\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-06 10:04:58', 1, 0, '{\"ar\": {\"title\": \"\\u0631\\u0628\\u0639 \\u062c\\u0646\\u064a\\u0647 \\u0630\\u0647\\u0628\"}}'),
(2, 'Eighth Gold Coin', 'Eighth Gold Coin', '/images/products/_2/Eighth George gold coin front.png', '/images/products/_2/Eighth George gold coin back.png', 4215, 4120, '1', '21', 67.55, 7.45, 1, 1, 22.5, 2, '{\r\n  \"royal\": {\r\n    \"title\": \"Royal\",\r\n    \"alias\": \"royal\",\r\n    \"id\": 15,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"george\": {\r\n        \"title\": \"George\",\r\n        \"alias\": \"george\",\r\n        \"id\": 5,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 15,\r\n        \"uid\": \"6bf37ee5b05c4b9f8e31d64c74a8ca0f\",\r\n        \"images\": \"images/products/f46ae677011346238b4d58789524669c__Eighth_George_gold_coin_front.png,images/products/2dc1a2543345476b946ffa9d696a0b52__Eighth_George_gold_coin_back.png\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:00:09', 0, 0, '{\"ar\": {\"title\": \"\\u062b\\u0645\\u0646 \\u062c\\u0646\\u064a\\u0647 \\u0630\\u0647\\u0628\"}}'),
(3, 'Half Gold Coin', 'Half Gold Coin', '/images/products/_3/half George gold coin front.png', '/images/products/_3/half George gold coin back.png', 16805, 16490, '4', '21', 53.55, 7.45, 1, 1, 22.5, 2, '{\r\n  \"royal\": {\r\n    \"title\": \"Royal\",\r\n    \"alias\": \"royal\",\r\n    \"id\": 15,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"george\": {\r\n        \"title\": \"George\",\r\n        \"alias\": \"george\",\r\n        \"id\": 5,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 15,\r\n        \"uid\": \"9ffd3d3df9724d07ae3fd910e9939d59\",\r\n        \"images\": \"images/products/76153da0d9d146bfa87c076d29d94109__half_George_gold_coin_front.png,images/products/6ffcd7bd37284a1d954ae1b22c7f886f__half_George_gold_coin_back.png\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:03:47', 1, 0, '{\"ar\": {\"title\": \"\\u0646\\u0635\\u0641 \\u062c\\u0646\\u064a\\u0647 \\u0630\\u0647\\u0628\"}}'),
(4, 'One Gold Coin', 'One Gold Coin', '/images/products/_4/one George gold coin front.png', '/images/products/_4/one George gold coin back.png', 33560, 32980, '8', '21', 47.55, 7.45, 1, 1, 22.5, 2, '{\r\n  \"royal\": {\r\n    \"title\": \"Royal\",\r\n    \"alias\": \"royal\",\r\n    \"id\": 15,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"george\": {\r\n        \"title\": \"George\",\r\n        \"alias\": \"george\",\r\n        \"id\": 5,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 15,\r\n        \"uid\": \"76d49e642fe6453a99db70588922487d\",\r\n        \"images\": \"images/products/1f7b3324867b49ee805dd6642f2f8d0b__one_George_gold_coin_front.png,images/products/ff26eceaf4e444e4b674da198019780a__one_George_gold_coin_back.png\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      },\r\n      \"elizabeth\": {\r\n        \"title\": \"Elizabeth\",\r\n        \"alias\": \"elizabeth\",\r\n        \"id\": 4,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 15,\r\n        \"uid\": \"448d9312907e4a37be03150a70b65d22\",\r\n        \"images\": \"images/products/a2fc5309e50444c5a7ac198060841f00__one_Elizabeth_gold_coin_front.png,images/products/dee28963814c41c3bce41937a130c006__one_Elizabeth_gold_coin_back.png\",\r\n        \"order\": \"2\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  },\r\n  \"egyptian\": {\r\n    \"title\": \"Egyptian\",\r\n    \"alias\": \"egyptian\",\r\n    \"id\": 1,\r\n    \"des\": \"Egyptian\",\r\n    \"data\": {\r\n      \"aswan\": {\r\n        \"title\": \"Aswan\",\r\n        \"alias\": \"aswan\",\r\n        \"id\": 10,\r\n        \"des\": \"Aswan\",\r\n        \"fk_parent_id\": 1,\r\n        \"uid\": \"e31ce53315bc490caf6b12d2b4ae38fa\",\r\n        \"images\": \"images/products/67594569b44345a084a802e55f65a0ce__one_gold_coin_Aswan.png,images/products/86f4b50c3a244a82b5b0363465b8b281__one_gold_coin_back.png,images/products/5a9a2200efd7425082ebfc5bcbbf5d92__aswan.png\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      },\r\n      \"countryside\": {\r\n        \"title\": \"Countryside\",\r\n        \"alias\": \"countryside\",\r\n        \"id\": 11,\r\n        \"des\": \"Countryside\",\r\n        \"fk_parent_id\": 1,\r\n        \"uid\": \"f5276db4d0da47ceb05afbdca910da90\",\r\n        \"images\": \"images/products/7f8ebd067b834e8aa7cfc8af5b4d3b1d__one_gold_coin_Egyptian_Countryside.png,images/products/32e1b8ca9d7b4334a5ac75bca30777e3__one_gold_coin_back.png,images/products/4b5f75ab71ea4880a205fe00b1683703__Egyptian_Countryside.png\",\r\n        \"order\": \"3\",\r\n        \"label\": \"\"\r\n      },\r\n      \"al_mermah_al_saeedi\": {\r\n        \"title\": \"Al Mermah Al Saeedi\",\r\n        \"alias\": \"al_mermah_al_saeedi\",\r\n        \"id\": 9,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 1,\r\n        \"uid\": \"a6fc6a255cf74aabbbfec1d9ee6b5ede\",\r\n        \"images\": \"images/products/e16b891e9fc949479fe48568e1f4f21e__one_gold_coin_Al_Mermah_Al_Saeedi.png,images/products/cd219a65f93e446f830700c5964293a1__one_gold_coin_back.png,images/products/7754a27e64e9463ba5a2320cb218b9c8__Al_Mermah_Al_Saeed.png\",\r\n        \"order\": \"4\",\r\n        \"label\": \"\"\r\n      },\r\n      \"siwa\": {\r\n        \"title\": \"Siwa\",\r\n        \"alias\": \"siwa\",\r\n        \"id\": 2,\r\n        \"des\": \"Siwa\",\r\n        \"fk_parent_id\": 1,\r\n        \"uid\": \"df7f05477a95445698db7d507083bb80\",\r\n        \"images\": \"images/products/c37b29e6e7d343309e3553e007881c35__one_gold_coin_Siwa.png,images/products/c5d4e62c536a4ebb983c437f1024d00e__one_gold_coin_back.png,images/products/6c4bea5f03a541c2873de0a1ae75c8ba__siwa.png\",\r\n        \"order\": \"2\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  },\r\n  \"islamic\": {\r\n    \"title\": \"Islamic\",\r\n    \"alias\": \"islamic\",\r\n    \"id\": 6,\r\n    \"des\": \"Islamic\",\r\n    \"data\": {\r\n      \"mawled_nabawy\": {\r\n        \"title\": \"mawled nabawy\",\r\n        \"alias\": \"mawled_nabawy\",\r\n        \"id\": 7,\r\n        \"des\": \"mawled nabawy\",\r\n        \"fk_parent_id\": 6,\r\n        \"uid\": \"8dcd5a2c74e74f6fa3124dd2f75fc541\",\r\n        \"images\": \"images/products/792a967e4bab4404bb46219d34854403__one_islamic_gold_coin_mawled_nabawy_front.png,images/products/c251e7f99e414e298eb54f6749dee69b__one_islamic_gold_coin_mawled_nabawy_back.png\",\r\n        \"order\": \"2\",\r\n        \"label\": \"\"\r\n      },\r\n      \"kaaba\": {\r\n        \"title\": \"kaaba\",\r\n        \"alias\": \"kaaba\",\r\n        \"id\": 8,\r\n        \"des\": \"kaaba\",\r\n        \"fk_parent_id\": 6,\r\n        \"uid\": \"ec4fe79066c44c958c2898136ecc5ad7\",\r\n        \"images\": \"images/products/22153013a6ee4755b94da40c047ae6ec__one_islamic_gold_coin_back_Kaaba.png,images/products/40dc6ff9f6fa478ea09a5734504e2378__one_islamic_gold_coin_front_Kaaba.png\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:04:13', 1, 0, '{\"ar\": {\"title\": \"\\u062c\\u0646\\u064a\\u0647 \\u0630\\u0647\\u0628\"}}'),
(5, 'Five Pound Coin', '- Five Pound Elizabeth Coin\r\n- Five Pound Elizabeth Coin\r\n- Five Pound Elizabeth Coin\r\n- Five Pound Elizabeth Coin\r\n\r\n\r\n', '/images/products/_5/five pound George gold coin front.png', '/images/products/_5/five pound George gold coin back.png', 167760, 164900, '40', '21', 46.55, 7.45, 1, 1, 22.5, 2, '{\r\n  \"royal\": {\r\n    \"title\": \"Royal\",\r\n    \"alias\": \"royal\",\r\n    \"id\": 15,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"george\": {\r\n        \"title\": \"George\",\r\n        \"alias\": \"george\",\r\n        \"id\": 5,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 15,\r\n        \"uid\": \"02535034b37f4295896d4452f81caea2\",\r\n        \"images\": \"images/products/cf9fd7b5b2cd4a33b0c87e2963f97988__five_pound_George_gold_coin_front.png,images/products/fb60dad7ace04d85be145e3b829ce43c__five_pound_George_gold_coin_back.png\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      },\r\n      \"elizabeth\": {\r\n        \"title\": \"Elizabeth\",\r\n        \"alias\": \"elizabeth\",\r\n        \"id\": 4,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 15,\r\n        \"uid\": \"d8aceef8346641198b7e293e6da1a578\",\r\n        \"images\": \"images/products/a83003bfeaf345a69e7d6288d31f89a5__five_Elizabeth_gold_coin_front.png,images/products/c138942185ae4dfda794d0579ab5a1f8__five_Elizabeth_gold_coin_back.png\",\r\n        \"order\": \"2\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:04:39', 1, 0, '{\"ar\": {\"title\": \"\\u062e\\u0645\\u0633\\u0629 \\u062c\\u0646\\u064a\\u0647 \\u0630\\u0647\\u0628\"}}'),
(6, '2.5gr Gold Baby Bottle (Girl)', '2.5gr Gold Baby Bottle (Girl)', 'images/products/_6/2.5 gm baby bottle (girl) front.jpg ', 'images/products/_6/2.5 gm baby bottle (girl) back.jpg', 12100, 11780, '2.5', '24', 98.82, 11.18, 1, 1, 26, 3, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"8feab375316a4b0e83083ed0c1803a66\",\r\n        \"images\": \"images/products/5dfe1a04c1be4535b46ef0c2a7c5d16c__2.5_gm_baby_bottle_girl_front.jpg,images/products/cbbf49448ac54751b740bf4188754905__2.5_gm_baby_bottle_girl_back.jpg,images/products/ae4a0d28793a46bda7c533ef2911fdb4__girl.png\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:06:45', 1, 0, '{\"ar\": {\"title\": \"(\\u0628\\u0628\\u0631\\u0648\\u0646\\u0647 \\u0630\\u0647\\u0628 2.5\\u062c\\u0645 (\\u0628\\u0646\\u062a\"}}'),
(7, '2.5gr Gold Baby Bottle (Boy)', '2.5gr Gold Baby Bottle (Boy)', 'images/products/_7/2.5 gm baby bottle (boy) front.jpg', 'images/products/_7/2.5 gm baby bottle (boy) back.jpg', 12100, 11780, '2.5', '24', 98.82, 11.18, 1, 1, 26, 3, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"b0b35b54120841e9a687285de515f5eb\",\r\n        \"images\": \"images/products/e7de8fb24aa042c9ba3e53dd1a5943ad__2.5_gm_baby_bottle_boy_front.jpg,images/products/4c3155b14507489682c3f32966559062__2.5_gm_baby_bottle_boy_back.jpg,images/products/2053c871201c4795a9db42757e5aae43__boy.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:07:00', 1, 0, '{\"ar\": {\"title\": \"(\\u0628\\u0628\\u0631\\u0648\\u0646\\u0647 \\u0630\\u0647\\u0628 2.5\\u062c\\u0645 (\\u0648\\u0644\\u062f\"}}'),
(8, '5gr Gold Baby Bottle (Girl)', '5gr Gold Baby Bottle (Girl)', 'images/products/_8/5_gm_baby_bottle_boy_front.jpg', 'images/products/_8/5_gm_baby_bottle_boy_back.jpg', 24155, 23555, '5', '24', 88.82, 11.18, 1, 1, 26, 3, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"cd26023e52a54c159c9e62496632219d\",\r\n        \"images\": \"images/products/26f4a9a100544e59bf5c8788fcd262a7__5_gm_baby_bottle_boy_front.jpg,images/products/440e20bec84e4d41942d90463ec4ba04__5_gm_baby_bottle_boy_back.jpg,images/products/f4c2c41e33c84b629481859441ab244b__girl.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:07:14', 1, 0, '{\"ar\": {\"title\": \"(\\u0628\\u0628\\u0631\\u0648\\u0646\\u0647 \\u0630\\u0647\\u0628 5\\u062c\\u0645 (\\u0628\\u0646\\u062a\"}}'),
(9, '5gr Gold Baby Bottle (Boy)', '5gr Gold Baby Bottle (Boy)', 'images/products/_9/5 _gm_baby_bottle_boy_front.jpg', 'images/products/_9/5_gm_baby_bottle_boy_back.jpg', 24155, 23555, '5', '24', 88.82, 11.18, 1, 1, 26, 3, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"1dff61db356b412db3fd77988daeb607\",\r\n        \"images\": \"images/products/08e0f45417b8412695626cbe716b88a5__5__gm_baby_bottle_boy_front.jpg,images/products/daecf942446b490781f19a6df7ae0a9a__5_gm_baby_bottle_boy_back.jpg,images/products/3e34c1f2863848a49ebeec774953accb__boy.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-13 12:07:27', 1, 0, '{\"ar\": {\"title\": \"(\\u0628\\u0628\\u0631\\u0648\\u0646\\u0647 \\u0630\\u0647\\u0628 5\\u062c\\u0645 (\\u0648\\u0644\\u062f\"}}'),
(12, '1gr Gold Bar', '1gr Gold Bar', 'images/products/_12/1_gm_bar_front.jpg', 'images/products/_12/1_gm_bar_back.jpg', 4870, 4710, '1', '24', 128.82, 11.18, 0, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"62756350d36f49899a88bfecaea491c7\",\r\n        \"images\": \"images/products/39bbf5ecb84c4c1a96424a2a9c649861__1_gm_bar_front.jpg,images/products/bb0ea332909c47c68020cec1c83bf800__1_gm_bar_back.jpg,images/products/dae155cdaf57414896f537c384437f10__1_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 09:59:43', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 1\\u062c\\u0645\"}}'),
(13, '2.5gr Gold Bar', '2.5gr Gold Bar', 'images/products/_13/2.5_gm_bar_front.jpg', 'images/products/_13/2.5_gm_bar_back.jpg', 12080, 11780, '2.5', '24', 88.82, 11.18, 1, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"610edd08dd25441184239704399c785d\",\r\n        \"images\": \"images/products/60f1dbe00e42479ab3de64ce5b31ab1f__2.5_gm_bar_front.jpg,images/products/e983c15082fc495aab357b1401b6e277__2.5_gm_bar_back.jpg,images/products/fc5b56c2ff51427fa11873cd005e3f18__2.5_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 09:59:54', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 2.5\\u062c\\u0645\"}}'),
(14, '5gr Gold Bar', '5gr Gold Bar', 'images/products/_14/5_gm_bar_front.jpg', 'images/products/_14/5_gm_bar_back.jpg', 23995, 23555, '5', '24', 56.82, 11.18, 1, 1, 26, 1, '{\"standard\": {\"title\": \"Standard\", \"alias\": \"standard\", \"id\": 14, \"des\": \"\", \"data\": {\"standard\": {\"title\": \"Standard\", \"alias\": \"standard\", \"id\": 16, \"des\": \"\", \"fk_parent_id\": 14, \"uid\": \"9cbd774a1a5f4c9c8fa03a86739b865e\", \"images\": \"images/products/586d550d864847d6804009079b06de3e__5_gm_bar_front.jpg,images/products/f976f28594f445638673fcee42b095de__5_gm_bar_back.jpg,images/products/727eae447eda4b9dbe6db72cd77823ae__5_gm_bar.jpg\", \"order\": \"1\", \"label\": \"\"}}}}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:00:17', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 5\\u062c\\u0645\"}}'),
(15, '10gr Gold Bar', '10gr Gold Bar', 'images/products/_15/10_gm_bar_front.jpg', 'images/products/_15/10_gm_bar_back.jpg', 47980, 47110, '10', '24', 55.82, 11.18, 1, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"8bd95733983f4446b262ed60fde153d1\",\r\n        \"images\": \"images/products/78f232909d874b2ead1a45c27eff9218__10_gm_bar_front.jpg,images/products/af05afd9804447acaf30b13b6216bfd1__10_gm_bar_back.jpg,images/products/1ccc0d427a3e49a586999504dc8173a6__10_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  },\r\n  \"islamic\": {\r\n    \"title\": \"Islamic\",\r\n    \"alias\": \"islamic\",\r\n    \"id\": 6,\r\n    \"des\": \"Islamic\",\r\n    \"data\": {\r\n      \"kaaba\": {\r\n        \"title\": \"kaaba\",\r\n        \"alias\": \"kaaba\",\r\n        \"id\": 8,\r\n        \"des\": \"kaaba\",\r\n        \"fk_parent_id\": 6,\r\n        \"uid\": \"e95966652c7843f4bcf23371848ed5dc\",\r\n        \"images\": \"images/products/a83f574788ed443cbc7caf0a5d085242__10_gm_bar_islamic_back.jpg,images/products/1423e66a47fc43168230cb42d9bc85bb__10_gm_bar_islami_front.jpg\",\r\n        \"order\": \"2\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:00:30', 1, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 10\\u062c\\u0645\"}}'),
(16, '15.55gr Gold Bar', 'Half Troy Ounce Gold Bar', 'images/products/_16/15.55_gm_bar_front.jpg', 'images/products/_16/15.55_gm_bar_back.jpg', 74595, 73255, '15.55', '24', 54.82, 11.18, 1, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"c486a012e5684cea879714aea3b6b007\",\r\n        \"images\": \"images/products/52e1803b325345fd883992b7d26f085f__15.55_gm_bar_front.jpg,images/products/654c1f2490df450a8aa6258d7d9cb4ad__15.55_gm_bar_back.jpg,images/products/f9138bf23260436c9118def268bf0ba2__15.55_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:00:40', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 \\u0646\\u0635\\u0641 \\u0627\\u0648\\u0646\\u0635\\u0629\"}}'),
(17, '20gr Gold Bar', '20gr Gold Bar', 'images/products/_17/20_gm_bar_front.jpg', 'images/products/_17/20_gm_bar_back.jpg', 95920, 94220, '20', '24', 53.82, 11.18, 1, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"b1710823571b484eac1bd2afebfcfc91\",\r\n        \"images\": \"images/products/224a56b8d216406ba76631349c47b86a__20_gm_bar_front.jpg,images/products/7f12737bbd4d4bc5922dea0d3350371e__20_gm_bar_back.jpg,images/products/a4a511e6256e4188b896b369407a9d34__20_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:00:51', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 20\\u062c\\u0645\"}}'),
(18, 'One Troy Ounce Gold Bar', 'One Troy Ounce Gold Bar', 'images/products/_18/31.10_gm_bar_front.jpg', 'images/products/_18/31.10_gm_bar_back.jpg', 149095, 146510, '31.10', '24', 51.82, 11.18, 1, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"da667d108c794436967eccf9ec5c23b8\",\r\n        \"images\": \"images/products/9fd9c9576dc14d48a31dfeb7dadb5b2a__31.10_gm_bar_front.jpg,images/products/8ddbb24f6aa84012bd906221cdd780a5__31.10_gm_bar_back.jpg,images/products/87556a049a6848438262831269072303__31.10_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  },\r\n  \"islamic\": {\r\n    \"title\": \"Islamic\",\r\n    \"alias\": \"islamic\",\r\n    \"id\": 6,\r\n    \"des\": \"Islamic\",\r\n    \"data\": {\r\n      \"kaaba\": {\r\n        \"title\": \"kaaba\",\r\n        \"alias\": \"kaaba\",\r\n        \"id\": 8,\r\n        \"des\": \"kaaba\",\r\n        \"fk_parent_id\": 6,\r\n        \"uid\": \"9c10c20f6b574dc6830e40a09a665746\",\r\n        \"images\": \"images/products/00b70db072874dadaf9e9bb02598f3f1__31.10_gm_bar_islamic_back.jpg,images/products/b72f857624c749a98ab8a5075e941e74__31.10_gm_bar_islamic_front.jpg\",\r\n        \"order\": \"2\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:01:05', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 \\u0627\\u0648\\u0646\\u0635\\u0629\"}}'),
(19, '50gr Gold Bar', '50gr Gold Bar', 'images/products/_19/50_gm_bar_front.jpg', 'images/products/_19/50_gm_bar_back.jpg', 239600, 235550, '50', '24', 49.82, 11.18, 1, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"f849c0325f8c4f9a979fb7c1ebc79243\",\r\n        \"images\": \"images/products/a8942ccc13d8427f8e73de4e1ef9874c__50_gm_bar_front.jpg,images/products/545d4a629b484fab9fb1e6af2584d26f__50_gm_bar_back.jpg,images/products/c546b9b4388c416782462730a7fd506d__50_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:01:19', 1, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 50\\u062c\\u0645\"}}'),
(20, '100gr Gold Bar', '100gr Gold Bar', 'images/products/_20/100_gm_bar_front.jpg', 'images/products/_20/100_gm_bar_back.jpg', 479100, 471100, '100', '24', 48.82, 11.18, 1, 1, 26, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"566f38afe4d14c978d7a1ec594d594bd\",\r\n        \"images\": \"images/products/8379f568fe6f478baa9be55c622bb1bb__100_gm_bar_front.jpg,images/products/bfd3d86c44ed4d59baff27254a1920ab__100_gm_bar_back.jpg,images/products/7c9d9f05625a4d41bb93031671151689__100_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:01:35', 1, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 100\\u062c\\u0645\"}}'),
(21, 'Ten Tolas Gold Bar', 'Ten Tolas Gold Bar', 'images/products/_21/116.65_gm_front.jpg', 'images/products/_21/116.65_gm_back.jpg', 557410, 548315, '116.65', '24', 47.5, 0, 1, 1, 15.5, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"e43a14f9cd16430996d57c330016042a\",\r\n        \"images\": \"images/products/c4b91fef50d24e57b4439d90d3e824a4__116.65_gm_front.jpg,images/products/4441cf8e0b6144e08405ab36dc57f350__116.65_gm_back.jpg,images/products/418cc8e194d8400aa108cdfcefc1ae0e__116.65_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:01:51', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 \\u0639\\u0634\\u0631\\u0629 \\u062a\\u0648\\u0644\\u0629\"}}'),
(22, '250gr Gold Bar', '250gr Gold Bar', 'images/products/_22/250_gm_front.jpg', 'images/products/_22/250_gm_back.jpg', 1193375, 1175000, '250', '24', 42.5, 0, 1, 1, 15, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"222645772f8b4130af446f266fefeeee\",\r\n        \"images\": \"images/products/0c30a49465f84b7482dae6bef5187ae8__250_gm_front.jpg,images/products/79cab4c066784a6d98bc4aaab2a4b6ef__250_gm_back.jpg,images/products/11dc91e3d80144c7a32496ffd313b795__250_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-01-14 10:02:08', 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 250\\u062c\\u0645\"}}'),
(33, '500gr Gold Bar', '500gr Gold Bar\r\n', 'images/products/_33/500_gm_bar_front.jpg', 'images/products/_33/500_gm_bar_front.jpg', 2386000, 2348500, '500', '24', 41, 0, 1, 1, 12, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"1363ed904b27404f91cb52dca261c6ed\",\r\n        \"images\": \"images/products/ff1e671d04a542c8bda928e2ea908aa9__500_gm_bar_front.jpg,images/products/b4e64c0e7cb1454286330c00d9ef9291__500.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-02-09 14:21:44', 1, 22, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 500\\u062c\\u0645\"}}'),
(34, '1000gr Gold Bar', '1000gr Gold Bar', 'images/products/_34/1000_gm_bar_front.jpg', 'images/products/_34/1000_gm_bar_front.jpg', 4770000, 4697000, '1000', '24', 39, 0, 1, 1, 12, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"85fe87e9cd9048fd921d8211907c2719\",\r\n        \"images\": \"images/products/f1e1dd7791524116b1c15a8e2bd409ff__1000_gm_bar_front.jpg,images/products/4f32d1ba70024386b023bf2ed9f4ac09__1000.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-02-09 14:22:49', 0, 434, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 1000\\u062c\\u0645\"}}'),
(35, '0.25gr Gold Bar', '0.25gr Gold Bar\r\n', 'images/products/_35/5_gm_bar_front.jpg', 'images/products/_35/5_gm_bar_back.jpg', 1380, 1190, '0.25', '24', 197.205, 2.795, 0, 0, 20, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"d5266c357c1f4819b33643693e5d4c70\",\r\n        \"images\": \"images/products/0e681435443a4cd5b8716d1c14bf2e46__5_gm_bar_front.jpg,images/products/946216fdcb90456eb106d93f731490f9__5_gm_bar_back.jpg,images/products/49af2cba77054f7c8a32290457ec5570__5_gm_bar.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-02-09 14:46:54', 0, 2222, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 0.25\\u062c\\u0645\"}}'),
(36, '0.5gr Gold Bar', '0.5gr Gold Bar', 'images/products/_36/25_gm_bar_front.jpg', 'images/products/_36/25_gm_bar_back.jpg', 2565, 2360, '0.5', '24', 194.41, 5.59, 0, 0, 20, 1, '{\r\n  \"standard\": {\r\n    \"title\": \"Standard\",\r\n    \"alias\": \"standard\",\r\n    \"id\": 14,\r\n    \"des\": \"\",\r\n    \"data\": {\r\n      \"standard\": {\r\n        \"title\": \"Standard\",\r\n        \"alias\": \"standard\",\r\n        \"id\": 16,\r\n        \"des\": \"\",\r\n        \"fk_parent_id\": 14,\r\n        \"uid\": \"5d3008d509314ea889951b5958b3eab9\",\r\n        \"images\": \"images/products/d48ca4aab7354c5cbf0db4ce7c66c6b7__25_gm_bar_front.jpg,images/products/4f3b15f2bcb642379a239c07d0172e1f__25_gm_bar.jpg,images/products/5351afeadae74a2abaa9e983678d53f3__25_gm_bar_back.jpg\",\r\n        \"order\": \"1\",\r\n        \"label\": \"\"\r\n      }\r\n    }\r\n  }\r\n}', 0, 0, '2025-03-02 11:51:16', '2025-02-09 14:47:18', 0, 22, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u064a\\u0643\\u0629 \\u0630\\u0647\\u0628 0.5\\u062c\\u0645\"}}');

-- --------------------------------------------------------

--
-- Table structure for table `gla_product_category`
--

CREATE TABLE `gla_product_category` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `des` text DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime NOT NULL,
  `kit_lang` text DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_product_category`
--

INSERT INTO `gla_product_category` (`id`, `title`, `des`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(1, 'Gold Bars', 'Gold Bars Gold Bars Gold Bars', 0, 0, '2025-02-10 12:41:51', '2025-01-13 11:48:52', '{\"ar\": {\"title\": \"\\u0633\\u0628\\u0627\\u0626\\u0643 \\u0627\\u0644\\u0630\\u0647\\u0628\"}}'),
(2, 'Gold Coins', 'Gold Coins Gold Coins Gold Coins ', 0, 0, '2025-02-10 12:42:01', '2025-01-13 11:48:52', '{\"ar\": {\"title\": \"\\u0639\\u0645\\u0644\\u0627\\u062a \\u0630\\u0647\\u0628\\u064a\\u0629\"}}'),
(3, 'Gifts', 'Gifts Gifts Gifts', 0, 0, '2025-02-10 12:42:14', '2025-01-13 11:48:52', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0647\\u062f\\u0627\\u064a\\u0627\"}}');

-- --------------------------------------------------------

--
-- Table structure for table `gla_product_types`
--

CREATE TABLE `gla_product_types` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `alias` varchar(25) NOT NULL,
  `des` text NOT NULL,
  `fk_parent_id` int(11) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime NOT NULL,
  `kit_lang` text NOT NULL,
  `fk_product_category_id` varchar(10) NOT NULL,
  `kit_order` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_product_types`
--

INSERT INTO `gla_product_types` (`id`, `title`, `alias`, `des`, `fk_parent_id`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`, `fk_product_category_id`, `kit_order`) VALUES
(1, 'Egyptian', 'egyptian', 'Egyptian', 0, 0, 0, '2025-02-16 10:05:06', '2025-01-28 10:40:09', '{\"ar\": {\"title\": \"\\u0645\\u0635\\u0631\\u064a\"}}', '2', 0),
(2, 'Siwa', 'siwa', 'Siwa', 1, 0, 0, '2025-02-16 10:05:25', '2025-01-28 10:40:55', '{\"ar\": {\"title\": \"\\u0633\\u064a\\u0648\\u0629\"}}', '', 0),
(4, 'Elizabeth', 'elizabeth', '', 15, 0, 0, '2025-02-16 10:05:54', '2025-01-28 11:19:24', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u064a\\u0632\\u0627\\u0628\\u064a\\u062b\"}}', '', 0),
(5, 'George', 'george', '', 15, 0, 0, '2025-02-16 10:06:09', '2025-01-28 11:19:58', '{\"ar\": {\"title\": \"\\u062c\\u0648\\u0631\\u062c\"}}', '', 0),
(6, 'Islamic', 'islamic', 'Islamic', 0, 0, 0, '2025-02-16 10:06:20', '2025-01-28 11:20:24', '{\"ar\": {\"title\": \"\\u0627\\u0633\\u0644\\u0627\\u0645\\u064a\"}}', '1,2', 0),
(7, 'mawled nabawy', 'mawled_nabawy', 'mawled nabawy', 6, 0, 0, '2025-02-16 10:06:31', '2025-01-28 11:21:38', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0645\\u0648\\u0644\\u062f \\u0627\\u0644\\u0646\\u0628\\u0648\\u064a \\u0627\\u0644\\u0634\\u0631\\u064a\\u0641\"}}', '', 0),
(8, 'kaaba', 'kaaba', 'kaaba', 6, 0, 0, '2025-02-16 10:06:44', '2025-01-28 11:21:55', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0643\\u0639\\u0628\\u0629\"}}', '', 0),
(9, 'Al Mermah Al Saeedi', 'al_mermah_al_saeedi', '', 1, 0, 0, '2025-02-19 13:40:15', '2025-01-28 11:23:51', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0645\\u0631\\u0645\\u0627\\u062d \\u0627\\u0644\\u0635\\u0639\\u064a\\u062f\\u064a\"}}', '', 0),
(10, 'Aswan', 'aswan', 'Aswan', 1, 0, 0, '2025-02-16 10:07:14', '2025-01-28 11:24:21', '{\"ar\": {\"title\": \"\\u0623\\u0633\\u0648\\u0627\\u0646\"}}', '', 0),
(11, 'Countryside', 'countryside', 'Countryside', 1, 0, 0, '2025-02-16 10:07:28', '2025-01-28 11:24:52', '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0631\\u064a\\u0641\"}}', '', 0),
(14, 'Standard', 'standard', '', 0, 0, 0, '2025-02-16 10:08:02', '2025-01-28 11:32:08', '{\"ar\": {\"title\": \"\\u0645\\u0639\\u064a\\u0627\\u0631\"}}', '1', 1),
(15, 'Royal', 'royal', '', 0, 0, 0, '2025-02-16 10:08:19', '2025-01-28 11:32:24', '{\"ar\": {\"title\": \"\\u0645\\u0644\\u0643\\u064a\"}}', '2', 1),
(16, 'Standard', 'standard', '', 14, 0, 0, '2025-02-16 10:08:32', '2025-01-28 11:32:08', '{\"ar\": {\"title\": \"\\u0645\\u0639\\u064a\\u0627\\u0631\"}}', '', 0),
(17, 'gdgerge', '', '', 7, 1, 0, '2025-02-26 12:01:57', '2025-02-26 12:00:45', '', '', 0);

-- --------------------------------------------------------

--
-- Table structure for table `gla_user_address`
--

CREATE TABLE `gla_user_address` (
  `id` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `first_name` varchar(25) NOT NULL,
  `last_name` varchar(25) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `city` varchar(25) NOT NULL,
  `state` varchar(25) NOT NULL,
  `address` varchar(255) DEFAULT NULL,
  `address_2` varchar(255) NOT NULL,
  `fk_user_id` int(11) NOT NULL DEFAULT 0,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `gla_user_address`
--

INSERT INTO `gla_user_address` (`id`, `title`, `first_name`, `last_name`, `email`, `phone`, `city`, `state`, `address`, `address_2`, `fk_user_id`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(1, 'Martin Philips 1', '', '', 'example@gmail.com', '8109817897 ', '', '', '701, Atulya IT Park, Khandwa Road, Indore City-2, Indore, Madhya Pradesh - 452002', '', 1, 0, 0, '2025-01-15 09:50:25', '2025-01-15 09:50:25'),
(2, 'Martin Philips 2', '', '', 'example@gmail.com', '8109817897 ', '', '', '701, Atulya IT Park, Khandwa Road, Indore City-2, Indore, Madhya Pradesh - 452002', '', 1, 0, 0, '2025-01-15 09:50:25', '2025-01-15 09:50:25'),
(3, 'Martin Philips 3', '', '', 'example@gmail.com', '8109817897 ', '', '', '701, Atulya IT Park, Khandwa Road, Indore City-2, Indore, Madhya Pradesh - 452002', '', 1, 0, 0, '2025-01-15 09:50:25', '2025-01-15 09:50:25'),
(4, 'Martin Philips 4', '', '', 'example@gmail.com', '8109817897 ', '', '', '701, Atulya IT Park, Khandwa Road, Indore City-2, Indore, Madhya Pradesh - 452002', '', 1, 0, 0, '2025-01-15 09:50:25', '2025-01-15 09:50:25'),
(14, 'Hossam Ahmed', '', '', 'hissam@gmail.com', '1312312', '', '', '3123', '32112312', 1, 0, 0, '0000-00-00 00:00:00', '2025-01-20 11:19:23'),
(13, 'dasd dasd', '', '', 'das', 'dasd', '', '', 'dasd', '', 1, 0, 0, '0000-00-00 00:00:00', '2025-01-16 15:16:33'),
(12, 'Store', '', '', 'hesham@e-scapes.me', '01123881630', '', '', 'Cairo Dokki ElGalla store', 'sadasdsadas', 1, 0, 0, '0000-00-00 00:00:00', '2025-01-16 14:09:49');

-- --------------------------------------------------------

--
-- Table structure for table `kit_content`
--

CREATE TABLE `kit_content` (
  `id` int(11) NOT NULL,
  `title` text DEFAULT NULL,
  `content` text DEFAULT NULL,
  `kit_deleted` tinyint(4) DEFAULT 0,
  `kit_disabled` tinyint(4) DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `kit_lang` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_content`
--

INSERT INTO `kit_content` (`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(208, 'body', '<div class=\"ins-flex ins-card ins-padding-xl \">\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n<br/>\r\n<br/>\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n\r\n<br/>\r\n<br/>\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n<br/>\r\n<br/>\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n\r\n\r\n\r\n</div>', 0, 0, '2024-11-22 12:58:05', '2022-05-25 16:49:24', ''),
(209, 'copyright', '<div class=\"ins-space-l\">\r\n</div>\r\n<div class=\"ins-col-12 ins-flex\">\r\n<div  class=\"\"><img style=\'width:150px\' src=\"/ins_web/ins_uploads/style/v.png\"></div>\r\n<div class=\" ins-col-grow\"></div>\r\n\r\n<div style=\'font-size:14px \'>© 2024 El Galla Gold All Rights Reserved  |  Shipping Policy  |  Refund Policy  |  Privacy Policy  |  Terms of Service </div>\r\n</div>', 0, 0, '2025-01-07 13:50:29', '2022-05-25 16:49:24', ''),
(211, 'slide show', '<div style=\'height: 340px;\' class=\"ins-col-12 img-bg-air  ins-flex-center\">\r\n   <div style=\"position: relative;\" class=\" serch_cont ins_mod_search  ins-container\">\r\n<h2 class=\'ins-strong ins-primary-color\'>CG Marketplace by the World\'s Best 3D Artists </h2>\r\n<h4 class=\'ins-strong\'>Find the exact right 3D content for your needs, including AR/VR, gaming, advertising, entertainment and 3D printing\r\n\r\n</h4 >\r\n\r\n    <div class=\" ui_row  ins-col-12   ui_parent ui_parent ui_search \">\r\n        <div>\r\n            <div class=\"ui_value ins-form-input  \">\r\n                <i class=\"fas fa-search\" style=\"margin: 7px;\"></i>\r\n                <input class=\"   ins_ui_input ins_ui_input  ins-form-input     search\" placeholder=\"SearchProducts\" value=\"\" name=\"search\">\r\n            </div>\r\n            <button class=\"search ins_search_btn ins-primary ins-button\" style=\"position: absolute;right: 10px;top: 8px;width: 120px;\" name=\"button\"> search</button>\r\n        </div>\r\n    </div>\r\n</div>\r\n\r\n\r\n</div>\r\n<div style=\'height: 60px;\' class=\"ins-col-12  ins-flex\">\r\n    <div class=\"ins-container sub-menu ins-flex-space-between\">\r\n        <ul class=\"ins-col-12 ins-flex-center ins-title-m\">\r\n            <li class=\"ins-padding-m ins-strong \"><a href=\"/home/\" title=\"Trending\"><span>Blender Tutorials</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/home/\" title=\"Trending\"><span>houdini Tutorials</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/home/\" title=\"Trending\"><span>Trending</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/about/\" data-title=\"collections\"><span>collections</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/Products/\" data-title=\"Products\"><span>3d Moduels</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/Products/\" data-title=\"Products\"><span>Basemeshes</span></a></li>\r\n        </ul>\r\n    </div>\r\n</div>', 0, 0, '2023-04-13 00:36:26', '2023-04-13 00:01:11', ''),
(293, 'footer', '<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. \r\n</div>\r\n\r\n', 0, 0, '2024-11-22 13:45:04', '2024-11-22 13:41:17', ''),
(294, 'Visit us', '<div class=\"visit_data\" style=\'margin-right:40px\'>\r\n\r\n    <div class=\'ins-title-m\'>Visit us</div>\r\n    <p>\r\n        <img src=\"/ins_web/ins_uploads/style/location.svg\" style=\"width: 20px; height: 20px; vertical-align: middle;\">\r\n        <a href=\"https://maps.app.goo.gl/Tot6YZVhhsQqeDTL7\" target=\"_blank\"> El Galla Gold, 60 El Moez Le Din Allah St., El Gamalia, Cairo </a>\r\n    </p>\r\n\r\n    <p>\r\n        <img src=\"/ins_web/ins_uploads/style/clock.svg\" style=\"width: 20px; height: 20px; vertical-align: middle;\">\r\n        <span> Opening hours: 11:00 AM - 8:30 PM </span>\r\n    </p>\r\n\r\n    <div class=\'ins-space\'></div>\r\n\r\n    <p>\r\n        <img src=\"/ins_web/ins_uploads/style/location.svg\" style=\"width: 20px; height: 20px; vertical-align: middle;\">\r\n        <a href=\"https://maps.app.goo.gl/kqrvtN3TSfZHgkZQA\" target=\"_blank\"> El Galla Gold, Street 88, Palm Hills, 6th of October, Giza </a>\r\n    </p>\r\n\r\n    <p>\r\n        <img src=\"/ins_web/ins_uploads/style/clock.svg\" style=\"width: 20px; height: 20px; vertical-align: middle;\">\r\n        <span> Opening hours: 11:00 AM - 8:30 PM </span>\r\n    </p>\r\n\r\n    <p>\r\n        <img src=\"/ins_web/ins_uploads/style/phone.svg\" style=\"width: 20px; height: 20px; vertical-align: middle;\">\r\n        <a href=\"tel:17153\"> 17153 </a>\r\n\r\n    </p>\r\n    <p>\r\n        <img src=\"/ins_web/ins_uploads/style/whatsapp.svg\" style=\"width: 20px; height: 20px; vertical-align: middle;\">\r\n        <a href=\"tel:01009539999\"> 01009539999</a>\r\n    </p>\r\n\r\n    <p>\r\n        <img src=\"/ins_web/ins_uploads/style/email.svg\" style=\"width: 20px; height: 20px; vertical-align: middle;\">\r\n        <a href=\"mailto:info@elgallagold.com\"> info@elgallagold.com </a>\r\n    </p>\r\n\r\n</div>', 0, 0, '2025-03-03 10:36:49', '2024-12-02 11:04:27', '{\"ar\": {\"content\": \"\\r\\n<div class=\\\"visit_data\\\" style=\'margin-right:40px\'>\\r\\n\\r\\n    <div class=\'ins-title-m\'>\\u0632\\u0648\\u0631\\u0646\\u0627</div>\\r\\n    <p>\\r\\n        <img src=\\\"/ins_web/ins_uploads/style/location.svg\\\" style=\\\"width: 20px; height: 20px; vertical-align: middle;\\\">\\r\\n        <a href=\\\"https://maps.app.goo.gl/Tot6YZVhhsQqeDTL7\\\" target=\\\"_blank\\\"> \\u0627\\u0644\\u062c\\u0627\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\u060c 60 \\u0634\\u0627\\u0631\\u0639 \\u0627\\u0644\\u0645\\u0639\\u0632 \\u0644\\u062f\\u064a\\u0646 \\u0627\\u0644\\u0644\\u0647\\u060c \\u0627\\u0644\\u062c\\u0645\\u0627\\u0644\\u064a\\u0629\\u060c \\u0627\\u0644\\u0642\\u0627\\u0647\\u0631\\u0629 </a>\\r\\n\\r\\n    </p>\\r\\n\\r\\n    <p>\\r\\n        <img src=\\\"/ins_web/ins_uploads/style/clock.svg\\\" style=\\\"width: 20px; height: 20px; vertical-align: middle;\\\">\\r\\n        <span> \\u0633\\u0627\\u0639\\u0627\\u062a \\u0627\\u0644\\u0639\\u0645\\u0644: 11:00 \\u0635\\u0628\\u0627\\u062d\\u064b\\u0627 - 8:30 \\u0645\\u0633\\u0627\\u0621\\u064b </span>\\r\\n    </p>\\r\\n\\r\\n    <div class=\'ins-space\'></div>\\r\\n\\r\\n    <p>\\r\\n        <img src=\\\"/ins_web/ins_uploads/style/location.svg\\\" style=\\\"width: 20px; height: 20px; vertical-align: middle;\\\">\\r\\n        <a href=\\\"https://maps.app.goo.gl/kqrvtN3TSfZHgkZQA\\\" target=\\\"_blank\\\"> \\u0627\\u0644\\u062c\\u0627\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\u060c \\u0634\\u0627\\u0631\\u0639 88\\u060c \\u0628\\u0644\\u0645 \\u0647\\u064a\\u0644\\u0632\\u060c \\u0627\\u0644\\u0633\\u0627\\u062f\\u0633 \\u0645\\u0646 \\u0623\\u0643\\u062a\\u0648\\u0628\\u0631\\u060c \\u0627\\u0644\\u062c\\u064a\\u0632\\u0629 </a>\\r\\n\\r\\n    </p>\\r\\n\\r\\n    <p>\\r\\n        <img src=\\\"/ins_web/ins_uploads/style/clock.svg\\\" style=\\\"width: 20px; height: 20px; vertical-align: middle;\\\">\\r\\n        <span> \\u0633\\u0627\\u0639\\u0627\\u062a \\u0627\\u0644\\u0639\\u0645\\u0644: 11:00 \\u0635\\u0628\\u0627\\u062d\\u064b\\u0627 - 8:30 \\u0645\\u0633\\u0627\\u0621\\u064b </span>\\r\\n    </p>\\r\\n\\r\\n    <p>\\r\\n        <img src=\\\"/ins_web/ins_uploads/style/phone.svg\\\" style=\\\"width: 20px; height: 20px; vertical-align: middle;\\\">\\r\\n        <a href=\\\"tel:17153\\\"> 17153 </a>\\r\\n\\r\\n    </p>\\r\\n    <p>\\r\\n        <img src=\\\"/ins_web/ins_uploads/style/whatsapp.svg\\\" style=\\\"width: 20px; height: 20px; vertical-align: middle;\\\">\\r\\n        <a href=\\\"tel:01009539999\\\"> 01009539999</a>\\r\\n    </p>\\r\\n\\r\\n    <p>\\r\\n        <img src=\\\"/ins_web/ins_uploads/style/email.svg\\\" style=\\\"width: 20px; height: 20px; vertical-align: middle;\\\">\\r\\n        <a href=\\\"mailto:info@elgallagold.com\\\"> info@elgallagold.com </a>\\r\\n    </p>\\r\\n\\r\\n</div>\"}}'),
(295, 'Resources', '<div class=\'\'>\r\n    <div class=\'ins-title-s ins-col-12\'>RESOURCES</div>\r\n    <div class=\'ins-space\'></div>\r\n    <li><a href=\'/product/do/filter/fk_product_category_id=1\'  class=\'ins-col-12\'>Gold Bars</a></li>\r\n    <li><a href=\'/product/do/filter/fk_product_category_id=2&types_data=royal\'  class=\'ins-col-12\'>Gold coins</a></li>\r\n    <li><a href=\'/product/do/filter/fk_product_category_id=3\'  class=\'ins-col-12\'>Gold Gifts</a></li>\r\n    <div class=\'ins-space\'></div>\r\n    \r\n    <div class=\'ins-title-s ins-col-12\'>FOLLOW US</div>\r\n    <div class=\'ins-space-s\'></div>\r\n    <div><i style=\"padding:4px\" class=\'lni ins-font-xl lni-facebook\'></i><i style=\"padding:4px\"  class=\'lni ins-font-xl lni-instagram\'></i> </div>\r\n    </div>', 0, 0, '2025-03-03 11:17:17', '2024-12-02 11:19:18', '{\"ar\": {\"content\": \"\\r\\n<div class=\'\'>\\r\\n    <div class=\'ins-title-s ins-col-12\'>\\u0627\\u0644\\u0645\\u0648\\u0627\\u0631\\u062f</div>\\r\\n    <div class=\'ins-space\'></div>\\r\\n    <li><a href=\'/product/do/filter/fk_product_category_id=1\' class=\'ins-col-12\'>\\u0633\\u0628\\u0627\\u0626\\u0643 \\u0627\\u0644\\u0630\\u0647\\u0628</a></li>\\r\\n    <li><a href=\'/product/do/filter/fk_product_category_id=2&types_data=royal\'  class=\'ins-col-12\'>\\u0639\\u0645\\u0644\\u0627\\u062a \\u0630\\u0647\\u0628\\u064a\\u0629</a></li>\\r\\n    <li><a href=\'/product/do/filter/fk_product_category_id=3\' class=\'ins-col-12\'>\\u0647\\u062f\\u0627\\u064a\\u0627 \\u0630\\u0647\\u0628\\u064a\\u0629</a></li>\\r\\n    <div class=\'ins-space\'></div>\\r\\n\\r\\n    <div class=\'ins-title-s ins-col-12\'>\\u062a\\u0627\\u0628\\u0639\\u0646\\u0627</div>\\r\\n    <div class=\'ins-space-s\'></div>\\r\\n    <div>\\r\\n        <i style=\\\"padding:4px\\\" class=\'lni ins-font-xl lni-facebook\'></i>\\r\\n        <i style=\\\"padding:4px\\\" class=\'lni ins-font-xl lni-instagram\'></i>\\r\\n    </div>\\r\\n</div>\\r\\n\"}}'),
(296, 'Discover', '<div class=\'\'>\r\n    <div class=\'ins-title-s ins-col-12\'>DISCOVER</div>\r\n    <div class=\'ins-space\'></div>\r\n    <ul>\r\n        <li><a href=\"/about_us/\" class=\'ins-col-12\'>About us</a></li>\r\n        <li><a href=\"/Blogs/\" class=\'ins-col-12\'>Blog</a></li>\r\n        <li><a href=\"/faq.html\" class=\'ins-col-12\'>FAQ</a></li>\r\n        <li><a href=\"/contact_us/\" class=\'ins-col-12\'>Contact Us</a></li>\r\n    </ul>\r\n</div>\r\n', 0, 0, '2025-03-03 10:37:57', '2024-12-04 09:54:34', '{\"ar\": {\"content\": \"<div class=\'\'>\\r\\n    <div class=\'ins-title-s ins-col-12\'>\\u0627\\u0643\\u062a\\u0634\\u0641</div>\\r\\n    <div class=\'ins-space\'></div>\\r\\n    <ul>\\r\\n        <li><a href=\\\"/about_us/\\\" class=\'ins-col-12\'>\\u0645\\u0646 \\u0646\\u062d\\u0646</a></li>\\r\\n        <li><a href=\\\"/Blogs/\\\" class=\'ins-col-12\'>\\u0627\\u0644\\u0645\\u062f\\u0648\\u0646\\u0629</a></li>\\r\\n        <li><a href=\\\"/faq.html\\\" class=\'ins-col-12\'>\\u0627\\u0644\\u0623\\u0633\\u0626\\u0644\\u0629 \\u0627\\u0644\\u0634\\u0627\\u0626\\u0639\\u0629</a></li>\\r\\n        <li><a href=\\\"/contact_us/\\\" class=\'ins-col-12\'>\\u0627\\u062a\\u0635\\u0644 \\u0628\\u0646\\u0627</a></li>\\r\\n    </ul>\\r\\n</div>\"}}'),
(297, 'address content', 'dsfsd asdsa asdasd', 0, 0, NULL, '2024-12-09 11:15:12', ''),
(298, 'ui', 'dfsd', 0, 0, '2025-01-07 12:06:19', '2024-12-09 11:15:20', ''),
(299, 'footer logo', '\n    <div style=\'margin-right:40px\'>\n        <div style=\"width:120px;height:120px\" class=\"gla-elogo-white\"></div>\n        <div class=\"ins-space\"></div>\n        <div>\n        <div class=\'ins-title-m\'>Stay in Touch</div>\n        <div class=\"ins-space-s\"></div>\n        <div   class=\"\">Subscribe to get special offers, free giveaways, and once-in-a-lifetime deals.</div>\n        <div class=\"ins-space\"></div>\n        </div>\n        </div>', 0, 0, '2025-02-05 13:02:10', '2025-01-07 12:06:55', '{\"ar\": {\"content\": \"<div style=\'margin-right:40px\'>\\r\\n    <div style=\\\"width:120px;height:120px\\\" class=\\\"gla-elogo-white\\\"></div>\\r\\n    <div class=\\\"ins-space\\\"></div>\\r\\n    <div>\\r\\n        <div class=\'ins-title-m\'>\\u0627\\u0628\\u0642\\u0649 \\u0639\\u0644\\u0649 \\u062a\\u0648\\u0627\\u0635\\u0644</div>\\r\\n        <div class=\\\"ins-space-s\\\"></div>\\r\\n        <div class=\\\"\\\">\\u0627\\u0634\\u062a\\u0631\\u0643 \\u0644\\u0644\\u062d\\u0635\\u0648\\u0644 \\u0639\\u0644\\u0649 \\u0639\\u0631\\u0648\\u0636 \\u062e\\u0627\\u0635\\u0629\\u060c \\u0647\\u062f\\u0627\\u064a\\u0627 \\u0645\\u062c\\u0627\\u0646\\u064a\\u0629\\u060c \\u0648\\u0639\\u0631\\u0648\\u0636 \\u0644\\u0627 \\u062a\\u064f\\u062a\\u0627\\u062d \\u0625\\u0644\\u0627 \\u0645\\u0631\\u0629 \\u0648\\u0627\\u062d\\u062f\\u0629 \\u0641\\u064a \\u0627\\u0644\\u0639\\u0645\\u0631.</div>\\r\\n        <div class=\\\"ins-space\\\"></div>\\r\\n    </div>\\r\\n</div>\"}}'),
(300, 'Quality Assurance', '<div   class=\' ins-primary-d ins-col-12 gla-primary-br \'>\r\n<div class=\' gla-container ins-flex \'>\r\n<div class=\'ins-col-4 ins-title-s ins-flex-center\'> <img src=\'\\ins_web\\ins_uploads\\style\\quality.svg\'></img> Quality Assurance</div>\r\n<div class=\'ins-col-4   ins-border ins-border-h ins-flex-center ins-title-s\'><img src=\'\\ins_web\\ins_uploads\\style\\secure.svg\'></img> Secure Transactions</div>\r\n<div class=\'ins-col-4 ins-flex-center ins-title-s\'><img src=\'\\ins_web\\ins_uploads\\style\\money_w.svg\'></img> Transparent Pricing</div>\r\n\r\n</div>\r\n</div>', 0, 0, '2025-02-16 09:02:40', '2025-01-07 14:23:52', '{\"ar\": {\"content\": \"<div class=\'ins-primary-d ins-col-12 gla-primary-br\' dir=\\\"rtl\\\">\\r\\n    <div class=\'gla-container ins-flex\'>\\r\\n        <div class=\'ins-col-4 ins-title-s ins-flex-center\'>\\r\\n            <img src=\'/ins_web/ins_uploads/style/quality.svg\'> \\u0636\\u0645\\u0627\\u0646 \\u0627\\u0644\\u062c\\u0648\\u062f\\u0629\\r\\n        </div>\\r\\n        <div class=\'ins-col-4 ins-border ins-border-h ins-flex-center ins-title-s\'>\\r\\n            <img src=\'/ins_web/ins_uploads/style/secure.svg\'> \\u0645\\u0639\\u0627\\u0645\\u0644\\u0627\\u062a \\u0622\\u0645\\u0646\\u0629\\r\\n        </div>\\r\\n        <div class=\'ins-col-4 ins-flex-center ins-title-s\'>\\r\\n            <img src=\'/ins_web/ins_uploads/style/money_w.svg\'> \\u062a\\u0633\\u0639\\u064a\\u0631 \\u0634\\u0641\\u0627\\u0641\\r\\n        </div>\\r\\n    </div>\\r\\n</div>\\r\\n\"}}'),
(301, 'See how much  gold you can own!', '<div class=\'ins-secondary ins-col-12\'>\r\n     <div class=\'gla-container ins-padding-2xl ins-flex-space-between\'>\r\n         <div class=\'ins-title-xl ins-strong-m\' style=\'line-height: 50px;\'>\r\n             SEE HOW MUCH <br/>\r\n             GOLD YOU CAN OWN!\r\n         </div>\r\n         <div class=\'ins-col-6 ins-flex-center\'>\r\n             <div class=\'ins-flex ins-border ins-radius-m ins-padding-m\' \r\n                 style=\'width: 720px; background-color: white;\' start=\'true\'>\r\n                 <div class=\'ins-border-end ins-padding-m ins-padding-h ins-title-20 ins-grey-color\' \r\n                     style=\'height: 24px; line-height: 24px;\'>\r\n                     EGP\r\n                 </div>\r\n                 <div class=\'ins-form-item ins-flex ins-form-number-cont ins-col-grow\' start=\'true\'>\r\n                     <div class=\'ins-form-value\' start=\'true\'>\r\n                         <input type=\'text\' class=\'-cal-update-nput ins-input-none ins-form-input\' \r\n                             placeholder=\'Enter your amount\' style=\'color: black !important\' pclass=\'ins-col-grow\'>\r\n                     </div>\r\n                 </div>\r\n                 <div class=\'ins-button-s -cal-update-btn ins-gold-d ins-flex-center\' style=\'height: 46px;\'>\r\n                     CALCULATOR <i class=\'lni ins-white-color lni-arrow-right\'></i>\r\n                 </div>\r\n             </div>\r\n         </div>\r\n     </div>\r\n </div>\r\n ', 0, 0, '2025-03-02 09:05:32', '2025-01-07 14:24:01', '{\"ar\": {\"content\": \"\\r\\n<div class=\' ins-secondary ins-col-12 \'>\\r\\n    <div class=\' gla-container ins-padding-2xl ins-flex-space-between \'>\\r\\n\\r\\n        <div style=\\\"line-height:50px\\\" class=\'ins-title-xl ins-strong-m \'>\\r\\n            \\u0623\\u062d\\u0635\\u0644 \\u0639\\u0644\\u0649 \\u0623\\u0641\\u0636\\u0644 <br/> \\u062e\\u0637\\u0629 \\u0627\\u062f\\u062e\\u0627\\u0631\\u064a\\u0629 \\u0644\\u0623\\u0645\\u0648\\u0627\\u0644\\u0643</div>\\r\\n\\r\\n\\r\\n        <div class=\'ins-col-6 ins-flex-center\'>\\r\\n            <div class=\'ins-flex ins-border ins-radius-m ins-padding-m\' style=\'width: 720px; background-color: white;\' start=\'true\'>\\r\\n                <div class=\'ins-border-end ins-padding-m ins-padding-h ins-title-20 ins-grey-color\' style=\'height: 24px; line-height: 24px;\'>\\r\\n                    \\u062c\\u0646\\u064a\\u0647\\r\\n                </div>\\r\\n                <div class=\'ins-form-item ins-flex ins-form-number-cont ins-col-grow\' start=\'true\'>\\r\\n                    <div class=\'ins-form-value\' start=\'true\'>\\r\\n                        <input type=\'text\' class=\'-cal-update-nput ins-input-none ins-form-input\' placeholder=\'\\u0623\\u062f\\u062e\\u0644 \\u0627\\u0644\\u0645\\u0628\\u0644\\u063a \\u0627\\u0644\\u062e\\u0627\\u0635 \\u0628\\u0643\' style=\'color: black !important\' pclass=\'ins-col-grow\'>\\r\\n                    </div>\\r\\n                </div>\\r\\n                <div class=\'ins-button-s -cal-update-btn ins-gold-d ins-flex-center\' style=\'height: 46px;\'>\\r\\n                    \\u0627\\u062d\\u0633\\u0628 <i class=\'lni ins-white-color lni-arrow-left\'></i>\\r\\n                </div>\\r\\n            </div>\\r\\n        </div>\\r\\n\\r\\n    </div>\\r\\n\\r\\n</div>\"}}'),
(302, 'Our Partners', '<div class=\' ins-col-12  \'>\r\n<div class=\"ins-space-xl\"></div>\r\n\r\n<div  class=\' ins-gap-o  ins-padding-2xl  gla-container ins-flex-space-between\'>\r\n<div style=\"    margin-right: 16px;\" class=\"ins-title-m  ins-text-upper ins-strong-m ins-grey-color\">Our Partners</div>\r\n<div  class=\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\"><img style=\'height: 100%;\' src=\"/ins_web/ins_uploads/images/20250209185545__Copy_of_Dahab_Masr_Signature_-_lookup_2.png\"></div>\r\n<div  class=\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\"><img style=\'height: 100%;\' src=\"/ins_web/ins_uploads/images/20250209185636__images.png\"></div>\r\n<div  class=\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\"><img style=\'height: 100%;\' src=\"/ins_web/ins_uploads/images/20250209191250__elgallajewel.jpg\"></div>\r\n<div  class=\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\"><img style=\'height: 100%;\' src=\"/ins_web/ins_uploads/images/20250209191614__El_Kady_K_logo-1.png\"></div>\r\n<div  class=\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\"><img style=\'height: 100%;\' src=\"/ins_web/ins_uploads/images/20250209191705__gold_souq_logo_final_241112_140149-1.png\"></div>\r\n<div  class=\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\"><img style=\'height: 100%;\' src=\"/ins_web/ins_uploads/images/20250209191832__Logo_Alzahraa-1.png\"></div>\r\n\r\n\r\n\r\n\r\n\r\n\r\n</div><div style=\"border-bottom:1px solid var(--primary)\" class=\"ins-space-2xl\"></div>\r\n\r\n\r\n</div>', 0, 0, '2025-02-16 16:56:54', '2025-01-07 14:24:09', '{\"ar\": {\"content\": \"<div class=\' ins-col-12  \'>\\r\\n<div class=\\\"ins-space-xl\\\"></div>\\r\\n\\r\\n<div  class=\' ins-gap-o  ins-padding-2xl  gla-container ins-flex-space-between\'>\\r\\n<div style=\\\"    margin-right: 16px;\\\" class=\\\"ins-title-m  ins-text-upper ins-strong-m ins-grey-color\\\">\\u0634\\u0631\\u0643\\u0627\\u0624\\u0646\\u0627</div>\\r\\n<div  class=\\\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\\\"><img style=\'height: 100%;\' src=\\\"/ins_web/ins_uploads/images/20250209185545__Copy_of_Dahab_Masr_Signature_-_lookup_2.png\\\"></div>\\r\\n<div  class=\\\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\\\"><img style=\'height: 100%;\' src=\\\"/ins_web/ins_uploads/images/20250209185636__images.png\\\"></div>\\r\\n<div  class=\\\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\\\"><img style=\'height: 100%;\' src=\\\"/ins_web/ins_uploads/images/20250209191250__elgallajewel.jpg\\\"></div>\\r\\n<div  class=\\\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\\\"><img style=\'height: 100%;\' src=\\\"/ins_web/ins_uploads/images/20250209191614__El_Kady_K_logo-1.png\\\"></div>\\r\\n<div  class=\\\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\\\"><img style=\'height: 100%;\' src=\\\"/ins_web/ins_uploads/images/20250209191705__gold_souq_logo_final_241112_140149-1.png\\\"></div>\\r\\n<div  class=\\\"gla-icon-card gla-shadow-s  ins-radius-m ins-white\\\"><img style=\'height: 100%;\' src=\\\"/ins_web/ins_uploads/images/20250209191832__Logo_Alzahraa-1.png\\\"></div>\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n</div><div style=\\\"border-bottom:1px solid var(--primary)\\\" class=\\\"ins-space-2xl\\\"></div>\\r\\n\\r\\n\\r\\n</div>\"}}'),
(303, 'none', '', 0, 0, NULL, '2025-01-09 13:21:12', '');
INSERT INTO `kit_content` (`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(304, 'about', '<!--Header-->\r\n<div class=\"ins-col-12  ins-border ins-border-bottom\" style=\"background:white;height:124px;position: relative;\">\r\n    <div class=\"gla-container ins-flex ins-padding-2xl\">\r\n        <div class=\"ins-col-12 ins-flex ins-text-upper\">\r\n            <a href=\"/\" class=\" ins-font-s	ins-grey-d-color ins-strong-m\">Home /</a>\r\n            <div class=\" ins-font-s	ins-grey-color ins-strong-m\">About Us</div>\r\n        </div>\r\n        <div class=\"ins-col-12 ins-title ins-strong-m ins-text-upper ins-grey-d-color \">\r\n            About Us\r\n        </div>\r\n    </div>\r\n</div>\r\n\r\n\r\n\r\n\r\n<!--Main Container-->\r\n<div class=\"ins-col-12 \" style=\"    margin-top: -8px;\">\r\n    <div start=\"true\" class=\"ins-flex  ins-padding-2xl gla-container \" style=\"padding-bottom:12px\">\r\n        <div class=\"ins-space-l\"></div>\r\n\r\n\r\n        <!--First Conent-->\r\n        <div start=\"true\" class=\"ins-flex  ins-col-12\">\r\n            <div class=\"ins-title-xl ins-grey-d-color ins-strong-m\" style=\"line-height:50px\">A Legacy of Gold – Three <br> The Story of El-Galla Gold </div>\r\n            <div class=\"ins-col-grow \"></div>\r\n            <div class=\"ins-space-l\"></div>\r\n            <div start=\"true\" class=\"ins-flex-center ins-grey-color \" style=\"width:500px;height:406px\">\r\n                <div class=\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\">The Beginning</div>\r\n                <div class=\"ins-space-s\"></div>\r\n                <div class=\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\" style=\"line-height:60px\">1950s</div>\r\n                <div class=\"ins-space-s\"></div>\r\n                <div class=\" ins-col-12 ins-strong-m \" style=\"line-height:24px;font-size:20px\">El Galla Gold was established in 1950, our family-owned business has been passed down through generations, each adding to our rich legacy with their unique knowledge and experience, carrying forward the vision that originally started with Hassan El Galla.</div>\r\n            </div>\r\n            <div class=\"ins-col-grow\"></div>\r\n            <div start=\"true\" class=\"ins-flex gla-alogo-primary-l\" style=\"    background-size: 166px auto;background-position: 58% top;\">\r\n                <div start=\"true\" class=\"ins-flex-start\"style=\"width:424px;height:273px;margin:0 10px\"><img src=\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/1950s.png\"></div>\r\n            </div>\r\n            El-Galla Gold, a story full of history, heritage, and passion, has been known in the Egyptian gold industry for over seven decades. It is a symbol of quality, trust, and tradition. Established in 1950, our family-owned business has been passed down through generations, each adding to our rich legacy with their unique knowledge and experience, carrying forward the vision that originally started with Hassan El Galla.\r\n            At El Galla Gold, our journey began with our father and founder, Hassan El Galla. The name \"El Galla\" means \"polish\" a key part of the process of creating gold products, it reflects the humble beginnings of the company, as Hassan started his journey by polishing gold before expanding into the thriving business it is today. Much like the gold he worked with, he was always known for his honesty and trustworthiness. The experiences and lessons he learned throughout his life shaped his dedication to quality which always ensured customer satisfaction. His morals and principles have been the foundation and driving force behind our success. They continue to guide us as we move forward, preserving a legacy that spans generations. \r\n        </div>\r\n        <div class=\"ins-space-3xl\"></div>\r\n\r\n\r\n        <div class=\"ins-line ins-col-12\"></div>\r\n\r\n        <div class=\"ins-space-3xl\"></div>\r\n\r\n        <!--Second Conent-->\r\n        <div start=\"true\" class=\"ins-flex  ins-col-12  ins-col-12\">\r\n            <div class=\"ins-col-6\"></div>\r\n            <div class=\"ins-space-l\"></div>\r\n\r\n            <div start=\"true\" class=\"ins-flex gla-alogo-primary-l ins-col-6\" style=\"    background-size: 166px auto;background-position: 42% top;\">\r\n                <div start=\"true\" class=\"ins-flex-end    \" style=\"width:450px;height:283px\"><img src=\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/1980s.png\"></div>\r\n            </div>\r\n            <div start=\"true\" class=\"ins-flex-center ins-grey-color ins-col-6\" style=\"    height: 406px;\">\r\n                <div start=\"true\" class=\"ins-flex-center ins-grey-color \" style=\"width:500px;height:406px\">\r\n                    <div class=\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\">The Beginning</div>\r\n                    <div class=\"ins-space-s\"></div>\r\n                    <div class=\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\" style=\"line-height:60px\">1980s</div>\r\n                    <div class=\"ins-space-s\"></div>\r\n                    <div class=\" ins-col-12 ins-strong-m \" style=\"line-height:24px;font-size:20px\">The second generation, led by Ahmed Hassan El-Galla, expanded our operations and embraced modern business practices. He was a mentor and leader to many, and his tenure marked a significant growth phase as we expanded our product range and strengthened our market presence.\r\n                    </div>\r\n                </div>\r\n            </div>\r\n            <div class=\"ins-col-grow\"></div>\r\n\r\n            As the company evolved, the second generation, led by Ahmed Hassan El-Galla, expanded our operations and embraced modern business practices, being the first in the industry to manufacture gold coins and bars. He was a mentor and leader to many, and his tenure marked a significant growth phase as we expanded our product range and strengthened our market presence.\r\n        </div>\r\n        <div class=\"ins-space-3xl\"></div>\r\n\r\n\r\n        <div class=\"ins-line ins-col-12\"></div>\r\n\r\n        <div class=\"ins-space-3xl\"></div>\r\n\r\n         <!--Third Conent-->\r\n         <div start=\"true\" class=\"ins-flex  ins-col-12\">\r\n            <div class=\"ins-col-grow \"></div>\r\n            <div class=\"ins-space-l\"></div>\r\n            <div start=\"true\" class=\"ins-flex-center ins-grey-color \" style=\"width:500px;height:406px\">\r\n                <div class=\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\">The Beginning</div>\r\n                <div class=\"ins-space-s\"></div>\r\n                <div class=\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\" style=\"line-height:60px\">2020s</div>\r\n                <div class=\"ins-space-s\"></div>\r\n                <div class=\" ins-col-12 ins-strong-m \" style=\"line-height:24px;font-size:20px\">Today, the third generation, under the leadership of our CEO Osama Ahmed Hassan El-Galla, continues to build upon the strong foundation laid by our predecessors. He introduced new ways of using technology to simplify buying and selling gold.\r\n                </div>\r\n            </div>\r\n            <div class=\"ins-col-grow\"></div>\r\n            <div start=\"true\" class=\"ins-flex gla-alogo-primary-l\" style=\"    background-size: 166px auto;background-position: 58% top;\">\r\n                <div start=\"true\" class=\"ins-flex-start\" style=\"width:424px;height:273px;margin:0 10px\"><img src=\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/2020.png\"></div>\r\n            </div>\r\n            Today, the third generation, under the leadership of our CEO Osama Ahmed Hassan El-Galla, continues to build upon the strong foundation laid by our predecessors. He introduced new ways of using technology to simplify buying and selling gold through our website and mobile application. Now, customers can view different products and make orders, all from the comfort of their homes. We actively engage with our customers across social media platforms such as Facebook, Instagram, YouTube, TikTok, and LinkedIn. \r\n\r\n        </div>\r\n        <div class=\"ins-space-3xl\"></div>\r\n\r\n\r\n        <div class=\"ins-line ins-col-12\"></div>\r\n\r\n        <div class=\"ins-space-3xl\"></div>\r\n        \r\n       \r\n        <!--Four Conent-->\r\n        <div start=\"true\" class=\"ins-flex  ins-col-12  ins-col-12\">\r\n            <div class=\"ins-col-6\"></div>\r\n            <div class=\"ins-space-l\"></div>\r\n\r\n            <div start=\"true\" class=\"ins-flex gla-alogo-primary-l ins-col-6\" style=\"    background-size: 166px auto;background-position: 42% top;\">\r\n                <div start=\"true\" class=\"ins-flex-end    \" style=\"width:450px;height:283px\"><img src=\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/now.png\"></div>\r\n            </div>\r\n            <div start=\"true\" class=\"ins-flex-center ins-grey-color ins-col-6\" style=\"    height: 406px;\">\r\n                <div start=\"true\" class=\"ins-flex-center ins-grey-color \" style=\"width:500px;height:406px\">\r\n                    <div class=\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\">The Beginning</div>\r\n                    <div class=\"ins-space-s\"></div>\r\n                    <div class=\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\" style=\"line-height:60px\">Present Day</div>\r\n                    <div class=\"ins-space-s\"></div>\r\n                    <div class=\" ins-col-12 ins-strong-m \" style=\"line-height:24px;font-size:20px\">As we look to the future, we remain committed to our heritage, morals, and passion. The name of El-Galla Gold will remain, as we have always promised, a symbol of trust.</div>\r\n                </div>\r\n            </div>\r\n            <div class=\"ins-col-grow\"></div>\r\n\r\n            We will continue to innovate, adapt to changing market trends, and provide our customers with the highest quality products and services. As life continues to change, we aim to help you adapt and secure your future. Gold is a tangible asset that not only retains its value through economic changes but also appreciates over time, making it a reliable choice for securing your savings. At the core of everything we do is the idea of family, whether it’s the Galla family, the people who have poured their hearts into this journey, or the extended families, those who buy our products with the same vision of having something valuable and sustainable for the future. \r\n            Our people are the heart of El-Galla Gold, as is our deep care and pride in every piece we create. We offer a diverse range of gold products, including gold coins ranging from 1/8 gold coin to 5-pound gold coin, as well as bars in various weights from 0.25 grams to 1 kilo, satisfying every customer’s needs.\r\n            We also have a production line for solid and hollow gold chains, available in a variety of sizes, designs, and weights, all crafted with precision and care. This line is exclusively available for wholesale to jewelry retail stores. All our products are stamped by the Egyptian Authority of Hallmarks and Weights. \r\n            \r\n        </div>\r\n        <div class=\"ins-space-3xl\"></div>\r\n\r\n\r\n        <div class=\"ins-line ins-col-12\"></div>\r\n\r\n        <div class=\"ins-space-3xl\"></div>\r\n\r\n\r\n    \r\n\r\n</div>', 0, 0, '2025-02-16 10:00:32', '2025-01-07 14:24:09', '{\"ar\": {\"content\": \"<!--Header-->\\r\\n<div class=\\\"ins-col-12  ins-border ins-border-bottom\\\" style=\\\"background:white;height:124px;position: relative;\\\">\\r\\n    <div class=\\\"gla-container ins-flex ins-padding-2xl\\\">\\r\\n        <div class=\\\"ins-col-12 ins-flex ins-text-upper\\\">\\r\\n            <a href=\\\"/\\\" class=\\\" ins-font-s\\tins-grey-d-color ins-strong-m\\\">\\u0627\\u0644\\u0631\\u0626\\u064a\\u0633\\u064a\\u0629/</a>\\r\\n            <div class=\\\" ins-font-s\\tins-grey-color ins-strong-m\\\">\\u0645\\u0639\\u0644\\u0648\\u0645\\u0627\\u062a \\u0639\\u0646\\u0627</div>\\r\\n        </div>\\r\\n        <div class=\\\"ins-col-12 ins-title ins-strong-m ins-text-upper ins-grey-d-color \\\">\\r\\n\\u0645\\u0639\\u0644\\u0648\\u0645\\u0627\\u062a \\u0639\\u0646\\u0627        </div>\\r\\n    </div>\\r\\n</div>\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n<!--Main Container-->\\r\\n<div class=\\\"ins-col-12 \\\" style=\\\"    margin-top: -8px;\\\">\\r\\n    <div start=\\\"true\\\" class=\\\"ins-flex  ins-padding-2xl gla-container \\\" style=\\\"padding-bottom:12px\\\">\\r\\n        <div class=\\\"ins-space-l\\\"></div>\\r\\n\\r\\n\\r\\n        <!--First Conent-->\\r\\n        <div start=\\\"true\\\" class=\\\"ins-flex  ins-col-12\\\">\\r\\n            <div class=\\\"ins-title-xl ins-grey-d-color ins-strong-m\\\" style=\\\"line-height:50px\\\">\\u0625\\u0631\\u062b \\u0645\\u0646 \\u0627\\u0644\\u0630\\u0647\\u0628 \\u2013 \\u062b\\u0644\\u0627\\u062b\\u0629 <br> \\u0642\\u0635\\u0629 \\u0627\\u0644\\u0630\\u0647\\u0628 \\u0627\\u0644\\u062c\\u0644\\u0627 </div>\\r\\n            <div class=\\\"ins-col-grow \\\"></div>\\r\\n            <div class=\\\"ins-space-l\\\"></div>\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex-center ins-grey-color \\\" style=\\\"width:500px;height:406px\\\">\\r\\n                <div class=\\\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\\\">\\u0627\\u0644\\u0628\\u062f\\u0627\\u064a\\u0629</div>\\r\\n                <div class=\\\"ins-space-s\\\"></div>\\r\\n                <div class=\\\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\\\" style=\\\"line-height:60px\\\">1950s</div>\\r\\n                <div class=\\\"ins-space-s\\\"></div>\\r\\n                <div class=\\\" ins-col-12 ins-strong-m \\\" style=\\\"line-height:24px;font-size:20px\\\">\\u062a\\u0623\\u0633\\u0633\\u062a \\u0634\\u0631\\u0643\\u0629 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f \\u0639\\u0627\\u0645 1950 \\u062a\\u062d\\u062a \\u0642\\u064a\\u0627\\u062f\\u0629 \\u0645\\u0624\\u0633\\u0633\\u0647\\u0627 \\u0627\\u0644\\u062d\\u0627\\u062c \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627\\u060c  \\u0648\\u062a\\u0645 \\u062a\\u0648\\u0627\\u0631\\u062b\\u0647\\u0627 \\u0645\\u0646 \\u062c\\u064a\\u0644 \\u0644\\u062c\\u064a\\u0644\\u060c \\u0648\\u0632\\u064a \\u0627\\u0644\\u0630\\u0647\\u0628 \\u0627\\u062a\\u0639\\u0631\\u0641 \\u0627\\u0644\\u062d\\u0627\\u062c \\u062d\\u0633\\u0646 \\u0628\\u0635\\u062f\\u0642\\u0647 \\u0648\\u0627\\u0644\\u062a\\u0632\\u0627\\u0645\\u0647 \\u0648\\u0643\\u0627\\u0646\\u062a \\u0627\\u0644\\u0642\\u064a\\u0645 \\u0648\\u0627\\u0644\\u062f\\u0631\\u0648\\u0633 \\u0627\\u0644\\u062a\\u064a \\u0627\\u0643\\u062a\\u0633\\u0628\\u0647\\u0627 \\u0641\\u064a \\u062d\\u064a\\u0627\\u062a\\u0647 \\u0645\\u0635\\u062f\\u0631 \\u0625\\u0644\\u0647\\u0627\\u0645 \\u0641\\u064a \\u0645\\u0633\\u064a\\u0631\\u062a\\u0647 \\u0644\\u062a\\u062d\\u0642\\u064a\\u0642 \\u0627\\u0644\\u062c\\u0648\\u062f\\u0629 \\u0648 \\u0627\\u0644\\u0648\\u0635\\u0648\\u0644 \\u0625\\u0644\\u0649 \\u0631\\u0636\\u0627\\u0621 \\u0627\\u0644\\u0639\\u0645\\u0644\\u0627\\u0621 \\u0648 \\u0627\\u0644\\u0644\\u064a \\u0628\\u0646\\u0639\\u062a\\u0628\\u0631\\u0647 \\u0627\\u0644\\u0642\\u0648\\u0629 \\u0627\\u0644\\u062f\\u0627\\u0641\\u0639\\u0629 \\u0648\\u0631\\u0627\\u0621 \\u0646\\u062c\\u0627\\u062d\\u0646\\u0627.</div>\\r\\n            </div>\\r\\n            <div class=\\\"ins-col-grow\\\"></div>\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex gla-alogo-primary-l\\\" style=\\\"    background-size: 166px auto;background-position: 58% top;\\\">\\r\\n                <div start=\\\"true\\\" class=\\\"ins-flex-start\\\"style=\\\"width:424px;height:273px;margin:0 10px\\\"><img src=\\\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/1950s.png\\\"></div>\\r\\n            </div>\\r\\n            \\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\u060c \\u062a\\u0627\\u0631\\u064a\\u062e \\u064a\\u0631\\u062a\\u0628\\u0637 \\u0628\\u0627\\u0644\\u0627\\u0635\\u0627\\u0644\\u0629 \\u0648\\u0627\\u0644\\u062c\\u0648\\u062f\\u0629 \\u0648\\u0627\\u0644\\u062b\\u0642\\u0629 \\u060c \\u0639\\u0644\\u064a \\u0645\\u062f\\u0627\\u0631 \\u0627\\u0644 \\u0667\\u0665 \\u0633\\u0646\\u0629 \\u0627\\u0644\\u0644\\u064a \\u0641\\u0627\\u062a\\u0648\\u0627 \\u0643\\u0627\\u0646\\u062a \\\"\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\\" \\u062d\\u062c\\u0631 \\u0627\\u0644\\u0632\\u0627\\u0648\\u064a\\u0629 \\u0641\\u064a \\u0635\\u0646\\u0627\\u0639\\u0629 \\u0627\\u0644\\u0630\\u0647\\u0628 \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\\u0629. \\u062a\\u0623\\u0633\\u0633\\u062a \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629 \\u0639\\u0627\\u0645 1950\\u060c \\u0648\\u062a\\u0645 \\u062a\\u0648\\u0627\\u0631\\u062b\\u0647\\u0627 \\u0645\\u0646 \\u062c\\u064a\\u0644 \\u0644\\u062c\\u064a\\u0644\\u060c \\u0648 \\u0643\\u0644 \\u062c\\u064a\\u0644 \\u0633\\u0627\\u0639\\u062f \\u0641\\u064a \\u062a\\u0639\\u0632\\u064a\\u0632 \\u0647\\u0630\\u0627 \\u0627\\u0644\\u0625\\u0631\\u062b \\u0627\\u0644\\u063a\\u0646\\u064a \\u0648 \\u0623\\u0636\\u0627\\u0641 \\u0628\\u0635\\u0645\\u062a\\u0647 \\u0627\\u0644\\u062e\\u0627\\u0635\\u0629 \\u0645\\u0646 \\u0627\\u0644\\u0645\\u0639\\u0631\\u0641\\u0629 \\u0648\\u0627\\u0644\\u062e\\u0628\\u0631\\u0629\\u060c \\u0648 \\u062f\\u0647 \\u0633\\u0627\\u0647\\u0645 \\u0641\\u064a \\u062a\\u062d\\u0642\\u064a\\u0642 \\u0627\\u0644\\u0631\\u0624\\u064a\\u0629 \\u0627\\u0644\\u062a\\u064a \\u0628\\u062f\\u0623\\u0647\\u0627 \\u0627\\u0644\\u062d\\u0627\\u062c \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0651\\u0627.\\r\\n            \\u0628\\u062f\\u0623\\u062a \\u0631\\u062d\\u0644\\u0629 \\\"\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\\" \\u062a\\u062d\\u062a \\u0642\\u064a\\u0627\\u062f\\u0629 \\u0645\\u0624\\u0633\\u0633\\u0647\\u0627 \\u0627\\u0644\\u062d\\u0627\\u062c \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627\\u060c \\u0648 \\u0623\\u0648\\u0644 \\u064a\\u0648\\u0645 \\u0623\\u0633\\u0633 \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629 \\u0645\\u0628\\u0646\\u064a\\u0629 \\u0639\\u0644\\u0649 \\u0645\\u0628\\u0627\\u062f\\u0626 \\u0623\\u062e\\u0644\\u0627\\u0642\\u064a\\u0629 \\u0642\\u0648\\u064a\\u0629 \\u0648\\u0627\\u0647\\u062a\\u0645\\u0627\\u0645 \\u063a\\u064a\\u0631 \\u0645\\u062d\\u062f\\u0648\\u062f \\u0628\\u0627\\u0644\\u062c\\u0648\\u062f\\u0629. \\u0627\\u0633\\u0645 \\\"\\u0627\\u0644\\u062c\\u0644\\u0627\\\"\\u060c \\u0639\\u0628\\u0627\\u0631\\u0629 \\u0639\\u0646 \\u0644\\u0642\\u0628 \\u0645\\u0639\\u0646\\u0627\\u0647 \\\"\\u062c\\u0644\\u064a \\u0627\\u0644\\u0630\\u0647\\u0628\\\"\\u060c \\u0648 \\u062f\\u0647 \\u062c\\u0632\\u0621 \\u0623\\u0633\\u0627\\u0633\\u064a \\u0641\\u064a \\u0635\\u0646\\u0627\\u0639\\u0629 \\u0627\\u0644\\u0645\\u0646\\u062a\\u062c\\u0627\\u062a \\u0627\\u0644\\u0630\\u0647\\u0628\\u064a\\u0629 \\u0648 \\u0647\\u0648 \\u064a\\u0639\\u0643\\u0633 \\u0628\\u062f\\u0627\\u064a\\u0629 \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629 \\u0644\\u0645\\u0627 \\u0643\\u0627\\u0646 \\u0627\\u0644\\u062d\\u0627\\u062c \\u062d\\u0633\\u0646 \\u0645\\u062a\\u062e\\u0635\\u0635 \\u0641\\u064a \\u062c\\u064e\\u0644\\u0652\\u064a \\u0648\\u062a\\u0644\\u0645\\u064a\\u0639 \\u0627\\u0644\\u0630\\u0647\\u0628 \\u0642\\u0628\\u0644 \\u0623\\u0646 \\u064a\\u062a\\u062d\\u0648\\u0644 \\u0625\\u0644\\u0649 \\u0647\\u0630\\u0627 \\u0627\\u0644\\u0639\\u0645\\u0644 \\u0627\\u0644\\u0645\\u0632\\u062f\\u0647\\u0631. \\u0648\\u0632\\u064a \\u0627\\u0644\\u0630\\u0647\\u0628 \\u0627\\u062a\\u0639\\u0631\\u0641 \\u0627\\u0644\\u062d\\u0627\\u062c \\u062d\\u0633\\u0646 \\u0628\\u0635\\u062f\\u0642\\u0647 \\u0648\\u0627\\u0644\\u062a\\u0632\\u0627\\u0645\\u0647 \\u0648\\u0643\\u0627\\u0646\\u062a \\u0627\\u0644\\u0642\\u064a\\u0645 \\u0648\\u0627\\u0644\\u062f\\u0631\\u0648\\u0633 \\u0627\\u0644\\u062a\\u064a \\u0627\\u0643\\u062a\\u0633\\u0628\\u0647\\u0627 \\u0641\\u064a \\u062d\\u064a\\u0627\\u062a\\u0647 \\u0645\\u0635\\u062f\\u0631 \\u0625\\u0644\\u0647\\u0627\\u0645 \\u0641\\u064a \\u0645\\u0633\\u064a\\u0631\\u062a\\u0647 \\u0644\\u062a\\u062d\\u0642\\u064a\\u0642 \\u0627\\u0644\\u062c\\u0648\\u062f\\u0629 \\u0648 \\u0627\\u0644\\u0648\\u0635\\u0648\\u0644 \\u0625\\u0644\\u0649 \\u0631\\u0636\\u0627\\u0621 \\u0627\\u0644\\u0639\\u0645\\u0644\\u0627\\u0621 \\u0648 \\u0627\\u0644\\u0644\\u064a \\u0628\\u0646\\u0639\\u062a\\u0628\\u0631\\u0647 \\u0627\\u0644\\u0642\\u0648\\u0629 \\u0627\\u0644\\u062f\\u0627\\u0641\\u0639\\u0629 \\u0648\\u0631\\u0627\\u0621 \\u0646\\u062c\\u0627\\u062d\\u0646\\u0627\\u060c \\u0648 \\u062f\\u0627\\u064a\\u0645\\u0627 \\u062d\\u0631\\u064a\\u0635\\u064a\\u0646 \\u0639\\u0644\\u0649 \\u0627\\u0644\\u062d\\u0641\\u0627\\u0638 \\u0639\\u0644\\u0649 \\u0647\\u0630\\u0627 \\u0627\\u0644\\u0625\\u0631\\u062b \\u0627\\u0644\\u0639\\u0631\\u064a\\u0642.\\r\\n            \\r\\n        </div>\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n\\r\\n\\r\\n        <div class=\\\"ins-line ins-col-12\\\"></div>\\r\\n\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n\\r\\n        <!--Second Conent-->\\r\\n        <div start=\\\"true\\\" class=\\\"ins-flex  ins-col-12  ins-col-12\\\">\\r\\n            <div class=\\\"ins-col-6\\\"></div>\\r\\n            <div class=\\\"ins-space-l\\\"></div>\\r\\n\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex gla-alogo-primary-l ins-col-6\\\" style=\\\"    background-size: 166px auto;background-position: 42% top;\\\">\\r\\n                <div start=\\\"true\\\" class=\\\"ins-flex-end    \\\" style=\\\"width:450px;height:283px\\\"><img src=\\\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/1980s.png\\\"></div>\\r\\n            </div>\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex-center ins-grey-color ins-col-6\\\" style=\\\"    height: 406px;\\\">\\r\\n                <div start=\\\"true\\\" class=\\\"ins-flex-center ins-grey-color \\\" style=\\\"width:500px;height:406px\\\">\\r\\n                    <div class=\\\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\\\">\\u0627\\u0644\\u0628\\u062f\\u0627\\u064a\\u0629</div>\\r\\n                    <div class=\\\"ins-space-s\\\"></div>\\r\\n                    <div class=\\\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\\\" style=\\\"line-height:60px\\\">1980s</div>\\r\\n                    <div class=\\\"ins-space-s\\\"></div>\\r\\n                    <div class=\\\" ins-col-12 ins-strong-m \\\" style=\\\"line-height:24px;font-size:20px\\\">\\u0648\\u0645\\u0639 \\u062a\\u0637\\u0648\\u0631 \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629\\u060c \\u0627\\u0628\\u062a\\u062f\\u064a \\u0627\\u0644\\u062c\\u064a\\u0644 \\u0627\\u0644\\u062b\\u0627\\u0646\\u064a \\u0628\\u0642\\u064a\\u0627\\u062f\\u0629 \\u0627\\u0644\\u062d\\u0627\\u062c \\u0623\\u062d\\u0645\\u062f \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u0641\\u064a \\u062a\\u0648\\u0633\\u064a\\u0639 \\u0639\\u0645\\u0644\\u064a\\u0627\\u062a\\u0646\\u0627 \\u0648\\u0627\\u0639\\u062a\\u0645\\u0627\\u062f \\u0645\\u0645\\u0627\\u0631\\u0633\\u0627\\u062a \\u062a\\u062c\\u0627\\u0631\\u064a\\u0629 \\u062d\\u062f\\u064a\\u062b\\u0629 \\u0648\\u0643\\u0627\\u0646 \\u0623\\u0648\\u0644 \\u0645\\u0646 \\u0628\\u062f\\u0623 \\u062a\\u0635\\u0646\\u064a\\u0639 \\u0628\\u064a\\u0639 \\u0627\\u0644\\u0639\\u0645\\u0644\\u0627\\u062a \\u0648\\u0627\\u0644\\u0633\\u0628\\u0627\\u0626\\u0643 \\u0627\\u0644\\u0630\\u0647\\u0628\\u064a\\u0629 \\u0641\\u064a \\u0627\\u0644\\u0633\\u0648\\u0642 \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\\u0629. \\u0645\\u0643\\u0646\\u0634 \\u0645\\u062c\\u0631\\u062f \\u0642\\u0627\\u0626\\u062f\\u060c \\u0628\\u0644 \\u0643\\u0627\\u0646 \\u0623\\u0628 \\u0631\\u0648\\u062d\\u064a \\u0644\\u0646\\u0627\\u0633 \\u0643\\u062a\\u064a\\u0631 \\u0641\\u064a \\u0635\\u0646\\u0627\\u0639\\u0629 \\u0648 \\u062a\\u062c\\u0627\\u0631\\u0629 \\u0627\\u0644\\u0630\\u0647\\u0628. \\u0643\\u0627\\u0646\\u062a \\u0627\\u0644\\u0641\\u062a\\u0631\\u0629 \\u062f\\u064a \\u0645\\u0631\\u062d\\u0644\\u0629 \\u0646\\u0645\\u0648 \\u0643\\u0628\\u064a\\u0631\\u0629\\u060c \\u0642\\u0645\\u0646\\u0627 \\u0628\\u062a\\u0648\\u0633\\u064a\\u0639 \\u0645\\u062c\\u0645\\u0648\\u0639\\u0629 \\u0645\\u0646\\u062a\\u062c\\u0627\\u062a\\u0646\\u0627 \\u0648\\u062a\\u0639\\u0632\\u064a\\u0632 \\u0648\\u062c\\u0648\\u062f\\u0646\\u0627 \\u0641\\u064a \\u0627\\u0644\\u0633\\u0648\\u0642.\\r\\n\\r\\n                    </div>\\r\\n                </div>\\r\\n            </div>\\r\\n            <div class=\\\"ins-col-grow\\\"></div>\\r\\n            \\u0648\\u0645\\u0639 \\u062a\\u0637\\u0648\\u0631 \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629\\u060c \\u0627\\u0628\\u062a\\u062f\\u064a \\u0627\\u0644\\u062c\\u064a\\u0644 \\u0627\\u0644\\u062b\\u0627\\u0646\\u064a \\u0628\\u0642\\u064a\\u0627\\u062f\\u0629 \\u0627\\u0644\\u062d\\u0627\\u062c \\u0623\\u062d\\u0645\\u062f \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u0641\\u064a \\u062a\\u0648\\u0633\\u064a\\u0639 \\u0639\\u0645\\u0644\\u064a\\u0627\\u062a\\u0646\\u0627 \\u0648\\u0627\\u0639\\u062a\\u0645\\u0627\\u062f \\u0645\\u0645\\u0627\\u0631\\u0633\\u0627\\u062a \\u062a\\u062c\\u0627\\u0631\\u064a\\u0629 \\u062d\\u062f\\u064a\\u062b\\u0629 \\u0648\\u0643\\u0627\\u0646 \\u0623\\u0648\\u0644 \\u0645\\u0646 \\u0628\\u062f\\u0623 \\u062a\\u0635\\u0646\\u064a\\u0639 \\u0628\\u064a\\u0639 \\u0627\\u0644\\u0639\\u0645\\u0644\\u0627\\u062a \\u0648\\u0627\\u0644\\u0633\\u0628\\u0627\\u0626\\u0643 \\u0627\\u0644\\u0630\\u0647\\u0628\\u064a\\u0629 \\u0641\\u064a \\u0627\\u0644\\u0633\\u0648\\u0642 \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\\u0629. \\u0645\\u0643\\u0646\\u0634 \\u0645\\u062c\\u0631\\u062f \\u0642\\u0627\\u0626\\u062f\\u060c \\u0628\\u0644 \\u0643\\u0627\\u0646 \\u0623\\u0628 \\u0631\\u0648\\u062d\\u064a \\u0644\\u0646\\u0627\\u0633 \\u0643\\u062a\\u064a\\u0631 \\u0641\\u064a \\u0635\\u0646\\u0627\\u0639\\u0629 \\u0648 \\u062a\\u062c\\u0627\\u0631\\u0629 \\u0627\\u0644\\u0630\\u0647\\u0628. \\u0643\\u0627\\u0646\\u062a \\u0627\\u0644\\u0641\\u062a\\u0631\\u0629 \\u062f\\u064a \\u0645\\u0631\\u062d\\u0644\\u0629 \\u0646\\u0645\\u0648 \\u0643\\u0628\\u064a\\u0631\\u0629\\u060c \\u0642\\u0645\\u0646\\u0627 \\u0628\\u062a\\u0648\\u0633\\u064a\\u0639 \\u0645\\u062c\\u0645\\u0648\\u0639\\u0629 \\u0645\\u0646\\u062a\\u062c\\u0627\\u062a\\u0646\\u0627 \\u0648\\u062a\\u0639\\u0632\\u064a\\u0632 \\u0648\\u062c\\u0648\\u062f\\u0646\\u0627 \\u0641\\u064a \\u0627\\u0644\\u0633\\u0648\\u0642.\\r\\n\\r\\n        </div>\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n\\r\\n\\r\\n        <div class=\\\"ins-line ins-col-12\\\"></div>\\r\\n\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n\\r\\n         <!--Third Conent-->\\r\\n         <div start=\\\"true\\\" class=\\\"ins-flex  ins-col-12\\\">\\r\\n            <div class=\\\"ins-col-grow \\\"></div>\\r\\n            <div class=\\\"ins-space-l\\\"></div>\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex-center ins-grey-color \\\" style=\\\"width:500px;height:406px\\\">\\r\\n                <div class=\\\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\\\">\\u0627\\u0644\\u0628\\u062f\\u0627\\u064a\\u0629</div>\\r\\n                <div class=\\\"ins-space-s\\\"></div>\\r\\n                <div class=\\\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\\\" style=\\\"line-height:60px\\\">2020s</div>\\r\\n                <div class=\\\"ins-space-s\\\"></div>\\r\\n                <div class=\\\" ins-col-12 ins-strong-m \\\" style=\\\"line-height:24px;font-size:20px\\\">\\u0627\\u0644\\u0646\\u0647\\u0627\\u0631\\u062f\\u0629\\u060c \\u0627\\u0644\\u062c\\u064a\\u0644 \\u0627\\u0644\\u062b\\u0627\\u0644\\u062b \\u0628\\u0642\\u064a\\u0627\\u062f\\u0629 \\u0627\\u0644\\u0645\\u0647\\u0646\\u062f\\u0633 \\u0623\\u0633\\u0627\\u0645\\u0629 \\u0623\\u062d\\u0645\\u062f \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u064a\\u0648\\u0627\\u0635\\u0644 \\u0627\\u0644\\u0628\\u0646\\u0627\\u0621 \\u0639\\u0644\\u0649 \\u0627\\u0644\\u0623\\u0633\\u0633 \\u0627\\u0644\\u0642\\u0648\\u064a\\u0629 \\u062e\\u0644\\u0627\\u0644 \\u0639\\u0645\\u0631 \\u0634\\u0631\\u0643\\u0629 \\\"\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\\". \\u0648\\u0628\\u062f\\u0623 \\u0627\\u0633\\u062a\\u062e\\u062f\\u0627\\u0645 \\u0637\\u0631\\u0642 \\u062c\\u062f\\u064a\\u062f\\u0629 \\u0632\\u064a \\u0627\\u0644\\u062a\\u0643\\u0646\\u0648\\u0644\\u0648\\u062c\\u064a\\u0627 \\u0644\\u062a\\u0633\\u0647\\u064a\\u0644 \\u0639\\u0645\\u0644\\u064a\\u0629 \\u0628\\u064a\\u0639 \\u0648\\u0634\\u0631\\u0627\\u0621 \\u0627\\u0644\\u0630\\u0647\\u0628 \\r\\n                </div>\\r\\n            </div>\\r\\n            <div class=\\\"ins-col-grow\\\"></div>\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex gla-alogo-primary-l\\\" style=\\\"    background-size: 166px auto;background-position: 58% top;\\\">\\r\\n                <div start=\\\"true\\\" class=\\\"ins-flex-start\\\" style=\\\"width:424px;height:273px;margin:0 10px\\\"><img src=\\\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/2020.png\\\"></div>\\r\\n            </div>\\r\\n            \\u0627\\u0644\\u0646\\u0647\\u0627\\u0631\\u062f\\u0629\\u060c \\u0627\\u0644\\u062c\\u064a\\u0644 \\u0627\\u0644\\u062b\\u0627\\u0644\\u062b \\u0628\\u0642\\u064a\\u0627\\u062f\\u0629 \\u0627\\u0644\\u0645\\u0647\\u0646\\u062f\\u0633 \\u0623\\u0633\\u0627\\u0645\\u0629 \\u0623\\u062d\\u0645\\u062f \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u064a\\u0648\\u0627\\u0635\\u0644 \\u0627\\u0644\\u0628\\u0646\\u0627\\u0621 \\u0639\\u0644\\u0649 \\u0627\\u0644\\u0623\\u0633\\u0633 \\u0627\\u0644\\u0642\\u0648\\u064a\\u0629 \\u062e\\u0644\\u0627\\u0644 \\u0639\\u0645\\u0631 \\u0634\\u0631\\u0643\\u0629 \\\"\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\\". \\u0648\\u0628\\u062f\\u0623 \\u0627\\u0633\\u062a\\u062e\\u062f\\u0627\\u0645 \\u0637\\u0631\\u0642 \\u062c\\u062f\\u064a\\u062f\\u0629 \\u0632\\u064a \\u0627\\u0644\\u062a\\u0643\\u0646\\u0648\\u0644\\u0648\\u062c\\u064a\\u0627 \\u0644\\u062a\\u0633\\u0647\\u064a\\u0644 \\u0639\\u0645\\u0644\\u064a\\u0629 \\u0628\\u064a\\u0639 \\u0648\\u0634\\u0631\\u0627\\u0621 \\u0627\\u0644\\u0630\\u0647\\u0628 \\u0645\\u0646 \\u062e\\u0644\\u0627\\u0644 \\u0645\\u0648\\u0642\\u0639\\u0646\\u0627 \\u0627\\u0644\\u0625\\u0644\\u0643\\u062a\\u0631\\u0648\\u0646\\u064a \\u0648\\u062a\\u0637\\u0628\\u064a\\u0642 \\u0627\\u0644\\u0645\\u0648\\u0628\\u0627\\u064a\\u0644. \\u062f\\u0644\\u0648\\u0642\\u062a\\u064a \\u064a\\u0645\\u0643\\u0646 \\u0644\\u0644\\u0639\\u0645\\u0644\\u0627\\u0621 \\u0645\\u0634\\u0627\\u0647\\u062f\\u0629 \\u0627\\u0644\\u0645\\u0646\\u062a\\u062c\\u0627\\u062a \\u0627\\u0644\\u0645\\u062e\\u062a\\u0644\\u0641\\u0629 \\u0648\\u0637\\u0644\\u0628\\u0647\\u0627 \\u0628\\u0643\\u0644 \\u0631\\u0627\\u062d\\u0629 \\u0645\\u0646 \\u0627\\u0644\\u0628\\u064a\\u062a. \\u0648 \\u0643\\u0645\\u0627\\u0646 \\u0639\\u0646\\u062f\\u0646\\u0627 \\u0642\\u0646\\u0648\\u0627\\u062a \\u0645\\u062a\\u0639\\u062f\\u062f\\u0629 \\u0639\\u0644\\u0649 \\u0648\\u0633\\u0627\\u0626\\u0644 \\u0627\\u0644\\u062a\\u0648\\u0627\\u0635\\u0644 \\u0627\\u0644\\u0627\\u062c\\u062a\\u0645\\u0627\\u0639\\u064a\\u060c \\u0632\\u064a \\u0641\\u064a\\u0633 \\u0628\\u0648\\u0643\\u060c \\u0627\\u0646\\u0633\\u062a\\u062c\\u0631\\u0627\\u0645\\u060c \\u064a\\u0648\\u062a\\u064a\\u0648\\u0628\\u060c \\u062a\\u064a\\u0643 \\u062a\\u0648\\u0643\\u060c \\u0648\\u0644\\u064a\\u0646\\u0643\\u062f \\u0625\\u0646.\\r\\n\\r\\n\\r\\n        </div>\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n\\r\\n\\r\\n        <div class=\\\"ins-line ins-col-12\\\"></div>\\r\\n\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n        \\r\\n       \\r\\n        <!--Four Conent-->\\r\\n        <div start=\\\"true\\\" class=\\\"ins-flex  ins-col-12  ins-col-12\\\">\\r\\n            <div class=\\\"ins-col-6\\\"></div>\\r\\n            <div class=\\\"ins-space-l\\\"></div>\\r\\n\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex gla-alogo-primary-l ins-col-6\\\" style=\\\"    background-size: 166px auto;background-position: 42% top;\\\">\\r\\n                <div start=\\\"true\\\" class=\\\"ins-flex-end    \\\" style=\\\"width:450px;height:283px\\\"><img src=\\\"http://127.0.0.1:5000/ins_web/ins_uploads/images/about_us/now.png\\\"></div>\\r\\n            </div>\\r\\n            <div start=\\\"true\\\" class=\\\"ins-flex-center ins-grey-color ins-col-6\\\" style=\\\"    height: 406px;\\\">\\r\\n                <div start=\\\"true\\\" class=\\\"ins-flex-center ins-grey-color \\\" style=\\\"width:500px;height:406px\\\">\\r\\n                    <div class=\\\"ins-text-upper ins-title-m  ins-strong-m ins-col-12\\\">\\u0627\\u0644\\u0628\\u062f\\u0627\\u064a\\u0629</div>\\r\\n                    <div class=\\\"ins-space-s\\\"></div>\\r\\n                    <div class=\\\"ins-text-upper ins-title-4xl ins-grey-d-color  ins-col-12\\\" style=\\\"line-height:60px\\\">\\u0627\\u0644\\u0648\\u0642\\u062a \\u0627\\u0644\\u062d\\u0627\\u0636\\u0631</div>\\r\\n                    <div class=\\\"ins-space-s\\\"></div>\\r\\n                    <div class=\\\" ins-col-12 ins-strong-m \\\" style=\\\"line-height:24px;font-size:20px\\\">\\u0646\\u0646\\u0638\\u0631 \\u0625\\u0644\\u0649 \\u0627\\u0644\\u0645\\u0633\\u062a\\u0642\\u0628\\u0644 \\u0628\\u0646\\u0641\\u0633 \\u0627\\u0644\\u0642\\u064a\\u0645 \\u0648\\u0627\\u0644\\u0645\\u0628\\u0627\\u062f\\u0626 \\u0627\\u0644\\u0644\\u064a \\u0628\\u062f\\u0623\\u0646\\u0627 \\u0628\\u064a\\u0647\\u0627\\u060c \\u0647\\u062f\\u0641\\u0646\\u0627 \\u0647\\u0648 \\u062a\\u0642\\u062f\\u064a\\u0645 \\u0642\\u0637\\u0639 \\u0645\\u0646 \\u0627\\u0644\\u0630\\u0647\\u0628 \\u062a\\u062d\\u0645\\u0644 \\u062c\\u0632\\u0621\\u064b\\u0627 \\u0645\\u0646 \\u062a\\u0627\\u0631\\u064a\\u062e\\u0646\\u0627\\u060c \\u0625\\u0644\\u0649 \\u0639\\u0645\\u0644\\u0627\\u0626\\u0646\\u0627. \\u062d\\u062a\\u0649 \\u062a\\u0633\\u062a\\u0645\\u0631 \\u0627\\u0644\\u0631\\u062d\\u0644\\u0629\\u060c \\u0648\\u064a\\u0628\\u0642\\u0649 \\u0627\\u0633\\u0645 \\\"\\u0627\\u0644\\u062c\\u0644\\u0651\\u0627 \\u062c\\u0648\\u0644\\u062f\\\"\\u060c \\u0632\\u064a \\u0645\\u0627 \\u0648\\u0639\\u062f\\u0646\\u0627\\u0643\\u0645 \\u062f\\u0627\\u0626\\u0645\\u064b\\u0627\\u060c \\u0631\\u0645\\u0632\\u064b\\u0627 \\u0644\\u0644\\u062b\\u0642\\u0629.</div>\\r\\n                </div>\\r\\n            </div>\\r\\n            <div class=\\\"ins-col-grow\\\"></div>\\r\\n\\r\\n            \\u0627\\u062d\\u0646\\u0627 \\u0645\\u0633\\u062a\\u0645\\u0631\\u0648\\u0646 \\u0641\\u064a \\u0627\\u0644\\u0627\\u0628\\u062a\\u0643\\u0627\\u0631\\u060c \\u0648\\u0645\\u0648\\u0627\\u0643\\u0628\\u0629 \\u062a\\u0637\\u0648\\u0631\\u0627\\u062a \\u0627\\u0644\\u0633\\u0648\\u0642\\u060c \\u0648\\u062a\\u0642\\u062f\\u064a\\u0645 \\u0623\\u0641\\u0636\\u0644 \\u0627\\u0644\\u0645\\u0646\\u062a\\u062c\\u0627\\u062a \\u0648\\u0627\\u0644\\u062e\\u062f\\u0645\\u0627\\u062a \\u0644\\u0639\\u0645\\u0644\\u0627\\u0626\\u0646\\u0627. \\u0648\\u0645\\u0639 \\u0627\\u0644\\u062a\\u063a\\u064a\\u0631\\u0627\\u062a \\u0627\\u0644\\u0645\\u0633\\u062a\\u0645\\u0631\\u0629 \\u0641\\u064a \\u0627\\u0644\\u0633\\u0648\\u0642\\u060c \\u0646\\u0647\\u062f\\u0641 \\u0625\\u0644\\u0649 \\u0645\\u0633\\u0627\\u0639\\u062f\\u062a\\u0643 \\u0641\\u064a \\u0627\\u0644\\u062a\\u0623\\u0642\\u0644\\u0645 \\u0648\\u062a\\u0623\\u0645\\u064a\\u0646 \\u0645\\u0633\\u062a\\u0642\\u0628\\u0644\\u0643. \\u0627\\u0644\\u0630\\u0647\\u0628 \\u0645\\u0634 \\u0645\\u062c\\u0631\\u062f \\u0645\\u0639\\u062f\\u0646 \\u062b\\u0645\\u064a\\u0646\\u060c \\u0644\\u0643\\u0646 \\u0627\\u0633\\u062a\\u062b\\u0645\\u0627\\u0631 \\u062d\\u0642\\u064a\\u0642\\u064a \\u064a\\u062d\\u0627\\u0641\\u0638 \\u0639\\u0644\\u0649 \\u0642\\u064a\\u0645\\u062a\\u0647\\u060c \\u0648 \\u0643\\u0645\\u0627\\u0646 \\u0628\\u064a\\u0632\\u064a\\u062f \\u0645\\u0639 \\u0627\\u0644\\u0648\\u0642\\u062a\\u060c \\u062f\\u0647 \\u064a\\u062e\\u0644\\u064a\\u0647 \\u0627\\u0644\\u062e\\u064a\\u0627\\u0631 \\u0627\\u0644\\u0623\\u0645\\u062b\\u0644 \\u0644\\u0644\\u062d\\u0641\\u0627\\u0638 \\u0639\\u0644\\u0649 \\u0645\\u062f\\u062e\\u0631\\u0627\\u062a\\u0643 \\u0648\\u062a\\u0646\\u0645\\u064a\\u062a\\u0647\\u0627.\\r\\n            \\u0641\\u064a \\\"\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\\" \\u0628\\u0646\\u0647\\u062a\\u0645 \\u0628\\u0641\\u0631\\u064a\\u0642 \\u0627\\u0644\\u0639\\u0645\\u0644 \\u0644\\u0623\\u0646\\u0647\\u0645 \\u0623\\u0633\\u0627\\u0633 \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629 \\u0632\\u064a \\u0627\\u0647\\u062a\\u0645\\u0627\\u0645\\u0646\\u0627 \\u0627\\u0644\\u0643\\u0628\\u064a\\u0631 \\u0648 \\u0641\\u062e\\u0631\\u0646\\u0627 \\u0628\\u0643\\u0644 \\u0642\\u0637\\u0639\\u0629 \\u0646\\u0635\\u0646\\u0639\\u0647\\u0627.\\r\\n             \\u0648 \\u0644\\u0623\\u0646 \\u062a\\u0644\\u0628\\u064a\\u0629 \\u0627\\u062d\\u062a\\u064a\\u0627\\u062c\\u0627\\u062a \\u0639\\u0645\\u0644\\u0627\\u0626\\u0646\\u0627 \\u0645\\u0646 \\u0623\\u0647\\u0645 \\u0623\\u0647\\u062f\\u0627\\u0641\\u0646\\u0627\\u060c \\u0628\\u0646\\u0642\\u062f\\u0645 \\u0645\\u062c\\u0645\\u0648\\u0639\\u0629 \\u0645\\u062a\\u0646\\u0648\\u0639\\u0629 \\u0645\\u0646 \\u0645\\u0646\\u062a\\u062c\\u0627\\u062a \\u0627\\u0644\\u0630\\u0647\\u0628\\u060c \\u0628\\u0645\\u0627 \\u0641\\u064a \\u0630\\u0644\\u0643 \\u0627\\u0644\\u0639\\u0645\\u0644\\u0627\\u062a \\u0627\\u0644\\u0630\\u0647\\u0628\\u064a\\u0629 \\u0627\\u0644\\u062a\\u064a \\u062a\\u062a\\u0631\\u0627\\u0648\\u062d \\u0645\\u0646 1/8 \\u062c\\u0646\\u064a\\u0647 \\u0630\\u0647\\u0628 \\u062d\\u062a\\u0649 5 \\u062c\\u0646\\u064a\\u0647\\u0627\\u062a \\u0630\\u0647\\u0628\\u064a\\u0629\\u060c \\u0648 \\u0633\\u0628\\u0627\\u0626\\u0643 \\u0628\\u0623\\u0648\\u0632\\u0627\\u0646 \\u0645\\u062e\\u062a\\u0644\\u0641\\u0629 \\u062a\\u0628\\u062f\\u0623 \\u0645\\u0646 0.25 \\u062c\\u0631\\u0627\\u0645 \\u062d\\u062a\\u0649 1 \\u0643\\u064a\\u0644\\u0648.\\r\\n             \\u0648 \\u0643\\u0645\\u0627\\u0646 \\u0639\\u0646\\u062f\\u0646\\u0627 \\u062e\\u0637 \\u0625\\u0646\\u062a\\u0627\\u062c \\u0633\\u0644\\u0627\\u0633\\u0644 \\u0627\\u0644\\u0630\\u0647\\u0628\\u060c \\u0645\\u062a\\u0648\\u0641\\u0631\\u0629 \\u0628\\u0645\\u062c\\u0645\\u0648\\u0639\\u0629 \\u0645\\u062a\\u0646\\u0648\\u0639\\u0629 \\u0645\\u0646 \\u0627\\u0644\\u0623\\u062d\\u062c\\u0627\\u0645 \\u0648\\u0627\\u0644\\u062a\\u0635\\u0627\\u0645\\u064a\\u0645 \\u0648\\u0627\\u0644\\u0623\\u0648\\u0632\\u0627\\u0646\\u060c \\u062a\\u062a\\u0635\\u0646\\u0639 \\u0628\\u062f\\u0642\\u0629 \\u0648\\u0639\\u0646\\u0627\\u064a\\u0629. \\u0627\\u0644\\u062e\\u0637 \\u062f\\u0647 \\u0645\\u062a\\u0627\\u062d \\u062d\\u0635\\u0631\\u064a\\u064b\\u0627 \\u0644\\u0644\\u0628\\u064a\\u0639 \\u0628\\u0627\\u0644\\u062c\\u0645\\u0644\\u0629 \\u0644\\u0645\\u062d\\u0644\\u0627\\u062a \\u0628\\u064a\\u0639 \\u0627\\u0644\\u0645\\u062c\\u0648\\u0647\\u0631\\u0627\\u062a. \\u0648 \\u0643\\u0644 \\u0645\\u0646\\u062a\\u062c\\u0627\\u062a\\u0646\\u0627 \\u0645\\u062e\\u062a\\u0648\\u0645\\u0629 \\u0645\\u0646 \\u0642\\u0628\\u0644 \\u0645\\u0635\\u0644\\u062d\\u0629 \\u062f\\u0645\\u063a \\u0627\\u0644\\u0645\\u0635\\u0648\\u063a\\u0627\\u062a \\u0648\\u0627\\u0644\\u0645\\u0648\\u0627\\u0632\\u064a\\u0646 \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\\u0629.\\r\\n            \\r\\n            \\u0627\\u062d\\u0646\\u0627 \\u0645\\u0648\\u062c\\u0648\\u062f\\u064a\\u0646 \\u0641\\u064a \\u0641\\u0631\\u0639\\u064a\\u0646. \\u0641\\u0631\\u0639 \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629 \\u0627\\u0644\\u0631\\u0626\\u064a\\u0633\\u064a  \\u0641\\u064a \\u0634\\u0627\\u0631\\u0639 \\u0627\\u0644\\u0645\\u0639\\u0632\\u060c \\u0648\\u064a\\u062e\\u062f\\u0645 \\u0639\\u0645\\u0644\\u0627\\u0621 \\u0627\\u0644\\u062c\\u0645\\u0644\\u0629 \\u0648\\u0627\\u0644\\u062a\\u062c\\u0632\\u0626\\u0629. \\u0623\\u0645\\u0627 \\u0641\\u0631\\u0639\\u0646\\u0627 \\u0627\\u0644\\u062b\\u0627\\u0646\\u064a\\u060c \\u0641\\u064a \\u0645\\u0648\\u0644 \\u0634\\u0627\\u0631\\u0639 88\\u060c \\u0628\\u0627\\u0644\\u0645 \\u0647\\u064a\\u0644\\u0632 \\u0632\\u0627\\u064a\\u062f\\u060c \\u0648\\u064a\\u062e\\u062a\\u0635 \\u062d\\u0635\\u0631\\u064a\\u064b\\u0627 \\u0628\\u0628\\u064a\\u0639 \\u0627\\u0644\\u0633\\u0628\\u0627\\u0626\\u0643 \\u0648\\u0627\\u0644\\u0639\\u0645\\u0644\\u0627\\u062a \\u0627\\u0644\\u0630\\u0647\\u0628\\u064a\\u0629 \\u0628\\u0627\\u0644\\u062a\\u062c\\u0632\\u0626\\u0629. \\u0648 \\u0643\\u0645\\u0627\\u0646 \\u062a\\u0642\\u062f\\u0631 \\u062a\\u0634\\u062a\\u0631\\u064a \\u0645\\u0646\\u062a\\u062c\\u0627\\u062a\\u0646\\u0627 \\u0645\\u0646 \\u062e\\u0644\\u0627\\u0644 \\u0645\\u0648\\u0632\\u0639\\u064a\\u0646\\u0627 \\u0627\\u0644\\u0645\\u062a\\u0648\\u0627\\u062c\\u062f\\u064a\\u0646 \\u0641\\u064a \\u0645\\u062e\\u062a\\u0644\\u0641 \\u0627\\u0644\\u0645\\u062d\\u0627\\u0641\\u0638\\u0627\\u062a \\u0627\\u0644\\u0645\\u0635\\u0631\\u064a\\u0629\\u060c \\u0632\\u064a \\u0627\\u0644\\u0642\\u0627\\u0647\\u0631\\u0629 \\u0648\\u0627\\u0644\\u0625\\u0633\\u0643\\u0646\\u062f\\u0631\\u064a\\u0629 \\u0648\\u0628\\u0648\\u0631\\u0633\\u0639\\u064a\\u062f \\u0648\\u0627\\u0644\\u0633\\u0648\\u064a\\u0633.\\r\\n            \\u0634\\u0631\\u0643\\u0629 \\\"\\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f\\\" \\u0639\\u0646\\u062f\\u0647\\u0627 \\u0639\\u0644\\u0627\\u0642\\u0627\\u062a \\u0645\\u062b\\u0645\\u0631\\u0629 \\u0639\\u0644\\u0649 \\u0645\\u062f\\u0627\\u0631 \\u0627\\u0644\\u0633\\u0646\\u064a\\u0646 \\u0627\\u0644\\u0644\\u064a \\u0641\\u0627\\u062a\\u062a \\u0645\\u0639 \\u0634\\u0631\\u0643\\u0627\\u062a \\u0643\\u062a\\u064a\\u0631\\u0629 \\u0633\\u0648\\u0627\\u0621 \\u0627\\u0644\\u0645\\u062d\\u0644\\u064a\\u0629 \\u0623\\u0648 \\u0627\\u0644\\u0639\\u0627\\u0644\\u0645\\u064a\\u0629 \\u0641\\u064a \\u0645\\u062e\\u062a\\u0644\\u0641 \\u0627\\u0644\\u0642\\u0637\\u0627\\u0639\\u0627\\u062a \\u0641\\u064a \\u0645\\u0635\\u0631 \\u0632\\u064a \\u0642\\u0637\\u0627\\u0639 \\u0627\\u0644\\u0633\\u0644\\u0639 \\u0627\\u0644\\u0627\\u0633\\u062a\\u0647\\u0644\\u0627\\u0643\\u064a\\u0629\\u060c \\u0648\\u0627\\u0644\\u0628\\u0646\\u0648\\u0643\\u060c \\u0648\\u0635\\u0646\\u0627\\u0639\\u0629 \\u0627\\u0644\\u0633\\u064a\\u0627\\u0631\\u0627\\u062a\\u060c \\u0648\\u0627\\u0644\\u0623\\u062c\\u0647\\u0632\\u0629 \\u0627\\u0644\\u0645\\u0646\\u0632\\u0644\\u064a\\u0629\\u060c \\u0648\\u0646\\u0642\\u062f\\u0645 \\u0644\\u0647\\u0645 \\u0645\\u0646\\u062a\\u062c\\u0627\\u062a \\u0630\\u0647\\u0628\\u064a\\u0629 \\u062a\\u0646\\u0627\\u0633\\u0628 \\u0627\\u062d\\u062a\\u064a\\u0627\\u062c\\u0627\\u062a \\u0634\\u0631\\u0643\\u0627\\u062a\\u0647\\u0645.\\r\\n            \\u0627\\u0644\\u062c\\u0644\\u0627 \\u062c\\u0648\\u0644\\u062f \\u0645\\u0634 \\u0645\\u062c\\u0631\\u062f \\u0634\\u0631\\u0643\\u0629\\u060c \\u0644\\u0643\\u0646 \\u0647\\u064a \\u0639\\u0627\\u0626\\u0644\\u0629 \\u062a\\u0623\\u0633\\u0633\\u062a \\u0628\\u062a\\u0627\\u0631\\u064a\\u062e \\u0645\\u0646 \\u0627\\u0644\\u062d\\u0628 \\u0648\\u0627\\u0644\\u062b\\u0642\\u0629\\u060c \\u0648\\u0627\\u0646\\u062a\\u0642\\u0644\\u062a \\u0639\\u0628\\u0631 \\u0627\\u0644\\u0623\\u062c\\u064a\\u0627\\u0644 \\u0645\\u0646 \\u0627\\u0644\\u0623\\u0628 \\u0625\\u0644\\u0649 \\u0627\\u0644\\u0627\\u0628\\u0646 \\u0625\\u0644\\u0649 \\u0627\\u0644\\u062d\\u0641\\u064a\\u062f. \\u0646\\u0639\\u0645\\u0644 \\u0644\\u0644\\u062d\\u0641\\u0627\\u0638 \\u0639\\u0644\\u0649 \\u0625\\u0631\\u062b \\u062d\\u0633\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u0648\\u062a\\u0637\\u0648\\u064a\\u0631\\u0647. \\u0645\\u0648\\u0638\\u0641\\u064a\\u0646\\u0627 \\u0647\\u0645 \\u062c\\u0632\\u0621 \\u0645\\u0646 \\u0639\\u0627\\u0626\\u0644\\u062a\\u0646\\u0627 \\u0627\\u0644\\u0645\\u0645\\u062a\\u062f\\u0629 \\u0648 \\u0645\\u0646\\u0647\\u0645 \\u064a\\u0639\\u0645\\u0644 \\u0641\\u064a \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629 \\u0645\\u0646\\u0630 \\u0623\\u0643\\u062b\\u0631 \\u0645\\u0646 \\u0664\\u0660 \\u0633\\u0646\\u0629\\u060c \\u0648\\u0643\\u0627\\u0646\\u0648\\u0627 \\u062f\\u0627\\u064a\\u0645\\u064b\\u0627 \\u062c\\u0632\\u0621 \\u0645\\u0646 \\u0631\\u062d\\u0644\\u0629 \\u0627\\u0644\\u0634\\u0631\\u0643\\u0629 \\u0648\\u0646\\u0645\\u0648\\u0647\\u0627. \\u0643\\u0644 \\u0642\\u0637\\u0639\\u0629 \\u0630\\u0647\\u0628 \\u0646\\u0644\\u0645\\u0633\\u0647\\u0627 \\u062a\\u062d\\u0643\\u064a \\u0642\\u0635\\u062a\\u0646\\u0627\\u060c \\u0648\\u062a\\u0636\\u0645\\u0646 \\u062a\\u0627\\u0631\\u064a\\u062e\\u0646\\u0627 \\u064a\\u0633\\u062a\\u0645\\u0631 \\u0644\\u0623\\u062c\\u064a\\u0627\\u0644 \\u0643\\u062a\\u064a\\u0631 \\u062c\\u0627\\u064a\\u0647.\\r\\n            \\u0646\\u0646\\u0638\\u0631 \\u0625\\u0644\\u0649 \\u0627\\u0644\\u0645\\u0633\\u062a\\u0642\\u0628\\u0644 \\u0628\\u0646\\u0641\\u0633 \\u0627\\u0644\\u0642\\u064a\\u0645 \\u0648\\u0627\\u0644\\u0645\\u0628\\u0627\\u062f\\u0626 \\u0627\\u0644\\u0644\\u064a \\u0628\\u062f\\u0623\\u0646\\u0627 \\u0628\\u064a\\u0647\\u0627\\u060c \\u0647\\u062f\\u0641\\u0646\\u0627 \\u0647\\u0648 \\u062a\\u0642\\u062f\\u064a\\u0645 \\u0642\\u0637\\u0639 \\u0645\\u0646 \\u0627\\u0644\\u0630\\u0647\\u0628 \\u062a\\u062d\\u0645\\u0644 \\u062c\\u0632\\u0621\\u064b\\u0627 \\u0645\\u0646 \\u062a\\u0627\\u0631\\u064a\\u062e\\u0646\\u0627\\u060c \\u0625\\u0644\\u0649 \\u0639\\u0645\\u0644\\u0627\\u0626\\u0646\\u0627. \\u062d\\u062a\\u0649 \\u062a\\u0633\\u062a\\u0645\\u0631 \\u0627\\u0644\\u0631\\u062d\\u0644\\u0629\\u060c \\u0648\\u064a\\u0628\\u0642\\u0649 \\u0627\\u0633\\u0645 \\\"\\u0627\\u0644\\u062c\\u0644\\u0651\\u0627 \\u062c\\u0648\\u0644\\u062f\\\"\\u060c \\u0632\\u064a \\u0645\\u0627 \\u0648\\u0639\\u062f\\u0646\\u0627\\u0643\\u0645 \\u062f\\u0627\\u0626\\u0645\\u064b\\u0627\\u060c \\u0631\\u0645\\u0632\\u064b\\u0627 \\u0644\\u0644\\u062b\\u0642\\u0629.\\r\\n            \\r\\n            \\r\\n            \\r\\n        </div>\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n\\r\\n\\r\\n        <div class=\\\"ins-line ins-col-12\\\"></div>\\r\\n\\r\\n        <div class=\\\"ins-space-3xl\\\"></div>\\r\\n\\r\\n\\r\\n    \\r\\n\\r\\n</div>\"}}');
INSERT INTO `kit_content` (`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(305, 'contact us', '<div class=\"ins-col-12  ins-border ins-border-bottom\" style=\"background:white;height:124px;position: relative;\">\r\n    <div class=\"gla-container ins-flex ins-padding-2xl\" >\r\n        <div class=\"ins-col-12 ins-flex ins-text-upper\"><a href=\"/\" class=\" ins-font-s	ins-grey-d-color ins-strong-m\">Home /</a>\r\n            <div class=\" ins-font-s	ins-grey-color ins-strong-m\">Contact Us</div>\r\n        </div>\r\n        <div class=\"ins-col-12 ins-title ins-strong-m ins-text-upper ins-grey-d-color \">\r\n            Contact Us\r\n        </div>\r\n    </div>\r\n</div>\r\n<div class=\"ins-col-12 \" style=\"    margin-top: -8px;\">\r\n<div class=\"ins-col-12 ins-flex-valign-start ins-gap-o gla-container\">\r\n<div class=\"ins-col-6  ins-padding-2xl\">\r\n<iframe src=\"https://www.google.com.qa/maps/d/u/0/embed?mid=1l8Aq_2LE34Xg78yim56U0s1e-7O1bqA&ehbc=2E312F&noprof=1\" width=\"100%\" height=\"450\" style=\"border:0;border-radius:8px;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade\"></iframe>\r\n</div>\r\n<div class=\"ins-col-5 ins-flex   ins-padding-2xl\" style=\"background:white;    height: 485px;   border-left: 1px solid var(--primary-l);\">\r\n<span class=\"ins-title-l\">Get in Touch</span>\r\n<div class=\"ins-space-m\"></div>\r\n<ul>\r\n<li><i class=\"lni lni-map-marker-5\"></i><a href=\"https://maps.app.goo.gl/Tot6YZVhhsQqeDTL7\" target=\"_blank\"> El Galla Gold, 60 El Moez Le Din Allah St., El Gamalia, Cairo</a> </li>\r\n<li><i class=\"lni lni-alarm-1\"></i> Opening hours : 11:00 AM - 8:00 PM </li>\r\n<li><i class=\"lni lni-map-marker-5\"></i><a href=\"https://maps.app.goo.gl/kqrvtN3TSfZHgkZQA\" target=\"_blank\"> El Galla Gold, Street 88 , Palm Hills , 6th of October, Giza </a></li>\r\n<li><i class=\"lni lni-alarm-1\"></i> Opening hours: 11:00 AM - 8:00 PM </li>\r\n<li><i class=\"lni lni-telephone-1\"></i> Call us:  <a href=\"tel:17153 \">17153 </a></li>\r\n<li><i class=\"lni lni-whatsapp\"></i> Whatsapp us:  <a href=\"whatsapp:contact=01009539999@s.whatsapp.com&message=\"I want to chat with you\">01009539999</a></li>\r\n<li><i class=\"lni lni-envelope-1\"></i> Email us: <a href=\"mailto:info@elgallagold.com\">info@elgallagold.com</a> </li>\r\n</ul>\r\n\r\n</div>\r\n</div></div>', 0, 0, '2025-03-03 10:32:14', NULL, '{\"ar\": {\"content\": \"<div class=\\\"ins-col-12  ins-border ins-border-bottom\\\" style=\\\"background:white;height:124px;position: relative;\\\">\\r\\n    <div class=\\\"gla-container ins-flex ins-padding-2xl\\\">\\r\\n        <div class=\\\"ins-col-12 ins-flex ins-text-upper\\\">\\r\\n            <a href=\\\"/\\\" class=\\\"ins-font-s ins-grey-d-color ins-strong-m\\\">\\u0627\\u0644\\u0631\\u0626\\u064a\\u0633\\u064a\\u0629 /</a>\\r\\n            <div class=\\\"ins-font-s ins-grey-color ins-strong-m\\\">\\u0627\\u062a\\u0635\\u0644 \\u0628\\u0646\\u0627</div>\\r\\n        </div>\\r\\n        <div class=\\\"ins-col-12 ins-title ins-strong-m ins-text-upper ins-grey-d-color \\\">\\r\\n            \\u0627\\u062a\\u0635\\u0644 \\u0628\\u0646\\u0627\\r\\n        </div>\\r\\n    </div>\\r\\n</div>\\r\\n<div class=\\\"ins-col-12 \\\" style=\\\"margin-top: -8px;\\\">\\r\\n    <div class=\\\"ins-col-12 ins-flex-valign-start ins-gap-o gla-container\\\">\\r\\n        <div class=\\\"ins-col-6 ins-padding-2xl\\\">\\r\\n            <iframe src=\\\"https://www.google.com.qa/maps/d/u/0/embed?mid=1l8Aq_2LE34Xg78yim56U0s1e-7O1bqA&ehbc=2E312F&noprof=1\\\" width=\\\"100%\\\" height=\\\"450\\\" style=\\\"border:0;border-radius:8px;\\\" allowfullscreen=\\\"\\\" loading=\\\"lazy\\\" referrerpolicy=\\\"no-referrer-when-downgrade\\\"></iframe>\\r\\n        </div>\\r\\n        <div class=\\\"ins-col-5 ins-flex ins-padding-2xl\\\" style=\\\"background:white; height: 485px; border-left: 1px solid var(--primary-l);\\\">\\r\\n            <span class=\\\"ins-title-l\\\">\\u062a\\u0648\\u0627\\u0635\\u0644 \\u0645\\u0639\\u0646\\u0627</span>\\r\\n            <div class=\\\"ins-space-m\\\"></div>\\r\\n            <ul>\\r\\n                <li><i class=\\\"lni lni-map-marker-5\\\"></i> <a href=\\\"https://maps.app.goo.gl/Tot6YZVhhsQqeDTL7\\\" target=\\\"_blank\\\"> \\u0627\\u0644\\u062c\\u0644\\u0627\\u0644\\u0647 \\u062c\\u0648\\u0644\\u062f\\u060c 60 \\u0634\\u0627\\u0631\\u0639 \\u0627\\u0644\\u0645\\u0639\\u0632 \\u0644\\u062f\\u064a\\u0646 \\u0627\\u0644\\u0644\\u0647\\u060c \\u0627\\u0644\\u062c\\u0645\\u0627\\u0644\\u064a\\u0629\\u060c \\u0627\\u0644\\u0642\\u0627\\u0647\\u0631\\u0629 </a></li>\\r\\n                <li><i class=\\\"lni lni-alarm-1\\\"></i> \\u0633\\u0627\\u0639\\u0627\\u062a \\u0627\\u0644\\u0639\\u0645\\u0644: 11:00 \\u0635\\u0628\\u0627\\u062d\\u064b\\u0627 - 8:00 \\u0645\\u0633\\u0627\\u0621\\u064b </li>\\r\\n                <li><i class=\\\"lni lni-map-marker-5\\\"></i> <a href=\\\"https://maps.app.goo.gl/kqrvtN3TSfZHgkZQA\\\" target=\\\"_blank\\\">\\u0627\\u0644\\u062c\\u0644\\u0627\\u0644\\u0647 \\u062c\\u0648\\u0644\\u062f\\u060c \\u0634\\u0627\\u0631\\u0639 88\\u060c \\u0628\\u0627\\u0644\\u0645 \\u0647\\u064a\\u0644\\u0632\\u060c 6 \\u0623\\u0643\\u062a\\u0648\\u0628\\u0631\\u060c \\u0627\\u0644\\u062c\\u064a\\u0632\\u0629 </a></li>\\r\\n                <li><i class=\\\"lni lni-alarm-1\\\"></i> \\u0633\\u0627\\u0639\\u0627\\u062a \\u0627\\u0644\\u0639\\u0645\\u0644: 11:00 \\u0635\\u0628\\u0627\\u062d\\u064b\\u0627 - 8:00 \\u0645\\u0633\\u0627\\u0621\\u064b </li>\\r\\n                <li><i class=\\\"lni lni-telephone-1\\\"></i> \\u0627\\u062a\\u0635\\u0644 \\u0628\\u0646\\u0627: <a href=\\\"tel:17153 \\\">17153</a></li>\\r\\n                <li><i class=\\\"lni lni-whatsapp\\\"></i> \\u062a\\u0648\\u0627\\u0635\\u0644 \\u0645\\u0639\\u0646\\u0627 \\u0639\\u0628\\u0631 \\u0648\\u0627\\u062a\\u0633\\u0627\\u0628: <a href=\\\"whatsapp:contact=01009539999@s.whatsapp.com&message=\\\" \\u0623\\u0631\\u063a\\u0628 \\u0641\\u064a \\u0627\\u0644\\u062f\\u0631\\u062f\\u0634\\u0629 \\u0645\\u0639\\u0643\\u0645 \\\">01009539999</a></li>\\r\\n                <li><i class=\\\"lni lni-envelope-1 \\\"></i> \\u0631\\u0627\\u0633\\u0644\\u0646\\u0627 \\u0639\\u0628\\u0631 \\u0627\\u0644\\u0628\\u0631\\u064a\\u062f \\u0627\\u0644\\u0625\\u0644\\u0643\\u062a\\u0631\\u0648\\u0646\\u064a: <a href=\\\"mailto:info@elgallagold.com \\\">info@elgallagold.com</a> </li>\\r\\n            </ul>\\r\\n        </div>\\r\\n    </div>\\r\\n</div>\"}}');

-- --------------------------------------------------------

--
-- Table structure for table `kit_email_template`
--

CREATE TABLE `kit_email_template` (
  `id` int(11) NOT NULL,
  `title` text DEFAULT NULL,
  `content` text DEFAULT NULL,
  `kit_deleted` tinyint(4) DEFAULT 0,
  `kit_disabled` tinyint(4) DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kit_image`
--

CREATE TABLE `kit_image` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `des` text DEFAULT NULL,
  `image` varchar(255) DEFAULT NULL,
  `fk_image_category_id` int(11) DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kit_image`
--

INSERT INTO `kit_image` (`id`, `title`, `des`, `image`, `fk_image_category_id`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(1, 'Image 1', 'Image 1 Image 1 Image 1 Image 1 Image 1 ', 'images/20250106161204__Screenshot_2024-10-16_213811.png', 1, 0, 0, NULL, '2025-01-06 14:12:18');

-- --------------------------------------------------------

--
-- Table structure for table `kit_image_category`
--

CREATE TABLE `kit_image_category` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `des` varchar(45) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kit_image_category`
--

INSERT INTO `kit_image_category` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `des`) VALUES
(1, 'dddd', 0, 0, '2025-01-05 12:54:14', '2024-11-22 12:52:47', 'dds'),
(2, 'dadas', 1, 0, '2025-01-05 12:54:51', '2025-01-05 12:52:01', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `kit_menu`
--

CREATE TABLE `kit_menu` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `src_area` varchar(255) NOT NULL,
  `tar_area` varchar(255) NOT NULL,
  `kit_tags` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_menu`
--

INSERT INTO `kit_menu` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `src_area`, `tar_area`, `kit_tags`) VALUES
(29, 'main menu', 0, 0, '2024-11-24 12:42:46', '2016-08-13 03:02:14', 'home', 'home', '1'),
(71, 'admin menu', 0, 0, '2024-11-25 09:19:42', '2016-08-13 03:02:14', 'ins_admin', 'ins_admin', '2,8,3,9'),
(72, 'admin settings menu', 0, 0, '2024-11-21 12:34:03', '2016-08-13 03:02:14', 'ins_admin', 'ins_admin', '2,3,1'),
(113, 'gla admin settings menu', 0, 0, '2024-11-21 12:34:03', '2016-08-13 03:02:14', 'ins_admin', 'ins_gla', '2,3,1'),
(112, 'gla admin menu', 0, 0, '2024-11-25 09:19:42', '2016-08-13 03:02:14', 'ins_admin', 'ins_gla', '2,8,3,9');

-- --------------------------------------------------------

--
-- Table structure for table `kit_menu_item`
--

CREATE TABLE `kit_menu_item` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `alias` varchar(255) NOT NULL,
  `fk_menu_id` int(11) NOT NULL DEFAULT 0,
  `kit_order` tinyint(4) NOT NULL DEFAULT 0,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `src_area` varchar(255) NOT NULL,
  `kit_home` tinyint(4) NOT NULL DEFAULT 0,
  `type` varchar(255) NOT NULL,
  `tar_area` varchar(255) NOT NULL,
  `fk_menu_item_id` int(11) NOT NULL,
  `kit_options` text NOT NULL,
  `css` varchar(255) NOT NULL,
  `class` varchar(255) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `add_to_url` text NOT NULL,
  `kit_hidden` tinyint(4) NOT NULL DEFAULT 0,
  `kit_level` int(11) NOT NULL,
  `hidden` tinyint(4) NOT NULL,
  `kit_lang` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_menu_item`
--

INSERT INTO `kit_menu_item` (`id`, `title`, `alias`, `fk_menu_id`, `kit_order`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `src_area`, `kit_home`, `type`, `tar_area`, `fk_menu_item_id`, `kit_options`, `css`, `class`, `icon`, `add_to_url`, `kit_hidden`, `kit_level`, `hidden`, `kit_lang`) VALUES
(29, 'home', 'home', 29, 0, 0, 0, '2025-02-05 13:48:10', '2016-08-13 03:02:14', 'home', 1, 'app_content', 'home', 0, '{\"id\": \"303\"}', '<style>\r\n.t-main{\r\ndisplay:none\r\n}\r\n</style>', '', '', '', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0631\\u0626\\u064a\\u0633\\u064a\\u0629\"}}'),
(71, 'admin menu', 'mcontent', 0, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_gla', 29, '', '', '', '', '', 0, 0, 0, ''),
(75, 'Content', 'mcontent', 112, 0, 0, 0, '2024-11-11 14:39:42', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_gla', 0, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-indent', '', 0, 0, 0, ''),
(72, 'About Us', 'about_us', 29, 1, 0, 0, '2025-02-05 13:48:34', '2016-08-13 03:02:14', 'home', 0, 'app_content', 'home', 0, '{\"id\": \"304\"}', '', '', '', '', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0645\\u0639\\u0644\\u0648\\u0645\\u0627\\u062a \\u0639\\u0646\\u0627\"}}'),
(73, 'Contact Us', 'contact_us', 29, 6, 0, 0, '2025-02-05 13:53:08', '2016-08-13 03:02:14', 'home', 0, 'app_content', 'home', 0, '{\"id\": \"305\"}', '', '', '', '', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0627\\u062a\\u0635\\u0644 \\u0628\\u0646\\u0627\"}}'),
(74, 'admin menu', 'mcontent', 0, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_gla', 29, '', '', '', '', '', 0, 0, 0, ''),
(77, 'Content', 'content', 112, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_gla', 75, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0, ''),
(79, 'templates', 'templates', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 0, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0, ''),
(80, 'Notifications', 'Notifications', 72, 0, 0, 0, '2024-11-11 14:34:51', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 79, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-message-2', '', 0, 0, 0, ''),
(108, 'DataBase', 'db', 72, 0, 0, 0, '2024-12-01 08:35:26', '2024-12-01 08:23:42', 'ins_admin', 0, 'app_db', 'ins_admin', 102, '', '', '', 'lni lni-database-2', '', 0, 0, 0, ''),
(122, 'Product', 'product', 112, 0, 0, 0, '2025-01-06 09:12:55', '2025-01-06 09:12:55', 'ins_gla', 0, 'app_product', 'ins_gla', 118, '', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(83, 'Options', 'Notifications_Templates', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 82, '', '', '', 'lni  lni-shortcode', '', 0, 0, 0, ''),
(84, 'Emails', 'Notifications_Templates', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 82, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0, ''),
(85, 'Site', 'config', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 0, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0, ''),
(86, 'Config', 'prosettings', 72, 0, 0, 0, '2025-02-06 13:06:55', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_settings', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-gear-1', '', 0, 0, 0, ''),
(88, 'menus', 'menus', 72, 0, 0, 0, '2024-11-11 14:32:29', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_menu', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-buildings-1', '', 0, 0, 0, ''),
(89, 'menus items', 'menus_items', 72, 0, 0, 0, '2024-11-11 14:30:56', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_menus_items', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni-link-2-angular-right lni', '', 0, 0, 0, ''),
(90, 'Templates', 'Templates', 0, 0, 0, 0, '2024-10-07 22:16:06', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_menus_items', 'ins_admin', 0, '{\n    \"id\": \"adasdasdasd77\"\n}', '', '', '', 'lni  lni-apartment', 0, 0, 0, ''),
(97, 'user', 'user', 72, 0, 0, 0, '2024-11-11 14:28:42', '2024-10-23 10:16:59', 'ins_admin', 0, 'app_user', 'ins_admin', 96, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-user-4', '  ', 0, 0, 0, ''),
(98, 'User Group', 'user_group', 72, 0, 0, 0, '2024-11-11 14:29:28', '2024-10-23 10:18:35', 'ins_admin', 0, 'app_user_group', 'ins_admin', 96, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-user-multiple-4', '', 0, 0, 0, ''),
(96, 'Users', 'Users', 72, 0, 0, 0, '2024-11-11 14:40:07', '2024-10-23 10:16:06', 'ins_admin', 0, 'app_user', 'ins_admin', 0, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-user-4', ' ', 0, 0, 0, ''),
(95, 'Widgets', 'widgets', 72, 0, 0, 0, '2024-11-11 14:30:01', '2024-10-21 09:40:17', 'ins_admin', 0, 'app_wdgts', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-dashboard-square-1', ' ', 0, 0, 0, ''),
(100, 'user', '', 0, 0, 0, 0, '2024-11-22 19:25:58', '2024-10-23 16:40:15', '', 0, '', 'ins_admin', 0, '', '', '', '', '', 0, 0, 0, ''),
(101, 'Admin Home', 'admin_home', 71, 0, 0, 0, '2024-11-11 09:34:25', '2024-11-06 13:19:53', 'ins_admin', 1, 'app_home', 'ins_admin', 0, '', '', '', 'lni lni-home', '', 1, 0, 0, ''),
(102, 'Tools', 'tools', 72, 0, 0, 0, NULL, '2024-11-07 10:04:06', 'home', 0, '', 'ins_admin', 0, '', '', '', 'lni lni-app-store', '', 0, 0, 0, ''),
(103, 'options', 'options', 72, 0, 0, 0, '2024-11-11 14:27:37', '2024-11-07 10:29:27', 'ins_admin', 0, 'app_options', 'ins_admin', 102, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-gears-3', '', 0, 0, 0, ''),
(104, 'ui guide', 'uiguide', 72, 0, 0, 0, '2024-11-11 14:27:11', '2024-11-07 10:32:17', 'ins_admin', 0, 'app_ui_guide', 'ins_admin', 102, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-hand-taking-leaf-1', '', 0, 0, 0, ''),
(105, 'email template', 'email_template', 72, 0, 0, 0, '2024-11-11 14:35:43', '2024-11-07 10:32:56', 'ins_admin', 0, 'app_email_template', 'ins_admin', 79, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-message-3-text', '', 0, 0, 0, ''),
(120, 'Blog', 'blog', 112, 0, 0, 0, '2025-01-06 09:12:55', '2025-01-06 09:12:55', 'ins_gla', 0, 'app_blog', 'ins_gla', 119, '', '', '', 'lni  lni-books-2', '', 0, 0, 0, ''),
(121, 'Blog category', 'blog_category', 112, 0, 0, 0, '2025-01-06 08:54:37', '2025-01-06 08:54:37', 'ins_gla', 0, 'app_blog_category', 'ins_gla', 119, '', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(106, 'tags', 'tags', 72, 0, 0, 0, '2024-11-22 17:30:01', '2024-11-22 17:25:54', 'ins_admin', 0, 'app_tags', 'ins_admin', 102, '', '', '', 'lni lni-flag-1', '', 0, 0, 0, ''),
(125, 'Get your plan', 'plan', 29, 4, 0, 0, '2025-02-05 13:51:44', '2025-01-26 12:01:30', 'ins_gla', 0, 'app_cal', 'home', 0, '', '', '', '', '', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0627\\u062d\\u0635\\u0644 \\u0639\\u0644\\u0649 \\u062e\\u0637\\u062a\\u0643\"}}'),
(113, 'Media/News', 'Blogs', 29, 5, 0, 0, '2025-02-05 14:08:04', '2024-12-12 09:33:04', 'ins_gla', 0, 'app_blogs', 'home', 0, '', '', '', '', '', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0623\\u062d\\u062f\\u062b \\u0627\\u0644\\u0623\\u062e\\u0628\\u0627\\u0631 \"}}'),
(123, 'Product category', 'product_category', 71, 0, 0, 0, '2025-02-06 10:36:52', '2025-01-06 08:54:37', 'ins_gla', 0, 'app_product_category', 'ins_gla', 130, '', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(115, 'Shop', 'product', 29, 3, 0, 0, '2025-02-05 13:51:18', '2024-12-12 09:33:04', 'ins_gla', 0, 'app_products', 'home', 0, '', '', '', '', '', 0, 0, 0, '{\"ar\": {\"title\": \"\\u062a\\u0633\\u0648\\u0642\"}}'),
(116, 'Checkout', 'checkout', 29, 0, 0, 0, '2024-12-18 13:40:08', '2024-12-12 09:33:04', 'ins_gla', 0, 'app_checkout', 'home', 0, '', '', '', '', '', 1, 0, 1, ''),
(119, 'Blog', 'mcontent', 112, 0, 0, 0, '2024-11-22 12:52:47', '2024-11-22 12:52:47', 'ins_admin', 0, 'app_mcontent', 'ins_gla', 0, '{     \"id\": \"\" }', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(124, 'image', 'image', 112, 0, 0, 0, '2024-11-22 12:52:47', '2024-11-22 12:52:47', 'ins_gla', 0, 'app_image', 'ins_gla', 75, '', '', '', 'lni  lni-books-2', '', 0, 0, 0, ''),
(126, 'Product Types', 'product_types', 112, 0, 0, 0, NULL, '2025-01-27 13:06:47', 'ins_gla', 0, 'app_product_types', 'ins_gla', 118, '', '', '', 'lni lni-layers-1', '', 0, 0, 0, ''),
(127, 'User data', 'puser', 29, 0, 0, 0, NULL, '2025-01-30 17:16:45', 'ins_gla', 0, 'app_users', 'home', 0, '', '', '', '', '', 1, 0, 0, ''),
(128, 'Orders', 'mcontent', 112, 0, 0, 0, '2024-11-22 12:52:47', '2024-11-22 12:52:47', 'ins_gla', 0, 'app_mcontent', 'ins_gla', 0, '{     \"id\": \"\" }', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(129, 'Order', 'order', 112, 0, 0, 0, '2025-01-06 09:12:55', '2025-01-06 09:12:55', 'ins_gla', 0, 'app_order', 'ins_gla', 128, '', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(130, 'Products', 'mcontent', 112, 0, 0, 0, '2024-11-22 12:52:47', '2024-11-22 12:52:47', 'ins_admin', 0, 'app_mcontent', 'ins_gla', 0, '{     \"id\": \"\" }', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(131, 'Products', 'product', 112, 0, 0, 0, '2025-01-06 09:12:55', '2025-01-06 09:12:55', 'ins_gla', 0, 'app_product', 'ins_gla', 130, '', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(132, 'project settings', 'project_settings', 71, 0, 0, 0, '2025-02-12 13:24:12', '2024-11-22 12:52:47', 'ins_admin', 0, 'app_settings', 'ins_admin', 75, '', '', '', 'lni  lni-books-2', '', 0, 0, 0, ''),
(133, 'Price', 'price', 112, 0, 0, 0, '2025-01-06 09:12:55', '2025-01-06 09:12:55', 'ins_gla', 0, 'app_price', 'ins_gla', 130, '', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(134, 'Partner', 'partner', 29, 4, 0, 0, '2025-02-16 13:50:11', '2025-01-26 12:01:30', 'ins_gla', 0, 'app_partners', 'home', 0, '', '', '', '', '', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0634\\u0631\\u0643\\u0627\\u0624\\u0646\\u0627\"}}'),
(135, 'Gold Bars', 'product', 29, 0, 0, 0, '2025-02-16 10:27:50', '2025-02-13 11:47:56', '-1', 0, '', 'home', 115, '', '', '', '', 'do/filter/fk_product_category_id=1', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0633\\u0628\\u0627\\u0626\\u0643 \\u0627\\u0644\\u0630\\u0647\\u0628\"}}'),
(136, 'Gold Coins', 'product', 29, 0, 0, 0, '2025-02-16 10:27:33', '2025-02-13 11:48:39', '-1', 0, '', 'home', 115, '', '', '', '', 'do/filter/fk_product_category_id=2&types_data=royal', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0639\\u0645\\u0644\\u0627\\u062a \\u0630\\u0647\\u0628\\u064a\\u0629\"}}'),
(137, 'Gifts', 'product', 29, 0, 0, 0, '2025-02-16 10:27:20', '2025-02-13 11:49:44', '-1', 0, '', 'home', 115, '', '', '', '', 'do/filter/fk_product_category_id=3', 0, 0, 0, '{\"ar\": {\"title\": \"\\u0627\\u0644\\u0647\\u062f\\u0627\\u064a\\u0627\"}}'),
(138, 'product types', 'product_types', 112, 0, 0, 0, '2025-01-06 09:12:55', '2025-01-06 09:12:55', 'ins_gla', 0, 'app_product_types', 'ins_gla', 130, '', '', '', 'lni  lni-pen-to-square', '', 0, 0, 0, ''),
(139, 'login', 'login', 29, 4, 0, 0, '2025-02-05 13:51:44', '2025-01-26 12:01:30', 'ins_gla', 0, 'app_login', 'home', 0, '', '', '', '', '', 1, 0, 1, ''),
(140, 'Payment Methods', 'payment_methods', 112, 0, 0, 0, NULL, '2025-02-18 12:32:43', 'ins_gla', 0, 'app_payment_methods', 'ins_gla', 75, '', '', '', 'lni lni-credit-card-multiple', '', 0, 0, 0, ''),
(141, 'Galla Admin Home', 'admin_home', 112, 0, 0, 0, '2024-11-11 09:34:25', '2024-11-06 13:19:53', 'ins_gla', 1, 'app_home', 'ins_gla', 0, '', '', '', 'lni lni-home', '', 1, 0, 0, ''),
(142, 'El Galla Addresses', 'addresses', 112, 0, 0, 0, '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'ins_gla', 0, 'app_address', 'ins_gla', 75, '', '', '', 'lni lni-map-marker-5', '', 0, 0, 0, ''),
(143, 'SMS Template', 'sms_template', 112, 0, 0, 0, NULL, '2025-03-04 19:45:15', 'ins_gla', 0, 'app_sms_template', 'ins_gla', 75, '', '', '', 'lni lni-envelope-1', '', 0, 0, 0, '');

-- --------------------------------------------------------

--
-- Table structure for table `kit_options`
--

CREATE TABLE `kit_options` (
  `id` int(11) NOT NULL,
  `title` text DEFAULT NULL,
  `content` text DEFAULT NULL,
  `kit_deleted` tinyint(4) DEFAULT 0,
  `kit_disabled` tinyint(4) DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_options`
--

INSERT INTO `kit_options` (`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(4, 'settings', '{\r\n\"otp_sms_id\":\"1\"\r\n}', 0, 0, NULL, '2025-03-04 19:46:59'),
(1, 'Weights', '{\r\n	\"1\": {\r\n		\"en\": {\r\n			\"0\": \"-\",\r\n			\"1\": \"1gm\",\r\n			\"5\": \"5gm\",\r\n			\"10\": \"10gm\",\r\n			\"50\": \"50gm\",\r\n			\"100\": \"100gm\",\r\n			\"250\": \"250gm\",\r\n			\"500\": \"500gm\",\r\n			\"1000\": \"1000gm\",\r\n			\"0.25\": \"0.25gm\",\r\n			\"0.5\": \"0.5gm\",\r\n			\"2.5\": \"2.5gm\",\r\n			\"15.55\": \"15.55gm / Half Troy Ounce\",\r\n			\"31.10\": \"One Troy Ounce\",\r\n			\"116.56\": \"10TOLAS\"\r\n		},\r\n		\"ar\": {\r\n			\"0\": \"-\",\r\n			\"1\": \"1 جرام\",\r\n			\"5\": \"5 جرام\",\r\n			\"10\": \"10 جرام\",\r\n			\"50\": \"50 جرام\",\r\n			\"100\": \"100 جرام\",\r\n			\"250\": \"250 جرام\",\r\n			\"500\": \"500 جرام\",\r\n			\"1000\": \"1000 جرام\",\r\n			\"0.25\": \"0.25 جرام\",\r\n			\"0.5\": \"0.5 جرام\",\r\n			\"2.5\": \"2.5 جرام\",\r\n			\"15.55\": \"15.55 جرام / نصف أونصة تروي\",\r\n			\"31.10\": \"أونصة تروي واحدة\",\r\n			\"116.56\": \"10 تولات\"\r\n		}\r\n	},\r\n	\"2\": {\r\n		\"en\": {\r\n			\"0\": \"-\",\r\n			\"1\": \"1gm\",\r\n			\"4\": \"4gm\",\r\n			\"8\": \"8gm\",\r\n			\"40\": \"40gm\"\r\n		},\r\n		\"ar\": {\r\n			\"0\": \"-\",\r\n			\"1\": \"1 جرام\",\r\n			\"2\": \"2 جرام\",\r\n			\"4\": \"4 جرام\",\r\n			\"8\": \"8 جرام\",\r\n			\"40\": \"40 جرام\"\r\n		}\r\n	},\r\n	\"3\": {\r\n		\"en\": {\r\n			\"0\": \"-\",\r\n			\"5\": \"5gm\",\r\n			\"2.5\": \"2.5gm\"\r\n		},\r\n		\"ar\": {\r\n			\"0\": \"-\",\r\n			\"5\": \"5 جرام\",\r\n			\"2.5\": \"2.5 جرام\"\r\n		}\r\n	},\r\n	\"gen\": {\r\n		\"en\": {\r\n			\"0\": \"-\",\r\n			\"1\": \"1gm\",\r\n			\"2\": \"2gm\",\r\n			\"4\": \"4gm\",\r\n			\"5\": \"5gm\",\r\n			\"8\": \"8gm\",\r\n			\"10\": \"10gm\",\r\n			\"40\": \"40gm\",\r\n			\"50\": \"50gm\",\r\n			\"100\": \"100gm\",\r\n			\"250\": \"250gm\",\r\n			\"500\": \"500gm\",\r\n			\"1000\": \"1000gm\",\r\n			\"0.25\": \"0.25gm\",\r\n			\"0.5\": \"0.5gm\",\r\n			\"2.5\": \"2.5gm\",\r\n			\"15.55\": \"15.55gm / Half Troy Ounce\",\r\n			\"31.10\": \"One Troy Ounce\",\r\n			\"116.56\": \"10TOLAS\"\r\n		},\r\n		\"ar\": {\r\n			\"0\": \"-\",\r\n			\"1\": \"1 جرام\",\r\n			\"2\": \"2 جرام\",\r\n			\"4\": \"4 جرام\",\r\n			\"5\": \"5 جرام\",\r\n			\"8\": \"8 جرام\",\r\n			\"10\": \"10 جرام\",\r\n			\"40\": \"40 جرام\",\r\n			\"50\": \"50 جرام\",\r\n			\"100\": \"100 جرام\",\r\n			\"250\": \"250 جرام\",\r\n			\"500\": \"500 جرام\",\r\n			\"1000\": \"1000 جرام\",\r\n			\"0.25\": \"0.25 جرام\",\r\n			\"0.5\": \"0.5 جرام\",\r\n			\"2.5\": \"2.5 جرام\",\r\n			\"15.55\": \"15.55 جرام / نصف أونصة تروي\",\r\n			\"31.10\": \"أونصة تروي واحدة\",\r\n			\"116.56\": \"10 تولات\"\r\n		}\r\n	}\r\n}', 0, 0, '2025-02-19 12:35:18', '2025-02-19 12:19:32');

-- --------------------------------------------------------

--
-- Table structure for table `kit_pro_settings`
--

CREATE TABLE `kit_pro_settings` (
  `id` int(11) NOT NULL,
  `header` text DEFAULT NULL,
  `title` text DEFAULT NULL,
  `page_title` text DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_created` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kit_pro_settings`
--

INSERT INTO `kit_pro_settings` (`id`, `header`, `title`, `page_title`, `kit_deleted`, `kit_disabled`, `kit_created`) VALUES
(1, NULL, 'el galla', 'el galla - ', 0, 0, '2025-02-05 12:29:40');

-- --------------------------------------------------------

--
-- Table structure for table `kit_settings`
--

CREATE TABLE `kit_settings` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `kit_order` tinyint(4) NOT NULL DEFAULT 0,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `kit_status` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_settings`
--

INSERT INTO `kit_settings` (`id`, `title`, `logo`, `kit_order`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_status`) VALUES
(1, '$title_val', '$logo_val', 0, 0, 0, '2024-12-02 11:19:41', '2024-12-02 11:19:41', '$kit_status_val');

-- --------------------------------------------------------

--
-- Table structure for table `kit_sms_template`
--

CREATE TABLE `kit_sms_template` (
  `id` int(11) NOT NULL,
  `title` text DEFAULT NULL,
  `content` text DEFAULT NULL,
  `kit_deleted` tinyint(4) DEFAULT 0,
  `kit_disabled` tinyint(4) DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `kit_lang` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_sms_template`
--

INSERT INTO `kit_sms_template` (`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_lang`) VALUES
(1, 'Send OTP', 'Hello from Elgalla Gold! This is OTP code @(otp)', 0, 0, '2025-03-04 19:51:29', '2025-03-04 19:46:20', '{\"ar\": {\"content\": \"\\u0645\\u0631\\u062d\\u0628\\u064b\\u0627 \\u0645\\u0646 \\u0627\\u0644\\u062c\\u0644\\u0627 \\u0644\\u0644\\u0630\\u0647\\u0628! \\u0647\\u0630\\u0627 \\u0647\\u0648 \\u0631\\u0645\\u0632 \\u0627\\u0644\\u062a\\u062d\\u0642\\u0642 @(otp)\", \"title\": \"\\u0627\\u0631\\u0633\\u0627\\u0644 \\u0631\\u0645\\u0632 \\u0627\\u0644\\u062a\\u062d\\u0642\\u0642\"}}');

-- --------------------------------------------------------

--
-- Table structure for table `kit_tags`
--

CREATE TABLE `kit_tags` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `src_area` varchar(255) NOT NULL,
  `obj` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_tags`
--

INSERT INTO `kit_tags` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `src_area`, `obj`, `color`) VALUES
(1, 'imp', 0, 0, NULL, NULL, '', '', '#71a3fa'),
(2, 'new', 0, 0, NULL, NULL, '', '', '#4be450'),
(3, 'only', 0, 0, NULL, NULL, '', 'kit_menu', '#f97979'),
(9, 'asdfdf', 0, 0, NULL, '2024-11-25 09:19:39', '', 'kit_menu', '#ffae00'),
(8, '78878', 0, 0, '2024-11-24 12:45:12', '2024-11-24 12:42:03', '', '', '#f0de14');

-- --------------------------------------------------------

--
-- Table structure for table `kit_template`
--

CREATE TABLE `kit_template` (
  `id` int(11) NOT NULL,
  `kit_default` tinyint(4) DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `kit_status` varchar(255) DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `src_area` varchar(255) NOT NULL,
  `sys_properties` text NOT NULL,
  `tar_area` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_template`
--

INSERT INTO `kit_template` (`id`, `kit_default`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_status`, `type`, `src_area`, `sys_properties`, `tar_area`, `title`) VALUES
(5, 1, 0, 0, '2021-09-23 12:41:58', '2016-11-04 20:31:48', '[]', 'tmp_admin_style', 'ins_admin', '{\"menu_type\":\"smenu\",\"body_background\":\"#f1f1f1\",\"body_color\":\"#333\",\"title_bar_backgoruntd\":\"#f8f9fb\",\"title_bar_color\":\"#333\",\"input_backgoruntd\":\"#f8f9fb\",\"input_color\":\"#333\",\"side_background\":\"#1a3048\",\"sub_side_background\":\"#131f2b\",\"top_bar_background\":\"#e3eaf4\",\"table_header_background\":\"#becae2\",\"\":\"nmenu\",\"style\":\"ins_style_insya\",\"width\":\"ins_container\"}', 'ins_admin', ''),
(10, 1, 0, 0, NULL, '2020-02-03 23:25:40', '[\"en\"]', 'gla_style', 'ins_gla ', '', 'home', ''),
(11, 1, 0, 0, '2024-12-18 13:56:00', '2024-12-18 13:56:00', '[]', 'gla_admin_style', 'ins_gla ', '{}', 'ins_gla', 'title');

-- --------------------------------------------------------

--
-- Table structure for table `kit_user`
--

CREATE TABLE `kit_user` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `user_name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `mobile` varchar(14) NOT NULL,
  `otp` varchar(10) NOT NULL,
  `image` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `groups` varchar(255) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email_status` varchar(20) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_user`
--

INSERT INTO `kit_user` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `user_name`, `email`, `mobile`, `otp`, `image`, `password`, `groups`, `first_name`, `last_name`, `email_status`) VALUES
(1, 'ismail mohamed', 0, 0, '2025-03-03 12:00:35', NULL, 'ismail mohamed', 'empcland@gmail.com', '1', '', 'users/20241125142835__wire.png', '4a16fe56b822500a67d470c9d0d0af7f5343eec5bd59c9d5e6d06c73680d2474', '2', 'ismail', 'mohamed', 'verified'),
(5, 'hossam ahmed', 0, 0, NULL, '2025-03-04 20:30:02', 'hossam ahmed', 'hossam@gmail.com', '01123881630', '', '', '4a16fe56b822500a67d470c9d0d0af7f5343eec5bd59c9d5e6d06c73680d2474', '4', 'hossam', 'ahmed', ''),
(4, 'Hesham Ehab', 0, 0, '0000-00-00 00:00:00', NULL, 'hesham ehab', 'hesham@gmail.com', '2', '', 'users/20241125142835__wire.png', '4a16fe56b822500a67d470c9d0d0af7f5343eec5bd59c9d5e6d06c73680d2474', '3', 'hesham', 'ehab', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `kit_user_group`
--

CREATE TABLE `kit_user_group` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `tar_area` varchar(255) NOT NULL,
  `apps_permissions` text NOT NULL,
  `custom_permissions` text NOT NULL,
  `all_permissions` tinyint(4) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_user_group`
--

INSERT INTO `kit_user_group` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `tar_area`, `apps_permissions`, `custom_permissions`, `all_permissions`) VALUES
(2, 'admin', 0, 0, '2024-11-04 14:39:15', '2024-10-23 16:41:24', 'ins_admin', '[{\"menu\": \"71\", \"app\": \"75\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163500\"}, {\"menu\": \"72\", \"app\": \"98\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163737\"}, {\"menu\": \"72\", \"app\": \"97\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163835\"}, {\"menu\": \"72\", \"app\": \"96\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163911\"}]', '[{\"name\": \"asdasd\", \"level\": \"844\", \"id\": \"20241024140637\"}, {\"name\": \"asdasdasd\", \"level\": \"010\", \"id\": \"20241024141944\"}]', 1),
(3, 'gla admin', 0, 0, '2024-11-04 14:39:15', '2024-10-23 16:41:24', 'ins_gla', '', '', 1),
(4, 'gla user', 0, 0, '2024-11-04 14:39:15', '2024-10-23 16:41:24', 'home', '', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `kit_wdgts`
--

CREATE TABLE `kit_wdgts` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `data` text DEFAULT NULL,
  `kit_order` tinyint(4) NOT NULL DEFAULT 0,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL,
  `kit_status` varchar(255) DEFAULT NULL,
  `view_all` tinyint(4) NOT NULL DEFAULT 0,
  `css` text DEFAULT NULL,
  `class` text DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `type` varchar(255) NOT NULL,
  `view_in` text NOT NULL,
  `src_area` varchar(255) NOT NULL,
  `tar_area` varchar(255) NOT NULL,
  `kit_options` text NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `kit_wdgts`
--

INSERT INTO `kit_wdgts` (`id`, `title`, `data`, `kit_order`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_status`, `view_all`, `css`, `class`, `position`, `type`, `view_in`, `src_area`, `tar_area`, `kit_options`) VALUES
(10, 'footer', NULL, 2, 0, 0, '2016-12-14 15:52:29', '2016-10-07 01:56:12', NULL, 0, '', 'about,contect', 'bottom', 'wdg_content', 'about', 'home', 'home', ''),
(8, 'main menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', 'ins-col-12', 'menu', 'wdg_menu', '', 'home', 'home', '{\"id\":\"29\"}'),
(12, 'admin menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', '', 'menu', 'wdg_menu', '', 'ins_admin', 'ins_admin', '{\"id\":\"71\"}'),
(13, 'admin settings menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', 'ins-col-12', 'settings', 'wdg_menu', '', 'ins_admin', 'ins_admin', '{\"id\":\"72\"}'),
(15, 'copy right', NULL, 7, 0, 0, '2024-11-22 13:43:40', '2024-11-22 13:17:34', NULL, 0, '', 'ins-col-12 ins-text-center', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"209\"}'),
(16, 'footer logo', NULL, 0, 0, 0, '2025-01-07 12:11:46', '2024-11-22 13:42:39', NULL, 1, '', 'ins-col-4', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"299\"}'),
(17, 'Visit us', NULL, 0, 0, 0, '2025-01-07 12:13:22', '2024-11-22 13:42:54', NULL, 1, '', 'ins-col-4', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"294\"}'),
(18, 'Discover', NULL, 3, 0, 0, '2025-01-07 12:23:54', '2024-11-22 13:42:55', NULL, 1, '', 'ins-col-2', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"296\"}'),
(22, 'Resources', NULL, 3, 0, 0, '2025-01-07 12:23:10', '2025-01-07 12:22:00', NULL, 1, '', 'ins-col-2', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"295\"}'),
(23, 'Quality Assurance', NULL, 0, 1, 0, '2025-01-07 14:47:54', '2025-01-07 14:25:13', NULL, 0, '', 'ins-col-12', 'top', 'wdg_content', '', 'home', 'home', '{\"id\": \"300\"}'),
(24, 'Quality Assurance', NULL, 0, 1, 0, '2025-01-07 14:47:54', '2025-01-07 14:29:22', NULL, 0, '', 'ins-col-12', 'top', 'wdg_content', '', 'home', 'home', '{\"id\": \"300\"}'),
(25, 'Quality Assurance', NULL, 0, 1, 0, '2025-01-07 14:47:54', '2025-01-07 14:30:00', NULL, 0, '', 'ins-col-12', 'top', 'wdg_content', '', 'home', 'home', '{\"id\": \"300\"}'),
(26, 'partners', NULL, 4, 0, 0, '2025-01-09 10:34:56', '2025-01-07 14:30:02', NULL, 0, '', 'ins-col-12', 'top', 'wdg_content', 'home', 'home', 'home', '{\"id\": \"302\"}'),
(28, 'see how ', NULL, 3, 0, 0, '2025-01-09 10:34:44', '2025-01-07 14:32:39', NULL, 0, '', 'ins-col-12', 'top', 'wdg_content', 'home', 'home', 'home', '{\"id\": \"301\"}'),
(43, 'top', NULL, 0, 0, 0, NULL, '2025-01-09 10:44:25', NULL, 0, '', NULL, 'top', 'wdg_slideshow', 'home', 'ins_gla', 'home', '{\"id\": \"0\"}'),
(42, 'store', NULL, 2, 0, 0, '2025-01-09 10:34:29', '2025-01-09 10:31:16', NULL, 0, '', 'ins-primary-bg', 'top', 'wdg_products', 'home', 'ins_gla', 'home', ''),
(41, 'legacy', NULL, 1, 0, 0, '2025-01-09 10:34:09', '2025-01-09 10:30:44', NULL, 0, '', '', 'top', 'wdg_legacy', 'home', 'ins_gla', 'home', ''),
(40, 'blog', NULL, 5, 0, 0, '2025-01-09 10:35:16', '2025-01-09 10:30:10', NULL, 0, '', '', 'top', 'wdg_blog', 'home', 'ins_gla', 'home', '{\"id\": \"0\"}'),
(37, 'Quality Assurance', NULL, 0, 0, 0, NULL, '2025-01-07 14:47:13', NULL, 0, '', 'ins-col-12', 'top', 'wdg_content', 'home', 'home', 'home', '{\"id\": \"300\"}'),
(44, 'Ticker', NULL, 0, 0, 0, NULL, '2025-02-16 14:54:41', NULL, 0, '', 'ins-col-12', 'ticker', 'wdg_ticker', 'home', 'ins_gla', 'home', ''),
(45, 'Galla settings menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', 'ins-col-12', 'settings', 'wdg_menu', '', 'ins_admin', 'ins_gla', '{\"id\":\"113\"}'),
(46, 'Galla Admin Menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', '', 'menu', 'wdg_menu', '', 'ins_admin', 'ins_gla', '{\"id\":\"112\"}');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `gla_address`
--
ALTER TABLE `gla_address`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_blog`
--
ALTER TABLE `gla_blog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_blog_category`
--
ALTER TABLE `gla_blog_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_login_temp`
--
ALTER TABLE `gla_login_temp`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_order`
--
ALTER TABLE `gla_order`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_order_item`
--
ALTER TABLE `gla_order_item`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_payment_methods`
--
ALTER TABLE `gla_payment_methods`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_price`
--
ALTER TABLE `gla_price`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_product`
--
ALTER TABLE `gla_product`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_product_category`
--
ALTER TABLE `gla_product_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_product_types`
--
ALTER TABLE `gla_product_types`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `gla_user_address`
--
ALTER TABLE `gla_user_address`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_content`
--
ALTER TABLE `kit_content`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_email_template`
--
ALTER TABLE `kit_email_template`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_image`
--
ALTER TABLE `kit_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_image_category`
--
ALTER TABLE `kit_image_category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_menu`
--
ALTER TABLE `kit_menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_menu_item`
--
ALTER TABLE `kit_menu_item`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_options`
--
ALTER TABLE `kit_options`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_pro_settings`
--
ALTER TABLE `kit_pro_settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_settings`
--
ALTER TABLE `kit_settings`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_sms_template`
--
ALTER TABLE `kit_sms_template`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_tags`
--
ALTER TABLE `kit_tags`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_template`
--
ALTER TABLE `kit_template`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_user`
--
ALTER TABLE `kit_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_user_group`
--
ALTER TABLE `kit_user_group`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kit_wdgts`
--
ALTER TABLE `kit_wdgts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `gla_address`
--
ALTER TABLE `gla_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `gla_blog`
--
ALTER TABLE `gla_blog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `gla_blog_category`
--
ALTER TABLE `gla_blog_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `gla_login_temp`
--
ALTER TABLE `gla_login_temp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `gla_order`
--
ALTER TABLE `gla_order`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `gla_order_item`
--
ALTER TABLE `gla_order_item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `gla_payment_methods`
--
ALTER TABLE `gla_payment_methods`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `gla_price`
--
ALTER TABLE `gla_price`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `gla_product`
--
ALTER TABLE `gla_product`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `gla_product_category`
--
ALTER TABLE `gla_product_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `gla_product_types`
--
ALTER TABLE `gla_product_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `gla_user_address`
--
ALTER TABLE `gla_user_address`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `kit_content`
--
ALTER TABLE `kit_content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=306;

--
-- AUTO_INCREMENT for table `kit_email_template`
--
ALTER TABLE `kit_email_template`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `kit_image`
--
ALTER TABLE `kit_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `kit_image_category`
--
ALTER TABLE `kit_image_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `kit_menu`
--
ALTER TABLE `kit_menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=114;

--
-- AUTO_INCREMENT for table `kit_menu_item`
--
ALTER TABLE `kit_menu_item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=144;

--
-- AUTO_INCREMENT for table `kit_options`
--
ALTER TABLE `kit_options`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `kit_pro_settings`
--
ALTER TABLE `kit_pro_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `kit_settings`
--
ALTER TABLE `kit_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `kit_sms_template`
--
ALTER TABLE `kit_sms_template`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `kit_tags`
--
ALTER TABLE `kit_tags`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `kit_template`
--
ALTER TABLE `kit_template`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `kit_user`
--
ALTER TABLE `kit_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `kit_user_group`
--
ALTER TABLE `kit_user_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `kit_wdgts`
--
ALTER TABLE `kit_wdgts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
