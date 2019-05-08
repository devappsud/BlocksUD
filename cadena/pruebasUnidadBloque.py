#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cadena.Transaccion import Transaccion
from cadena.Bloque import Bloque
from random import randrange
from random import uniform
from random import random
import jsonpickle
import jsonpickle.backend
import jsonpickle.handlers
import pprint

"""
En esta clase se realizan pruebas de unidad
"""
class pruebasUnidadBloque(object):
        
    def main():
       #Cada bloque de prueba se ha creado con un conjunto aleatorio transacciones
       transacciones = [];
       #Se construye una conjunto aleatorio de transacciones para bloque genésis
       emisor = Bloque.generarBloqueHash(random())
       receptor = Bloque.generarBloqueHash(random())
       cantidad = uniform(2.5, 1000.0) 
       transacciones.append(Transaccion(emisor, receptor,cantidad));
       #0 para indicar que el bloque no ha sido minado
       genesis = Bloque(0,0,Bloque.generarBloqueHash(0),transacciones);
       cadena = [genesis];
       
        #Se construye una pseudocadena con 5 bloques
       for i in range(1,5):
              transacciones = [];
              #Se construye una conjunto aleatorio de transacciones
              for t in range(1+randrange(3)):
                  emisor = Bloque.generarBloqueHash(random())
                  receptor = Bloque.generarBloqueHash(random())
                  cantidad = uniform(2.5, 1000.0) 
                  transacciones.append(Transaccion(emisor, receptor,cantidad));
                  
              cadena.append(Bloque(i,0,Bloque.generarBloqueHash(cadena[i-1].gethashBloque()) , transacciones));
 
       pprint.pprint(jsonpickle.pickler.Pickler().flatten(cadena))
           
    if __name__ == "__main__":
        main()