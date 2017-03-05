# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__) # template_folder = ' nombre del la carpeta diferente a templates'

@app.route( '/' )
def index():
    return(render_template( 'index.html' ))

if __name__ == '__main__':
    app.run( debug=True, port=8000 )
