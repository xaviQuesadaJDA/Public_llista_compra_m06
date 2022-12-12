#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Persistencia_usuari

class Usuari:
    def __init__(self, persistencia, id, user, password_hash):
        self.id = id
        self.user = user
        self.password_hash = password_hash
        assert issubclass(type(persistencia), Persistencia_usuari.Persistencia_usuari)
        self.persistencia = persistencia

    def get_nom(self):
        return self.user
    
    def get_password_hash(self):
        return self.password_hash

    def get_id(self):
        return self.id

    def desa(self):
        self.id = self.persistencia.desa(self)
        return self

    def delete(self):
        return self.persistencia.delete(self.get_id())

    def set_sessio(self, id_sessio):
        return self.persistencia.set_sessio(id_sessio, self)

