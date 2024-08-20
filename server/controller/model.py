import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sqlalchemy import create_engine

# SQLAlchemy veritabanı motoru oluştur
engine = create_engine("mysql+pymysql://root:@localhost/envanterys")


def train_knn_model():
    query = """
    SELECT ProductID, ProductName, Season
    FROM inventory_data
    """
    data = pd.read_sql(query, engine)

    # Özellikleri ve etiketleri ayır
    X = data[["ProductID"]]  # Özellikler (bu örnekte sadece ProductID kullanıyoruz)
    y = data["Season"]  # Etiketler (Mevsim)

    # KNN modelini oluştur ve eğit
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X, y)

    return knn


def recommend_products(season, product_id):
    model = train_knn_model()

    query = """
    SELECT ProductID, ProductName
    FROM inventory_data
    WHERE Season = %s AND ProductID != %s
    """
    data = pd.read_sql(query, engine, params=(season, product_id))

    X_new = data[["ProductID"]]
    recommendations = model.predict(X_new)
    data["Recommendation"] = recommendations

    # Mevsim ile aynı ürünleri filtrele
    recommended_products = data[data["Recommendation"] == season]

    return recommended_products.to_dict(orient="records")
