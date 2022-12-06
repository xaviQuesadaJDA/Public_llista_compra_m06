#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Usuari:
    def __init__(self, persistencia, id, user, password_hash):
        self.id = id
        self.user = user
        self.password_hash = password_hash
        self.persistencia = persistencia

    def get_nom(self):
        return self.user
    
    def get_password_hash(self):
        return self.password_hash.decode('utf8', 'strict')

    def get_id(self):
        return self.id

    def desa(self):
        self.id = self.persistencia.desa(self)
        return self

    def delete(self):
        return self.persistencia.delete(self.get_id())
