from flask import Flask, request, session, jsonify
import mysql.connector
from mysql.connector import errorcode
from flask_session import Session
from flask_cors import CORS
import bcrypt
import os

app = Flask(__name__)

# Konfigürasyon
app.secret_key = os.urandom(24)
app.config["SESSION_TYPE"] = "filesystem"

# MySQL bağlantı ayarları
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DB = "envanterys"

# CORS'u etkinleştirin
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
# Session yapılandırması
sess = Session(app)


# MySQL bağlantısını kurma
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD, database=MYSQL_DB
        )
        return connection
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Kullanıcı adı veya şifre yanlış")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Veritabanı bulunamadı")
        else:
            print(err)


@app.route("/api/register", methods=["POST"])
def register():
    data = request.json
    fullname = data["fullname"]
    password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    email = data["mail"]

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (email, password, fullname) VALUES (%s, %s, %s)",
        (email, password, fullname),
    )
    connection.commit()

    # Kayıttan sonra kullanıcıyı sorgulayıp bilgileri döndürme
    cursor.execute("SELECT * FROM users WHERE email = %s", [email])
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user:
        return (
            jsonify(
                message="Kayıt başarılı!",
                user={
                    "userID": user[0],  # Kullanıcı ID'sini döndürüyoruz
                    "email": user[1],
                    "password": user[2],
                    "fullname": user[3],
                },
            ),
            200,
        )
    else:
        return jsonify(message="Kullanıcı bilgileri alınamadı."), 500


@app.route("/api/updateUser", methods=["POST"])
def update_user():
    data = request.json
    user_id = data.get("id")
    fullname = data.get("fullname")
    password = data.get("password")
    oldPassword = data.get("oldpassword")
    email = data.get("email")

    connection = get_db_connection()
    try:
        cursor = connection.cursor()

        # Mevcut kullanıcı bilgilerini çek
        cursor.execute("SELECT password FROM users WHERE userid = %s", [user_id])
        current_password = cursor.fetchone()[0]

        # Eğer yeni şifre girilmişse, şifreyi hash'leyin
        if password:
            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            ).decode("utf-8")
        else:
            hashed_password = current_password

        query = """
        UPDATE users
        SET email = %s, password = %s, fullname = %s
        WHERE userid = %s
        """
        cursor.execute(query, (email, hashed_password, fullname, user_id))
        connection.commit()
    finally:
        cursor.close()
        connection.close()

    return jsonify({"hashed_password": hashed_password, "password": password})


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data["mail"]
    password = data["password"].encode("utf-8")

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE email = %s", [email])
    user = cursor.fetchone()
    cursor.close()
    connection.close()

    if user and bcrypt.checkpw(password, user[2].encode("utf-8")):
        session["user_id"] = user[0]
        return jsonify(
            message="Giriş başarılı!",
            user={
                "userID": user[0],
                "email": user[1],
                "password": user[2],
                "fullname": user[3],
            },
        )
    else:
        return jsonify(message="Geçersiz mail veya şifre."), 401


@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return jsonify(message="Çıkış başarılı!")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
