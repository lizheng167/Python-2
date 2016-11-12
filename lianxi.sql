/*
 Navicat MySQL Data Transfer

 Source Server         : lizheng167
 Source Server Version : 50716
 Source Host           : localhost
 Source Database       : lianxi

 Target Server Version : 50716
 File Encoding         : utf-8

 Date: 11/12/2016 11:57:07 AM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `station`
-- ----------------------------
DROP TABLE IF EXISTS `station`;
CREATE TABLE `station` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `from_station_name` char(30) NOT NULL,
  `to_station_name` char(30) NOT NULL,
  `station_train_code` char(10) NOT NULL,
  `start_station_name` char(20) NOT NULL,
  `end_station_name` char(20) NOT NULL,
  `start_time` char(30) NOT NULL,
  `arrive_time` char(30) NOT NULL,
  `tz_num` char(10) NOT NULL,
  `zy_num` char(10) NOT NULL,
  `ze_num` char(10) NOT NULL,
  `lishi` char(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `wiki_urls`
-- ----------------------------
DROP TABLE IF EXISTS `wiki_urls`;
CREATE TABLE `wiki_urls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_name` varchar(200) NOT NULL,
  `url_href` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
