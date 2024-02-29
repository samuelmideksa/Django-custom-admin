# Django-custom-admin

# Bookstore Management System

This project is a Bookstore Management System designed to help users manage books, authors, genres, publishers, series,
and languages efficiently. It provides features for adding, editing, and deleting records for each entity.

## Features

- **Book Management**: Add, edit, and delete books. Includes fields for title, authors, series, cover image, rating, genres, ISBN, publisher, published date, languages, and plot.
- **Author Management**: Add, edit, and delete authors. Includes fields for name, image, and bio.

## Technologies Used

- **Django**: Django is used as the web framework for this project, providing a scalable architecture 
for building web applications.
- **Bootstrap**: Bootstrap is used for front-end styling and layout, providing a responsive and modern user interface.
- **SQLite**: SQLite is used as the database management system for storing application data.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/bookstore.git
   ```

2. Navigate to the project directory:
   ```
   cd bookstore
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

6. Access the application at http://localhost:8000/ in your web browser.

## Usage

- Once the server is running, you can access the Bookstore Management System through your web browser.
- Use the navigation menu to access different sections of the application, Books and Authors.
- Each section allows you to perform CRUD (Create, Read, Update, Delete) operations on the corresponding entity.

