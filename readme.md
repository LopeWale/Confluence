# Confluence API Integration

This program is an object-oriented Python script that integrates the Atlassian Confluence REST API with a MySQL database. It uses the `APIConnection` class to make API calls and the `DatabaseConnection` class to interact with the database.

## Objective

The objective of this program is to fetch data from the Confluence REST API and store it in a MySQL database. The program fetches user info, user group info, and content info, and it can add, delete, and check content watchers. Additionally, it supports fetching blog data from specified spaces and provides methods to handle pagination when fetching data.

## Required API Keys/Parameters

To run this program, you need the following:

- Base URL of your Confluence instance
- Headers for the API requests, which should include the Authorization header with your base64-encoded username and password
- MySQL host, user, password, and database name

Replace placeholders in the `confluenceAPIconnection.py` and `database.py` files with your actual details.

## How to Run the Program

1. Make sure that Python and the required packages (`requests` and `mysql-connector-python`) are installed on your system.

2. Save the `confluenceAPIconnection.py`, `database.py`, and `main.py` files in the same directory or in a directory that's included in the Python path.

3. Open a terminal and navigate to the directory where the files are saved.

4. Run the `main.py` script with the command `python main.py`.

The script will create an instance of `DatabaseConnection`, pass it to the `APIConnection` constructor, and make API calls that automatically insert data into the database. It will also fetch blog data from specified spaces and handle pagination when fetching data from the API.

## Unit Testing

The program includes unit tests to ensure the correctness of the `APIConnection` and `DatabaseConnection` classes. The test results will be logged in the `test.log` file. To run the unit tests, execute the `test_main.py` script using the command `python test_main.py`.

## Additional Modifications

- The `confluenceAPIconnection.py` module has been updated to include methods for fetching blog data from specified spaces and handling pagination when fetching data.
- The `database.py` module has been updated to include methods for inserting and fetching blog data from the database.

### In confluenceAPIconnection.py:

base_url: Replace with the base URL of your Confluence instance.
headers: Replace with the headers for the API requests. This should include the Authorization header with your base64-encoded username and password.

### In database.py:

host: Replace with the hostname of your MySQL database.
user: Replace with the MySQL username.
password: Replace with the MySQL password.
database: Replace with the name of your MySQL database.

### In main.py:

Ensure that you have saved the required files (confluenceAPIconnection.py and database.py) in the same directory as main.py or in a directory included in the Python path.
These changes are necessary to customize the program to work with your specific Confluence instance and MySQL database. Replace the placeholders with the appropriate values specific to your setup. After making these changes, the program will be ready to fetch data from your Confluence instance and store it in the MySQL database as per your requirements.