from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    
    # add Relationship
    reservations = db.relationship('Reservation', back_populates='guests')

    # add Validations
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
        
        phone_regex = r'^\+\d{12}$'
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
    price_per_night = db.Column(db.Numeric, nullable=False)
    status = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())    

    # add Relationships
    reservations = db.relationship('Reservation', back_populates='rooms')

    # add Validations
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

    #  serialization rules
    serialize_rules = ('-reservations.rooms',)  


class Reservation(db.Model, SerializerMixin):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    check_in_date = db.Column(db.DateTime, nullable=False)
    check_out_date = db.Column(db.DateTime, nullable=False)
    total_price = db.Column(db.Numeric, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())    

    # add Relationships
    guests = db.relationship('Guest', back_populates='reservations')
    rooms = db.relationship('Rooms', back_populates='reservations')   

    # add Validations
    @validates('check_in_date', 'check_out_date')
    def validate_dates(self, key, date):
        if date < db.func.current_timestamp():
            raise ValueError(f'{key.capitalize()} date cannot be in the past')
        return date

    @validates('total_price')
    def validate_total_price(self, key, total_price):
        if total_price < 0:
            raise ValueError('Total price cannot be negative')
        return total_price

    # serialization rules
    serialize_rules = ('-guests.reservations', '-rooms.reservations') 
