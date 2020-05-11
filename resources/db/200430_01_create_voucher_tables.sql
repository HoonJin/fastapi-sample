CREATE TABLE `vouchers` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `name` varchar(64) NOT NULL,
  `par_value` decimal(20, 2) NOT NULL,
  `category` varchar(32) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  `deleted_at` datetime(3) NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uix_uuid` (`uuid`),
  UNIQUE KEY `uix_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


create table `voucher_stores` (
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
  `store_id` bigint(1) NOT NULL,
  `side` varchar(4) NOT NULL,
  `price` decimal(20, 2) NOT NULL,
  `sequence_id` bigint(1) NOT NULL DEFAULT 0,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  `deleted_at` datetime(3) NULL,
  PRIMARY KEY (`id`),
  KEY `ix_voucher_id_created_at` (`voucher_id`, `created_at`),
  KEY `ix_side_voucher_id_created_at` (`side`, `voucher_id`, `created_at`),
  KEY `ix_store_id_voucher_id_created_at` (`store_id`, `voucher_id`, `created_at`),
  KEY `ix_sequence_id` (`sequence_id`, `voucher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
