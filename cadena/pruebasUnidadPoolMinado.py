#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cadena.CadenaBloques import CadenaBloques
from cliente.Usuario import Usuario
from cadena.NodoMinador import NodoMinador
from cadena.Transaccion import Transaccion
from cadena.Bloque import Bloque
from cadena.PoolMinado import PoolMinado
from random import randrange
from random import uniform
from random import random
from threading import Thread

"""
En esta clase se realizan pruebas de unidad
"""
class pruebasUnidadPoolMinado(Thread):
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
       print("La cadena tiene un " + str(len(blockchain._cadena)) + " Bloque, el genésis")
       print("Agregando nodos mineros para la blockchain ...");
       
       maxUsuarios = 25;
       maxMineros = 5;
       maxTransaccionesPorBloque = 10;
       totalBloquesCaena = 100;
    
       usuarios = {};
       for i in range(maxUsuarios):
           temp = Usuario(i);
           temp.setHashUsuario();
           usuarios[temp.gethashUsuario] = temp;
       
       #Se construye una conjunto aleatorio de nodos mineros
       usuariosNodo = [];
       usuariosMineros = {};
       contador = maxUsuarios//maxMineros - 1;
       aux = 0;
       for key in usuarios:
           usuariosMineros[key] = usuarios[key];
           if(aux < contador):
              aux += 1;
           else:
               usuariosNodo.append(usuariosMineros);
               aux = 0;
               usuariosMineros = {};
               
       for i in range(len(usuariosNodo)):
           address = "127.0.0." + str(1+randrange(253))
           puerto = 1025+randrange(60000)
           descripcion = "nodo minero " + str(i)
           minerito = NodoMinador(address, puerto,descripcion,usuariosNodo[i]);
           minerito.actualizarCadena(blockchain);
           pool.adicionarMinero(minerito);
           
           
       print("agregados " + str(len(usuariosNodo)) + " mineros ...");  
       print("Iniciando la simulación de crecimiento de la blockchain");  
       #Se construye una cadena de bloques con 10 bloques
       for i in range(1,totalBloquesCaena):
              transacciones = [];
              #Se construye una conjunto aleatorio de transacciones
              for tr in range(1+randrange(maxTransaccionesPorBloque)):
                  emisor = Bloque.generarBloqueHash(random())
                  receptor = Bloque.generarBloqueHash(random())
                  cantidad = uniform(2.5, 1000.0) 
                  transacciones.append(Transaccion(emisor, receptor,cantidad))
              #print("Bloque de transacciones: " + str(i) + " , Agregadas " + str(tr+1) + " transacciones ..."); 
              pool.torneoPorNuevoBloque(transacciones)              
              #print("La cadena tiene ahora " + str(len(blockchain._cadena)) + " Bloques")
       print("Fin de la simulación");
       print("{Descripcion} , {Dirección} , {Puerto} , {Utilidad} , {#Bloques}, {#Minadores}");
       print(pool);
       print("id\t hash \t saldo");
       for key in usuarios:
           print(str(usuarios[key]));
    if __name__ == "__main__":
        main()