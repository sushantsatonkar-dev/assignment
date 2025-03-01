Mutual Fund Backend - Setup and Usage Guide

Prerequisites

Ensure you have the following installed on your system:

Python 3.12+

pip (Python package manager)

PostgreSQL or SQLite (as per your database preference)

Git

Virtualenv (recommended for dependency isolation)

1. Clone the Repository

git clone https://github.com/sushantsatonkar-dev/assignment.git
cd assignment/mutual_fund_backend

2. Create and Activate a Virtual Environment

python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate on Mac/Linux
venv\Scripts\activate  # Activate on Windows

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file in the project root directory:

touch .env

Edit .env and add the following configuration:

SECRET_KEY=your_secret_key
DEBUG=True  # Set False in production
DATABASE_URL=sqlite:///db.sqlite3  # Change if using PostgreSQL
RAPIDAPI_KEY=your_rapidapi_key

Ensure you replace your_secret_key and your_rapidapi_key with actual values.

5. Apply Database Migrations

Run the initial database migration scripts:

python manage.py migrate

6. Create a Superuser (Optional, for Admin Access)

python manage.py createsuperuser

Follow the prompts to create an admin user.

7. Run the Development Server

python manage.py runserver

Access the application at: http://127.0.0.1:8000/

8. API Endpoints

Authentication

Register User: POST /api/register/

Login: POST /api/login/

Mutual Fund APIs

Fetch Open-ended Schemes: GET /api/funds/open-ended/

9. Running Tests (Optional)

To ensure everything is working correctly:

python manage.py test

10. Deployment Steps (Basic Guide)

Use gunicorn or uWSGI for running the app in production.

Configure environment variables correctly.

Use a reverse proxy (Nginx/Apache) if deploying on a server.
