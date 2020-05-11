create table crawling_sequences (
  `id` bigint(1) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(32) NOT NULL,
  `timestamp` bigint(1) NOT NULL,
  `created_at` datetime(3) NOT NULL,
  `updated_at` datetime(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_job_name_created_at` (`job_name`, `created_at`)
) ENGINE =InnoDB DEFAULT CHARSET=utf8;
