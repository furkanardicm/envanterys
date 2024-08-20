from app import db


class InventoryData(db.Model):
    __tablename__ = "inventory_data"

    UserID = db.Column(db.Integer, nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Season = db.Column(db.String(20), nullable=False)
    ProductID = db.Column(db.Integer, nullable=False)
    ProductName = db.Column(db.String(100), nullable=False)
    InventoryLevel = db.Column(db.Integer, nullable=False)

    # Birincil anahtar olarak (UserID, Date, ProductID) kombinasyonu
    __table_args__ = (db.PrimaryKeyConstraint("UserID", "Date", "ProductID"),)

    def to_dict(self):
        return {
            "UserID": self.UserID,
            "Date": self.Date,
            "Season": self.Season,
            "ProductID": self.ProductID,
            "ProductName": self.ProductName,
            "InventoryLevel": self.InventoryLevel,
        }
