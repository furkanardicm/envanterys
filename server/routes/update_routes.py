from flask import Blueprint, request, jsonify
from extensions import db
from models.inventory_data import InventoryData
from models.product import Product

bp = Blueprint("update_routes", __name__)


@bp.route("/api/update", methods=["PUT"])
def update():
    data = request.json
    try:
        # Ürün ID'si ve kullanıcı ID'sine göre envanter verisini bul
        item = InventoryData.query.filter_by(
            ProductID=data["ProductID"], UserID=data["UserID"]
        ).first()

        if not item:
            return jsonify({"status": "error", "message": "Ürün bulunamadı"}), 404

        # Yeni ürün adıyla aynı isimde bir ürün olup olmadığını kontrol et
        existing_product = Product.query.filter_by(
            ProductName=data["ProductName"]
        ).first()
        if existing_product and existing_product.ProductID != data["ProductID"]:
            existing_product.InventoryLevel = data["InventoryLevel"]
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "Bu ürün adıyla başka bir ürün mevcut",
                    }
                ),
                400,
            )

        # Envanter verisini güncelle
        item.InventoryLevel = data["InventoryLevel"]
        item.Season = data["Season"]

        # Ürün adını güncelle
        product = Product.query.filter_by(ProductID=data["ProductID"]).first()
        if product:
            product.ProductName = data["ProductName"]

        db.session.commit()
        response = {"status": "success", "message": "Ürün başarıyla güncellendi"}
    except Exception as e:
        db.session.rollback()
        response = {"status": "error", "message": str(e)}

    return jsonify(response)
