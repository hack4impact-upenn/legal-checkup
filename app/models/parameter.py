from .. import db

class Parameter(db.Model):
    __tablename__ = 'parameters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    param_type = db.Column(db.String(64))
    count = db.Column(db.Integer)

    def __init__(self, name, param_type, count):
        self.name = name
        self.param_type = param_type
        self.count = count

    def __repr__(self):
        return '<Parameter \'%s %s %s\'>' % (self.name, self.param_type, self.count)
