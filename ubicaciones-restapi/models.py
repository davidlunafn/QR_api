from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class QrPlace(db.Model):
    __tablename__ = 'place'

    id_place = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False) 
    address = db.Column(db.String(50), nullable=False) 
    coordinate_N = db.Column(db.String(50), nullable=False) 
    coordinate_W = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    tipo = db.Column(db.String(50), nullable=False) 

    @classmethod
    def create(cls, data):
        qr = QrPlace(name=data['name'],
                            address=data['address'],
                            coordinate_N=data['coordinate_N'],
                            coordinate_W=data['coordinate_W'],
                            tipo=data['tipo'] )


        return qr.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self
        except:
            return False

    def json(self):
        return {
            'id_place': self.id_place,
            'name': self.name,
            'address': self.address,
            'coordinate_N': self.coordinate_N,
            'coordinate_W': self.coordinate_W,
            'created_at': self.created_at,
            'tipo': self.tipo,

        }



class Ubicaciones(db.Model):
    __tablename__ = 'ubicaciones'

    id = db.Column(db.Integer, primary_key=True)
    id_device = db.Column(db.String(50), nullable=False) 
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    id_place = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    @classmethod
    def create(cls, data):
        ubicacion = Ubicaciones(id_place=data['id_place'],id_device=data['id_device'],status=data['status'] )
        return ubicacion.save()

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()

            return self
        except:
            return False

    def json(self):
        return {
            'id': self.id,
            'id_place': self.id_place,
            'id_device': self.id_device,
            'status': self.status,
            'created_at': self.created_at
        }

