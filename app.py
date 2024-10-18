#!/usr/bin/env python3

from models import db, Guest, Rooms, Reservation 
from flask_migrate import Migrate
from flask import Flask, request, make_response, jsonify
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'hotel.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate after db is initialized
migrate = Migrate(app, db)

@app.route('/')
def index():
    return '<h1>Welcome to Hotel Management System</h1>'

# CRUD for Guests
@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    response_data = [guest.to_dict() for guest in guests]
    return make_response(jsonify(response_data), 200)

@app.route('/guests/<int:id>', methods=['GET'])
def get_guest(id):
    guest = db.session.get(Guest, id)
    if guest:
        return make_response(jsonify(guest.to_dict()), 200)
    return jsonify({'error': 'Guest not found'}), 404

@app.route('/guests', methods=['POST'])
def create_guest():
    data = request.get_json()
    try:
        new_guest = Guest(
            name=data['name'],
            email=data['email'],
            phone=data['phone']
        )
        db.session.add(new_guest)
        db.session.commit()
        return make_response(jsonify(new_guest.to_dict()), 201)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/guests/<int:id>', methods=['PATCH'])
def update_guest(id):
    guest = db.session.get(Guest, id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404

    data = request.get_json()
    if 'name' in data:
        guest.name = data['name']
    if 'email' in data:
        try:
            guest.email = data['email']
        except ValueError as e:
            return jsonify({'error': str(e)}), 400
    if 'phone' in data:
        try:
            guest.phone = data['phone']
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

    db.session.commit()
    return make_response(jsonify(guest.to_dict()), 200)

@app.route('/guests/<int:id>', methods=['DELETE'])
def delete_guest(id):
    guest = db.session.get(Guest, id)
    if not guest:
        return jsonify({'error': 'Guest not found'}), 404
    db.session.delete(guest)
    db.session.commit()
    return make_response('', 204)

# CRUD for Rooms
@app.route('/rooms', methods=['GET'])
def get_rooms():
    rooms = Rooms.query.all()
    response_data = [room.to_dict() for room in rooms]
    return make_response(jsonify(response_data), 200)

@app.route('/rooms/<int:id>', methods=['GET'])
def get_room(id):
    room = db.session.get(Rooms, id)
    if room:
        return jsonify(room.to_dict()), 200
    return jsonify({'error': 'Room not found'}), 404

@app.route('/rooms', methods=['POST'])
def create_room():
    data = request.get_json()
    try:
        new_room = Rooms(
            room_number=data['room_number'],
            room_type=data['room_type'],
            price_per_night=data['price_per_night'],
            status=data['status']
        )
        db.session.add(new_room)
        db.session.commit()
        return make_response(jsonify(new_room.to_dict()), 201)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rooms/<int:id>', methods=['DELETE'])
def delete_room(id):
    room = db.session.get(Rooms, id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    db.session.delete(room)
    db.session.commit()
    return make_response('', 204)

# CRUD for Reservations
@app.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    response_data = [reservation.to_dict() for reservation in reservations]
    return make_response(jsonify(response_data), 200)

@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    reservation = db.session.get(Reservation, id)
    if reservation:
        return jsonify(reservation.to_dict()), 200
    return jsonify({'error': 'Reservation not found'}), 404

@app.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.get_json()
    try:
        new_reservation = Reservation(
            check_in_date=data['check_in_date'],
            check_out_date=data['check_out_date'],
            total_price=data['total_price'],
            guest_id=data['guest_id'],
            room_id=data['room_id']
        )
        db.session.add(new_reservation)
        db.session.commit()
        return make_response(jsonify(new_reservation.to_dict()), 201)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/reservations/<int:id>', methods=['DELETE'])
def delete_reservation(id):
    reservation = db.session.get(Reservation, id)
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404
    db.session.delete(reservation)
    db.session.commit()
    return make_response('', 204)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
