# Django CRUD Project

This is a simple **Django CRUD (Create, Read, Update, Delete)** project that performs basic operations on **user data** via a REST API. It is useful for learning or using as a boilerplate for other projects.

---

## 🚀 Features

* Create new user entries
* View list of users
* Update existing user data
* Delete user data
* API tested using Postman

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Database:** SQLite (default), can be replaced with PostgreSQL, MySQL, etc.
* **API Testing:** Postman
* **Development Tools:** VS Code / Any IDE

---

## ✅ Pre-requisites

Before you begin, ensure you have the following installed:

* Python 3.8+
* pip (Python package manager)
* Git
* Postman
* VS Code or any preferred IDE

---

## 📦 Installation & Setup

Follow these steps to set up the project locally.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/django-crud-project.git
cd django-crud-project
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL Database :

1. Login into the `psql` shell

    ```bash
    sudo -u postgres psql
    ```

2. Create user and database on PostgreSQL

    ```sql
    postgres=# CREATE DATABASE db_name;
    postgres=# CREATE USER user_name WITH PASSWORD 'password';
    postgres=# GRANT ALL PRIVILEGES ON DATABASE db_name TO user_name;
    ```

### 5. Set up the environment variables

* Create a `.env` file in the root directory.
* Copy the content from `.env.example` and paste it into `.env`.

Example:

```
DATABASE_NAME="my-test-db"
PASSWORD="******"
HOST="127.0.0.1"
PORT="587"
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

The project will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

To create a superuser and access the Django admin panel:

```bash
python manage.py createsuperuser
```

Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


