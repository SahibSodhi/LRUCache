from flask import Flask, request, jsonify
from collection_cache import CollectionCache

app = Flask(__name__)

collection_cache = CollectionCache()

@app.route('/collections', methods=['POST'])
def create_collection():
    try:
        collection_id = request.json.get('collection_id')
        capacity = request.json.get('capacity')
        collection_cache.create_collection(collection_id, capacity)
        return jsonify({'message': 'Collection created successfully'}), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@app.route('/collections/<collection_id>/capacity', methods=['PUT'])
def update_capacity(collection_id):
    try:
        capacity = request.json.get('capacity')
        collection_cache.update_capacity(collection_id, capacity)
        return jsonify({'message': 'Capacity updated successfully'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

@app.route('/collections/<collection_id>/data', methods=['PUT'])
def put_data(collection_id):
    try:
        key = request.json.get('key')
        value = request.json.get('value')
        collection_cache.put_data(collection_id, key, value)
        return jsonify({'message': 'Data added successfully'}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

@app.route('/collections/<collection_id>/data/<key>', methods=['GET'])
def get_data(collection_id, key):
    try:
        value = collection_cache.get_data(collection_id, key)
        return jsonify({'value': value}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

@app.route('/collections/<collection_id>/data', methods=['GET'])
def get_collection_data(collection_id):
    try:
        data = collection_cache.get_collection_data(collection_id)
        return jsonify({'data': data}), 200
    except ValueError as e:
        return jsonify({'message': str(e)}), 404

if __name__ == '__main__':
    app.run(debug=True)
