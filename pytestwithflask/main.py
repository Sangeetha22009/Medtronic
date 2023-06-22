from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data
flowers = [
    {'id': 1, 'color': 'red', 'name': 'Rose'},
    {'id': 2, 'color': 'yellow', 'name': 'Sunflower'},
    {'id': 3, 'color': 'purple', 'name': 'Lavender'},
    {'id': 4, 'color': 'pink', 'name': 'Carnation'},
    {'id': 5, 'color': 'orange', 'name': 'Marigold'}
]


@app.route('/flowers', methods=['GET'])
def get_flowers():
    return jsonify(flowers)


@app.route('/flowers', methods=['POST'])
def create_flowers():
    new_flower = {
        'id': len(flowers) + 1,
        'name': request.json.get('name'),
        'color': request.json.get('color')
    }
    flowers.append(new_flower)
    return jsonify(new_flower), 201


@app.route('/flowers/<int:flower_id>', methods=['GET'])
def get_flower(flower_id):
    flower = next((flower for flower in flowers if flower['id'] == flower_id), None)
    if flower:
        return jsonify(flower)
    else:
        return jsonify({'error': 'flower not found'}), 404


@app.route('/flowers/<int:flower_id>', methods=['PUT'])
def update_flower(flower_id):
    flower = next((flower for flower in flowers if flower['id'] == flower_id), None)
    if flower:
        flower['name'] = request.json.get('name')
        flower['color'] = request.json.get('color')
        return jsonify(flower)
    else:
        return jsonify({'error': 'flower not found'}), 404


@app.route('/flowers/<int:flower_id>', methods=['DELETE'])
def delete_flower(flower_id):
    flower = next((flower for flower in flowers if flower['id'] == flower_id), None)
    if flower:
        flowers.remove(flower)
        return jsonify({'message': 'flower deleted'})
    else:
        return jsonify({'error': 'flower not found'}), 404


if __name__ == '__main__':
    app.run()
