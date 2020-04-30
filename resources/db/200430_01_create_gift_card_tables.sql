CREATE TABLE `vouchers` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `par_value` decimal(20, 2) NOT NULL,
  `category` varchar(32) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  `deleted_at` datetime(3) NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uix_name_` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


create table `voucher_sellers` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `url` varchar(1024) NOT NULL,
  `tel` varchar(16) NULL,
  `address` varchar(256) NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  `deleted_at` datetime(3) NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


create table `voucher_prices` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `voucher_id` bigint(1) NOT NULL,
  `seller_id` bigint(1) NOT NULL,
  `side` varchar(4) NOT NULL,
  `price` decimal(20, 2) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  `deleted_at` datetime(3) NULL,
  PRIMARY KEY (`id`),
  KEY `ix_voucher_id` (`voucher_id`),
  KEY `ix_side_voucher_id` (`side`, `voucher_id`),
  KEY `ix_seller_id_voucher_id` (`seller_id`, `voucher_id`),
  KEY `ix_voucher_id_created_at` (`voucher_id`, `created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
