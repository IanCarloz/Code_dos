# -*- coding: utf8 -*-
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Esto es una calculadora"

@app.route("/suma")
def index():
    result = "Resultado: "
    number_1 = int(request.args.get('a'))
    number_2 = int(request.args.get('b'))
    resultado = number_1 + number_2
    # result = result + "%s" % (resultado)


if __name__ == "__main__":
    app.run()
