from .. import db

association_table = db.Table('association_table',
    db.Column('api_id', db.Integer, db.ForeignKey('api.id')),
    db.Column('parameter_id', db.Integer, db.ForeignKey('parameter.id'))
    db.Column('parameter_description', db.String(128),
        db.ForeignKey('parameter_description.id'))
)

class Api(db.Model):
    __tablename__ = 'apis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    region = db.Column(db.String(64))
    description = db.Column(db.String(128))
    parameters = db.relationship(
        'Parameter',
        secondary=association_table,
        backref=db.backref('parameters', lazy='dynamic'))

    def __init__(self, name, region, description):
        self.name = name
        self.region = region
        self.description = description

    def __repr__(self):
        return '<Api \'%s %s %s\'>' % (self.name, self.region, self.description)
