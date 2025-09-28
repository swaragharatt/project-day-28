from flask import Flask, jsonify, request, abort, render_template

app = Flask(__name__)

products = [
    {'id': 1, 'name': 'Dell XPS 15 Laptop', 'price': 120000.00, 'stock': 5, 'category': 'Electronics', 'description': 'High-performance laptop for professionals.'},
    {'id': 2, 'name': 'Logitech MX Master 3 Mouse', 'price': 8500.00, 'stock': 15, 'category': 'Peripherals', 'description': 'Ergonomic mouse with advanced features.'},
    {'id': 3, 'name': 'Anne Pro 2 Mechanical Keyboard', 'price': 10500.00, 'stock': 10, 'category': 'Peripherals', 'description': 'Compact 60% mechanical keyboard.'},
    {'id': 4, 'name': 'Samsung 27" Curved Monitor', 'price': 25000.00, 'stock': 7, 'category': 'Electronics', 'description': 'Immersive curved display for work and play.'},
    {'id': 5, 'name': 'Bose QC 35 II Headphones', 'price': 29999.00, 'stock': 8, 'category': 'Audio', 'description': 'Industry-leading noise cancelling headphones.'}
]
next_id = 6

@app.route('/')
def home():
    return render_template('blog_welcome.html')

@app.route('/shop')
def view_shop():
    return render_template('index.html', products=products)

@app.route('/api/products', methods=['GET'])
def get_products_api():
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        abort(404, description=f"Product with ID {product_id} not found")
    return jsonify(product)

@app.route('/api/products', methods=['POST'])
def create_product():
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        abort(400, description="Missing 'name' or 'price' in request data")

    global next_id
    new_product = {
        'id': next_id,
        'name': request.json['name'],
        'price': request.json['price'],
        'stock': request.json.get('stock', 0),
        'category': request.json.get('category', 'General'),
        'description': request.json.get('description', '')
    }
    products.append(new_product)
    next_id += 1
    return jsonify(new_product), 201

@app.route('/api/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        abort(404, description=f"Product with ID {product_id} not found")
    
    data = request.json
    product['name'] = data.get('name', product['name'])
    product['price'] = data.get('price', product['price'])
    product['stock'] = data.get('stock', product['stock'])
    product['category'] = data.get('category', product['category'])
    product['description'] = data.get('description', product['description'])
    
    return jsonify(product)

@app.route('/api/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    initial_length = len(products)
    products = [p for p in products if p['id'] != product_id]
    
    if len(products) == initial_length:
        abort(404, description=f"Product with ID {product_id} not found")
        
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
