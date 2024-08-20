import pymysql
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt


# MySQL veritabanına bağlanma
def get_db_connection():
    return pymysql.connect(
        host="localhost",  # MySQL sunucu adresi
        user="root",  # MySQL kullanıcı adı
        password="",  # MySQL şifresi
        database="envanterys",  # Veritabanı adı
    )


# Envanter tahmini yapma
def forecast_inventory(product_id, user_id):
    connection = get_db_connection()

    # SQL sorgusu ile veri çekme
    query = """
    SELECT Date, InventoryLevel
    FROM inventory_data
    WHERE ProductID = %s AND UserID = %s
    """

    # Veriyi DataFrame olarak yükleme
    data = pd.read_sql(query, connection, params=(product_id, user_id))

    # Bağlantıyı kapatma
    connection.close()

    # Tarih formatını dönüştürme
    data["Date"] = pd.to_datetime(data["Date"])

    # Model için veri hazırlığı
    product_data = data[["Date", "InventoryLevel"]]
    product_data.rename(columns={"Date": "ds", "InventoryLevel": "y"}, inplace=True)

    # NaN değerlerini kontrol etme ve kaldırma
    print("NaN değer sayıları:")
    print(product_data.isna().sum())
    product_data = product_data.dropna()

    # Veri çerçevesinde yeterli veri olup olmadığını kontrol etme
    if len(product_data) < 2:
        raise ValueError(
            "Veri çerçevesinde yeterli veri bulunmuyor. Prophet modeli en az 2 veri noktası gerektirir."
        )

    # Modeli oluşturma
    model = Prophet()
    model.fit(product_data)

    # Gelecek dönemi oluşturma
    future = model.make_future_dataframe(periods=30)  # Örneğin, 30 gün ileriye tahmin

    # Tahmin yapma
    forecast = model.predict(future)

    # Sonuçları görselleştirme
    fig = model.plot(forecast)
    plt.title(
        f"Envanter Seviyeleri Tahmini (ProductID: {product_id}, UserID: {user_id})"
    )
    plt.xlabel("Tarih")
    plt.ylabel("Envanter Seviyesi")
    plt.show()


# Mevsimsel öneri yapma
def get_suggested_products(season):
    connection = get_db_connection()

    # Mevsimsel ürünleri çekme
    query = """
    SELECT DISTINCT ProductID, ProductName
    FROM inventory_data
    WHERE Season = %s LIMIT 5
    """

    # Veri çekme
    data = pd.read_sql(query, connection, params=(season,))

    # Bağlantıyı kapatma
    connection.close()

    return data


def main():
    # Öneri almak istenilen mevsimi tanımlama
    current_season = "İlkbahar"  # Örnek olarak 'Yaz' mevsimi

    # Öneri fonksiyonunu çağırma
    suggested_products = get_suggested_products(current_season)

    # Önerileri yazdırma
    if not suggested_products.empty:
        print(f"{current_season} mevsiminde daha önce envantere eklenen ürünler:")
        print(suggested_products)
    else:
        print(f"{current_season} mevsiminde envantere eklenen ürün bulunmuyor.")

    # Envanter tahmini yapma (Örnek: ProductID=1, UserID=3)
    forecast_inventory(product_id=7, user_id=1)


if __name__ == "__main__":
    main()
