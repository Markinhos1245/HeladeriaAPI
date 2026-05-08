from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

productos = [
    {
        "id": 1,
        "nombre": "Chocolate",
        "precio": 3500
    },
    {
        "id": 2,
        "nombre": "Dulce de leche",
        "precio": 4000
    },
    {
        "id": 3,
        "nombre": "Frutilla",
        "precio": 3000
    },
    {
        "id": 4,
        "nombre": "Vainilla",
        "precio": 3200
    },
    {
        "id": 5,
        "nombre": "Crema americana",
        "precio": 3300
    },
    {
        "id": 6,
        "nombre": "Menta Granizada",
        "precio": 3250
    }
]

carrito = []


@app.route('/productos', methods=['GET'])
def ver_productos():
    """
    Ver productos
    ---
    responses:
      200:
        description: Lista de productos
    """

    return jsonify(productos)


@app.route('/carrito', methods=['GET'])
def ver_carrito():
    """
    Ver carrito
    ---
    responses:
      200:
        description: Productos del carrito
    """

    return jsonify(carrito)


@app.route('/carrito', methods=['POST'])
def agregar_al_carrito():
    """
    Agregar producto al carrito
    ---
    parameters:
      - in: body
        name: producto

    responses:
      200:
        description: Producto agregado
    """

    datos = request.get_json()

    producto_id = datos.get('productoId')
    cantidad = datos.get('cantidad', 1)

    producto = None

    for producto_lista in productos:
        if producto_lista["id"] == producto_id:
            producto = producto_lista

    if not producto:
        return jsonify({
            "error": "Producto no encontrado"
        }), 404

    carrito.append({
        "productoId": producto["id"],
        "nombre": producto["nombre"],
        "precio": producto["precio"],
        "cantidad": cantidad
    })

    return jsonify({
        "mensaje": "Producto agregado al carrito"
    })

@app.route('/carrito/<int:producto_id>', methods=['DELETE'])
def eliminar_del_carrito(producto_id):
    """
    Eliminar cantidad de producto del carrito
    ---
    parameters:
      - in: body
        name: producto

    responses:
      200:
        description: Producto actualizado
    """

    datos = request.get_json()

    cantidad = datos.get('cantidad', 1)

    producto = None

    for producto_carrito in carrito:
        if producto_carrito["productoId"] == producto_id:
            producto = producto_carrito

    if not producto:
        return jsonify({
            "error": "Producto no encontrado en el carrito"
        }), 404

    producto["cantidad"] -= cantidad

    if producto["cantidad"] <= 0:
        carrito.remove(producto)

    return jsonify({
        "mensaje": "Cantidad eliminada correctamente"
    })

@app.route('/carrito/total', methods=['GET'])
def calcular_total():
    """
    Calcular total del carrito
    ---
    responses:
      200:
        description: Total calculado
    """

    total = 0

    for producto in carrito:
        total += producto["precio"] * producto["cantidad"]

    return jsonify({
        "total": total
    })


if __name__ == '__main__':
    app.run(debug=True)
