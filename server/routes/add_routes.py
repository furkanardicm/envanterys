from flask import Blueprint, request, jsonify
from app import db
from models.product import Product
from models.inventory_data import InventoryData
from datetime import datetime

bp = Blueprint("add_routes", __name__)


@bp.route("/api/add", methods=["POST"])
def add():
    data = request.json
    try:
        # Ürün olup olmadığını kontrol et ve gerekirse ekle
        product = Product.query.filter_by(ProductName=data["ProductName"]).first()
        if not product:
            product = Product(ProductName=data["ProductName"])
            db.session.add(product)
            db.session.commit()

        # Ürün ID'sini al
        product_id = product.ProductID

        # Mevcut envanter verisini kontrol et
        existing_inventory = InventoryData.query.filter_by(
            UserID=data["UserID"],
            Date=datetime.strptime(data["Date"], "%Y-%m-%d"),
            ProductID=product_id,
        ).first()

        if existing_inventory:
            # Mevcut veriyi güncelle
            existing_inventory.InventoryLevel += data["InventoryLevel"]
        else:
            # Mevcut envanter verisi yoksa, en yakın tarihli ürünü bul
            closest_inventory = (
                InventoryData.query.filter_by(
                    UserID=data["UserID"], ProductID=product_id
                )
                .order_by(InventoryData.Date.desc())
                .first()
            )

            # Eğer en yakın tarihli ürün bulunursa, onun InventoryLevel'ını ekle
            if closest_inventory:
                previous_inventory_level = closest_inventory.InventoryLevel
            else:
                previous_inventory_level = 0

            # Yeni envanter verisi ekle
            new_inventory = InventoryData(
                UserID=data["UserID"],
                Date=datetime.strptime(data["Date"], "%Y-%m-%d"),
                Season=data["Season"],
                ProductID=product_id,
                ProductName=data["ProductName"],
                InventoryLevel=data["InventoryLevel"] + previous_inventory_level,
            )
            db.session.add(new_inventory)

        db.session.commit()
        response = {
            "status": "success",
            "message": "Ürün başarıyla eklendi veya güncellendi",
            "ProductID": product_id,  # ProductID'yi yanıt olarak döndür
        }
    except Exception as e:
        db.session.rollback()
        response = {"status": "error", "message": str(e)}
    return jsonify(response)
