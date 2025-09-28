#project-day-28
#Mini E-Commerce Backend & Shop 

A Flask (Python)-powered web application that serves as a minimal e-commerce platform, providing both a RESTful API for product data and a visual frontend shop built with Jinja templates.
The project demonstrates essential backend functions (CRUD) and applies modern, dark-themed styling to the visual component.

---

## Features
RESTful API Endpoints (/api/products) for CRUD operations using JSON.

Visual Web Shop (/shop) rendered using Jinja templating.

Hardcoded product data (easily replaceable with SQLite or PostgreSQL).

Prices displayed in Indian Rupees (₹).

Clean dark UI styled with custom CSS to match a blog theme.

Minimal dependencies for quick setup and execution.

---

## Technologies Used
Flask – Python micro-framework for backend routing and logic.

Jinja2 – Templating engine for server-side generation of HTML/CSS shop views.

Python 3 – Core language.

HTML/CSS – Frontend structure and dark theme styling.

---

## Project Structure
mini-ecommerce/
│── app.py          # All Flask routes, API logic, and product data
└── templates/
    ├── blog_welcome.html # Homepage template
    └── index.html      # Visual Shop template

---

## How to Run
Clone the repository (or ensure you have all files in your project folder).

Install dependencies:

pip install Flask

Activate the Virtual Environment (Mandatory):

# For Windows Command Prompt (CMD):
venv\Scripts\activate

# For macOS/Linux (or PowerShell):
source venv/bin/activate

Run the Development Server:
To avoid port conflicts, we run the server on Port 8000:

set FLASK_APP=app.py     # For Windows CMD
flask run --host=0.0.0.0 --port=8000

Access the Application:

Visual Homepage: http://127.0.0.1:8000/

Visual Shop: http://127.0.0.1:8000/shop

Raw JSON API: http://127.0.0.1:8000/api/products

API Endpoints
Method

Endpoint

Description

GET

/api/products

Retrieves the list of all products (JSON).

GET

/api/products/<id>

Retrieves a single product by ID (JSON).

POST

/api/products

Creates a new product (requires JSON body).

PUT

/api/products/<id>

Updates an existing product (requires JSON body).

DELETE

/api/products/<id>

Deletes a product.

## Output 

<img width="1919" height="911" alt="Screenshot 2025-09-27 163745" src="https://github.com/user-attachments/assets/f98f04c1-353c-4113-bee7-a29879c26b22" />


Author
Swara Gharat
