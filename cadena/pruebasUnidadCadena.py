#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cadena.CadenaBloques import CadenaBloques
from cadena.NodoMinador import NodoMinador
from cadena.Transaccion import Transaccion
from cadena.Bloque import Bloque
from cadena.PoolMinado import PoolMinado
from cliente.Usuario import Usuario
from random import randrange
from random import uniform
from random import random
import jsonpickle
import jsonpickle.backend
import jsonpickle.handlers
import pprint
import copy

"""
En esta clase se realizan pruebas de unidad
"""
class pruebasUnidadCadena(object):
    def main():
       pool = PoolMinado()
       transacciones = [];
       blockchain = CadenaBloques()
       #Se construye una transacción aleatoria para bloque genésis
       emisor = Bloque.generarBloqueHash(random())
       receptor = Bloque.generarBloqueHash(random())
       cantidad = uniform(2.5, 1000.0) 
       transacciones.append(Transaccion(emisor, receptor,cantidad));
       blockchain.bloqueGenesis(transacciones)
       
       print("Agregando nodos mineros para la blockchain ...");
       totalUsuarios = 25;
       totalMineros = 5;
    
       usuarios = {};
       for i in range(totalUsuarios):
           temp = Usuario(i);
           temp.setHashUsuario();
           usuarios[temp.gethashUsuario] = temp;
       
       #Se construye una conjunto aleatorio de nodos mineros
       usuariosNodo = [];
       usuariosMineros = {};
       contador = totalUsuarios//totalMineros - 1;
       aux = 0;
       for key in usuarios:
           usuariosMineros[key] = usuarios[key];
           if(aux < contador):
              aux += 1;
           else:
               usuariosNodo.append(copy.copy(usuariosMineros));
               aux = 0;
               usuariosMineros = {};

       mineros = [];
       for i in range(len(usuariosNodo)):
           address = "127.0.0." + str(1+randrange(253))
           puerto = 1025+randrange(60000)
           descripcion = "nodo minero número " + str(i)
           nodo = NodoMinador(address, puerto,descripcion,usuariosNodo[i])
           nodo.actualizarCadena(blockchain)
           mineros.append(nodo);
         
       #Se construye una cadena de bloques con 10 bloques
       for i in range(1,10):
              transacciones = [];
              #Se construye una conjunto aleatorio de transacciones
              for tr in range(1+randrange(3)):
                  emisor = Bloque.generarBloqueHash(random())
                  receptor = Bloque.generarBloqueHash(random())
                  cantidad = uniform(2.5, 1000.0) 
                  transacciones.append(Transaccion(emisor, receptor,cantidad))
                  
              pool.torneoPorNuevoBloque(transacciones)
              print("Iteracion " + str(i) +" La cadena es válida? " + str(blockchain.validarBlockchain()) + " ahora tiene " + str(len(blockchain._cadena)) + " bloques")
    
       pprint.pprint(jsonpickle.pickler.Pickler().flatten(blockchain))
       
    
    if __name__ == "__main__":
        main()