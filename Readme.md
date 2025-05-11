# Blog Server - FastAPI

## Introduction

This is a simple and efficient blog server built using **FastAPI**. The primary goal of this project is to implement a backend system using skills gained from self-learning. This backend application features both **user routes** and **post routes**, utilizing **MySQL** as the database with **SQLAlchemy** as the ORM for database interactions. The server handles all **CRUD operations** for users and posts, demonstrating modularity and proper project organization. Additionally, it features **JWT authentication** and **OAuth2** for secure user login and authorization.

site is live 👉: https://blogserver-0oi3.onrender.com/
---

## Features

* Full **CRUD operations** for Users and Posts.
* **JWT authentication** and **OAuth2** integration for secure login and authorization.
* **Modular structure**, organized into dedicated folders for better maintainability.
* **SQLAlchemy** integration with MySQL for efficient database management.
* **FastAPI** as the primary framework for building a responsive API.
* Comprehensive **unit testing** using the `unittest` framework.
* Proper commenting and structured code for easy understanding.

---

## Installation

1. Clone the repository:

   ```bash
   git clone git@github.com:naga251602/blogserver.git
   cd blogserver
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

---

## Running Tests

Execute the unit tests to ensure everything is working correctly:

```bash
python -m unittest discover tests -p "test_2_*.py"
```

---

## Project Structure

* `db/` - Consists of Database config files and models of tables.
* `models/` - this folder consists of req and res models of server.
* `routes/` - API endpoints for user and post CRUD operations.
* `services/authentication.py` - JWT and OAuth2 authentication logic.
* `services/jwttoken.py` - creates jwt token.
* `tests/` - Unit tests to ensure functionality.
* `requirements.txt` - Python package dependencies.

---

## Pros

* Highly **modular** code, promoting separation of concerns.
* Well-commented for **clear understanding**.
* Follows best practices for backend development.
* **Secure authentication** using JWT and OAuth2.

## Future Goals

* Add support for pagination in post retrieval.
* Implement role-based access control (RBAC).

---

## Contributing

Feel free to fork the project, submit issues, or create pull requests. Contributions are welcome to make this project even better!