from app import db


class Product(db.Model):
    __tablename__ = "products"
    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductName = db.Column(db.String(100), nullable=False)
