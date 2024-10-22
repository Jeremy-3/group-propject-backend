from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
import re
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.String(12), nullable=False, unique=True)  # Changed to String to preserve leading zeros
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # Relationship
    reservations = db.relationship('Reservation', back_populates='guests', cascade='all, delete-orphan')

    # Validations
    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Invalid email address')
        
        if len(email) > 50:
            raise ValueError('Email address too long')
        
        return email
    
    @validates('phone')
    def validate_phone(self, key, phone):
        if len(str(phone)) != 12:
            raise ValueError('Phone number must be 12 digits')
        phone_regex = r'^\d{12}$'
        if not re.match(phone_regex, str(phone)):
            raise ValueError('Invalid phone number format')
        return phone

    # Specify serialization rules
    serialize_rules = ('-reservations.guests',)  


class Rooms(db.Model, SerializerMixin):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.Integer, nullable=False, unique=True)
    room_type = db.Column(db.String, nullable=False)
    price_per_night = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) 
    image = db.Column(db.String, nullable=False)   

    # Relationships
    reservations = db.relationship('Reservation', back_populates='rooms', cascade='all, delete-orphan')

    # Validations
    @validates('room_type')
    def validate_room_type(self, key, room_type):
        if room_type not in ['single', 'double', 'suite']:
            raise ValueError('Invalid room type')
        return room_type

    @validates('status')
    def validate_status(self, key, status):
        if status not in ['available', 'occupied', 'under_maintenance']:
            raise ValueError('Invalid status')
        return status

    # Serialization rules
    serialize_rules = ('-reservations.rooms',)  


class Reservation(db.Model, SerializerMixin):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())    

    # Relationships
    guests = db.relationship('Guest', back_populates='reservations')
    rooms = db.relationship('Rooms', back_populates='reservations')   

    # Validations
    @validates('check_in_date', 'check_out_date')
    def validate_dates(self, key, date):
        # Strip any leading/trailing spaces
        date = date.strip() 
        try:
            # Convert the string to a datetime object (use '%Y-%m-%d' or '%Y-%m-%d %H:%M:%S' based on your input)
            date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            # Raise error if the format is wrong
            raise ValueError(f'Invalid date format for {key}. Expected YYYY-MM-DD HH:MM:SS.')
        # Compare the parsed date object to the current time
        if date_obj < datetime.now():
            raise ValueError(f'{key.capitalize()} cannot be in the past.')
        return date_obj  # Return the datetime object
    @validates('total_price')
    def validate_total_price(self, key, total_price):
        if total_price < 0:
            raise ValueError('Total price cannot be negative')
        return total_price

    # Serialization rules
    serialize_rules = ('-guests.reservations', '-rooms.reservations')
    
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Role: 'admin' or 'user'
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)