#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Configurador, Usuari
import os
import bcrypt


"""
    Punt únic d'entrada a la nostra aplicació de la llista de la compra.
"""

FITXER_CONFIGURACIO = "configuracio.yml"
class App_llista_compra:
    def __init__(self):
        self.configurador = Configurador.Configurador(
            os.path.join(
                os.path.dirname(__file__), 
                FITXER_CONFIGURACIO
                )
            )
        self.usuaris = []

    def get_configurador(self):
        return self.configurador

    def create_usuari(self, user, password):
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        nou_usuari = Usuari.Usuari(self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory(), None, user, password_hash)
        nou_usuari = nou_usuari.desa()
        self.usuaris.append(nou_usuari)
        return nou_usuari

if __name__ == "__main__":
    # proves locals
    app = App_llista_compra()
    print("[config] Base de dades:\n\t", app.get_configurador().get_config()["base de dades"])
    nou_usuari = app.create_usuari('Alex', '1234')
    print(nou_usuari.get_id())
    print(nou_usuari.get_nom())
    print(nou_usuari.get_password_hash())
    print("Llista d'usuaris:")
    print("-----")
    for usuari in app.get_configurador().get_Persistencia_factory().get_Persistencia_usuari_factory().get_llista():
        print(usuari.get_id(), usuari.get_nom())