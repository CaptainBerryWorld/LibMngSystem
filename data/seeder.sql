-- Seeding Roles table
INSERT INTO Roles (role_name, description) VALUES
('Admin', 'System administrator with full access'),
('Librarian', 'Manages library operations'),
('Reader', 'Regular library reader');

-- Seeding Users table
INSERT INTO Users (username, password, email, address, phone, registration_date, last_login, role_id) VALUES
('admin', 'admin123', 'admin@library.com', '123 Main St, Cityville', '1234567890', '2022-01-01', '2024-04-19 10:00:00', 1),
('librarian1', 'lib123', 'librarian1@library.com', '456 Oak Rd, Cityville', '9876543210', '2022-02-15', '2024-04-18 14:30:00', 2),
('librarian2', 'lib456', 'librarian2@library.com', '789 Elm St, Townville', '5551234567', '2023-06-01', '2024-04-17 09:15:00', 2),
('reader1', 'read123', 'reader1@email.com', '321 Pine Ave, Cityville', '9871236540', '2023-05-10', '2024-04-17 18:45:00', 3),
('reader2', 'read456', 'reader2@email.com', '654 Maple Ln, Townville', '7891011121', '2022-11-25', '2024-04-16 12:30:00', 3);

-- Seeding BookTypes table
INSERT INTO BookTypes (type_name, description) VALUES
('Hardcover', 'Books with a rigid protective cover'),
('Paperback', 'Books with a flexible paper cover'),
('E-book', 'Digital books readable on electronic devices'),
('Audio Book', 'Books in audio format');

-- Seeding Genres table
INSERT INTO Genres (genre_name, description) VALUES
('Fiction', 'Imaginative literary works'),
('Non-Fiction', 'Factual literary works'),
('Biography', 'Life stories of individuals'),
('Mystery', 'Novels involving a puzzle or crime to be solved'),
('Science Fiction', 'Speculative fiction involving futuristic or imaginative settings');

-- Seeding Publishers table
INSERT INTO Publishers (publisher_name, address, contact_info) VALUES
('Publisher A', '111 Publishing St, Cityville', 'info@publishera.com'),
('Publisher B', '222 Book Ln, Townville', 'contact@publisherb.com'),
('Publisher C', '333 Print Rd, Villageton', 'publisherc@email.com'),
('Publisher D', '444 Ink Ave, Cityville', 'publisherd@company.com'),
('Publisher E', '555 Tome Blvd, Townville', 'publishere@books.com');

-- Seeding Languages table
INSERT INTO Languages (language_name) VALUES
('English'),
('Spanish'),
('French'),
('German'),
('Japanese');

-- Seeding Charges table
INSERT INTO Charges (charge_name, description, charge_amount) VALUES
('Late Fee', 'Charge for returning a book after the due date', 0.50),
('Replacement Fee', 'Charge for lost or damaged books', 20.00),
('Membership Fee', 'Annual fee for library membership', 25.00),
('Processing Fee', 'Fee for processing new book acquisitions', 5.00);

-- Seeding BookCodes table
INSERT INTO BookCodes (book_code, description) VALUES
('NEW', 'New book'),
('USED', 'Used book'),
('REF', 'Reference book'),
('RARE', 'Rare or out-of-print book');

-- Seeding Books table
INSERT INTO Books (title, author, publication_date, isbn, book_type_id, genre_id, publisher_id, language_id, edition, total_copies, available_copies) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10', '9780743273565', 1, 1, 1, 1, '1st Edition', 10, 8),
('To Kill a Mockingbird', 'Harper Lee', '1960-07-11', '9780446310789', 2, 1, 2, 1, '2nd Edition', 15, 12),
('Autobiography of a Yogi', 'Paramahansa Yogananda', '1946-03-07', '9780876120835', 1, 3, 3, 1, '1st Edition', 5, 3),
('The Da Vinci Code', 'Dan Brown', '2003-03-18', '9780385504201', 2, 4, 4, 1, '1st Edition', 20, 15),
('Dune', 'Frank Herbert', '1965-08-01', '9780441013593', 1, 5, 5, 1, '3rd Edition', 8, 5),
('El Alquimista', 'Paulo Coelho', '1988-01-01', '9788408035245', 2, 1, 1, 2, '5th Edition', 12, 9),
('Der Zauberberg', 'Thomas Mann', '1924-11-24', '9783518368725', 1, 1, 2, 4, '2nd Edition', 6, 4);

-- Seeding Loans table
INSERT INTO Loans (user_id, book_id, issue_date, due_date, return_date, fine_amount) VALUES
(4, 1, '2024-04-10', '2024-04-24', NULL, NULL),
(4, 2, '2024-04-01', '2024-04-15', '2024-04-18', 1.50),
(5, 4, '2024-03-25', '2024-04-08', '2024-04-10', 1.00);

-- Seeding Reservations table
INSERT INTO Reservations (user_id, book_id, reservation_date, status) VALUES
(4, 3, '2024-04-15', 'Pending'),
(3, 1, '2024-04-12', 'Confirmed'),
(5, 5, '2024-04-18', 'Pending');

-- Seeding Reviews table
INSERT INTO Reviews (user_id, book_id, review_date, rating, comment) VALUES
(4, 1, '2024-04-18', 5, 'An American classic! Highly recommended.'),
(4, 2, '2024-04-19', 4, 'A powerful story about courage and justice.'),
(5, 4, '2024-04-20', 3, 'An exciting mystery, but the ending fell a bit flat.');

-- Seeding Transactions table
INSERT INTO Transactions (user_id, transaction_date, transaction_type, book_id, amount_paid) VALUES
(4, '2024-04-01 10:30:00', 'Issue', 2, 0.00),
(4, '2024-04-18 16:45:00', 'Return', 2, 1.50),
(5, '2024-03-25 14:20:00', 'Issue', 4, 0.00),
(5, '2024-04-10 11:00:00', 'Return', 4, 1.00);