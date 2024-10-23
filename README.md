# 🏨 Hotel Management System Backend
Welcome to the Hotel Management System backend! This project is designed to be the central management system for a hotel, allowing you to efficiently handle rooms, bookings, guests, and staff. The backend is built using Flask, a lightweight and powerful web framework, with SQLAlchemy for database management and JWT-based authentication for secure access.

## 🚀 Project Overview
Our hotel management system helps hotels streamline their operations by automating key functions such as:

- Room management (availability, pricing, room types)
- Booking management (check-in, check-out, guest details)
- Guest management (personal information, booking history)
- Staff management (roles, login, and authentication)
- User authentication with JWT tokens for secure login and session handling
- Custom error handling for smooth user experience

## 🎯 Features
Here’s a quick breakdown of the features our system provides:

1. **Room Management**
Add, update, delete, or retrieve hotel rooms.
Manage room types (Single, Double, Suite, etc.).
Keep track of room availability and pricing.
2. **Guest Management**
Store and manage guest information (name, email, phone).
Retrieve guest booking history and current stays.
Add new guests when they check in.
3. **Booking Management**
Create and manage hotel bookings.
Track check-in and check-out dates for guests.
Associate each booking with a specific room and guest.
4. **Staff Management**
Staff can log in and access different system features based on their role.
5. **JWT Authentication**
Secure authentication using JSON Web Tokens (JWT).
Staff members can sign up and log in.
Sessions are protected, and token-based authentication ensures secure access.
## 🛠️ Technologies Used
The backend is built using modern technologies to ensure performance, scalability, and maintainability:

- **Flask:** A lightweight and flexible web framework for building robust applications.
**SQLAlchemy:** A powerful ORM (Object-Relational Mapping) library for interacting with the database.
**Flask-Migrate:** For managing database migrations and schema changes.
**JWT (JSON Web Tokens):** Secure and scalable authentication method.
**SQLite:** A simple and lightweight database for storing data.
## 🔥 Getting Started
To get the backend up and running on your local machine, follow these steps:

1. **Clone the Repository**
```bash
git clone https://github.com/Jeremy-3/group-propject-backend.git
```
2. **Set Up Your Environment**
It’s recommended to use a virtual environment for your project dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install Dependencies**
Install all the required Python packages listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```
4. **Database Setup**
Before running the application, set up the database:

- *Initialize the database:*

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```
- *Seed the database:*
```bash
python seed.py
```

5. **Running the Application**
Now can run the server:

```bash
python app.py
```
The application will run on http://localhost:5000. 🎉

## 📖 API Documentation
This project follows the RESTful API design, with different endpoints for each feature. Here’s a quick guide to the available API routes:

## 🏨 Rooms
GET /api/rooms - Retrieve all rooms.
POST /api/rooms - Add a new room.
PUT /api/rooms/
- Update room details.
DELETE /api/rooms/
- Delete a room.
## 👤 Guests
GET /api/guests - Retrieve all guests.
POST /api/guests - Add a new guest.
## 🛏️ Bookings
GET /api/bookings - Retrieve all bookings.
POST /api/bookings - Create a new booking.

## 📝 Contributing
We welcome contributions to make this project even better! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bug fix (`git checkout -b feature-name`).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to your branch (git push origin feature-name).
5. Create a Pull Request and describe the changes in detail.

## 🛠️ Deployment
This project can be deployed using platforms like Heroku, Vercel, or AWS. Ensure that the database is set up appropriately and the necessary environment variables (like SECRET_KEY and DATABASE_URI) are configured.

## 🎉 Future Enhancements
Here are some exciting features that could be added in future iterations of this project:

- Payment integration for guests during booking.
- Advanced reporting to track room occupancy and guest statistics.
-  Role-based access control to limit what certain staff members can do.
- Email notifications to inform guests about their bookings or changes.
- Automated room cleaning management for housekeeping staff.
## 🙏 Acknowledgments
Flask for being an awesome Python framework.
SQLAlchemy for making database interactions smooth.
Flask-Migrate for managing database migrations with ease.
The open-source community for the amazing resources and libraries used in this project.
## 📜 License
This project is licensed under the MIT License. Feel free to use and modify it as you see fit!

## 🧐 Questions?
Feel free to open an issue if you find a bug or have a feature request. We’re also happy to receive feedback to improve the system!

Let’s build an amazing hotel management system together! 🏨✨

## ✍️ Authors

1. Elvis Kimani
2. Jeremy Gitau
3. Tony Maina
4. Keith Mwai
5. Franklin Ndegwa