/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50173
Source Host           : localhost:3306
Source Database       : modal

Target Server Type    : MYSQL
Target Server Version : 50173
File Encoding         : 65001

Date: 2015-04-30 18:21:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `menu`
-- ----------------------------
DROP TABLE IF EXISTS `menu`;
CREATE TABLE `menu` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `pid` bigint(20) DEFAULT NULL,
  `description` varchar(150) DEFAULT NULL,
  `pageurl` varchar(255) DEFAULT NULL,
  `type` int(10) NOT NULL,
  `sort` int(10) NOT NULL,
  `icon` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of menu
-- ----------------------------

-- ----------------------------
-- Table structure for `permission`
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `permission` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `available` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_permission_permission` (`permission`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of permission
-- ----------------------------

-- ----------------------------
-- Table structure for `role`
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `role` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `available` bit(1) DEFAULT b'0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_role_role` (`role`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role
-- ----------------------------
INSERT INTO `role` VALUES ('1', 'normal', '1', '');
INSERT INTO `role` VALUES ('2', 'add', '2', '');

-- ----------------------------
-- Table structure for `role_menu`
-- ----------------------------
DROP TABLE IF EXISTS `role_menu`;
CREATE TABLE `role_menu` (
  `role_id` bigint(20) NOT NULL,
  `menu_id` bigint(20) NOT NULL,
  PRIMARY KEY (`role_id`,`menu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role_menu
-- ----------------------------

-- ----------------------------
-- Table structure for `role_permission`
-- ----------------------------
DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE `role_permission` (
  `role_id` bigint(20) NOT NULL DEFAULT '0',
  `permission_id` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`role_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of role_permission
-- ----------------------------

-- ----------------------------
-- Table structure for `team`
-- ----------------------------
DROP TABLE IF EXISTS `team`;
CREATE TABLE `team` (
  `id` bigint(20) NOT NULL,
  `team` varchar(100) NOT NULL,
  `parent_id` bigint(20) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `available` bit(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of team
-- ----------------------------
INSERT INTO `team` VALUES ('1', '软件工程部', '0', null, '');
INSERT INTO `team` VALUES ('2', '系统集成部', '0', null, '');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `userid` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  `salt` varchar(100) DEFAULT NULL,
  `locked` varchar(10) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_user_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'test', '测试', 'c4ca4238a0b923820dcc509a6f75849b', '123', '0');
INSERT INTO `user` VALUES ('2', 'cxj', '程小进', 'c4ca4238a0b923820dcc509a6f75849b', '123', '0');
INSERT INTO `user` VALUES ('3', 'admin', '管理员', 'c4ca4238a0b923820dcc509a6f75849b', '123', '0');
INSERT INTO `user` VALUES ('4', '张丽芳', '张丽芳', 'c4ca4238a0b923820dcc509a6f75849b', '123', '0');

-- ----------------------------
-- Table structure for `user_role`
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `user_id` bigint(20) NOT NULL DEFAULT '0',
  `role_id` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`user_id`,`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_role
-- ----------------------------
INSERT INTO `user_role` VALUES ('1', '1');
INSERT INTO `user_role` VALUES ('1', '2');
INSERT INTO `user_role` VALUES ('2', '1');
INSERT INTO `user_role` VALUES ('2', '2');
INSERT INTO `user_role` VALUES ('3', '1');
INSERT INTO `user_role` VALUES ('4', '1');
INSERT INTO `user_role` VALUES ('4', '2');

-- ----------------------------
-- Table structure for `user_team`
-- ----------------------------
DROP TABLE IF EXISTS `user_team`;
CREATE TABLE `user_team` (
  `user_id` bigint(20) NOT NULL,
  `team_id` bigint(20) NOT NULL,
  PRIMARY KEY (`user_id`,`team_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_team
-- ----------------------------
INSERT INTO `user_team` VALUES ('1', '1');

DROP TABLE IF EXISTS `server`;
CREATE TABLE `server` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `team` bigint(20) NOT NULL,
  `type` varchar(40) NOT NULL,
  `cluster_name` varchar(128),
  `role` varchar(40),
  `ip` varchar(128) NOT NULL,
  `hostname` varchar(128) NOT NULL,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `description` varchar(128),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `component`;
CREATE TABLE `component` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `server_id` bigint(20) NOT NULL,
  `type` varchar(40) NOT NULL,
  `install_dir` varchar(128),
  `data_dir` varchar(128),
  `log_dir` varchar(128),
  `description` varchar(128),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
