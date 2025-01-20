-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 05 ديسمبر 2024 الساعة 11:09
-- إصدار الخادم: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `py_insya`
--

-- --------------------------------------------------------

--
-- بنية الجدول `jmnbnbnmnbm`
--

CREATE TABLE `jmnbnbnmnbm` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `asdasd` text DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `jmnbnbnmnbm`
--

INSERT INTO `jmnbnbnmnbm` (`id`, `title`, `asdasd`, `kit_deleted`, `kit_disabled`, `kit_modified`) VALUES
(2, '8888', '$asdasd_val', 0, 0, '2024-12-02 13:34:01');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_content`
--

CREATE TABLE `kit_content` (
  `id` int(11) NOT NULL,
  `title` text DEFAULT NULL,
  `content` text DEFAULT NULL,
  `kit_deleted` tinyint(4) DEFAULT 0,
  `kit_disabled` tinyint(4) DEFAULT 0,
  `kit_modified` datetime DEFAULT NULL,
  `kit_created` datetime DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- إرجاع أو استيراد بيانات الجدول `kit_content`
--

INSERT INTO `kit_content` (`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(208, 'body', '<div class=\"ins-flex ins-card ins-padding-xl \">\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n<br/>\r\n<br/>\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n\r\n<br/>\r\n<br/>\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n<br/>\r\n<br/>\r\n<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\r\n</div>\r\n\r\n\r\n\r\n</div>', 0, 0, '2024-11-22 12:58:05', '2022-05-25 16:49:24'),
(209, 'copyright', '<div class=\"ins-line ins-col-12\"></div>\r\n<div  sclass=\"ins-col-12 ins-font-m ins-text-center\">Copyright 25 @Escapes</div>', 0, 0, '2024-11-22 13:46:32', '2022-05-25 16:49:24'),
(211, 'slide show', '<div style=\'height: 340px;\' class=\"ins-col-12 img-bg-air  ins-flex-center\">\r\n   <div style=\"position: relative;\" class=\" serch_cont ins_mod_search  ins-container\">\r\n<h2 class=\'ins-strong ins-primary-color\'>CG Marketplace by the World\'s Best 3D Artists </h2>\r\n<h4 class=\'ins-strong\'>Find the exact right 3D content for your needs, including AR/VR, gaming, advertising, entertainment and 3D printing\r\n\r\n</h4 >\r\n\r\n    <div class=\" ui_row  ins-col-12   ui_parent ui_parent ui_search \">\r\n        <div>\r\n            <div class=\"ui_value ins-form-input  \">\r\n                <i class=\"fas fa-search\" style=\"margin: 7px;\"></i>\r\n                <input class=\"   ins_ui_input ins_ui_input  ins-form-input     search\" placeholder=\"SearchProducts\" value=\"\" name=\"search\">\r\n            </div>\r\n            <button class=\"search ins_search_btn ins-primary ins-button\" style=\"position: absolute;right: 10px;top: 8px;width: 120px;\" name=\"button\"> search</button>\r\n        </div>\r\n    </div>\r\n</div>\r\n\r\n\r\n</div>\r\n<div style=\'height: 60px;\' class=\"ins-col-12  ins-flex\">\r\n    <div class=\"ins-container sub-menu ins-flex-space-between\">\r\n        <ul class=\"ins-col-12 ins-flex-center ins-title-m\">\r\n            <li class=\"ins-padding-m ins-strong \"><a href=\"/home/\" title=\"Trending\"><span>Blender Tutorials</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/home/\" title=\"Trending\"><span>houdini Tutorials</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/home/\" title=\"Trending\"><span>Trending</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/about/\" data-title=\"collections\"><span>collections</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/Products/\" data-title=\"Products\"><span>3d Moduels</span></a></li>\r\n            <li class=\"ins-padding-m ins-strong\"><a href=\"/Products/\" data-title=\"Products\"><span>Basemeshes</span></a></li>\r\n        </ul>\r\n    </div>\r\n</div>', 0, 0, '2023-04-13 00:36:26', '2023-04-13 00:01:11'),
(293, 'footer', '<div class=\"ins-col-12 ins-strong ins-title-m\"> Lorem Ipsum  Title </div>\r\n<div class=\"ins-col-12\">\r\nLorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. \r\n</div>\r\n\r\n', 0, 0, '2024-11-22 13:45:04', '2024-11-22 13:41:17'),
(294, '$title_val', '$ dasda', 0, 0, '2024-12-02 11:04:27', '2024-12-02 11:04:27'),
(295, '$title_val', '$content_val', 0, 0, '2024-12-02 11:19:18', '2024-12-02 11:19:18'),
(296, 'address content', 'dsfsd asdsa asdasd', 0, 0, NULL, '2024-12-04 09:54:34');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_email_template`
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
-- بنية الجدول `kit_menu`
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
-- إرجاع أو استيراد بيانات الجدول `kit_menu`
--

INSERT INTO `kit_menu` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `src_area`, `tar_area`, `kit_tags`) VALUES
(29, 'main menu', 0, 0, '2024-11-24 12:42:46', '2016-08-13 03:02:14', 'home', 'home', '1'),
(71, 'admin menu', 0, 0, '2024-11-25 09:19:42', '2016-08-13 03:02:14', 'ins_admin', 'ins_admin', '2,8,3,9'),
(72, 'admin settings menu', 0, 0, '2024-11-21 12:34:03', '2016-08-13 03:02:14', 'ins_admin', 'ins_admin', '2,3,1'),
(79, 'admin settings menu', 0, 0, '2024-11-21 12:34:03', '2024-11-25 10:25:34', 'ins_admin', 'ins_admin', '2,3,1');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_menu_item`
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
  `hidden` tinyint(4) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- إرجاع أو استيراد بيانات الجدول `kit_menu_item`
--

INSERT INTO `kit_menu_item` (`id`, `title`, `alias`, `fk_menu_id`, `kit_order`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `src_area`, `kit_home`, `type`, `tar_area`, `fk_menu_item_id`, `kit_options`, `css`, `class`, `icon`, `add_to_url`, `kit_hidden`, `kit_level`, `hidden`) VALUES
(29, 'home', 'home', 29, 0, 0, 0, '2024-11-22 12:52:47', '2016-08-13 03:02:14', 'home', 1, 'app_content', 'home', 0, '{\"id\": \"208\"}', '', '', '', '', 0, 0, 0),
(71, 'admin menu', 'mcontent', 0, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 29, '', '', '', '', '', 0, 0, 0),
(75, 'Content', 'mcontent', 71, 0, 0, 0, '2024-11-11 14:39:42', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 0, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-indent', '', 0, 0, 0),
(72, 'about', 'about', 29, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'home', 0, 'app_content', 'home', 29, '{\"id\":\"199\"}', '', '', '', '', 0, 0, 0),
(73, 'contect us', 'contect ', 29, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'home', 0, 'app_content', 'home', 29, '{\"id\":\"199\"}', '', '', '', '', 0, 0, 0),
(74, 'admin menu', 'mcontent', 0, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 29, '', '', '', '', '', 0, 0, 0),
(77, 'Content', 'mcontent', 71, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 75, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0),
(79, 'templates', 'templates', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 0, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0),
(80, 'Notifications', 'Notifications', 72, 0, 0, 0, '2024-11-11 14:34:51', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 79, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-message-2', '', 0, 0, 0),
(108, 'DataBase', 'db', 72, 0, 0, 0, '2024-12-01 08:35:26', '2024-12-01 08:23:42', 'ins_admin', 0, 'app_db', 'ins_admin', 102, '', '', '', 'lni lni-database-2', '', 0, 0, 0),
(109, 'Face Book', 'fbook', 71, 0, 0, 0, '2024-12-02 14:23:15', '2024-12-02 14:21:10', 'ins_admin', 0, 'app_book', 'ins_admin', 75, '{\"id\": \"dfgdfgdfgdfgdfg\"}', '', '', '', '', 0, 0, 0),
(83, 'Options', 'Notifications_Templates', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 82, '', '', '', 'lni  lni-shortcode', '', 0, 0, 0),
(84, 'Emails', 'Notifications_Templates', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 82, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0),
(85, 'Site', 'config', 72, 0, 0, 0, '2016-08-13 04:10:23', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 0, '', '', '', 'lni  lni-pencil-alt', '', 0, 0, 0),
(86, 'Config', 'Config', 72, 0, 0, 0, '2024-11-11 14:33:49', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_mcontent', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-gear-1', '', 0, 0, 0),
(88, 'menus', 'menus', 72, 0, 0, 0, '2024-11-11 14:32:29', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_menu', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-buildings-1', '', 0, 0, 0),
(89, 'menus items', 'menus_items', 72, 0, 0, 0, '2024-11-11 14:30:56', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_menus_items', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni-link-2-angular-right lni', '', 0, 0, 0),
(90, 'Templates', 'Templates', 0, 0, 0, 0, '2024-10-07 22:16:06', '2016-08-13 03:02:14', 'ins_admin', 0, 'app_menus_items', 'ins_admin', 0, '{\n    \"id\": \"adasdasdasd77\"\n}', '', '', '', 'lni  lni-apartment', 0, 0, 0),
(97, 'user', 'user', 72, 0, 0, 0, '2024-11-11 14:28:42', '2024-10-23 10:16:59', 'ins_admin', 0, 'app_user', 'ins_admin', 96, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-user-4', '  ', 0, 0, 0),
(98, 'User Group', 'user_group', 72, 0, 0, 0, '2024-11-11 14:29:28', '2024-10-23 10:18:35', 'ins_admin', 0, 'app_user_group', 'ins_admin', 96, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-user-multiple-4', '', 0, 0, 0),
(96, 'Users', 'Users', 72, 0, 0, 0, '2024-11-11 14:40:07', '2024-10-23 10:16:06', 'ins_admin', 0, 'app_user', 'ins_admin', 0, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-user-4', ' ', 0, 0, 0),
(95, 'Widgets', 'widgets', 72, 0, 0, 0, '2024-11-11 14:30:01', '2024-10-21 09:40:17', 'ins_admin', 0, 'app_wdgts', 'ins_admin', 85, '{\n    \"id\": \"\"\n}', '', '', 'lni  lni-dashboard-square-1', ' ', 0, 0, 0),
(100, 'user', '', 0, 0, 0, 0, '2024-11-22 19:25:58', '2024-10-23 16:40:15', '', 0, '', 'ins_admin', 0, '', '', '', '', '', 0, 0, 0),
(101, 'Admin Home', 'admin_home', 71, 0, 0, 0, '2024-11-11 09:34:25', '2024-11-06 13:19:53', 'ins_admin', 1, 'app_home', 'ins_admin', 0, '', '', '', 'lni lni-home', '', 1, 0, 0),
(102, 'Tools', 'tools', 72, 0, 0, 0, NULL, '2024-11-07 10:04:06', 'home', 0, '', 'ins_admin', 0, '', '', '', 'lni lni-app-store', '', 0, 0, 0),
(103, 'options', 'options', 72, 0, 0, 0, '2024-11-11 14:27:37', '2024-11-07 10:29:27', 'ins_admin', 0, 'app_options', 'ins_admin', 102, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-gears-3', '', 0, 0, 0),
(104, 'ui guide', 'uiguide', 72, 0, 0, 0, '2024-11-11 14:27:11', '2024-11-07 10:32:17', 'ins_admin', 0, 'app_ui_guide', 'ins_admin', 102, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-hand-taking-leaf-1', '', 0, 0, 0),
(105, 'email template', 'email_template', 72, 0, 0, 0, '2024-11-11 14:35:43', '2024-11-07 10:32:56', 'ins_admin', 0, 'app_email_template', 'ins_admin', 79, '{\n    \"id\": \"\"\n}', '', '', 'lni lni-message-3-text', '', 0, 0, 0),
(110, 'ddddd', 'ddddd', 71, 0, 0, 0, NULL, '2024-12-02 14:23:48', 'ins_admin', 0, 'app_book', 'ins_admin', 75, '{\"id\": \"77777777777\"}', '', '', '', '', 0, 0, 0),
(106, 'tags', 'tags', 72, 0, 0, 0, '2024-11-22 17:30:01', '2024-11-22 17:25:54', 'ins_admin', 0, 'app_tags', 'ins_admin', 102, '', '', '', 'lni lni-flag-1', '', 0, 0, 0);

-- --------------------------------------------------------

--
-- بنية الجدول `kit_options`
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
-- إرجاع أو استيراد بيانات الجدول `kit_options`
--

INSERT INTO `kit_options` (`id`, `title`, `content`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(1, 'fsdf', '{\r\n  \r\n \"asdasdas\":\"ddddd\" \r\n}', 0, 0, '2024-11-07 14:11:22', '2024-11-07 11:26:06');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_settings`
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
-- إرجاع أو استيراد بيانات الجدول `kit_settings`
--

INSERT INTO `kit_settings` (`id`, `title`, `logo`, `kit_order`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_status`) VALUES
(1, '$title_val', '$logo_val', 0, 0, 0, '2024-12-02 11:19:41', '2024-12-02 11:19:41', '$kit_status_val');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_tags`
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
-- إرجاع أو استيراد بيانات الجدول `kit_tags`
--

INSERT INTO `kit_tags` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `src_area`, `obj`, `color`) VALUES
(1, 'imp', 0, 0, NULL, NULL, '', '', '#71a3fa'),
(2, 'new', 0, 0, NULL, NULL, '', '', '#4be450'),
(3, 'only', 0, 0, NULL, NULL, '', 'kit_menu', '#f97979'),
(9, 'asdfdf', 0, 0, NULL, '2024-11-25 09:19:39', '', 'kit_menu', '#ffae00'),
(8, '78878', 0, 0, '2024-11-24 12:45:12', '2024-11-24 12:42:03', '', '', '#f0de14');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_template`
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
-- إرجاع أو استيراد بيانات الجدول `kit_template`
--

INSERT INTO `kit_template` (`id`, `kit_default`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_status`, `type`, `src_area`, `sys_properties`, `tar_area`, `title`) VALUES
(5, 1, 0, 0, '2021-09-23 12:41:58', '2016-11-04 20:31:48', '[]', 'tmp_admin_style', 'ins_admin', '{\"menu_type\":\"smenu\",\"body_background\":\"#f1f1f1\",\"body_color\":\"#333\",\"title_bar_backgoruntd\":\"#f8f9fb\",\"title_bar_color\":\"#333\",\"input_backgoruntd\":\"#f8f9fb\",\"input_color\":\"#333\",\"side_background\":\"#1a3048\",\"sub_side_background\":\"#131f2b\",\"top_bar_background\":\"#e3eaf4\",\"table_header_background\":\"#becae2\",\"\":\"nmenu\",\"style\":\"ins_style_insya\",\"width\":\"ins_container\"}', 'ins_admin', ''),
(10, 1, 0, 0, NULL, '2020-02-03 23:25:40', '[\"en\"]', 'tmp_style', 'home', '', 'home', '');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_user`
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
  `image` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `groups` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- إرجاع أو استيراد بيانات الجدول `kit_user`
--

INSERT INTO `kit_user` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `user_name`, `email`, `image`, `password`, `groups`) VALUES
(1, 'ismail', 0, 0, '2024-11-25 12:30:51', NULL, '', 'empcland@gmail.com', 'users/20241125142835__wire.png', '4a16fe56b822500a67d470c9d0d0af7f5343eec5bd59c9d5e6d06c73680d2474', '2'),
(2, 'dasdasd', 0, 0, NULL, '2024-11-25 12:32:26', '', 'asdasd', 'users/20241125143214__wire.png', '', '');

-- --------------------------------------------------------

--
-- بنية الجدول `kit_user_group`
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
-- إرجاع أو استيراد بيانات الجدول `kit_user_group`
--

INSERT INTO `kit_user_group` (`id`, `title`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `tar_area`, `apps_permissions`, `custom_permissions`, `all_permissions`) VALUES
(2, 'admin', 0, 0, '2024-11-04 14:39:15', '2024-10-23 16:41:24', 'ins_admin', '[{\"menu\": \"71\", \"app\": \"75\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163500\"}, {\"menu\": \"72\", \"app\": \"98\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163737\"}, {\"menu\": \"72\", \"app\": \"97\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163835\"}, {\"menu\": \"72\", \"app\": \"96\", \"add\": \"1\", \"edit\": \"1\", \"delete\": \"1\", \"level\": \"0\", \"id\": \"20241104163911\"}]', '[{\"name\": \"asdasd\", \"level\": \"844\", \"id\": \"20241024140637\"}, {\"name\": \"asdasdasd\", \"level\": \"010\", \"id\": \"20241024141944\"}]', 1);

-- --------------------------------------------------------

--
-- بنية الجدول `kit_wdgts`
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
-- إرجاع أو استيراد بيانات الجدول `kit_wdgts`
--

INSERT INTO `kit_wdgts` (`id`, `title`, `data`, `kit_order`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`, `kit_status`, `view_all`, `css`, `class`, `position`, `type`, `view_in`, `src_area`, `tar_area`, `kit_options`) VALUES
(10, 'footer', NULL, 2, 0, 0, '2016-12-14 15:52:29', '2016-10-07 01:56:12', NULL, 0, '', 'about,contect', 'bottom', 'wdg_content', 'about', 'home', 'home', ''),
(8, 'main menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', 'ins-col-12', 'menu', 'wdg_menu', '', 'home', 'home', '{\"id\":\"29\"}'),
(12, 'admin menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', '', 'menu', 'wdg_menu', '', 'ins_admin', 'ins_admin', '{\"id\":\"71\"}'),
(13, 'admin settings menu', NULL, 1, 0, 0, '2019-03-05 15:54:02', '2016-09-18 23:32:41', '[]', 1, '', 'ins-col-12', 'settings', 'wdg_menu', '', 'ins_admin', 'ins_admin', '{\"id\":\"72\"}'),
(14, 'dasdasd', NULL, 1, 0, 0, '2024-10-21 12:04:17', '2024-10-21 11:54:12', NULL, 0, 'dasd', 'adas', NULL, 'wdg_menu', '', 'ins_admin', 'home', '{\n    \"id\": \"asdasdas77\"\n}'),
(15, 'copy right', NULL, 7, 0, 0, '2024-11-22 13:43:40', '2024-11-22 13:17:34', NULL, 1, '', 'ins-col-12 ins-text-center', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"209\"}'),
(16, 'footer aa ', NULL, 0, 0, 0, '2024-12-04 10:11:24', '2024-11-22 13:42:39', NULL, 1, '', 'ins-col-3 ins-primary ins-padding-5xl', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"293\"}'),
(17, 'footer aa ', NULL, 0, 0, 0, '2024-12-04 10:05:26', '2024-11-22 13:42:54', NULL, 1, '', 'ins-col-3', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"293\"}'),
(18, 'footer a', NULL, 4, 0, 0, '2024-12-04 10:06:44', '2024-11-22 13:42:55', NULL, 1, '', 'ins-col-grow', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"293\"}'),
(19, 'vist us ', NULL, 0, 0, 0, '2024-12-04 10:05:16', '2024-12-04 10:01:31', NULL, 1, '', 'ins-col-3', 'footer', 'wdg_content', '', 'home', 'home', '{\"id\": \"296\"}');

-- --------------------------------------------------------

--
-- بنية الجدول `table_name`
--

CREATE TABLE `table_name` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `table_name`
--

INSERT INTO `table_name` (`id`, `title`) VALUES
(4, 'dasdasd'),
(9, '$title_val');

-- --------------------------------------------------------

--
-- بنية الجدول `tt`
--

CREATE TABLE `tt` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `des` text DEFAULT NULL,
  `kit_deleted` tinyint(4) NOT NULL DEFAULT 0,
  `kit_disabled` tinyint(4) NOT NULL DEFAULT 0,
  `kit_modified` datetime NOT NULL,
  `kit_created` datetime NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- إرجاع أو استيراد بيانات الجدول `tt`
--

INSERT INTO `tt` (`id`, `title`, `des`, `kit_deleted`, `kit_disabled`, `kit_modified`, `kit_created`) VALUES
(3, '$title_val', '$des_val', 0, 0, '2024-12-02 12:14:57', '2024-12-02 12:14:57'),
(4, '$title_val', '$des_val', 0, 0, '2024-12-02 12:14:58', '2024-12-02 12:14:58'),
(6, '$title_val', '$des_val', 0, 0, '2024-12-02 12:15:50', '2024-12-02 12:15:50');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `jmnbnbnmnbm`
--
ALTER TABLE `jmnbnbnmnbm`
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
-- Indexes for table `kit_settings`
--
ALTER TABLE `kit_settings`
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
-- Indexes for table `table_name`
--
ALTER TABLE `table_name`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tt`
--
ALTER TABLE `tt`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `jmnbnbnmnbm`
--
ALTER TABLE `jmnbnbnmnbm`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `kit_content`
--
ALTER TABLE `kit_content`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=297;

--
-- AUTO_INCREMENT for table `kit_email_template`
--
ALTER TABLE `kit_email_template`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `kit_menu`
--
ALTER TABLE `kit_menu`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;

--
-- AUTO_INCREMENT for table `kit_menu_item`
--
ALTER TABLE `kit_menu_item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT for table `kit_options`
--
ALTER TABLE `kit_options`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `kit_settings`
--
ALTER TABLE `kit_settings`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `kit_user`
--
ALTER TABLE `kit_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `kit_user_group`
--
ALTER TABLE `kit_user_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `kit_wdgts`
--
ALTER TABLE `kit_wdgts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT for table `table_name`
--
ALTER TABLE `table_name`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;

--
-- AUTO_INCREMENT for table `tt`
--
ALTER TABLE `tt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
