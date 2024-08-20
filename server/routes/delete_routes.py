from flask import Blueprint, request, jsonify
from extensions import db
from models.inventory_data import InventoryData

bp = Blueprint("delete_routes", __name__)


@bp.route("/api/delete", methods=["POST"])
def delete():
    data = request.json
    try:
        # Ürün ID ve kullanıcı ID'ye göre filtreleme yaparak tüm kayıtları seç
        items = InventoryData.query.filter_by(
            ProductID=data["ProductID"], UserID=data["UserID"]
        ).all()

        if items:
            # Tüm bulunan kayıtları sil
            for item in items:
                db.session.delete(item)
            db.session.commit()
            response = {"status": "success", "message": "Ürün başarıyla silindi"}
        else:
            response = {"status": "error", "message": "Ürün bulunamadı"}
    except Exception as e:
        db.session.rollback()
        response = {"status": "error", "message": str(e)}

    return jsonify(response)
