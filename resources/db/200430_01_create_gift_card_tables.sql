CREATE TABLE `clients` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `user_id` bigint(1) NOT NULL,
  `name` varchar(32) NOT NULL default 'default',
  `client_id` varchar(32) NOT NULL,
  `encrypted_secret` varchar(1024) NOT NULL,
  `scope` varchar(191) NOT NULL default '',
  `trusted` tinyint(1) NOT NULL default 1,
  `expires_at` datetime(3) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uix_user_id_name` (`user_id`, `name`),
  UNIQUE KEY `uix_client_id` (`client_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
