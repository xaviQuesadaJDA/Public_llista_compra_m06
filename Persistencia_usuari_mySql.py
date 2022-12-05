#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_usuari
import mysql.connector

class Persistencia_usuari_mySql(Persistencia_usuari.Persistencia_usuari):
    def __init__(self, host, user, password, base_dades):
        self.host = host
        self.user = user
        self.password = password
        self.base_dades = base_dades

    def get(self, id):
        raise NotImplementedError("get")

    def desa(self, usuari):
        db = mysql.connector.connect(
          host = self.host,
          user = self.user,
          password = self.password,
          database = self.base_dades)
        id = self.get_id_by_nom(usuari.get_nom())
        if id is None:
            query = "Insert into usuaris (usuari, password_hash) " + \
                "values(%s, %s);"
            valors = (usuari.get_nom(), usuari.get_password_hash())

            cursor = db.cursor()
            resultat = None
            try:
                cursor.execute(query, valors)
                db.commit();
                id = self.get_id_by_nom(usuari.get_nom())
            except mysql.connector.IntegrityError as error:
                print(str(error))
                id = None
            cursor.close()
            db.close()
        return id
        
    def get_id_by_nom(self, nom):
        db = mysql.connector.connect(
          host = self.host,
          user = self.user,
          password = self.password,
          database = self.base_dades)
        
        query = "Select id from usuaris where usuari=%s;"
        valors = (nom,)
        cursor = db.cursor()
        cursor.execute(query, valors)

        registres = cursor.fetchall()
        if len(registres) > 0:
            return registres[0][0]
        return None 

    def get_llista(self):
        raise NotImplementedError("get_llista")

    def delete(self, id):
        raise NotImplementedError("delete")