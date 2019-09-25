CREATE TABLE `gupiao_xinlang` (
  `gupiao_name` varchar(64) NOT NULL DEFAULT '',
  `gupiao_id` varchar(64) NOT NULL DEFAULT '',
  `date_info` varchar(64) NOT NULL DEFAULT '',
  `opening_price` float(5,2) DEFAULT NULL ,
  `high_price` float(5,2) DEFAULT NULL ,
  `closing_price` float(5,2) DEFAULT NULL ,
  `low_price` float(5,2) DEFAULT NULL ,
  `total_volume` int(11) DEFAULT NULL ,
  `total_price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;