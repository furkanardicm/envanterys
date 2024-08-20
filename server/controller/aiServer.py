from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from prophet import Prophet

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # İzin verilen kaynaklar ve URL'ler


def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="envanterys"
    )


@app.route("/api/forecast", methods=["POST"])
def get_forecast():
    data = request.json
    product_id = data.get("ProductID")
    user_id = data.get("UserID")

    if not product_id or not user_id:
        return jsonify({"error": "ProductID ve UserID gereklidir"}), 400

    conn = get_db_connection()

    query = """
    SELECT Date, InventoryLevel
    FROM inventory_data
    WHERE ProductID = %s AND UserID = %s
    """
    try:
        df = pd.read_sql(query, conn, params=(product_id, user_id))
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500

    conn.close()

    if df.empty:
        return (
            jsonify({"error": "No data found for the specified ProductID and UserID"}),
            404,
        )

    df["Date"] = pd.to_datetime(df["Date"])
    df.rename(columns={"Date": "ds", "InventoryLevel": "y"}, inplace=True)
    df = df.dropna()

    if len(df) < 2:
        return jsonify({"error": "Yetersiz veri"}), 400

    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=30)
    forecast = model.predict(future)
    forecast_data = forecast[["ds", "yhat"]].to_dict(orient="records")

    return jsonify(forecast_data)


@app.route("/api/recommendations", methods=["GET"])
def get_recommendations():
    season = request.args.get("season")
    product_id = request.args.get("productID")
    user_id = request.args.get("userID")

    if not season or not product_id or not user_id:
        return jsonify({"error": "Season, ProductID ve UserID gereklidir"}), 400

    conn = get_db_connection()

    query = """
    SELECT UserID, Date, Season, ProductID, ProductName, InventoryLevel
    FROM inventory_data
    """
    try:
        df = pd.read_sql(query, conn)
    except Exception as e:
        conn.close()
        return jsonify({"error": str(e)}), 500

    conn.close()

    # Veriyi işleme
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.month
    df["Year"] = df["Date"].dt.year

    # Kullanıcıya özel filtreleme
    user_df = df[df["UserID"] == int(user_id)]
    filtered_df = user_df[user_df["Season"].str.lower() == season.lower()]

    if filtered_df.empty:
        return (
            jsonify(
                {
                    "error": f"No data found for the userID {user_id} and season: {season}"
                }
            ),
            404,
        )

    # Özellikler ve hedef değişkenler
    features = filtered_df[["UserID", "ProductID", "Month", "Year"]]
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    def recommend_similar_products(product_id, features_scaled, filtered_df):
        if filtered_df[filtered_df["ProductID"] == product_id].empty:
            return pd.DataFrame()  # Boş bir DataFrame döndür

        product_index = filtered_df[filtered_df["ProductID"] == product_id].index[0]
        product_features = features_scaled[filtered_df["ProductID"] == product_id]

        # Benzerlik hesaplama
        similarities = cosine_similarity([product_features[0]], features_scaled)

        # Benzerliklere göre sıralama
        similar_products = pd.DataFrame(
            {"ProductID": filtered_df["ProductID"], "Similarity": similarities[0]}
        ).sort_values(by="Similarity", ascending=False)

        # Eşiği geçmeyen ürünleri filtreleme
        recommended_products = similar_products[
            (similar_products["ProductID"] != product_id)
            & (similar_products["Similarity"] >= 0.6)
        ]

        # Tekrarlayan ürün ID'lerini kaldırma
        recommended_products = recommended_products.drop_duplicates(subset="ProductID")

        return recommended_products.head(15)  # İlk 15 benzer ürünü döndür

    # Öneri yapma
    recommended_products = recommend_similar_products(
        int(product_id), features_scaled, filtered_df
    )

    if not recommended_products.empty:
        return jsonify(recommended_products.to_dict(orient="records"))
    else:
        return (
            jsonify(
                {
                    "error": f"No similar products found for ProductID {product_id} in season {season} with similarity >= 0.6"
                }
            ),
            404,
        )


if __name__ == "__main__":
    app.run(port=5002, debug=True)
