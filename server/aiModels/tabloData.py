import pymysql
import random
from faker import Faker

# Veritabanı bağlantı bilgileri
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",  # Şifrenizi buraya ekleyin
    "database": "envanterys",  # Veritabanı adınızı buraya yazın
}

# Örnek veri listeleri
products = [
    "Deniz Şortu",
    "Kış Ceketi",
    "Sonbahar Botu",
    "Baharlık Mont",
    "Yazlık Elbise",
    "Yün Eldiven",
    "Trençkot",
    "Çiçekli Bluz",
    "Güneş Şapkası",
    "Sıcak Termal Üst",
    "Yüksek Bel Pantolon",
    "Gömlek Ceket",
    "Plaj Çantası",
    "Kışlık Çorap",
    "Küçük Çanta",
    "Kareli Gömlek",
    "Şapka",
    "Kürk Yelek",
    "Rüzgarlık",
    "Kombin Elbise",
    "Bikini",
    "Kış Botu",
    "Çizme",
    "Hırka",
    "Sandalet",
    "Kalın Kazak",
    "Bere",
    "Şort",
    "Yaz Tişörtü",
    "İsperme Mont",
    "Yüksek Bel Etek",
    "Yazlık Çanta",
    "Güneş Gözlüğü",
    "Sıcak Termal Çorap",
    "Süveter",
    "Hafif Ceket",
    "Kısa Şort",
    "Kışlık Şapka",
    "Palto",
    "Bluz",
    "Kapri",
    "Şal",
    "Etek",
    "Tişört",
]

user_ids = [1, 2, 3]

seasons = ["İlkbahar", "Yaz", "Sonbahar", "Kış"]

# Faker nesnesi
fake = Faker()

# Veritabanı bağlantısı
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

# SQL Insert komutu
insert_query = """
INSERT INTO inventory_data (UserID, Date, Season, ProductID, ProductName, InventoryLevel)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# SQL kontrol komutu
select_query = """
SELECT COUNT(*) FROM inventory_data 
WHERE UserID = %s AND Date = %s AND ProductID = %s
"""

# Veriyi oluşturup ekleme
for _ in range(150):  # 50 satır veri eklemek için döngü
    user_id = random.choice(user_ids)
    date = fake.date_this_month()
    season = random.choice(seasons)
    product_id = random.randint(1, len(products))  # Ürün ID'si
    product_name = products[product_id - 1]  # Ürün adı
    inventory_level = random.randint(30, 250)  # Stok seviyesi

    # Kayıt mevcut mu kontrol et
    cursor.execute(select_query, (user_id, date, product_id))
    if cursor.fetchone()[0] == 0:  # Kayıt bulunamazsa
        cursor.execute(
            insert_query,
            (user_id, date, season, product_id, product_name, inventory_level),
        )
    else:
        print(
            f"Veri zaten mevcut: UserID={user_id}, Date={date}, ProductID={product_id}"
        )

# Değişiklikleri kaydet ve bağlantıyı kapat
connection.commit()
connection.close()

print("Veri tabanına veri eklendi.")
