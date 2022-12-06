#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_usuari, Usuari
import mysql.connector

class Persistencia_usuari_mySql(Persistencia_usuari.Persistencia_usuari):
    def __init__(self, host, user, password, base_dades, configurador):
        self.host = host
        self.user = user
        self.password = password
        self.base_dades = base_dades
        self.configurador = configurador

    def get(self, id):
        db = self.__get_db_connection()
        query = "Select usuari, password_hash from usuaris where id=%s;"
        valors = (id,)
        cursor = db.cursor()
        cursor.execute(query, valors)

        registres = cursor.fetchall()
        if len(registres) > 0:
            usuari_nom = registres[0][0]
            usuari_password_hash = registres[0][1]
            resultat = Usuari.Usuari(self.configurador, id, usuari_nom, usuari_password_hash)
            return resultat
        return None

    def desa(self, usuari):
        db = self.__get_db_connection()
        id = self.__get_id_by_nom(usuari.get_nom())
        if id is None:
            query = "Insert into usuaris (usuari, password_hash) " + \
                "values(%s, %s);"
            valors = (usuari.get_nom(), usuari.get_password_hash())

            cursor = db.cursor()
            resultat = None
            try:
                cursor.execute(query, valors)
                db.commit();
                id = self.__get_id_by_nom(usuari.get_nom())
            except mysql.connector.IntegrityError as error:
                print(str(error))
                id = None
            cursor.close()
            db.close()
        return id

    def get_llista(self):
        llista = []
        db = self.__get_db_connection()
        
        query = "Select id from usuaris;"
        cursor = db.cursor()
        cursor.execute(query)

        registres = cursor.fetchall()
        for id in registres:
            llista.append(self.get(id[0]))
        return llista

    def delete(self, id):
        db = self.__get_db_connection()
        query = "Delete from usuaris " + \
                "Where id=%s;"
        valors = (id, )

        cursor = db.cursor()
        resultat = None
        cursor.execute(query, valors)
        db.commit()
        resultat = True
        cursor.close()
        db.close()
        return resultat


    def __get_db_connection(self):
        return mysql.connector.connect(
          host = self.host,
          user = self.user,
          password = self.password,
          database = self.base_dades)
          
    def __get_id_by_nom(self, nom):
        db = self.__get_db_connection()
        
        query = "Select id from usuaris where usuari=%s;"
        valors = (nom,)
        cursor = db.cursor()
        cursor.execute(query, valors)

        registres = cursor.fetchall()
        if len(registres) > 0:
            return registres[0][0]
        return None 
