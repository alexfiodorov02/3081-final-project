# Contact Management App
![sorting](https://github.com/alexfiodorov02/3081-final-project/assets/47510094/7a93328f-b06e-4fcd-b599-b637c2446ce6)
## Setup
1. Clone repo to your hard drive and navigate to the directory
2. Enter virtual environment (Unix/Mac: `source myworld/bin/activate`)
3. Navigate to djangoproject and run Django server (Mac: `python3 manage.py runserver`)
## Project Overview
The Contact Management App is a web application designed to manage contact information for employees and customers. It provides a user-friendly interface to view, search, and sort contact records. The application is built using Django and SQLite, and leverages Bootstrap and jQuery DataTables for the frontend.
### Functionalities
 -	View Records: The application displays a list of all employees and customers in a tabular format.
 -	Search Records: Users can search for specific keywords using the search bar.
 -	Sort Records: Users can sort the displayed records by any attribute without requiring a page reload.
## Technical Description
The application consists of two main models: Customer and Employee.
### Customer Model
The Customer model has the following attributes:
 -	`first_name:` A CharField that requires 3-255 characters. It validates input using `MaxLengthValidator` and `MinLengthValidator`.
 -	`last_name:` A CharField that requires 3-255 characters. It validates input using `MaxLengthValidator` and `MinLengthValidator`.
 -	`phone_number:` A CharField that requires 10-15 characters. It validates input using `MaxLengthValidator`, `MinLengthValidator`, and `RegexValidator (^\+?1?\d{9,15}$)`.
 -	`email:` An EmailField that requires 3-255 characters. It validates input using `MaxLengthValidator`, `MinLengthValidator`, and `EmailValidator`.
 -	`company:` A CharField that requires at least 3-255 characters. It validates input using `MaxLengthValidator` and `MinLengthValidator`.
### Employee Model
The Employee model has the following attributes:
 -	`first_name:` A CharField that requires 3-255 characters. It validates input using `MaxLengthValidator` and `MinLengthValidator`.
 -	`last_name:` A CharField that requires 3-255 characters. It validates input using `MaxLengthValidator` and `MinLengthValidator`.
 -	`phone_number:` A CharField that requires 10-15 characters. It validates input using `MaxLengthValidator`, `MinLengthValidator`, and `RegexValidator (^\+?1?\d{9,15}$)`.
 -	`email:` An EmailField that requires 3-255 characters. It validates input using `MaxLengthValidator`, `MinLengthValidator`, and `EmailValidator`.
 -	`role:` A CharField that requires at least 3-255 characters. It validates input using `MaxLengthValidator` and `MinLengthValidator`.
### Implementation
The application runs on Django and uses Bootstrap for styling and jQuery DataTables for the interactive tables. The database is managed by SQLite. Sorting is handled client-side by jQuery. The tables are set to disable client-side searching to allow the Django backend to handle search queries. The search form in the navigation bar sends a GET request to the Django backend to search for records. The search results are then displayed in their respective table.
## Challenges and Solutions
I could not get my first search function to work for both the Customer and Employee models. I managed to get search working for both models by separating the search functionality into two different functions, `search_customers` and `search_employees`. These functions had separate attributes and were responsible for searching within its respective model. I then refactored these two functions into three functions. I created a generic function called `search` that can be used to search any model. The `search_customers` and `search_employees` functions just call the `search` function with the appropriate parameters. This way, if I need to change the way searching is done, I only need to change the `search` function. This reduces repetition and makes my code easier to maintain.
