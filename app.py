from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
data = [
    {"id": 1, "name": "Alice", "role": "Engineer"},
    {"id": 2, "name": "Bob", "role": "Designer"},
    {"id": 3, "name": "Charlie", "role": "Manager"}
]

# Home route
@app.route('/')
def home():
    return "Welcome to the Simple Flask API!"

# Get all data
@app.route('/data', methods=['GET'])
def get_all_data():
    return jsonify(data)

# Get data by ID
@app.route('/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    entry = next((item for item in data if item["id"] == data_id), None)
    if entry:
        return jsonify(entry)
    return jsonify({"error": "Data not found"}), 404

# Add new data
@app.route('/data', methods=['POST'])
def add_data():
    new_entry = request.get_json()
    data.append(new_entry)
    return jsonify(new_entry), 201

# Delete data by ID
@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    global data
    data = [item for item in data if item["id"] != data_id]
    return jsonify({"message": "Data deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
