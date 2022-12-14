#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_usuari, Usuari
import redis

class Persistencia_usuari_redis(Persistencia_usuari.Persistencia_usuari):
    def __init__(self, host, configurador):
        self.host = host
        self.configurador = configurador

    def get(self, id):
        db = self.__get_db_connection()
        key = 'usuari:' + id.decode()

        
        usuari_nom = db.hget(key, 'nom').decode()
        if usuari_nom:
            usuari_password_hash = db.hget(key, 'password_hash').decode()
            resultat = Usuari.Usuari(
                self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory(), 
                id, 
                usuari_nom, 
                usuari_password_hash)
            return resultat
        db.quit()
        return None

    def get_from_apikey(self, id_sessio):
        raise NotImplementedError("# TODO get_from_apikey")
        # db = self.__get_db_connection()
        # query = "select id, usuaris.usuari, password_hash from usuaris inner join sessions_usuaris on (sessions_usuaris.usuari = usuaris.id) where sessions_usuaris.uuid = %s;"
        # valors = (id_sessio,)
        # cursor = db.cursor()
        # cursor.execute(query, valors)

        # registres = cursor.fetchall()
        # if len(registres) > 0:
        #     usuari_id = registres[0][0]
        #     usuari_nom = registres[0][1]
        #     usuari_password = registres[0][2]
        #     resultat = Usuari.Usuari(self.configurador.get_Persistencia_factory().get_Persistencia_usuari_factory(), usuari_id, usuari_nom, usuari_password)
        #     return resultat
        # return None

    def desa(self, usuari):
        db = self.__get_db_connection()
        id = usuari.get_nom()
        key = 'usuari:'+id
        db.hset(key, 'id',  id)
        db.hset(key, 'nom',  usuari.get_nom())
        db.hset(key, 'password_hash',  usuari.get_password_hash())
        db.sadd('usuaris', id)
        db.quit()
        return id

    def get_llista(self):
        llista = []
        db = self.__get_db_connection()

        registres = db.smembers('usuaris')
        db.quit()
        for id in registres:
            llista.append(self.get(id))
        return llista

    def delete(self, id):
        db = self.__get_db_connection()
        db.delete('usuari:' + id)
        resultat = True
        db.quit()
        return resultat


    def __get_db_connection(self):
        return redis.Redis(
          host = self.host
          )

    def set_sessio(self, id_sessio, usuari):
        db = self.__get_db_connection()

        db.rpush('sessions' + id_sessio, usuari.get_id())
        db.quit()
        return id_sessio