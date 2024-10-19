from app import app
from models import db, Guest, Rooms, Reservation
from datetime import datetime, timedelta

def seed_data():
    with app.app_context():
        # Delete existing data
        db.session.query(Reservation).delete()
        db.session.query(Rooms).delete()
        db.session.query(Guest).delete()
        db.session.commit()

        # Seed guests
        guest1 = Guest(name='Alice Kimani', email='alice@example.com', phone='+123456789012')
        guest2 = Guest(name='Bob Otieno', email='bob@example.com', phone='+123456789013')
        guest3 = Guest(name='Cynthia Mwangi', email='cynthia@example.com', phone='+123456789014')

        db.session.add_all([guest1, guest2, guest3])
        db.session.commit()

        # Seed rooms with images
        room1 = Rooms(room_number=101, room_type='single', price_per_night=50, status='available', image='/static/images/room1.jpg')
        room2 = Rooms(room_number=102, room_type='double', price_per_night=75, status='available', image='/static/images/room2.jpg')
        room3 = Rooms(room_number=103, room_type='suite', price_per_night=150, status='occupied', image='/static/images/room3.jpg')

        db.session.add_all([room1, room2, room3])
        db.session.commit()

        # Seed reservations
        reservation1 = Reservation(
            check_in_date=datetime.now() + timedelta(days=5),
            check_out_date=datetime.now() + timedelta(days=10),
            total_price=200,
            guest_id=guest1.id,
            room_id=room1.id
        )
        reservation2 = Reservation(
            check_in_date=datetime.now() + timedelta(days=6),
            check_out_date=datetime.now() + timedelta(days=11),
            total_price=300,
            guest_id=guest2.id,
            room_id=room2.id
        )

        db.session.add_all([reservation1, reservation2])
        db.session.commit()

seed_data()