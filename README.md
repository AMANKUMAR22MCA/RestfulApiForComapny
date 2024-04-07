

# RestfulApiForCompany
## This project is a RESTful API for managing company information.

# Installation :
Clone the repository:
git clone https://github.com/AMANKUMAR22MCA/RestfulApiForComapny.git
Install dependencies:
pip install django and pip install djangorestframework
Apply database migrations:
python manage.py migrate
Start the development server:
python manage.py runserver

# Usage
API Endpoints:

/api/v1/companies/: List all companies or create a new company.
/api/v1/companies/<id>/: Retrieve, update, or delete a specific company.
Authentication:

Use token-based authentication. Obtain a token by sending a POST request to /api/token/ with your username and password in the request body.
Sample Requests:

List Companies:
curl http://127.0.0.1:8000/api/v1/companies/
![rest1](https://github.com/AMANKUMAR22MCA/RestfulApiForComapny/assets/126316303/0ab6942e-fad0-4e11-99ba-f8443a22a28b)
![rest2](https://github.com/AMANKUMAR22MCA/RestfulApiForComapny/assets/126316303/5004a3f0-c35f-40c5-a892-c8307cc81f19)

Retrieve Company:
curl http://127.0.0.1:8000/api/v1/companies/1/
![rest3](https://github.com/AMANKUMAR22MCA/RestfulApiForComapny/assets/126316303/f767f877-e98f-4326-81f0-d5788f98b1c6)
![rest4](https://github.com/AMANKUMAR22MCA/RestfulApiForComapny/assets/126316303/e6199b31-8eb0-4981-9e06-9f074b043b2b)



