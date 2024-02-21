# Invoice Management System

This project is an Invoice Management System built using Django and Django Rest Framework. It provides a set of RESTful APIs for managing invoices and their details.

## Features
- Create, retrieve, update, and delete invoices.
- Create, retrieve, update, and delete invoice details associated with invoices.
- API endpoints for invoices and invoice details support CRUD operations.
- Nested representation of invoice details within invoice responses.

## Technologies Used
- Django
- Django Rest Framework

## Getting Started

1. **Installation**: Clone this repository and Install the required dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

2. **Database Setup**: Run database migrations using:

    ```bash
    python manage.py migrate
    ```

3. **Create Superuser**: Create a superuser to access the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

4. **Run Development Server**: Start the development server:

    ```bash
    python manage.py runserver
    ```
    
5. Access the API endpoints at:
   ```bash
    http://127.0.0.1:8000/
   ```

## API Documentation

### Invoices

- **GET /invoices/**
  - Retrieve a list of all invoices.
  
- **POST /invoices/**
  - Create a new invoice.
  - Request Body:
    ```json
    {
        "date": "YYYY-MM-DD",
        "customer_name": "Customer Name"
    }
    ```
  - Response:
    ```json
    {
        "id": 1,
        "date": "YYYY-MM-DD",
        "customer_name": "Customer Name",
        "details": []
    }
    ```

- **GET /invoices/{id}/**
  - Retrieve details of a specific invoice by ID.

- **PUT /invoices/{id}/**
  - Update details of a specific invoice by ID.

- **DELETE /invoices/{id}/**
  - Delete a specific invoice by ID.

### Invoice Details

- **GET /invoice_details/**
  - Retrieve a list of all invoice details.
  
- **POST /invoice_details/**
  - Create a new invoice detail.
  - Request Body:
    ```json
    {
        "invoice": 1,
        "description": "Description",
        "quantity": 1,
        "unit_price": 10.00,
        "price": 10.00
    }
    ```
  - Response:
    ```json
    {
        "id": 1,
        "invoice": 1,
        "description": "Description",
        "quantity": 1,
        "unit_price": 10.00,
        "price": 10.00
    }
    ```

- **GET /invoice_details/{id}/**
  - Retrieve details of a specific invoice detail by ID.

- **PUT /invoice_details/{id}/**
  - Update details of a specific invoice detail by ID.

- **DELETE /invoice_details/{id}/**
  - Delete a specific invoice detail by ID.
 
## Contributors

- Pavel-Khan17
- pavelkhan1999@gmail.com
- pavelkhan.dev@gmail.com
