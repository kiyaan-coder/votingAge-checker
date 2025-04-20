from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests from different origins

@app.route('/check_age', methods=['POST'])
def check_age():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')

    if name is None or age is None:
        return jsonify({"error": "Name and age are required"}), 400

    try:
        age = int(age)
    except ValueError:
        return jsonify({"error": "Invalid age format"}), 400

    if age >= 18:
        return jsonify({"message": f"{name}, you are eligible to vote!"})
    else:
        return jsonify({"message": f"Sorry {name}, you are not eligible to vote yet."})

if __name__ == '__main__':
    app.run(debug=True)
