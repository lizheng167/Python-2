/*
 Navicat MySQL Data Transfer

 Source Server         : lizheng167
 Source Server Version : 50716
 Source Host           : localhost
 Source Database       : lianxi

 Target Server Version : 50716
 File Encoding         : utf-8

 Date: 11/06/2016 14:47:48 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `user`
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES ('1', 'lizheng'), ('2', 'zishan');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
