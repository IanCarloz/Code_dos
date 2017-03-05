# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return( 'Hola, ¿Quieres tu lista?' )

@app.route("/lista")
def lista():
    tareas = [
        {
            'tarea': 'Estudiarr Vue',
            'completada': False
        },{
            'tarea': 'Estudiarr Python',
            'completada': True
        },{
            'tarea': 'Estudiarr JS',
            'completada': False
        },{
            'tarea': 'Estudiarr Flask',
            'completada': True
        },{
            'tarea': 'Estudiarr Mate',
            'completada': False
        }
        ]
    return jsonify({'tareas':tareas})


if __name__ == "__main__":
    app.run(debug=True)
