from db import db


class FairModel(db.Model):
    __tablename__ = 'fairs'

    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.String(100))
    latitude = db.Column(db.String(100))
    setcens = db.Column(db.String(100))
    areap = db.Column(db.String(100))
    coddist = db.Column(db.String(100))
    distrito = db.Column(db.String(100))
    codsubpref = db.Column(db.String(100))
    subpref = db.Column(db.String(100))
    regiao5 = db.Column(db.String(100))
    regiao8 = db.Column(db.String(100))
    nome_feira = db.Column(db.String(100))
    registro = db.Column(db.String(100))
    logradouro = db.Column(db.String(100))
    numero = db.Column(db.String(100))
    bairro = db.Column(db.String(100))
    referencia = db.Column(db.String(100))

    def __init__(self, longitude, latitude,
                 setcens, areap, coddist,
                 distrito, codsubpref, subpref,
                 regiao5, regiao8, nome_feira,
                 registro, logradouro, numero,
                 bairro, referencia):
        self.longitude = longitude
        self.latitude = latitude
        self.setcens = setcens
        self.areap = areap
        self.coddist = coddist
        self.distrito = distrito
        self.codsubpref = codsubpref
        self.subpref = subpref
        self.regiao5 = regiao5
        self.regiao8 = regiao8
        self.nome_feira = nome_feira
        self.registro = registro
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.referencia = referencia

    def json(self):
        return {
            'id': self.id,
            'longitude': self.longitude,
            'latitude': self.latitude,
            'setcens': self.setcens,
            'areap': self.areap,
            'coddist': self.coddist,
            'distrito': self.distrito,
            'codsubpref': self.codsubpref,
            'subpref': self.subpref,
            'regiao5': self.regiao5,
            'regiao8': self.regiao8,
            'nome_feira': self.nome_feira,
            'registro': self.registro,
            'logradouro': self.logradouro,
            'numero': self.numero,
            'bairro': self.bairro,
            'referencia': self.referencia,
        }

    @classmethod
    def find_by_id(cls, fair_id):
        return cls.query.filter_by(id=fair_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
