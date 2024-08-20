import pandas as pd
from collections import defaultdict, Counter
from sklearn.neighbors import NearestNeighbors
import numpy as np

data = [
    (1, "Kış Ceketi", "2024-01-10", "Kış"),
    (2, "Kar Botu", "2024-01-15", "Kış"),
    (3, "Isıtıcı", "2024-02-01", "Kış"),
    (4, "Bahçe Eldiveni", "2024-03-05", "İlkbahar"),
    (5, "Çim Biçme Makinesi", "2024-03-10", "İlkbahar"),
    (6, "Bahçe Feneri", "2024-04-01", "İlkbahar"),
    (7, "Plaj Havlusu", "2024-05-12", "Yaz"),
    (8, "Güneş Gözlüğü", "2024-06-20", "Yaz"),
    (9, "Serinletici Fan", "2024-07-15", "Yaz"),
    (10, "Deniz Ayakkabısı", "2024-08-22", "Yaz"),
    (11, "İç Mekan Halısı", "2024-09-01", "Sonbahar"),
    (12, "Okul Çantası", "2024-10-10", "Sonbahar"),
    (13, "Sıcak Çikolata Karışımı", "2024-11-15", "Kış"),
    (14, "Kışlık Termos", "2024-12-05", "Kış"),
    (15, "Elektrikli Battaniye", "2024-12-20", "Kış"),
    (16, "Kış Eldiveni", "2024-01-20", "Kış"),
    (17, "Kar Kayakları", "2024-02-15", "Kış"),
    (18, "Kış Şapkası", "2024-03-01", "Kış"),
    (19, "Bahçe Kürekleri", "2024-03-15", "İlkbahar"),
    (20, "Bahçe Sandalyeleri", "2024-04-10", "İlkbahar"),
    (21, "Bahçe Masası", "2024-05-01", "İlkbahar"),
    (22, "Plaj Şemsiyesi", "2024-06-15", "Yaz"),
    (23, "Su Geçirmez Çanta", "2024-07-05", "Yaz"),
    (24, "Serinletici Sprey", "2024-08-10", "Yaz"),
    (25, "Deniz Şortu", "2024-08-25", "Yaz"),
    (26, "Öğrenci Defteri", "2024-09-10", "Sonbahar"),
    (27, "Termal Çorap", "2024-10-01", "Sonbahar"),
    (28, "Sıcak Su Şişesi", "2024-11-05", "Kış"),
    (29, "Kışlık Mont", "2024-11-20", "Kış"),
    (30, "Kar Eşyaları", "2024-12-10", "Kış"),
    (31, "İlkbahar Elbiseleri", "2024-03-25", "İlkbahar"),
    (32, "Çiçek Sulama Sistemi", "2024-04-15", "İlkbahar"),
    (33, "Çim Tohumu", "2024-05-05", "İlkbahar"),
    (34, "Deniz Şapka", "2024-06-10", "Yaz"),
    (35, "Güneş Yağı", "2024-07-20", "Yaz"),
    (36, "Yazlık Terlik", "2024-08-15", "Yaz"),
    (37, "Sonbahar Montu", "2024-09-20", "Sonbahar"),
    (38, "Sonbahar Şal", "2024-10-05", "Sonbahar"),
    (39, "Termal Yatak Yastığı", "2024-11-25", "Kış"),
    (40, "Kışlık Çanta", "2024-12-15", "Kış"),
    (41, "Kış Eşarbı", "2024-01-25", "Kış"),
    (42, "Kar Dış Giyimi", "2024-02-20", "Kış"),
    (43, "Bahçe Teleskopu", "2024-03-20", "İlkbahar"),
    (44, "Bahçe Masası", "2024-04-20", "İlkbahar"),
    (45, "Plaj Çantası", "2024-05-25", "Yaz"),
    (46, "Su Şişesi", "2024-06-25", "Yaz"),
    (47, "Yazlık T-shirt", "2024-07-30", "Yaz"),
    (48, "Sonbahar Pantolonu", "2024-09-25", "Sonbahar"),
    (49, "İç Mekan Lambası", "2024-10-20", "Sonbahar"),
    (50, "Kış Spor Ayakkabısı", "2024-12-30", "Kış"),
]

# DataFrame oluşturun
df = pd.DataFrame(data, columns=["ID", "Ürün Adı", "Tarih", "Mevsim"])

# Mevsime göre gruplandırın
grouped = df.groupby("Mevsim")["Ürün Adı"].apply(list).reset_index()

# Mevsime göre ürünleri içeren bir sözlük oluşturun
seasonal_items = defaultdict(list)
for _, row in grouped.iterrows():
    seasonal_items[row["Mevsim"]] = row["Ürün Adı"]

# Frekanslı öğe çiftlerini oluşturun
pair_counter = defaultdict(Counter)
for items in seasonal_items.values():
    for i, item1 in enumerate(items):
        for item2 in items[i + 1 :]:
            pair_counter[item1][item2] += 1
            pair_counter[item2][item1] += 1

# KNN için veri hazırlığı
product_list = list(pair_counter.keys())
product_index = {product: idx for idx, product in enumerate(product_list)}

# KNN modelini oluştur
knn_data = np.zeros((len(product_list), len(product_list)))
for i, item1 in enumerate(product_list):
    for item2, count in pair_counter[item1].items():
        j = product_index[item2]
        knn_data[i, j] = count

knn = NearestNeighbors(n_neighbors=5, metric="cosine")
knn.fit(knn_data)


# Öneri fonksiyonu
def get_recommendations(product_name, knn_model, product_list, product_index):
    if product_name not in product_index:
        return "Ürün bulunamadı."

    idx = product_index[product_name]
    distances, indices = knn_model.kneighbors(knn_data[idx, :].reshape(1, -1))

    recommendations = []
    for i in indices.flatten():
        if i != idx:
            recommendations.append(product_list[i])

    return recommendations


# Örnek kullanım
if __name__ == "__main__":
    product_to_check = "Bahçe Kürekleri"
    print(
        f"Tavsiyeler ({product_to_check} için):",
        get_recommendations(product_to_check, knn, product_list, product_index),
    )
