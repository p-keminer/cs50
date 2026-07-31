CREATE TABLE `users` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `first_name` VARCHAR(32) NOT NULL,
        `last_name` VARCHAR(32) NOT NULL,
        `username` VARCHAR(32) NOT NULL UNIQUE,
        `password` VARCHAR(128) NOT NULL

);

CREATE TABLE `schools` (
        `id` INT AUTO_INCREMENT  PRIMARY KEY,
        `name` VARCHAR(64) NOT NULL,
        `kind` ENUM('Primary','Secondary','Higher Education') NOT NULL,
        `city` VARCHAR(32),
        `year` YEAR
);

CREATE TABLE 'companys' (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `name` VARCHAR(64) NOT NULL,
        `branche` ENUM('Education','Technology','Business') NOT NULL,
        `city` VARCHAR(32)

);

CREATE TABLE `connections_users` (
        `id` INT AUTO_INCREMENT PRIMARY KEY,
        `user_id1` INT UNSIGNED NOT NULL,
        `user_id2` INT UNSIGNED NOT NULL,
        `type` ENUM('Follow','Connection') NOT NULL,
        FOREIGN KEY(`user_id1`) REFERENCES `users`(`id`),
        FOREIGN KEY(`user_id2`) REFERENCES `users`(`id`)
);

CREATE TABLE `connections_schools` (
        `id` INT AUTO_INCREMENT  PRIMARY KEY,
        `user_id` INT UNSIGNED NOT NULL,
        `school_id` INT UNSIGNED NOT NULL,
        `studied_from` DATE ,
        `graduation` ENUM('B','BA','MA','PhD'),
        `studied_to` DATE ,
        `worked_from` DATE,
        `worked_to` DATE ,
        `type` ENUM('follow','working','studied') NOT NULL,
        FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
        FOREIGN KEY(`school_id`) REFERENCES `schools`(`id`)
);

CREATE TABLE `connections_companys` (
        `id` INT AUTO_INCREMENT  PRIMARY KEY,
        `user_id` INT UNSIGNED NOT NULL,
        `company_id` INT UNSIGNED NULL,
        `position` VARCHAR(128),
        `experience` VARCHAR(128),
        `worked_from` DATE ,
        `worked_to` DATE ,
        `type` ENUM('follow','working') NOT NULL,
        FOREIGN KEY(`user_id`) REFERENCES `users`(`id`),
        FOREIGN KEY(`company_id`) REFERENCES `companys`(`id`)
);
