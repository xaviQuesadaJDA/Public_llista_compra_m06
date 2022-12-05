#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Usuari:
    def __init__(self, configurador, id, user, password_hash):
        self.configurador = configurador
        self.id = id
        self.user = user
        self.password_hash = password_hash
        self.persistencia = configurador.get_Persistencia_factory().get_Persistencia_usuari_factory()

    def get_nom(self):
        return self.user
    
    def get_password_hash(self):
        return self.password_hash.decode('utf8', 'strict')

    def get_id(self):
        return self.id

    def desa(self):
        self.id = self.persistencia.desa(self)
        return self