#!/usr/bin/python3
# -*- coding: utf-8 -*-

import abc

class Persistencia_usuari(abc.ABC):
    @abc.abstractmethod
    def get(self, id):
        pass

    @abc.abstractmethod
    def desa(self, usuari):
        pass

    @abc.abstractmethod
    def get_llista(self):
        pass

    @abc.abstractmethod
    def delete(self, id):
        pass
