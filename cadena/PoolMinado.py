#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define la organización para los nodos que van a minar la cadena.
"""
from random import random
from multiprocessing.pool import ThreadPool
import numpy as np
from random import randint


class PoolMinado(object):
    
    def __init__(self):    
        """
        Inicialización del pool de minería
        :param _nodos: conjunto de nodos mineros
        :param _hasRate Simula la capacidad de computo del pool de mineria
        :param _recompensaPorBloque cantidad que se recompensa a los nodos que resuelvan el problema
        :param _dificultad  valor usado para simular el incremento de dificultad del proceso de minado
        """
        self._nodos =  [];
        self._hashRate = 0;
        self._recompensaPorBloque = 10;
        self._dificultad = 1000;
    
    def adicionarMinero(self, minador):
        """
        Agrega  un nodo minero al conjunto de nodos minadores de la blockchain. Si el nodo adicionado aumenta
        el hashrate del pool ylo iguala o supera el 60% de la dificultad, esta última se incrementa en un
        20%
        @param minador: Nuevo nodo minero
        @return True si el nodo de mineria se puede adicionar, False en otro caso
        """
        self._nodos.append(minador)
        self._hashRate += minador._hashRateNodo
        if self._dificultad * 0.6 < self._hashRate:
            self._dificultad *= 1.2;
  
        return True  
    
    @staticmethod
    def pruebaDeTrabajo(indiceUltimoMinado):
        """
        Algoritmo de minado por prueba de trabajo.
        En esta versión se implementa una prueba basada en números primos, en la cual el
        valor de minado del bloque actual y del último bloque de la cadena debe ser un número primo.
        @param indiceUltimoMinado, Valor generado por la minería para el último bloque de la cadena
        @return minadoNuevo Valor de minado obtenido para el nuevo bloque
        """
        minadoNuevo = indiceUltimoMinado + 1
        while not PoolMinado.esPrimo(minadoNuevo + indiceUltimoMinado):
            minadoNuevo += 1

        return minadoNuevo
    
    @staticmethod
    def esPrimo(numero):
        """
        Determina si un número es primo
        @param numero, Número que necesitamos determinar si es primo
        @return True si numero es primo, False en otro caso
        """
        if numero < 2:
            return False
        elif numero == 2:
            return True
        else:
            for x in range(2,numero):
                if(numero % x==0):
                    return False
        return True  
    
    def minarBloque(self,nodoMinero, numeroNodo, output):
        """
        Algoritmo que realiza el minado de un bloque para un nodo en especifico.
        @param nodoMinero, Nodo minero que realizará la prueba de trabajo
        @param numeroNodo, identificador entero del nodo minero en el pool de minería
        @param output, Parámetro de salida donde se conserva la información de 
        la prueba de trabajo ejecutada por el iésimo nodo minero.
        @return minadoNuevo Valor de minado obtenido para el nuevo bloque
        """
        trabajo = 0
        for i in range(self._dificultad - nodoMinero._hashRateNodo + randint(1,10000)):
            trabajo += 1
        ultimo = nodoMinero._cadenaBloques.obtenerUltimoBloque()
        nuevoValorMinado = PoolMinado.pruebaDeTrabajo(ultimo._minado)
        #print("[" + nodoMinero._descripcion + "] ha trabajado " + str(trabajo) + " nuevo valor de minado " + str(nuevoValorMinado))  
        output[numeroNodo][0] = numeroNodo;
        output[numeroNodo][1] = nuevoValorMinado;
        output[numeroNodo][2] = trabajo;

    
    def torneoPorNuevoBloque(self,transacciones):
        """
        Realiza un torneo para la adjudicación del nuevo bloque a un nodo minero. 
        El nodo ganador será el que realice mayor trabajo.
        @param transacciones, Bloque de transacciones que tendrá el nuevo bloque de la cadena
        """
        try:
            #print("Total nodos " + str(len(self._nodos)))
            numOfThreads = int(len(self._nodos))
            pool = ThreadPool(numOfThreads)
            output = [];
            for x in range(numOfThreads):
                output.append([0]*3)

            for i in range(numOfThreads):
                pool.apply_async(self.minarBloque(self._nodos[i],i,output))
            pool.close()
            pool.join()
            utilidadObtenida = np.max(output);
            ganador = np.argmax(output)//(numOfThreads-1)+randint(0,1);
            #print("utilidad obtenida " + str(utilidadObtenida))
            self._nodos[ganador]._cantidadBloquesMinados += 1;
            self._nodos[ganador]._utilidad += utilidadObtenida;
            self.minadoBloque(self._nodos[ganador],transacciones);
            nueva = self._nodos[ganador]._cadenaBloques;
            self.sincronizarCadena(nueva);
            
            totalMinadores = len(self._nodos[ganador]._usuariosMineros);
            for key in self._nodos[ganador]._usuariosMineros:
                self._nodos[ganador]._usuariosMineros[key]._saldo += utilidadObtenida/totalMinadores/self._dificultad;
                #print(self._nodos[ganador]._usuariosMineros[key]._saldo);
            #print("=======================================================")
            
        except:
            #print ("Error: un hilo ha fallado. ",sys.exc_info())
            #print("-");
            errorhilo = True;
    @staticmethod
    def minadoBloque(nodoMinero, transacciones):
        """
        Realiza el proceso de minado de un nuevo bloque en la cadena
        @param nodoMinero que realiza el intento de minar el bloque
        @param transacciones: Conjunto de Transacciones del nuevo bloque
        """
        ultimo = nodoMinero._cadenaBloques.obtenerUltimoBloque();
        nodoMinero._cadenaBloques.nuevoBloque(PoolMinado.pruebaDeTrabajo(ultimo._minado), ultimo.generarBloqueHash(random()), transacciones.copy())
  
    def sincronizarCadena(self,nuevaCadena):
        """
        Realiza una sincronización de la cadena actualizada a todos los mineros
        @param nuevaCadena, Cadena con el nuevo bloque
        """
        for i in range(len(self._nodos)):
            self._nodos[i].actualizarCadena(nuevaCadena);
    
    def __str__(self):
        """
        Genera un string con la información del pool de minería
        :return: representación en String del nodo
        """
        a = "";
        for i in range(len(self._nodos)):
            a += str(self._nodos[i]) + "\n";
        return a;