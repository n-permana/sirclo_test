from sirclo import db
from datetime import datetime

class BeratBadan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tanggal = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    max = db.Column(db.Float)
    min = db.Column(db.Float)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'tanggal': self.tanggal,
            'max': "{0:.1f}".format(self.max),
            'min': "{0:.1f}".format(self.min),
            'range': "{0:.1f}".format(self.max - self.min)
        }
    