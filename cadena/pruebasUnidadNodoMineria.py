#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cadena.CadenaBloques import CadenaBloques
from cadena.NodoMinador import NodoMinador
from cadena.Transaccion import Transaccion
from cliente.Usuario import Usuario
from cadena.Bloque import Bloque
from random import randrange
from random import uniform
from random import random
import copy

"""
En esta clase se realizan pruebas de unidad
"""
class pruebasUnidadNodoMineria(object):
    def main():
       transacciones = [];
       blockchain = CadenaBloques()
       #Se construye una transacción aleatoria para bloque genésis
       emisor = Bloque.generarBloqueHash(random())
       receptor = Bloque.generarBloqueHash(random())
       cantidad = uniform(2.5, 1000.0) 
       transacciones.append(Transaccion(emisor, receptor,cantidad));
       blockchain.bloqueGenesis(transacciones)
       
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
       
       print("CONJUNTO ALEATORIO DE NODOS MINEROS")
       #pprint.pprint(jsonpickle.pickler.Pickler().flatten(mineros))
       for i in mineros:
           print(i);
           print("Usuarios Mineros en el Nodo");
           for key in i._usuariosMineros:
               print(i._usuariosMineros[key]);
           print("==========================================================")

           
    if __name__ == "__main__":
        main()