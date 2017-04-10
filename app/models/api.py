from .. import db

class Association(db.Model):
    __tablename__ = 'assocation'
    api_id = Column(Integer, ForeignKey('api.id'), primary_key=True)
    parameter_id = Column(Integer, ForeignKey('parameter.id'), primary_key=True)
    parameter_description = Column(String(128))
    parameter = db.relationship('Parameter', backref='api_associations')

    def __init__(self, parameter_description):
        self.parameter_description = parameter_description

    def __repr__(self):
        return '<Association \'%s %s %s\'>' % (self.api_id, self.parameter_id,
            self.parameter_description)

class Api(db.Model):
    __tablename__ = 'apis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    region = db.Column(db.String(64))
    description = db.Column(db.String(128))
    parameters = db.relationship(
        'Association',
        backref=db.backref('parameter', lazy='dynamic'))

    def __init__(self, name, region, description):
        self.name = name
        self.region = region
        self.description = description

    def __repr__(self):
        return '<Api \'%s %s %s\'>' % (self.name, self.region, self.description)
