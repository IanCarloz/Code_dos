from flask import Flask, request

app = Flask(__name__)

@app.route( '/' )
def index():
    return('Hola mundo. <3')

@app.route( '/parametros' )
def obtener_parametros():
    parametro_1 = request.args.get( 'param1', 'No hay parametro uno' )
    parametro_2 = request.args.get( 'param2', 'No hay parametro dos' )
    return( 'Parametros: {}, {}' .format(parametro_1, parametro_2) )
@app.route( '/params/' )
@app.route( '/params/<name>' )
def params( name = 'default' ):
    return( 'Parametro = {}' .format(name) )

@app.route( '/suma' )
def sumar():
    a = request.args.get( 'a' )
    b = request.args.get( 'b' )
    if a != None or b != None:
        r = int(a) + int(b)
        return( 'el resultado de sumar {} mas {} es {}.' .format(a, b, r) )
    else:
        return 'introduce numeros'

@app.route( '/sumaa' )
def sumarr():
    a = request.args.get( 'a', 'A' )
    b = request.args.get( 'b', 'B' )
    if a == 'A' or b == 'B':
        return 'introduce los numeros para sumar'
    else:
        r = int(a) + int(b)
        return( 'el resultado de sumar {} mas {} es {}.' .format(a, b, r) )

@app.route( '/calculadora/suma/<int:a>/<int:b>' )
def suma(a, b):
    return('a = {} y b = {}' .format(a, b))

if __name__ == '__main__':
    app.run( debug=True, port=8000 )
