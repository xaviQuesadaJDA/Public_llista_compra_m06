#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import App_llista_compra

app = Flask(__name__)
app_llista_compra = App_llista_compra.App_llista_compra()

@app.route("/")
def hello():
    return jsonify({"missatge": "Benvingut a la llista de la compra!"}), 200


@app.route("/registre/<nom_usuari>/<password>")
def registre(nom_usuari, password):
    resultat = app_llista_compra.registre_usuari(nom_usuari, password)
    return jsonify(resultat), resultat["estatus"]

@app.route("/login/<nom_usuari>/<password>")
def login(nom_usuari, password):
    resultat = app_llista_compra.login_usuari(nom_usuari, password)
    return jsonify(resultat), resultat["estatus"]

if __name__ == "__main__":
    app.run()