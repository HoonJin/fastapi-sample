CREATE TABLE `users` (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `uuid` varchar(36) NOT NULL,
  `email` varchar(128) NOT NULL,
  `encrypted_password` varchar(191) NOT NULL,
  `confirmation_token` varchar(64),
  `confirmed_at` datetime(3),
  `status` varchar(16) NOT NULL DEFAULT 'unconfirmed',
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uix_uuid` (`uuid`),
  UNIQUE KEY `uix_email` (`email`),
  UNIQUE KEY `uix_confirmation_token` (`confirmation_token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
