from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_KEY = "0s8jikuEdHV3ExK5QDtq"
PROJECT = "baikraproud-1cfhc"
VERSION = 7
URL = f"https://detect.roboflow.com/{PROJECT}/{VERSION}?api_key={API_KEY}"

@app.route("/")
def index():
    return render_template("mommy.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    response = requests.post(URL, files={"file": file})
    result = response.json()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

app.run(host="0.0.0.0", port=5000, debug=True)

# "อย่ามาทำเก่งใส่ฉันหน่อยเลย คนที่ยังแยกไม่ออกว่าตัวเองหิวจริงหรือแค่เบื่อเฉย ๆ ยังมีหน้าจะมาสั่งสอนฉันเรื่องการใช้ชีวิตอีกเหรอ เห็นพิมพ์ใส่แป้นคีย์บอร์ดมันส์ ๆ ก็อย่านึกว่าตัวเองคือเทพแห่งการถกเถียง พอเอาจริงก็เงียบเป็นเป่าสาก เหมือน Wi-Fi ฟรีร้านกาแฟที่คนเต็มร้านแต่สัญญาณไม่มีสักขีดอะนะ"
