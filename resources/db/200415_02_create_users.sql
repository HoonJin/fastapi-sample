CREATE TABLE `users` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(128) NOT NULL,
  `password` varchar(191) NOT NULL,
  `confirm_token` varchar(64),
  `confirmed_at` datetime(3),
  `status` varchar(16) NOT NULL DEFAULT 'unconfirmed',
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uix_email` (`email`),
  UNIQUE KEY `uix_confirm_token` (`confirm_token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
