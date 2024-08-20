from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Veritabanı ayarları
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/envanterys"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__ = "products"
    ProductID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProductName = db.Column(db.String(100), nullable=False)


class InventoryData(db.Model):
    __tablename__ = "inventory_data"
    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, nullable=False)
    Date = db.Column(db.Date, nullable=False)
    Season = db.Column(db.String(20), nullable=False)
    ProductID = db.Column(
        db.Integer, db.ForeignKey("products.ProductID"), nullable=False
    )
    ProductName = db.Column(db.String(100), nullable=False)
    InventoryLevel = db.Column(db.Integer, nullable=False)
    product = db.relationship(
        "Product", backref=db.backref("inventory_data", lazy=True)
    )


@app.route("/api/select", methods=["GET"])
def select():
    try:
        results = InventoryData.query.all()
        data = [
            {
                "ID": item.ID,
                "UserID": item.UserID,
                "Date": item.Date.strftime("%Y-%m-%d"),
                "Season": item.Season,
                "ProductID": item.ProductID,
                "ProductName": item.ProductName,
                "InventoryLevel": item.InventoryLevel,
            }
            for item in results
        ]
        response = {"status": "success", "data": data}
    except Exception as e:
        response = {"status": "error", "message": str(e)}
    return jsonify(response)


@app.route("/api/update", methods=["POST"])
def update():
    data = request.json
    try:
        item = InventoryData.query.filter_by(ProductID=data["ID"]).first()
        if item:
            item.ProductName = data["ProductName"]
            item.InventoryLevel = data["InventoryLevel"]
            item.Season = data["Season"]
            db.session.commit()
            response = {"status": "success", "message": "Ürün başarıyla güncellendi"}
        else:
            response = {"status": "error", "message": "Ürün bulunamadı"}
    except Exception as e:
        response = {"status": "error", "message": str(e)}
    return jsonify(response)


@app.route("/api/delete", methods=["POST"])
def delete():
    data = request.json
    try:
        item = InventoryData.query.filter_by(ProductID=data["ID"]).first()
        if item:
            db.session.delete(item)
            db.session.commit()
            response = {"status": "success", "message": "Ürün başarıyla silindi"}
        else:
            response = {"status": "error", "message": "Ürün bulunamadı"}
    except Exception as e:
        response = {"status": "error", "message": str(e)}
    return jsonify(response)


@app.route("/api/add", methods=["POST"])
def add():
    data = request.json
    try:
        new_product = Product(ProductName=data["ProductName"])
        db.session.add(new_product)
        db.session.commit()

        new_inventory = InventoryData(
            UserID=data["UserID"],
            Date=datetime.strptime(data["Date"], "%Y-%m-%d"),
            Season=data["Season"],
            ProductID=new_product.ProductID,
            ProductName=data["ProductName"],
            InventoryLevel=data["InventoryLevel"],
        )
        db.session.add(new_inventory)
        db.session.commit()

        response = {"status": "success", "message": "Ürün başarıyla eklendi"}
    except Exception as e:
        response = {"status": "error", "message": str(e)}
    return jsonify(response)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Bu sadece ilk çalıştırmada gerekli
    app.run(port=5001, debug=True)
