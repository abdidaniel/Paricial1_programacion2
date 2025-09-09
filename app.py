from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.update(
    MYSQL_HOST='127.0.0.1',
    MYSQL_PORT=3306,
    MYSQL_USER='root',
    MYSQL_PASSWORD='',
    MYSQL_DB='proyectowebflask',
    MYSQL_CURSORCLASS='DictCursor',
)

mysql = MySQL(app)

# Ruta para obtener todos los equipos
@app.route('/api/equipos', methods=['GET'])
def obtener_equipos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM equipos ORDER BY id DESC")
    equipos = cur.fetchall()
    return jsonify(equipos)

# Ruta para guardar un nuevo equipo
@app.route('/api/equipos', methods=['POST'])
def guardar_equipo():
    descripcion = request.json['descripcion']
    email = request.json['email']
    sql = "INSERT INTO equipos (descripcion, email) VALUES (%s, %s)"
    cur = mysql.connection.cursor()
    cur.execute(sql, (descripcion, email))
    mysql.connection.commit()
    return jsonify({'message': 'Equipo guardado'}), 201

# Ruta para editar un equipo
@app.route('/api/equipos/<int:id>', methods=['PUT'])
def editar_equipo(id):
    descripcion = request.json['descripcion']
    email = request.json['email']
    sql = "UPDATE equipos SET descripcion=%s, email=%s WHERE id=%s"
    cur = mysql.connection.cursor()
    cur.execute(sql, (descripcion, email, id))
    mysql.connection.commit()
    return jsonify({'message': 'Equipo actualizado'})

# Ruta para borrar un equipo
@app.route('/api/equipos/<int:id>', methods=['DELETE'])
def borrar_equipo(id):
    sql = "DELETE FROM equipos WHERE id=%s"
    cur = mysql.connection.cursor()
    cur.execute(sql, (id,))
    mysql.connection.commit()
    return jsonify({'message': 'Equipo borrado'})



if __name__ == '__main__':
    app.run(debug=True)
