from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}', weight='{self.weight}', quantity='{self.quantity}', price='{self.price}')"