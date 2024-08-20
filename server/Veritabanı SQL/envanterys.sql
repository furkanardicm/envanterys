-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 20 Ağu 2024, 13:15:40
-- Sunucu sürümü: 10.4.32-MariaDB
-- PHP Sürümü: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `envanterys`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `inventory_data`
--

CREATE TABLE `inventory_data` (
  `UserID` int(11) NOT NULL,
  `Date` date NOT NULL,
  `Season` enum('Yaz','İlkbahar','Kış','Sonbahar') DEFAULT NULL,
  `ProductID` int(11) NOT NULL,
  `ProductName` varchar(255) DEFAULT NULL,
  `InventoryLevel` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `inventory_data`
--

INSERT INTO `inventory_data` (`UserID`, `Date`, `Season`, `ProductID`, `ProductName`, `InventoryLevel`) VALUES
(1, '2024-08-01', 'Yaz', 8, 'Çiçekli Bluz', 76),
(1, '2024-08-01', 'Kış', 10, 'Sıcak Termal Üst', 64),
(1, '2024-08-01', 'Kış', 19, 'Rüzgarlık', 89),
(1, '2024-08-01', 'Kış', 21, 'Bikini', 128),
(1, '2024-08-01', 'İlkbahar', 30, 'İsperme Mont', 112),
(1, '2024-08-01', 'Sonbahar', 33, 'Güneş Gözlüğü', 138),
(1, '2024-08-01', 'Yaz', 34, 'Sıcak Termal Çorap', 80),
(1, '2024-08-01', 'Kış', 35, 'Süveter', 227),
(1, '2024-08-01', 'Sonbahar', 41, 'Kapri', 170),
(1, '2024-08-02', 'Yaz', 7, 'Trençkot', 239),
(1, '2024-08-02', 'Yaz', 11, 'Yüksek Bel Pantolon', 118),
(1, '2024-08-02', 'Sonbahar', 16, 'Kareli Gömlek', 97),
(1, '2024-08-02', 'Kış', 17, 'Şapka', 69),
(1, '2024-08-02', 'Kış', 18, 'Kürk Yelek', 142),
(1, '2024-08-02', 'İlkbahar', 20, 'Kombin Elbise', 201),
(1, '2024-08-02', 'Kış', 23, 'Çizme', 102),
(1, '2024-08-02', 'İlkbahar', 28, 'Şort', 137),
(1, '2024-08-02', 'Sonbahar', 32, 'Yazlık Çanta', 143),
(1, '2024-08-02', 'İlkbahar', 34, 'Sıcak Termal Çorap', 142),
(1, '2024-08-02', 'Yaz', 39, 'Palto', 71),
(1, '2024-08-03', 'İlkbahar', 8, 'Çiçekli Bluz', 31),
(1, '2024-08-03', 'İlkbahar', 10, 'Sıcak Termal Üst', 94),
(1, '2024-08-03', 'İlkbahar', 18, 'Kürk Yelek', 124),
(1, '2024-08-03', 'Yaz', 26, 'Kalın Kazak', 144),
(1, '2024-08-03', 'Kış', 30, 'İsperme Mont', 157),
(1, '2024-08-03', 'Kış', 31, 'Yüksek Bel Etek', 97),
(1, '2024-08-03', 'Kış', 34, 'Sıcak Termal Çorap', 111),
(1, '2024-08-03', 'Sonbahar', 39, 'Palto', 157),
(1, '2024-08-03', 'Yaz', 40, 'Bluz', 139),
(1, '2024-08-03', 'İlkbahar', 41, 'Kapri', 103),
(1, '2024-08-04', 'Sonbahar', 1, 'Deniz Şortu', 132),
(1, '2024-08-04', 'Sonbahar', 7, 'Trençkot', 114),
(1, '2024-08-04', 'Sonbahar', 18, 'Kürk Yelek', 72),
(1, '2024-08-04', 'Kış', 20, 'Kombin Elbise', 206),
(1, '2024-08-04', 'İlkbahar', 22, 'Kış Botu', 113),
(1, '2024-08-04', 'Yaz', 23, 'Çizme', 126),
(1, '2024-08-04', 'İlkbahar', 26, 'Kalın Kazak', 92),
(1, '2024-08-04', 'Kış', 29, 'Yaz Tişörtü', 92),
(1, '2024-08-04', 'Yaz', 31, 'Yüksek Bel Etek', 54),
(1, '2024-08-04', 'Kış', 32, 'Yazlık Çanta', 79),
(1, '2024-08-04', 'Kış', 33, 'Güneş Gözlüğü', 83),
(1, '2024-08-04', 'Yaz', 39, 'Palto', 122),
(1, '2024-08-04', 'İlkbahar', 41, 'Kapri', 128),
(1, '2024-08-05', 'Kış', 6, 'Yün Eldiven', 174),
(1, '2024-08-05', 'Sonbahar', 7, 'Trençkot', 160),
(1, '2024-08-05', 'Yaz', 8, 'Çiçekli Bluz', 90),
(1, '2024-08-05', 'Sonbahar', 11, 'Yüksek Bel Pantolon', 130),
(1, '2024-08-05', 'Kış', 13, 'Plaj Çantası', 97),
(1, '2024-08-05', 'İlkbahar', 14, 'Kışlık Çorap', 91),
(1, '2024-08-05', 'Yaz', 15, 'Küçük Çanta', 147),
(1, '2024-08-05', 'Kış', 17, 'Şapka', 136),
(1, '2024-08-05', 'Yaz', 22, 'Kış Botu', 117),
(1, '2024-08-05', 'Sonbahar', 23, 'Çizme', 74),
(1, '2024-08-05', 'İlkbahar', 28, 'Şort', 82),
(1, '2024-08-05', 'İlkbahar', 33, 'Güneş Gözlüğü', 131),
(1, '2024-08-05', 'Yaz', 37, 'Kısa Şort', 50),
(1, '2024-08-05', 'İlkbahar', 42, 'Şal', 81),
(1, '2024-08-05', 'Kış', 44, 'Tişört', 91),
(1, '2024-08-06', 'Kış', 3, 'Sonbahar Botu', 124),
(1, '2024-08-06', 'İlkbahar', 5, 'Yazlık Elbise', 124),
(1, '2024-08-06', 'Kış', 9, 'Güneş Şapkası', 135),
(1, '2024-08-06', 'Sonbahar', 15, 'Küçük Çanta', 184),
(1, '2024-08-06', 'Sonbahar', 16, 'Kareli Gömlek', 138),
(1, '2024-08-06', 'Yaz', 18, 'Kürk Yelek', 54),
(1, '2024-08-06', 'Sonbahar', 24, 'Hırka', 236),
(1, '2024-08-06', 'Kış', 25, 'Sandalet', 133),
(1, '2024-08-06', 'İlkbahar', 33, 'Güneş Gözlüğü', 168),
(1, '2024-08-06', 'İlkbahar', 38, 'Kışlık Şapka', 120),
(1, '2024-08-06', 'İlkbahar', 42, 'Şal', 154),
(1, '2024-08-06', 'İlkbahar', 43, 'Etek', 121),
(1, '2024-08-07', 'İlkbahar', 4, 'Baharlık Mont', 55),
(1, '2024-08-07', 'Sonbahar', 5, 'Yazlık Elbise', 150),
(1, '2024-08-07', 'Kış', 6, 'Yün Eldiven', 245),
(1, '2024-08-07', 'Kış', 7, 'Trençkot', 145),
(1, '2024-08-07', 'Yaz', 9, 'Güneş Şapkası', 69),
(1, '2024-08-07', 'İlkbahar', 11, 'Yüksek Bel Pantolon', 120),
(1, '2024-08-07', 'Sonbahar', 19, 'Rüzgarlık', 69),
(1, '2024-08-07', 'Yaz', 21, 'Bikini', 117),
(1, '2024-08-07', 'Kış', 24, 'Hırka', 113),
(1, '2024-08-07', 'Yaz', 29, 'Yaz Tişörtü', 129),
(1, '2024-08-07', 'Kış', 30, 'İsperme Mont', 231),
(1, '2024-08-07', 'Sonbahar', 37, 'Kısa Şort', 51),
(1, '2024-08-07', 'İlkbahar', 39, 'Palto', 113),
(1, '2024-08-07', 'Sonbahar', 44, 'Tişört', 66),
(1, '2024-08-08', 'İlkbahar', 6, 'Yün Eldiven', 143),
(1, '2024-08-08', 'Yaz', 7, 'Trençkot', 161),
(1, '2024-08-08', 'Sonbahar', 14, 'Kışlık Çorap', 54),
(1, '2024-08-08', 'Kış', 15, 'Küçük Çanta', 124),
(1, '2024-08-08', 'Kış', 16, 'Kareli Gömlek', 64),
(1, '2024-08-08', 'Kış', 21, 'Bikini', 64),
(1, '2024-08-08', 'Kış', 25, 'Sandalet', 30),
(1, '2024-08-08', 'İlkbahar', 26, 'Kalın Kazak', 68),
(1, '2024-08-08', 'Kış', 29, 'Yaz Tişörtü', 164),
(1, '2024-08-08', 'İlkbahar', 33, 'Güneş Gözlüğü', 139),
(1, '2024-08-08', 'İlkbahar', 35, 'Süveter', 110),
(1, '2024-08-09', 'Yaz', 43, 'Etek', 130),
(1, '2024-08-20', 'İlkbahar', 56, 'Kalemtraş', 90),
(2, '2024-08-01', 'Sonbahar', 3, 'Sonbahar Botu', 147),
(2, '2024-08-01', 'Kış', 8, 'Çiçekli Bluz', 191),
(2, '2024-08-01', 'Kış', 10, 'Sıcak Termal Üst', 144),
(2, '2024-08-01', 'İlkbahar', 14, 'Kışlık Çorap', 72),
(2, '2024-08-01', 'Kış', 16, 'Kareli Gömlek', 160),
(2, '2024-08-01', 'Kış', 19, 'Rüzgarlık', 92),
(2, '2024-08-01', 'Yaz', 24, 'Hırka', 122),
(2, '2024-08-01', 'Yaz', 25, 'Sandalet', 77),
(2, '2024-08-01', 'İlkbahar', 26, 'Kalın Kazak', 165),
(2, '2024-08-01', 'Yaz', 27, 'Bere', 207),
(2, '2024-08-01', 'İlkbahar', 31, 'Yüksek Bel Etek', 163),
(2, '2024-08-01', 'Kış', 36, 'Hafif Ceket', 93),
(2, '2024-08-01', 'Kış', 40, 'Bluz', 223),
(2, '2024-08-01', 'Yaz', 43, 'Etek', 118),
(2, '2024-08-01', 'Yaz', 44, 'Tişört', 175),
(2, '2024-08-02', 'Yaz', 2, 'Kış Ceketi', 66),
(2, '2024-08-02', 'Kış', 4, 'Baharlık Mont', 139),
(2, '2024-08-02', 'Sonbahar', 14, 'Kışlık Çorap', 73),
(2, '2024-08-02', 'İlkbahar', 15, 'Küçük Çanta', 199),
(2, '2024-08-02', 'Yaz', 18, 'Kürk Yelek', 140),
(2, '2024-08-02', 'İlkbahar', 19, 'Rüzgarlık', 162),
(2, '2024-08-02', 'Yaz', 20, 'Kombin Elbise', 65),
(2, '2024-08-02', 'İlkbahar', 25, 'Sandalet', 161),
(2, '2024-08-02', 'Sonbahar', 26, 'Kalın Kazak', 94),
(2, '2024-08-02', 'İlkbahar', 31, 'Yüksek Bel Etek', 175),
(2, '2024-08-02', 'Sonbahar', 32, 'Yazlık Çanta', 72),
(2, '2024-08-02', 'Sonbahar', 33, 'Güneş Gözlüğü', 63),
(2, '2024-08-02', 'Yaz', 36, 'Hafif Ceket', 98),
(2, '2024-08-02', 'İlkbahar', 40, 'Bluz', 125),
(2, '2024-08-02', 'Kış', 43, 'Etek', 100),
(2, '2024-08-03', 'Yaz', 3, 'Sonbahar Botu', 162),
(2, '2024-08-03', 'İlkbahar', 5, 'Yazlık Elbise', 229),
(2, '2024-08-03', 'Sonbahar', 10, 'Sıcak Termal Üst', 117),
(2, '2024-08-03', 'Yaz', 11, 'Yüksek Bel Pantolon', 88),
(2, '2024-08-03', 'Yaz', 18, 'Kürk Yelek', 228),
(2, '2024-08-03', 'Sonbahar', 21, 'Bikini', 207),
(2, '2024-08-03', 'Kış', 27, 'Bere', 60),
(2, '2024-08-03', 'Kış', 38, 'Kışlık Şapka', 103),
(2, '2024-08-03', 'Yaz', 43, 'Etek', 175),
(2, '2024-08-04', 'Kış', 2, 'Kış Ceketi', 130),
(2, '2024-08-04', 'Yaz', 3, 'Sonbahar Botu', 176),
(2, '2024-08-04', 'Sonbahar', 4, 'Baharlık Mont', 66),
(2, '2024-08-04', 'Sonbahar', 5, 'Yazlık Elbise', 132),
(2, '2024-08-04', 'Kış', 8, 'Çiçekli Bluz', 119),
(2, '2024-08-04', 'Kış', 10, 'Sıcak Termal Üst', 105),
(2, '2024-08-04', 'Yaz', 12, 'Gömlek Ceket', 100),
(2, '2024-08-04', 'İlkbahar', 20, 'Kombin Elbise', 82),
(2, '2024-08-04', 'İlkbahar', 21, 'Bikini', 149),
(2, '2024-08-04', 'Kış', 25, 'Sandalet', 230),
(2, '2024-08-04', 'Yaz', 38, 'Kışlık Şapka', 73),
(2, '2024-08-04', 'İlkbahar', 42, 'Şal', 121),
(2, '2024-08-04', 'Sonbahar', 44, 'Tişört', 81),
(2, '2024-08-05', 'Yaz', 4, 'Baharlık Mont', 150),
(2, '2024-08-05', 'İlkbahar', 8, 'Çiçekli Bluz', 125),
(2, '2024-08-05', 'İlkbahar', 11, 'Yüksek Bel Pantolon', 71),
(2, '2024-08-05', 'Kış', 16, 'Kareli Gömlek', 102),
(2, '2024-08-05', 'Sonbahar', 17, 'Şapka', 175),
(2, '2024-08-05', 'Sonbahar', 18, 'Kürk Yelek', 239),
(2, '2024-08-05', 'Yaz', 37, 'Kısa Şort', 161),
(2, '2024-08-05', 'Sonbahar', 38, 'Kışlık Şapka', 92),
(2, '2024-08-06', 'Yaz', 3, 'Sonbahar Botu', 96),
(2, '2024-08-06', 'Sonbahar', 4, 'Baharlık Mont', 101),
(2, '2024-08-06', 'Yaz', 7, 'Trençkot', 136),
(2, '2024-08-06', 'Yaz', 16, 'Kareli Gömlek', 108),
(2, '2024-08-06', 'Sonbahar', 20, 'Kombin Elbise', 224),
(2, '2024-08-06', 'Kış', 21, 'Bikini', 96),
(2, '2024-08-06', 'Sonbahar', 32, 'Yazlık Çanta', 53),
(2, '2024-08-06', 'İlkbahar', 33, 'Güneş Gözlüğü', 101),
(2, '2024-08-06', 'Yaz', 35, 'Süveter', 124),
(2, '2024-08-06', 'Sonbahar', 41, 'Kapri', 113),
(2, '2024-08-07', 'Sonbahar', 5, 'Yazlık Elbise', 72),
(2, '2024-08-07', 'Yaz', 7, 'Trençkot', 96),
(2, '2024-08-07', 'İlkbahar', 14, 'Kışlık Çorap', 70),
(2, '2024-08-07', 'Sonbahar', 18, 'Kürk Yelek', 156),
(2, '2024-08-07', 'Yaz', 21, 'Bikini', 149),
(2, '2024-08-07', 'Sonbahar', 23, 'Çizme', 96),
(2, '2024-08-07', 'Kış', 29, 'Yaz Tişörtü', 130),
(2, '2024-08-07', 'Yaz', 33, 'Güneş Gözlüğü', 154),
(2, '2024-08-07', 'Yaz', 42, 'Şal', 115),
(2, '2024-08-07', 'Kış', 43, 'Etek', 189),
(2, '2024-08-08', 'Sonbahar', 6, 'Yün Eldiven', 125),
(2, '2024-08-08', 'Yaz', 10, 'Sıcak Termal Üst', 105),
(2, '2024-08-08', 'Yaz', 11, 'Yüksek Bel Pantolon', 67),
(2, '2024-08-08', 'Kış', 15, 'Küçük Çanta', 113),
(2, '2024-08-08', 'Kış', 20, 'Kombin Elbise', 112),
(2, '2024-08-08', 'Yaz', 21, 'Bikini', 130),
(2, '2024-08-08', 'Yaz', 32, 'Yazlık Çanta', 66),
(2, '2024-08-08', 'Kış', 39, 'Palto', 139),
(2, '2024-08-08', 'Kış', 40, 'Bluz', 116),
(3, '2024-08-01', 'Yaz', 9, 'Güneş Şapkası', 192),
(3, '2024-08-01', 'Yaz', 11, 'Yüksek Bel Pantolon', 107),
(3, '2024-08-01', 'İlkbahar', 14, 'Kışlık Çorap', 102),
(3, '2024-08-01', 'Kış', 15, 'Küçük Çanta', 63),
(3, '2024-08-01', 'Kış', 16, 'Kareli Gömlek', 143),
(3, '2024-08-01', 'Sonbahar', 20, 'Kombin Elbise', 81),
(3, '2024-08-01', 'Sonbahar', 21, 'Bikini', 166),
(3, '2024-08-01', 'İlkbahar', 24, 'Hırka', 240),
(3, '2024-08-01', 'İlkbahar', 25, 'Sandalet', 80),
(3, '2024-08-01', 'Kış', 26, 'Kalın Kazak', 148),
(3, '2024-08-01', 'Kış', 27, 'Bere', 96),
(3, '2024-08-01', 'Yaz', 31, 'Yüksek Bel Etek', 97),
(3, '2024-08-01', 'Kış', 34, 'Sıcak Termal Çorap', 115),
(3, '2024-08-01', 'İlkbahar', 38, 'Kışlık Şapka', 116),
(3, '2024-08-01', 'Sonbahar', 39, 'Palto', 30),
(3, '2024-08-01', 'Sonbahar', 41, 'Kapri', 136),
(3, '2024-08-02', 'Sonbahar', 3, 'Sonbahar Botu', 157),
(3, '2024-08-02', 'Kış', 9, 'Güneş Şapkası', 146),
(3, '2024-08-02', 'Sonbahar', 14, 'Kışlık Çorap', 144),
(3, '2024-08-02', 'Yaz', 15, 'Küçük Çanta', 136),
(3, '2024-08-02', 'Kış', 20, 'Kombin Elbise', 76),
(3, '2024-08-02', 'Kış', 21, 'Bikini', 64),
(3, '2024-08-02', 'İlkbahar', 26, 'Kalın Kazak', 117),
(3, '2024-08-02', 'Sonbahar', 30, 'İsperme Mont', 172),
(3, '2024-08-02', 'Kış', 32, 'Yazlık Çanta', 71),
(3, '2024-08-03', 'Yaz', 4, 'Baharlık Mont', 244),
(3, '2024-08-03', 'Kış', 13, 'Plaj Çantası', 165),
(3, '2024-08-03', 'İlkbahar', 14, 'Kışlık Çorap', 141),
(3, '2024-08-03', 'Sonbahar', 15, 'Küçük Çanta', 50),
(3, '2024-08-03', 'Yaz', 21, 'Bikini', 62),
(3, '2024-08-03', 'Sonbahar', 25, 'Sandalet', 105),
(3, '2024-08-03', 'İlkbahar', 29, 'Yaz Tişörtü', 44),
(3, '2024-08-03', 'Yaz', 34, 'Sıcak Termal Çorap', 84),
(3, '2024-08-03', 'Kış', 36, 'Hafif Ceket', 76),
(3, '2024-08-03', 'Kış', 38, 'Kışlık Şapka', 60),
(3, '2024-08-03', 'İlkbahar', 41, 'Kapri', 113),
(3, '2024-08-04', 'Kış', 13, 'Plaj Çantası', 131),
(3, '2024-08-04', 'Kış', 15, 'Küçük Çanta', 132),
(3, '2024-08-04', 'Sonbahar', 16, 'Kareli Gömlek', 112),
(3, '2024-08-04', 'Sonbahar', 18, 'Kürk Yelek', 210),
(3, '2024-08-04', 'Sonbahar', 19, 'Rüzgarlık', 59),
(3, '2024-08-04', 'Sonbahar', 23, 'Çizme', 80),
(3, '2024-08-04', 'Sonbahar', 35, 'Süveter', 232),
(3, '2024-08-04', 'İlkbahar', 41, 'Kapri', 65),
(3, '2024-08-04', 'Yaz', 42, 'Şal', 44),
(3, '2024-08-04', 'Sonbahar', 43, 'Etek', 53),
(3, '2024-08-05', 'Kış', 5, 'Yazlık Elbise', 137),
(3, '2024-08-05', 'İlkbahar', 9, 'Güneş Şapkası', 63),
(3, '2024-08-05', 'Yaz', 10, 'Sıcak Termal Üst', 61),
(3, '2024-08-05', 'Yaz', 11, 'Yüksek Bel Pantolon', 227),
(3, '2024-08-05', 'İlkbahar', 14, 'Kışlık Çorap', 94),
(3, '2024-08-05', 'Sonbahar', 16, 'Kareli Gömlek', 54),
(3, '2024-08-05', 'Kış', 18, 'Kürk Yelek', 35),
(3, '2024-08-05', 'Yaz', 28, 'Şort', 115),
(3, '2024-08-05', 'Kış', 29, 'Yaz Tişörtü', 99),
(3, '2024-08-05', 'İlkbahar', 31, 'Yüksek Bel Etek', 49),
(3, '2024-08-06', 'Kış', 5, 'Yazlık Elbise', 113),
(3, '2024-08-06', 'Yaz', 12, 'Gömlek Ceket', 195),
(3, '2024-08-06', 'İlkbahar', 13, 'Plaj Çantası', 68),
(3, '2024-08-06', 'Yaz', 21, 'Bikini', 238),
(3, '2024-08-06', 'Yaz', 23, 'Çizme', 236),
(3, '2024-08-06', 'İlkbahar', 24, 'Hırka', 138),
(3, '2024-08-06', 'Sonbahar', 26, 'Kalın Kazak', 114),
(3, '2024-08-06', 'Kış', 28, 'Şort', 106),
(3, '2024-08-06', 'İlkbahar', 33, 'Güneş Gözlüğü', 191),
(3, '2024-08-06', 'Sonbahar', 39, 'Palto', 138),
(3, '2024-08-06', 'Yaz', 42, 'Şal', 121),
(3, '2024-08-07', 'Kış', 5, 'Yazlık Elbise', 158),
(3, '2024-08-07', 'Kış', 10, 'Sıcak Termal Üst', 120),
(3, '2024-08-07', 'Kış', 14, 'Kışlık Çorap', 95),
(3, '2024-08-07', 'Sonbahar', 16, 'Kareli Gömlek', 111),
(3, '2024-08-07', 'Sonbahar', 17, 'Şapka', 88),
(3, '2024-08-07', 'Yaz', 20, 'Kombin Elbise', 55),
(3, '2024-08-07', 'Sonbahar', 26, 'Kalın Kazak', 106),
(3, '2024-08-07', 'İlkbahar', 30, 'İsperme Mont', 189),
(3, '2024-08-07', 'Sonbahar', 33, 'Güneş Gözlüğü', 111),
(3, '2024-08-07', 'Kış', 35, 'Süveter', 236),
(3, '2024-08-07', 'Sonbahar', 40, 'Bluz', 63),
(3, '2024-08-08', 'Yaz', 21, 'Bikini', 87),
(3, '2024-08-08', 'Yaz', 22, 'Kış Botu', 111),
(3, '2024-08-08', 'İlkbahar', 26, 'Kalın Kazak', 70),
(3, '2024-08-08', 'Sonbahar', 30, 'İsperme Mont', 65),
(3, '2024-08-08', 'Kış', 32, 'Yazlık Çanta', 123),
(3, '2024-08-08', 'Sonbahar', 44, 'Tişört', 74),
(4, '2024-08-15', 'Yaz', 17, 'Şapka', 57),
(4, '2024-08-15', 'Yaz', 43, 'Etek', 150),
(4, '2024-08-15', 'İlkbahar', 50, 'Biberon', 21),
(4, '2024-08-15', 'İlkbahar', 51, 'Kanca', 46),
(4, '2024-08-15', 'Sonbahar', 52, 'Kolye', 100),
(4, '2024-08-15', 'Kış', 53, 'Akıllı Saat', 51);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `products`
--

CREATE TABLE `products` (
  `ProductID` int(11) NOT NULL,
  `ProductName` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `products`
--

INSERT INTO `products` (`ProductID`, `ProductName`) VALUES
(1, 'Deniz Şortu'),
(2, 'Kış Ceketi'),
(3, 'Sonbahar Botu'),
(4, 'Baharlık Mont'),
(5, 'Yazlık Elbise'),
(6, 'Yün Eldiven'),
(7, 'Trençkot'),
(8, 'Çiçekli Bluz'),
(9, 'Güneş Şapkası'),
(10, 'Sıcak Termal Üst'),
(11, 'Yüksek Bel Pantolon'),
(12, 'Gömlek Ceket'),
(13, 'Plaj Çantası'),
(14, 'Kışlık Çorap'),
(15, 'Küçük Çanta'),
(16, 'Kareli Gömlek'),
(17, 'Şapka'),
(18, 'Kürk Yelek'),
(19, 'Rüzgarlık'),
(20, 'Kombin Elbise'),
(21, 'Bikini'),
(22, 'Kış Botu'),
(23, 'Çizme'),
(24, 'Hırka'),
(25, 'Sandalet'),
(26, 'Kalın Kazak'),
(27, 'Bere'),
(28, 'Şort'),
(29, 'Yaz Tişörtü'),
(30, 'İsperme Mont'),
(31, 'Yüksek Bel Etek'),
(32, 'Yazlık Çanta'),
(33, 'Güneş Gözlüğü'),
(34, 'Sıcak Termal Çorap'),
(35, 'Süveter'),
(36, 'Hafif Ceket'),
(37, 'Kısa Şort'),
(38, 'Kışlık Şapka'),
(39, 'Palto'),
(40, 'Bluz'),
(41, 'Kapri'),
(42, 'Şal'),
(43, 'Etek'),
(44, 'Tişört'),
(45, 'Su Şişesi'),
(46, 'Telefon Kılıfı'),
(47, 'Telefon Tutacağı'),
(49, 'Tuzluk'),
(50, 'Biberon'),
(51, 'Kanca'),
(52, 'Kolye'),
(53, 'Akıllı Saat'),
(54, 'Tarak'),
(55, 'Limon Sıkacağı'),
(56, 'Kalemtraş');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `users`
--

CREATE TABLE `users` (
  `userid` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fullname` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_turkish_ci;

--
-- Tablo döküm verisi `users`
--

INSERT INTO `users` (`userid`, `email`, `password`, `fullname`) VALUES
(1, 'furkanardcm@gmail.com', '$2b$12$MpzaXS.rdinOMMzjQHJWXuf8IH2r9qEg1PFEqQ0ROMYSYBL5UoFp.', 'Muhammed Furkan Ardıç'),
(2, 'x@x.com', '$2b$12$8LQSVtA9FmrBMmN1m2ic8O3qD7Dodlqw1psBH92ERjdGxUSXeeCAS', 'x'),
(3, 'fake@fake.com', '$2b$12$MpzaXS.rdinOMMzjQHJWXuf8IH2r9qEg1PFEqQ0ROMYSYBL5UoFp.', 'Jhon Doe'),
(4, 'deneme@123.com', '$2b$12$IdaiVdQqRktki0VqVkBszuOGaLus1VSF4xwea0PA6ZeMnub3z2zQa', 'Ali Veli');

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `inventory_data`
--
ALTER TABLE `inventory_data`
  ADD PRIMARY KEY (`UserID`,`Date`,`ProductID`);

--
-- Tablo için indeksler `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`ProductID`);

--
-- Tablo için indeksler `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`userid`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `products`
--
ALTER TABLE `products`
  MODIFY `ProductID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- Tablo için AUTO_INCREMENT değeri `users`
--
ALTER TABLE `users`
  MODIFY `userid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
