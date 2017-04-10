from .. import db

class ApiParameterLink(db.Model):
    __tablename__ = 'api_parameter_link'
    api_id = db.Column(db.Integer, db.ForeignKey('api.id'), primary_key=True)
    parameter_id = db.Column(db.Integer, db.ForeignKey('parameter.id'), primary_key=True)
    parameter_description = db.Column(String(128))
    api = db.relationship('Api', backref=db.backref('parameter_associations'))
    parameter = db.relationship('Parameter', backref=db.backref('api_associations'))

    def __init__(self, api, param, description):
        self.api = api
        self.parameter = param
        self.parameter_description = description

    def __repr__(self):
        return '<ApiParameterLink \'%s %s %s\'>' % (self.api.name, self.parameter.name,
            self.parameter_description)

class Api(db.Model):
    __tablename__ = 'apis'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    region = db.Column(db.String(64))
    description = db.Column(db.String(128))
    parameters = db.relationship('Parameter', secondary='api_parameter_link')

    def add_params(self, params):
        for param, description in params:
            self.api_parameter_link.append(ApiParameterLink(api=self,
                param=param, description=description))

    def __init__(self, name, region, description):
        self.name = name
        self.region = region
        self.description = description

    def __repr__(self):
        return '<Api \'%s %s %s\'>' % (self.name, self.region, self.description)

class Parameter(db.Model):
    __tablename__ = 'parameters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    param_type = db.Column(db.String(64))
    count = db.Column(db.Integer)
    apis = db.relationship('Api', secondary='api_parameter_link')

    def __init__(self, name, param_type, count):
        self.name = name
        self.param_type = param_type
        self.count = count

    def __repr__(self):
        return '<Parameter \'%s %s %s\'>' % (self.name, self.param_type,
            self.count)
