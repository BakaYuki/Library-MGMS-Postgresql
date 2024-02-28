
-- Create the admin table
CREATE TABLE admin (
    admin_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Create the student table
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
);

-- Create the books table
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100),
    genre VARCHAR(100),
    stock INT DEFAULT 0
    available BOOLEAN DEFAULT TRUE,
);

-- Create the issued table
CREATE TABLE issued (
    issued_id SERIAL PRIMARY KEY,
    student_id INTEGER REFERENCES student(student_id),
    book_id INTEGER REFERENCES books(book_id),
    issue_date DATE NOT NULL,
    CONSTRAINT unique_issue_per_student_book UNIQUE (student_id, book_id)
);
