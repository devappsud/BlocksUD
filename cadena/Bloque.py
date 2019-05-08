#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import hashlib
import json

"""
Define la estructura del bloque.
"""

class Bloque(object):

    def __init__(self, indice, minado, hashBloque, transacciones, marcaTiempo=None):
        """
        Inicialización del bloque
        :param indice: Valor entero que representa la posición de cada bloque en la cadena
        :param minado: Número entero usado en el proceso de minería
        :param hashBloque:  hash del bloque actual en la cadena
        :param transacciones: Conjunto de transacciones del bloque 
        :param marcaTiempo: Instante de tiempo de creación del nuevo bloque
        """
        self._indice = indice
        self._minado = minado
        self._hashBloque = hashBloque
        self._transacciones = transacciones.copy()
        self._marcaTiempo = marcaTiempo or time.time()

    def gethashBloque(self):
        """
        Obtiene el valor actual del hash del bloque
        :return: Hash del bloque
        """
        return self._hashBloque;
    
    def setHashBloque(self):
        self._hashBloque = Bloque.generarBloqueHash(self)
    
    @staticmethod
    def generarBloqueHash(self):
        """
        Genera Hash la información del bloque
        :return: Hash construido a partir de la información del bloque
        """
        return hashlib.sha256(str(self).encode()).hexdigest()
    
    
    def __str__(self):
        """
        Genera un string con la información del bloque
        :return: representación en String del bloque
        """
        return "{} , {} , {}  , {}".format(self._indice, self._minado, self._hashBloque, self._marcaTiempo)
    
    def __repr__(self):
            return json.JSONEncoder().encode(self)
        
    def consultarBloque(self):
        a = ""
        a = a + str(self._indice) + " " + str(self._minado) + " " + str(self._hashBloque) + "\n";
        a = a + "Transacciones del bloque";
        for i in range(len(self._transacciones)):
            a = a + "\n" + str(self._transacciones[i]);
        a = a + "\nFin Transacciones del bloque";
        return a;
