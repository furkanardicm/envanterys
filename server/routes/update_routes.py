from flask import Blueprint, request, jsonify
from extensions import db
from models.inventory_data import InventoryData
from models.product import Product
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint("update_routes", __name__)


@bp.route("/api/update", methods=["PUT"])
def update():
    data = request.json
    product_id = data.get("ProductID")
    user_id = data.get("UserID")
    new_product_name = data.get("ProductName")
    new_inventory_level = data.get("InventoryLevel")
    new_season = data.get("Season")

    try:
        # Envanter verisini bul
        item = (
            InventoryData.query.filter_by(ProductID=product_id, UserID=user_id)
            .order_by(InventoryData.Date.desc())
            .first()
        )

        if not item:
            return (
                jsonify({"status": "error", "message": "Envanter verisi bulunamadı"}),
                404,
            )

        # Ürün adı değişmişse, çakışmaları kontrol et
        if new_product_name:
            # Aynı isimde başka bir ürün olup olmadığını kontrol et
            existing_product = Product.query.filter_by(
                ProductName=new_product_name
            ).first()

            if existing_product and existing_product.ProductID != product_id:
                return (
                    jsonify(
                        {
                            "status": "error",
                            "message": "Bu ürün adıyla başka bir ürün mevcut",
                        }
                    ),
                    400,
                )

            # Ürün adını güncelle
            product = Product.query.filter_by(ProductID=product_id).first()
            inventory_data = (
                InventoryData.query.filter_by(ProductID=product_id, UserID=user_id)
                .order_by(InventoryData.Date.desc())
                .first()
            )
            if product:
                product.ProductName = new_product_name
                inventory_data.ProductName = new_product_name

        # Envanter verisini güncelle
        item.InventoryLevel = new_inventory_level
        item.Season = new_season

        db.session.commit()
        response = {"status": "success", "message": "Ürün başarıyla güncellendi"}

    except SQLAlchemyError as e:
        db.session.rollback()
        response = {"status": "error", "message": str(e)}

    return jsonify(response)
