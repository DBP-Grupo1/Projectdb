from app import db
from datetime import datetime

DEFAULT_RESERVATION_LENGTH = 2 # 2 horas
MAX_TABLE_CAPACITY = 8 # 8 personas

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(8),nullable=False)
    telefono = db.Column(db.String(80), index=True, unique=True)
    def __repr__(self):
        return f'<Person: {self.id},{self.username},{self.email},{self.password}>'
    
class Mesa(db.Model):
    __tablename__ = 'mesa'
    id = db.Column(db.Integer, primary_key=True)
    capacidad = db.Column(db.Integer, index=True)

class Reservacion(db.Model):
    __tablename__ = 'reservacion'
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')
    mesa_id = db.Column(db.Integer, db.ForeignKey('mesa.id'))
    mesa = db.relationship('Mesa')
    num_personas = db.Column(db.Integer, index=True)
    hora_reservacion = db.Column(db.DateTime, index=True)

db.create_all()
