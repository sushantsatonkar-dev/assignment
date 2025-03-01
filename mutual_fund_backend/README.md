## Mutual Fund Backend - Setup and Usage Guide

# Prerequisites

Ensure you have the following installed on your system:

Python 3.12+

pip (Python package manager)

Git

# 1. Clone the Repository

git clone https://github.com/sushantsatonkar-dev/assignment.git

cd assignment/mutual_fund_backend

# 2. Configure Environment Variables

RAPIDAPI_KEY=your_rapidapi_key

Ensure you replace your_secret_key and your_rapidapi_key with actual values.

# 3. Apply Database Migrations

Run the initial database migration scripts:

python manage.py migrate

# 4. Run the Development Server

python manage.py runserver

Access the application at: http://127.0.0.1:8000/

# 5. API Endpoints

**Authentication**

Register User: POST /api/register/

Login: POST /api/login/

Refresh: POST /api/refresh/

**Mutual Fund APIs**

Fetch Open-ended Schemes: GET /api/open-ended-funds/
