from flask import Blueprint, jsonify
from models.inventory_data import InventoryData
from sqlalchemy import func
from app import db

bp = Blueprint("select_routes", __name__)


@bp.route("/api/select/<int:userID>", methods=["GET"])
def select(userID):
    try:
        # Alt sorgu: her ürün için en güncel tarihi seç
        subquery = (
            db.session.query(
                InventoryData.ProductID, func.max(InventoryData.Date).label("max_date")
            )
            .filter(InventoryData.UserID == userID)
            .group_by(InventoryData.ProductID)
            .subquery()
        )

        # Ana sorgu: en güncel tarihli ürünleri seç
        data = (
            db.session.query(InventoryData)
            .join(
                subquery,
                (InventoryData.ProductID == subquery.c.ProductID)
                & (InventoryData.Date == subquery.c.max_date),
            )
            .filter(InventoryData.UserID == userID)
            .all()
        )

        return jsonify({"status": "success", "data": [item.to_dict() for item in data]})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})
