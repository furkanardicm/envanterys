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

        if new_product_name:
            # Aynı isimde başka bir ürün olup olmadığını kontrol et
            existing_product = Product.query.filter_by(
                ProductName=new_product_name
            ).first()
            print("İşte: ", existing_product)

            if existing_product:
                # Eğer aynı isimde başka ürün varsa ve ProductID'leri farklıysa hata döndür
                if int(existing_product.ProductID) != int(product_id):
                    print("Hataya Sebep Olan:")
                    print(f"Mevcut Ürün ID: {existing_product.ProductID}")
                    print(f"Güncellenmek İstenilen Ürün ID: {product_id}")
                    return (
                        jsonify(
                            {
                                "status": "error",
                                "message": "Bu ürün adıyla başka bir ürün mevcut",
                            }
                        ),
                        400,
                    )
                # Eğer aynı isim ve aynı ProductID'ye sahip ürün varsa, en güncel olanı bulup güncelle
                else:
                    current_item = (
                        InventoryData.query.filter_by(
                            ProductID=product_id, UserID=user_id
                        )
                        .order_by(InventoryData.Date.desc())
                        .first()
                    )
                    if current_item:
                        current_item.InventoryLevel = new_inventory_level
                        current_item.Season = new_season

            else:
                # Eğer isim değiştirilecekse ve aynı isimde başka ürün yoksa, ürünün adını güncelle
                product = Product.query.filter_by(ProductID=product_id).first()
                if product:
                    product.ProductName = new_product_name

                # Güncellenmiş ürünün en güncel olanını bul ve güncelle
                current_item = (
                    InventoryData.query.filter_by(ProductID=product_id, UserID=user_id)
                    .order_by(InventoryData.Date.desc())
                    .first()
                )
                if current_item:
                    current_item.ProductName = new_product_name
                    current_item.InventoryLevel = new_inventory_level
                    current_item.Season = new_season

        else:
            # Ürün adı değişmemişse, sadece en güncel olanın envanter seviyesini ve sezonu güncelle
            item.InventoryLevel = new_inventory_level
            item.Season = new_season

        db.session.commit()
        response = {"status": "success", "message": "Ürün başarıyla güncellendi"}

    except SQLAlchemyError as e:
        db.session.rollback()
        response = {"status": "error", "message": f"Veritabanı hatası: {str(e)}"}

    return jsonify(response)
