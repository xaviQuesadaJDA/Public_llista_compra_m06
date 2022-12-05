#!/usr/bin/python3
# -*- coding: utf-8 -*-

import yaml
import os
import Persistencia_factory_mySql

"""
    Configurador.py
    És la classe encarregada de llegir el fitxer
    de configuració i obtenir les classes concretes
    adients a la nostra aplicació.
"""
class Configurador:
    def __init__(self, path_fitxer_configuracio):
        print (f"configurador {__name__=}")
        self.yaml_config = path_fitxer_configuracio
        self.config = {}
        with open(path_fitxer_configuracio, 'r') as conf:
            self.config = yaml.safe_load(conf)
    
    def get_config(self):
        return self.config

    def get_Persistencia_factory(self):
        if self.config["base de dades"]["motor"].lower().strip() == "mysql":
            host = self.config["base de dades"]["host"]
            usuari = self.config["base de dades"]["user"]
            paraula_pas = self.config["base de dades"]["password"]
            base_dades = self.config["base de dades"]["base_dades"]
            return Persistencia_factory_mySql.Persistencia_factory_mySql(
                host,
                usuari,
                paraula_pas,
                base_dades
            )
        
if __name__ == "__main__":
    path_mysql = os.path.join(os.path.dirname(__file__), "configuracio_mysql.yml")
    path_sqlite = os.path.join(os.path.dirname(__file__), "configuracio_sqlite.yml")

    configurador = Configurador(path_mysql)
    print("mysql: ", end="\t")
    print(configurador.get_config()["base de dades"])
    pf = configurador.get_Persistencia_factory()
    print(pf.get_Persistencia_usuari_factory())

    print("sqlite: ", end="\t")
    configurador = Configurador(path_sqlite)
    print(configurador.get_config()["base de dades"])
