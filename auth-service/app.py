from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock users
users = {"admin": "password123"}

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if users.get(username) == password:
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    if username in users:
        return jsonify({"message": "User already exists!"}), 400
    users[username] = password
    return jsonify({"message": "User registered successfully!"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
