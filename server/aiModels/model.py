import mysql.connector
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
import numpy as np

# Veritabanı bağlantısı
conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="envanterys"
)

# Ürün verisini çekme
query = """
SELECT UserID, Date, Season, ProductID, ProductName, InventoryLevel
FROM inventory_data
"""
df = pd.read_sql(query, conn)

# Veriyi işleme
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year

# Kullanıcının belirttiği ürün ve mevsim
input_product_id = 43
input_season = "Yaz"  # Burada doğru sezon değerini kullanın

# Benzer ürünleri bulmak için mevsime göre filtreleme
filtered_df = df[df["Season"].str.lower() == input_season.lower()]

# Veri kontrolü
if filtered_df.empty:
    print(f"No data found for the season: {input_season}")
    conn.close()
    exit()

# Özellikler ve hedef değişkenler
features = filtered_df[["UserID", "ProductID", "Month", "Year"]]
target = filtered_df["InventoryLevel"]

# Özelliklerin ölçeklendirilmesi
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)


# Kullanıcıya öneri fonksiyonu
def recommend_similar_products(product_id, features_scaled, filtered_df):
    if filtered_df[filtered_df["ProductID"] == product_id].empty:
        print(f"No data found for ProductID: {product_id}")
        return pd.DataFrame()  # Boş bir DataFrame döndür

    product_index = filtered_df[filtered_df["ProductID"] == product_id].index[0]
    product_features = features_scaled[filtered_df["ProductID"] == product_id]

    # Benzerlik hesaplama
    similarities = cosine_similarity([product_features[0]], features_scaled)

    # Benzerliklere göre sıralama
    similar_products = pd.DataFrame(
        {"ProductID": filtered_df["ProductID"], "Similarity": similarities[0]}
    ).sort_values(by="Similarity", ascending=False)

    # Veritabanındaki mevcut ürünü hariç tutma
    recommended_products = similar_products[similar_products["ProductID"] != product_id]
    return recommended_products.head(10)  # İlk 10 benzer ürünü döndür


# Öneri yapma
recommended_products = recommend_similar_products(
    input_product_id, features_scaled, filtered_df
)

if not recommended_products.empty:
    print(
        f"Recommended products similar to ProductID {input_product_id} for season {input_season}:"
    )
    print(recommended_products)
else:
    print(
        f"No similar products found for ProductID {input_product_id} in season {input_season}"
    )

# Veritabanı bağlantısını kapatma
conn.close()
