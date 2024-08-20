from extensions import db


class Product(db.Model):
    __tablename__ = "products"
    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductName = db.Column(
        db.String(100), nullable=False, unique=True
    )  # Ürün adı tekil olmalı


class InventoryData(db.Model):
    __tablename__ = "inventory_data"
    UserID = db.Column(db.Integer, nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Season = db.Column(db.String(20), nullable=False)
    ProductID = db.Column(
        db.Integer, db.ForeignKey("products.ProductID"), nullable=False
    )
    InventoryLevel = db.Column(db.Integer, nullable=False)
    # ProductName burada redundant olabilir çünkü Product tablosunda var
    # Ancak, özel bir neden varsa tutulabilir
    ProductName = db.Column(db.String(100), nullable=False)

    # Bir ürünle ilişki kurar
    product = db.relationship(
        "Product", backref=db.backref("inventory_data", lazy=True)
    )

    # Birincil anahtar olarak (UserID, Date, ProductID) kombinasyonunu kullanabiliriz
    __table_args__ = (db.PrimaryKeyConstraint("UserID", "Date", "ProductID"),)
