You are the consultant for a small software development company specialising in developing applications for industry. You have just been awarded the contract to develop a simple Library Management Application for Accra Technical University Library. You are required to design this application using python tkinter module. The application comprises of these module registration page, login form, administrator menu (parameters/security), user maintenance menu, administrators menu (utility), librarian menu, library menu (book options), add a new book, readers option (find a book), readers options (edit book details), librarian menu (readers options), librarian menu (general options), Today’s issue inquiry, issue a book, return a book, find a book, reports, user report, book code report, book type report and about menu.
TITLE: LBRARY MANAGEMENT APPLICATION: ACCRA TECHNICAL UNIVERSITY
This is the Library Management software to be developed using python tkinter to computerize Accra Technical University Library System, ensuring that all transactions run smoothly without error. To access the software, you must first log in with your user name and password. It fulfils all of the functions of a modern library, including book circulation, book return, and fine calculation. By performing a simple search on the book id, readers can issue books, return books, and locate books in the library. Fines can be modified or changed based on the administrator's requirements. It keeps track of all books distributed to consumers, allowing the administrator to update his daily reports. Additionally, reader and book information is preserved, and the administrator maintains the primary account. Security and authentication are ensured by maintaining a database of reader names and passwords; the administrator is assigned the primary account and password. Numerous reports can be generated, including daily reports and user reports, as well as book type and book code reports.
SYSTEM OBJECTIVES
The goals of this project are:
•	Security – The user has to provide password in order to enter. Hence it provides security.
•	Easiness – The user simply has to follow series of instruction which makes project very simple to use.
•	Speedup result processing – While manually it may take time to search for books but it helps speed up processing, and also issue and return processes are easy, also database for students and books help in speeding up work of management of library.
•	Library management application is software for automating the manual library system of the university.
•	Functionalities of active library like issuing of books, returning of books and query processing.
•	The books and students are given a particular unique ID no. So that they can be accessed correctly without errors. The aim of the project is to get the correct information about a particular student and books available in the library.
•	The Library Management Application is standalone in nature.
•	To keep record of updated books and student database.
The project should be implemented to bring a simple interface for the users and provide them with easy search and access methods.
Using the PYTHON TKINTER produce the following sample dialog boxes for the Accra Technical University Library Management Project.
Document the code for this project and submit during the period of examination.


Project Structure

LibraryManagementSystem/
├── src/
│   ├── main.py
│   ├── admin/
│   │   ├── admin_menu.py
│   │   ├── user_management.py
│   │   ├── book_management.py
│   │   └── reports.py
│   ├── librarian/
│   │   ├── librarian_menu.py
│   │   ├── book_operations.py
│   │   └── loan_management.py
│   ├── reader/
│   │   ├── reader_menu.py
│   │   ├── book_search.py
│   │   └── loan_operations.py
│   ├── common/
│   │   ├── authentication.py
│   │   ├── database.py
│   │   └── utils.py
│   └── gui/
│       ├── app.py
│       ├── widgets.py
│       └── styles.py
├── tests/
│   ├── test_admin.py
│   ├── test_librarian.py
│   └── test_reader.py
├── data/
│   ├── schema.sql
│   ├── seed_data.sql
│   └── db_connection.py
├── docs/
│   └── README.md
└── README.md



Given the project requirements and the structure of your project, here's a step-by-step guide on how you might approach coding this project:

Start with the common/authentication.py: Implement the login functionality here. You'll need to connect to the database and verify the user credentials.

Move to common/database.py: Set up your database connection here. You'll use this to interact with your database throughout the project.

Next, admin/user_management.py: Implement the functionality for managing users (add, remove, update). You'll need to create forms for user input and interact with the database.

Then, admin/book_management.py: Similar to user management, implement the functionality for managing books.

After that, admin/reports.py: Implement the functionality for generating reports. This will likely involve complex database queries.

Next, librarian/book_operations.py and librarian/loan_management.py: Implement the functionality for librarians to manage books and loans.

Then, reader/book_search.py and reader/loan_operations.py: Implement the functionality for readers to search for books and manage their loans.

After that, gui/app.py, gui/widgets.py, and gui/styles.py: Implement the GUI for your application. Use the customtkinter module as specified in your requirements.txt file.

Finally, src/main.py: This is your application's entry point. Set up the initial login screen here and direct the user to the appropriate menu (admin, librarian, or reader) based on their credentials.

Write tests: As you're building your application, write tests for each module in the tests/ directory. This will help ensure your code is working as expected.

Update your README.md: Document your project, including how to set it up and use it.



Database Schema:
For a more advanced database schema for the Library Management Application, we can include additional entities to handle more complex scenarios and functionalities. Here's an advanced schema:

### Users Table
- **user_id** (Primary Key, Auto Increment)
- username
- password
- email
- address
- phone
- registration_date
- last_login
- role_id (Foreign Key referencing Roles table)

### Roles Table
- **role_id** (Primary Key, Auto Increment)
- role_name (Admin, Librarian, Reader)
- description

### Books Table
- **book_id** (Primary Key, Auto Increment)
- title
- author
- publication_date
- ISBN
- book_type_id (Foreign Key referencing BookTypes table)
- genre_id (Foreign Key referencing Genres table)
- publisher_id (Foreign Key referencing Publishers table)
- language_id (Foreign Key referencing Languages table)
- edition
- total_copies
- available_copies

### BookTypes Table
- **book_type_id** (Primary Key, Auto Increment)
- type_name
- description

### Genres Table
- **genre_id** (Primary Key, Auto Increment)
- genre_name
- description

### Publishers Table
- **publisher_id** (Primary Key, Auto Increment)
- publisher_name
- address
- contact_info

### Languages Table
- **language_id** (Primary Key, Auto Increment)
- language_name

### Charges Table
- **charge_id** (Primary Key, Auto Increment)
- charge_name
- description
- charge_amount

### BookCodes Table
- **book_code_id** (Primary Key, Auto Increment)
- book_code
- description

### Loans Table
- **loan_id** (Primary Key, Auto Increment)
- user_id (Foreign Key referencing Users table)
- book_id (Foreign Key referencing Books table)
- issue_date
- due_date
- return_date
- fine_amount

### Reservations Table
- **reservation_id** (Primary Key, Auto Increment)
- user_id (Foreign Key referencing Users table)
- book_id (Foreign Key referencing Books table)
- reservation_date
- status (Pending, Confirmed, Cancelled)

### Reviews Table
- **review_id** (Primary Key, Auto Increment)
- user_id (Foreign Key referencing Users table)
- book_id (Foreign Key referencing Books table)
- review_date
- rating
- comment

### Transactions Table
- **transaction_id** (Primary Key, Auto Increment)
- user_id (Foreign Key referencing Users table)
- transaction_date
- transaction_type (Issue, Return, Renewal)
- book_id (Foreign Key referencing Books table)
- amount_paid

This advanced schema incorporates entities such as roles, genres, publishers, languages, reservations, reviews, and transactions to handle various aspects of the library management system in a more detailed manner.

Given the complexity of the project, it's not feasible to provide all the code in a single response. so lets do it one at a time when you end one just state which one is next then we handle it like that. We are using mysql and tkinter for this, advanced codes