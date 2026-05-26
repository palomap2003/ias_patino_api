from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": []})

@app.route("/users", methods=["POST"])
def create_user():
    return jsonify({"message": "user created"})