CREATE TABLE `clients` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(1) NOT NULL,
  `name` varchar(32) NOT NULL default 'default',
  `client_id` varchar(128) NOT NULL,
  `client_secret` varchar(191) NOT NULL,
  `scope` varchar(191) NOT NULL default '',
  `trusted` tinyint(1) NOT NULL default 0,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uix_user_id_name` (`user_id`, `name`),
  UNIQUE KEY `uix_client_id` (`client_id`),
  UNIQUE KEY `uix_client_secret` (`client_secret`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
