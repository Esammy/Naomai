# Design and Implementation of Off-campus Accommodation System

# Off-Campus Accommodation Portal

Welcome to the Off-Campus Accommodation Portal! This platform provides a convenient way for students to find and book accommodation options off campus. It allows landlords to showcase their properties and enables students to create accounts, browse available lodges, and make bookings. This README file serves as a guide to help you understand the features and functionality of our platform.

## Features

1. User Registration and Authentication:
   - Students can create accounts with their personal information.
   - Secure authentication system ensures the privacy and security of user data.

2. Property Listings:
   - Landlords can create listings for their properties.
   - Each property listing includes detailed information such as location, amenities, rental prices, and others
   - Properties are displayed in a user-friendly and searchable format.

3. Booking System:
   - Students can search for available lodges based on their preferences (location, price, amenities, etc.).
   - Booking functionality allows students to reserve their preferred lodges.
   - Notifications and confirmation emails are sent to both students and landlords upon successful bookings.


## Getting Started

To get started with the Off-Campus Accommodation Portal, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```

2. Install the necessary dependencies:
   ```bash
   pip install -r requirement.txt
   ```

3. Set up the database:
   - Create a PostgreSQL or MySQL database for the project.
   - Update the database configuration in the `settings.py` file.

4. Run the application:
   ```bash
   python manage.py runserver
   ```

5. Access the application:
   - Open your web browser and navigate to `http://localhost:8000`.
   - The application should now be up and running.

## Technologies Used

The Off-Campus Accommodation Portal is built using the following technologies:

- **Django**: Python web framework for building the application.
- **HTML, CSS, JavaScript**: Front-end development for the user interface.
- **PostgreSQL or MySQL**: Database management system for storing data.
- **Django Rest Framework**: Enables building RESTful APIs for communication between front-end and back-end.
- **Authentication**: Django's built-in authentication system for user registration and login.
- **Payment**: Integration with a preferred payment gateway (e.g., PayPal, Stripe).

## Contact

If you have any questions, suggestions, or feedback, please feel free to reach out to our team at [your-email@example.com](mailto:your-email@example.com).

Thank you for choosing the Off-Campus Accommodation Portal! We hope it provides a valuable service for students seeking off-campus accommodation.
