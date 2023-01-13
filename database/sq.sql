/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - fireshop
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`fireshop` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `fireshop`;

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `card_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `card_no` varchar(50) DEFAULT NULL,
  `card_name` varchar(60) DEFAULT NULL,
  `exp_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`card_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `card` */

insert  into `card`(`card_id`,`customer_id`,`card_no`,`card_name`,`exp_date`) values 
(8,1,'7898798979949464','athul','04'),
(7,1,'7898798979949464','athul','01');

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_name` varchar(50) DEFAULT NULL,
  `cat_desc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`cat_id`,`cat_name`,`cat_desc`) values 
(1,'cats','category');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(520) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `complaint_date` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`complaint_id`,`customer_id`,`complaint`,`reply`,`complaint_date`) values 
(1,1,'bad','sorry for the issue','12/02/2023');

/*Table structure for table `courier` */

DROP TABLE IF EXISTS `courier`;

CREATE TABLE `courier` (
  `courier_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `usernname` varchar(50) DEFAULT NULL,
  `cour_name` varchar(50) DEFAULT NULL,
  `cour_email` varchar(50) DEFAULT NULL,
  `cour_street` varchar(50) DEFAULT NULL,
  `cour_city` varchar(50) DEFAULT NULL,
  `cour_state` varchar(50) DEFAULT NULL,
  `cour_pincode` varchar(50) DEFAULT NULL,
  `cour_phone` varchar(50) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`courier_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `courier` */

insert  into `courier`(`courier_id`,`staff_id`,`usernname`,`cour_name`,`cour_email`,`cour_street`,`cour_city`,`cour_state`,`cour_pincode`,`cour_phone`,`status`) values 
(1,0,'cour@gmail.com','courname','cour@gmail.com','32nd street','cherthala','kerala','68754','7894561230','inactive');

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `c_fname` varchar(20) DEFAULT NULL,
  `c_lname` varchar(20) DEFAULT NULL,
  `c_housename` varchar(20) DEFAULT NULL,
  `c_street` varchar(20) DEFAULT NULL,
  `c_city` varchar(20) DEFAULT NULL,
  `c_state` varchar(20) DEFAULT NULL,
  `c_pincode` varchar(20) DEFAULT NULL,
  `c_phone` varchar(20) DEFAULT NULL,
  `c_email` varchar(100) DEFAULT NULL,
  `c_gender` varchar(20) DEFAULT NULL,
  `c_dob` varchar(20) DEFAULT NULL,
  `c_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

insert  into `customer`(`customer_id`,`username`,`c_fname`,`c_lname`,`c_housename`,`c_street`,`c_city`,`c_state`,`c_pincode`,`c_phone`,`c_email`,`c_gender`,`c_dob`,`c_status`) values 
(1,'arun@gmail.com','arun','kumar','arunnivas','2nd street','kochi','ernakulam','685495','7894681235','arunkumar@gmail.com','male','12/02/2023','active'),
(2,'hokofim411@nazyno.com','rrrr','rrrr','rerrr','rrrr','rrrr','rrrrq','666666','8564562516','hokofim411@nazyno.com','male','2023-01-17','inactive');

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `courier_id` int(11) DEFAULT NULL,
  `delivery_date` varchar(50) DEFAULT NULL,
  `delivery_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(20) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`type`,`status`) values 
('admin','admin','admin','active'),
('pthalika8@gmail.com','pthalika','staff','inactive'),
('cour@gmail.com','cour','courier','inactive'),
('hokofim411@nazyno.com','wwww','customer','active'),
('arun@gmail.com','arun','customer','active');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `total_price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`order_details_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`order_details_id`,`order_master_id`,`product_id`,`quantity`,`total_price`) values 
(18,6,5,'1','1040'),
(17,6,1,'1','1150'),
(16,6,4,'1','2300');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `ostatus` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`customer_id`,`total_amount`,`date`,`ostatus`) values 
(6,1,'4490','2023-01-11','pending');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `card_id` int(11) DEFAULT NULL,
  `order_master_id` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `payment_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`card_id`,`order_master_id`,`amount`,`payment_date`) values 
(4,8,'3','5750','2023-01-11 14:30:43'),
(3,7,'3','5750','2023-01-11 14:28:11');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcat_id` int(11) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `product_desc` varchar(50) DEFAULT NULL,
  `product_img` varchar(500) DEFAULT NULL,
  `stock` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`subcat_id`,`product_name`,`product_desc`,`product_img`,`stock`,`status`) values 
(1,1,'glass braker','glass breaker axe','static/uploads/a0fd90b1-2bf0-42d2-9ea1-915cd00d5564cool-4k-wallpaper-2.jpg','0','active'),
(4,2,'asfgajksgs','rrrrrr','static/uploads/1593044d-a7f3-41ba-bd14-d41283b64ed8rubiks-cube-digital-art-wallpaper.jpg','0','active'),
(5,2,'asfgajksgs','asd','static/uploads/f84a7262-4d91-456d-aad6-4b983a8dd4c529534.jpg','0','active');

/*Table structure for table `purchase_details` */

DROP TABLE IF EXISTS `purchase_details`;

CREATE TABLE `purchase_details` (
  `pdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `pmaster_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `cost_price` varchar(50) DEFAULT NULL,
  `selling_price` varchar(50) DEFAULT NULL,
  `quantity` varchar(550) DEFAULT NULL,
  PRIMARY KEY (`pdetails_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_details` */

insert  into `purchase_details`(`pdetails_id`,`pmaster_id`,`product_id`,`cost_price`,`selling_price`,`quantity`) values 
(1,1,1,'1000','1150','10'),
(2,2,2,'2000','2300','10'),
(3,2,4,'2000','2300','6'),
(4,2,5,'1000','1040','10');

/*Table structure for table `purchase_master` */

DROP TABLE IF EXISTS `purchase_master`;

CREATE TABLE `purchase_master` (
  `pmaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `pstatus` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  `date_added` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pmaster_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `purchase_master` */

insert  into `purchase_master`(`pmaster_id`,`vendor_id`,`staff_id`,`pstatus`,`total_amount`,`date_added`) values 
(1,1,0,'paid','40000','2023-01-10 09:09:12'),
(2,1,0,'paid','60000','2023-01-11 09:31:22');

/*Table structure for table `purchased` */

DROP TABLE IF EXISTS `purchased`;

CREATE TABLE `purchased` (
  `purchased_id` int(11) NOT NULL AUTO_INCREMENT,
  `pdetails_id` int(11) DEFAULT NULL,
  `order_details_id` int(11) DEFAULT NULL,
  `qty_purchased` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`purchased_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `purchased` */

insert  into `purchased`(`purchased_id`,`pdetails_id`,`order_details_id`,`qty_purchased`) values 
(13,4,18,'1'),
(12,1,17,'1'),
(11,3,16,'1');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `staff_fname` varchar(20) DEFAULT NULL,
  `staff_lname` varchar(20) DEFAULT NULL,
  `staff_housename` varchar(20) DEFAULT NULL,
  `staff_street` varchar(20) DEFAULT NULL,
  `staff_city` varchar(20) DEFAULT NULL,
  `staff_dist` varchar(20) DEFAULT NULL,
  `staff_pincode` varchar(20) DEFAULT NULL,
  `staff_phone` varchar(20) DEFAULT NULL,
  `staff_email` varchar(20) DEFAULT NULL,
  `staff_gender` varchar(20) DEFAULT NULL,
  `staff_dob` varchar(20) DEFAULT NULL,
  `staff_status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_housename`,`staff_street`,`staff_city`,`staff_dist`,`staff_pincode`,`staff_phone`,`staff_email`,`staff_gender`,`staff_dob`,`staff_status`) values 
(1,'pthalika8@gmail.com','amal','amal','amalnivas','32nd street','cherthala','alappy','68754','7894561230','pthalika8@gmail.com','male','2023-01-04','inactive');

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcat_id` int(11) NOT NULL AUTO_INCREMENT,
  `cat_id` int(50) DEFAULT NULL,
  `subcat_name` varchar(50) DEFAULT NULL,
  `subcat_desc` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subcat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

insert  into `subcategory`(`subcat_id`,`cat_id`,`subcat_name`,`subcat_desc`) values 
(1,1,'asd','asd'),
(2,1,'asds','asdasd');

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `v_name` varchar(50) DEFAULT NULL,
  `v_email` varchar(50) DEFAULT NULL,
  `v_street` varchar(50) DEFAULT NULL,
  `v_city` varchar(50) DEFAULT NULL,
  `v_pincode` varchar(50) DEFAULT NULL,
  `v_phone` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

insert  into `vendor`(`vendor_id`,`staff_id`,`v_name`,`v_email`,`v_street`,`v_city`,`v_pincode`,`v_phone`,`status`) values 
(1,0,'hubolt','hubolt@gmail.com','11th street','kochi','798888','0987654321','inactive');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
