# Medicine Python Project

## Overview

This project is a simple web application built using Flask, a Python web framework, to manage customer information for a medicine store. The application allows users to submit their personal information and prescriptions. The data is stored in a MySQL database.

## Directory Structure

Here's what each of these files and directories does:

- `app.py`: This is the main Python script that contains the Flask application. It handles the routing, form submissions, and database interactions.

- `static/`: This directory is used to store static files like CSS, JavaScript, and images. In this project, it contains a `styles.css` file to define the CSS styles for the web application.

- `templates/`: This directory contains HTML templates used by the Flask application. It includes an `index.html` template, which is the main page where users can input their information.

## How the App Works

1. When you run the Flask application using `app.py`, it starts a local development server.

2. Users can access the application by navigating to the root URL (usually, `http://localhost:5000/` if you're running the development server locally).

3. The main page, `index.html`, is displayed, providing a form where users can enter their full name, mobile number, age, address, and upload a prescription.

4. When a user submits the form, the data is sent to the Flask server, and the server stores the information in the MySQL database under the `customers` table.

5. If the data submission is successful, a "Success" message is displayed, and the information is stored in the database.

## Project Usage

To use this project, make sure you have Python, Flask, and a MySQL database set up and running. You'll need to configure the MySQL database connection in the `app.py` script. Then, run the Flask application, and you can access it through your web browser to input customer data.

This is a simple example of a web application for managing customer information in a medicine store. You can extend it by adding more features, such as customer search, data retrieval, and more.
