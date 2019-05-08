#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cadena.Transaccion import Transaccion
from cadena.Bloque import Bloque
from random import uniform
from random import random
import jsonpickle
import jsonpickle.backend
import jsonpickle.handlers
import pprint

"""
En esta clase se realizan pruebas de unidad
"""
class pruebasUnidadTransaccion(object):
    
    @staticmethod
    def jsonDefault(object):
        return object.__dict__
    
    def main():
       transacciones = [];
       #Se construye una conjunto aleatorio de transacciones
       for i in range(5):
           emisor = Bloque.generarBloqueHash(random())
           receptor = Bloque.generarBloqueHash(random())
           cantidad = uniform(2.5, 1000.0) 
           transacciones.append(Transaccion(emisor, receptor,cantidad));
       
       print("CONJUNTO ALEATORIO DE TRANSACCIONES")
       pprint.pprint(jsonpickle.pickler.Pickler().flatten(transacciones))
           
    if __name__ == "__main__":
        main()