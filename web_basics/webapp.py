# -*- coding: utf8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Mi primera app web"

@app.route("/about")
def about():
    return "About"

@app.route("/saludar")
def saludar():
    # http://localhost:5000/saludar?name=sebastian
    # name = request.args.get("name", "fulano")
    name = request.args.get("name")
    if not name:
        return "No hay a quien saludar"

    return "hola " + name

@app.route("/echo")
def echo():
    txt = u'Recibí: '
    parametros = request.args

    for k, v in parametros.iteritems():
        txt = txt + (' key: %s, val: %s' % (k, v))

    return txt

@app.route("/suma")
def suma():
    result = "Resultado: "
    number_1 = int(request.args.get('a'))
    number_2 = int(request.args.get('b'))
    resultado = number_1 + number_2
    return str(resultado)


@app.route("/home")
def home():
    # jinja 2
    return render_template("home.html", app_name="First template", nombre="Ian")

# def sumar()
# Calculadora con rutas y parametros

@app.route("/bio")
def bio():
    params = {
       "nombre":"Ian",
       "bio":"etc...",
       "edad":27
    }
    return render_template("bio.html", **params)

@app.route("/list")
def lista():
    lista = [{
        "nombre":"Ximena", "apodo":"Jimmy"
    },{
        "nombre":"Antonio", "apodo":u"Patrón"
    },{
        "nombre":u"Julían", "apodo":"Julaians"
    }]
    return render_template("lista.html", lista=lista, title="Lista de Grupo")

@app.route("/alumno/<ids>")
def get_by_apodo(ids):
    alumnos = {
        'ximena': {"nombre": "Ximena Ortega", "bio": "Alumna DevF" },
        'tono': {"nombre": "Antonio Banderas", "bio": "Le dicen el Patronceto"},
        'pablo': {"nombre": u"Pablo Velázquez", "bio": "Colorear"}
    }

    # Buscar ids en el diccionario
    alumno = alumnos.get(ids) # None en caso de que no lo encuentre
    # Mandar lo que necuentre en la plantilla
    return render_template("alumnos.html", alumno=alumno)

    # if alumnos.get(ids):
    #     return render_template("bio.html", **alumnos.get(ids))
    # else:
    #     return u"No se localizó el alumno"

    #buscar id en diccionario
    #mandar lo que encuentre a plantilla
    # alumno = alumnos.get
    # Mostrar alumno o decir que no
    # return ids

if __name__ == "__main__":
    app.run(debug = True)
