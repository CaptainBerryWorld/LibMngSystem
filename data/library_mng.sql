-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 19, 2024 at 07:40 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_mng`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookcodes`
--

CREATE TABLE `bookcodes` (
  `book_code_id` int(11) NOT NULL,
  `book_code` varchar(20) NOT NULL,
  `description` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bookcodes`
--

INSERT INTO `bookcodes` (`book_code_id`, `book_code`, `description`) VALUES
(1, 'NEW', 'New book'),
(2, 'USED', 'Used book'),
(3, 'REF', 'Reference book'),
(4, 'RARE', 'Rare or out-of-print book');

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `book_id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `publication_date` date NOT NULL,
  `isbn` varchar(20) NOT NULL,
  `book_type_id` int(11) NOT NULL,
  `genre_id` int(11) NOT NULL,
  `publisher_id` int(11) NOT NULL,
  `language_id` int(11) NOT NULL,
  `edition` varchar(20) DEFAULT NULL,
  `total_copies` int(11) NOT NULL,
  `available_copies` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`book_id`, `title`, `author`, `publication_date`, `isbn`, `book_type_id`, `genre_id`, `publisher_id`, `language_id`, `edition`, `total_copies`, `available_copies`) VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10', '9780743273565', 1, 1, 1, 1, '1st Edition', 10, 8),
(2, 'To Kill a Mockingbird', 'Harper Lee', '1960-07-11', '9780446310789', 2, 1, 2, 1, '2nd Edition', 15, 12),
(3, 'Autobiography of a Yogi', 'Paramahansa Yogananda', '1946-03-07', '9780876120835', 1, 3, 3, 1, '1st Edition', 5, 3),
(4, 'The Da Vinci Code', 'Dan Brown', '2003-03-18', '9780385504201', 2, 4, 4, 1, '1st Edition', 20, 15),
(5, 'Dune', 'Frank Herbert', '1965-08-01', '9780441013593', 1, 5, 5, 1, '3rd Edition', 8, 5),
(6, 'El Alquimista', 'Paulo Coelho', '1988-01-01', '9788408035245', 2, 1, 1, 2, '5th Edition', 12, 9),
(7, 'Der Zauberberg', 'Thomas Mann', '1924-11-24', '9783518368725', 1, 1, 2, 4, '2nd Edition', 6, 4);

-- --------------------------------------------------------

--
-- Table structure for table `booktypes`
--

CREATE TABLE `booktypes` (
  `book_type_id` int(11) NOT NULL,
  `type_name` varchar(50) NOT NULL,
  `description` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booktypes`
--

INSERT INTO `booktypes` (`book_type_id`, `type_name`, `description`) VALUES
(1, 'Hardcover', 'Books with a rigid protective cover'),
(2, 'Paperback', 'Books with a flexible paper cover'),
(3, 'E-book', 'Digital books readable on electronic devices'),
(4, 'Audio Book', 'Books in audio format');

-- --------------------------------------------------------

--
-- Table structure for table `charges`
--

CREATE TABLE `charges` (
  `charge_id` int(11) NOT NULL,
  `charge_name` varchar(50) NOT NULL,
  `description` varchar(200) DEFAULT NULL,
  `charge_amount` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `charges`
--

INSERT INTO `charges` (`charge_id`, `charge_name`, `description`, `charge_amount`) VALUES
(1, 'Late Fee', 'Charge for returning a book after the due date', '0.50'),
(2, 'Replacement Fee', 'Charge for lost or damaged books', '20.00'),
(3, 'Membership Fee', 'Annual fee for library membership', '25.00'),
(4, 'Processing Fee', 'Fee for processing new book acquisitions', '5.00');

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

CREATE TABLE `genres` (
  `genre_id` int(11) NOT NULL,
  `genre_name` varchar(50) NOT NULL,
  `description` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `genres`
--

INSERT INTO `genres` (`genre_id`, `genre_name`, `description`) VALUES
(1, 'Fiction', 'Imaginative literary works'),
(2, 'Non-Fiction', 'Factual literary works'),
(3, 'Biography', 'Life stories of individuals'),
(4, 'Mystery', 'Novels involving a puzzle or crime to be solved'),
(5, 'Science Fiction', 'Speculative fiction involving futuristic or imaginative settings');

-- --------------------------------------------------------

--
-- Table structure for table `languages`
--

CREATE TABLE `languages` (
  `language_id` int(11) NOT NULL,
  `language_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `languages`
--

INSERT INTO `languages` (`language_id`, `language_name`) VALUES
(1, 'English'),
(2, 'Spanish'),
(3, 'French'),
(4, 'German'),
(5, 'Japanese');

-- --------------------------------------------------------

--
-- Table structure for table `loans`
--

CREATE TABLE `loans` (
  `loan_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `issue_date` date NOT NULL,
  `due_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `fine_amount` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `loans`
--

INSERT INTO `loans` (`loan_id`, `user_id`, `book_id`, `issue_date`, `due_date`, `return_date`, `fine_amount`) VALUES
(1, 4, 1, '2024-04-10', '2024-04-24', NULL, NULL),
(2, 4, 2, '2024-04-01', '2024-04-15', '2024-04-18', '1.50'),
(3, 5, 4, '2024-03-25', '2024-04-08', '2024-04-10', '1.00');

-- --------------------------------------------------------

--
-- Table structure for table `publishers`
--

CREATE TABLE `publishers` (
  `publisher_id` int(11) NOT NULL,
  `publisher_name` varchar(100) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `contact_info` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publishers`
--

INSERT INTO `publishers` (`publisher_id`, `publisher_name`, `address`, `contact_info`) VALUES
(1, 'Publisher A', '111 Publishing St, Cityville', 'info@publishera.com'),
(2, 'Publisher B', '222 Book Ln, Townville', 'contact@publisherb.com'),
(3, 'Publisher C', '333 Print Rd, Villageton', 'publisherc@email.com'),
(4, 'Publisher D', '444 Ink Ave, Cityville', 'publisherd@company.com'),
(5, 'Publisher E', '555 Tome Blvd, Townville', 'publishere@books.com');

-- --------------------------------------------------------

--
-- Table structure for table `reservations`
--

CREATE TABLE `reservations` (
  `reservation_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `reservation_date` date NOT NULL,
  `status` enum('Pending','Confirmed','Cancelled') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reservations`
--

INSERT INTO `reservations` (`reservation_id`, `user_id`, `book_id`, `reservation_date`, `status`) VALUES
(1, 4, 3, '2024-04-15', 'Pending'),
(2, 3, 1, '2024-04-12', 'Confirmed'),
(3, 5, 5, '2024-04-18', 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `reviews`
--

CREATE TABLE `reviews` (
  `review_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `review_date` date NOT NULL,
  `rating` int(11) NOT NULL CHECK (`rating` between 1 and 5),
  `comment` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reviews`
--

INSERT INTO `reviews` (`review_id`, `user_id`, `book_id`, `review_date`, `rating`, `comment`) VALUES
(1, 4, 1, '2024-04-18', 5, 'An American classic! Highly recommended.'),
(2, 4, 2, '2024-04-19', 4, 'A powerful story about courage and justice.'),
(3, 5, 4, '2024-04-20', 3, 'An exciting mystery, but the ending fell a bit flat.');

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `role_id` int(11) NOT NULL,
  `role_name` varchar(50) NOT NULL,
  `description` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`role_id`, `role_name`, `description`) VALUES
(1, 'Admin', 'System administrator with full access'),
(2, 'Librarian', 'Manages library operations'),
(3, 'Reader', 'Regular library reader');

-- --------------------------------------------------------

--
-- Table structure for table `transactions`
--

CREATE TABLE `transactions` (
  `transaction_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `transaction_date` datetime NOT NULL,
  `transaction_type` enum('Issue','Return','Renewal') NOT NULL,
  `book_id` int(11) NOT NULL,
  `amount_paid` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `transactions`
--

INSERT INTO `transactions` (`transaction_id`, `user_id`, `transaction_date`, `transaction_type`, `book_id`, `amount_paid`) VALUES
(1, 4, '2024-04-01 10:30:00', 'Issue', 2, '0.00'),
(2, 4, '2024-04-18 16:45:00', 'Return', 2, '1.50'),
(3, 5, '2024-03-25 14:20:00', 'Issue', 4, '0.00'),
(4, 5, '2024-04-10 11:00:00', 'Return', 4, '1.00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `registration_date` date NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `email`, `address`, `phone`, `registration_date`, `last_login`, `role_id`) VALUES
(1, 'admin', 'admin123', 'admin@library.com', '123 Main St, Cityville', '1234567890', '2022-01-01', '2024-04-19 10:00:00', 1),
(2, 'librarian1', 'lib123', 'librarian1@library.com', '456 Oak Rd, Cityville', '9876543210', '2022-02-15', '2024-04-18 14:30:00', 2),
(3, 'librarian2', 'lib456', 'librarian2@library.com', '789 Elm St, Townville', '5551234567', '2023-06-01', '2024-04-17 09:15:00', 2),
(4, 'reader1', 'read123', 'reader1@email.com', '321 Pine Ave, Cityville', '9871236540', '2023-05-10', '2024-04-17 18:45:00', 3),
(5, 'reader2', 'read456', 'reader2@email.com', '654 Maple Ln, Townville', '7891011121', '2022-11-25', '2024-04-16 12:30:00', 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookcodes`
--
ALTER TABLE `bookcodes`
  ADD PRIMARY KEY (`book_code_id`);

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`book_id`),
  ADD KEY `book_type_id` (`book_type_id`),
  ADD KEY `genre_id` (`genre_id`),
  ADD KEY `publisher_id` (`publisher_id`),
  ADD KEY `language_id` (`language_id`);

--
-- Indexes for table `booktypes`
--
ALTER TABLE `booktypes`
  ADD PRIMARY KEY (`book_type_id`);

--
-- Indexes for table `charges`
--
ALTER TABLE `charges`
  ADD PRIMARY KEY (`charge_id`);

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`genre_id`);

--
-- Indexes for table `languages`
--
ALTER TABLE `languages`
  ADD PRIMARY KEY (`language_id`);

--
-- Indexes for table `loans`
--
ALTER TABLE `loans`
  ADD PRIMARY KEY (`loan_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `book_id` (`book_id`);

--
-- Indexes for table `publishers`
--
ALTER TABLE `publishers`
  ADD PRIMARY KEY (`publisher_id`);

--
-- Indexes for table `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`reservation_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `book_id` (`book_id`);

--
-- Indexes for table `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`review_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `book_id` (`book_id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indexes for table `transactions`
--
ALTER TABLE `transactions`
  ADD PRIMARY KEY (`transaction_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `book_id` (`book_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `role_id` (`role_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookcodes`
--
ALTER TABLE `bookcodes`
  MODIFY `book_code_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `book_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `booktypes`
--
ALTER TABLE `booktypes`
  MODIFY `book_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `charges`
--
ALTER TABLE `charges`
  MODIFY `charge_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `genres`
--
ALTER TABLE `genres`
  MODIFY `genre_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `languages`
--
ALTER TABLE `languages`
  MODIFY `language_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `loans`
--
ALTER TABLE `loans`
  MODIFY `loan_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `publishers`
--
ALTER TABLE `publishers`
  MODIFY `publisher_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `reservations`
--
ALTER TABLE `reservations`
  MODIFY `reservation_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `reviews`
--
ALTER TABLE `reviews`
  MODIFY `review_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transactions`
--
ALTER TABLE `transactions`
  MODIFY `transaction_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `books`
--
ALTER TABLE `books`
  ADD CONSTRAINT `books_ibfk_1` FOREIGN KEY (`book_type_id`) REFERENCES `booktypes` (`book_type_id`),
  ADD CONSTRAINT `books_ibfk_2` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`genre_id`),
  ADD CONSTRAINT `books_ibfk_3` FOREIGN KEY (`publisher_id`) REFERENCES `publishers` (`publisher_id`),
  ADD CONSTRAINT `books_ibfk_4` FOREIGN KEY (`language_id`) REFERENCES `languages` (`language_id`);

--
-- Constraints for table `loans`
--
ALTER TABLE `loans`
  ADD CONSTRAINT `loans_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `loans_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`);

--
-- Constraints for table `reservations`
--
ALTER TABLE `reservations`
  ADD CONSTRAINT `reservations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `reservations_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`);

--
-- Constraints for table `reviews`
--
ALTER TABLE `reviews`
  ADD CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`);

--
-- Constraints for table `transactions`
--
ALTER TABLE `transactions`
  ADD CONSTRAINT `transactions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`),
  ADD CONSTRAINT `transactions_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `books` (`book_id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
