#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define la estructura de un nodo responsable de minar la cadena de bloques
"""
import time
import copy

class NodoMinador(object):

    def __init__(self, direccion, puerto, descripcion, usuariosMineros):
        """
        Creación de un nodo para la minería de blockchain
        :param _direccción: Dirección ip del nodo minero
        :param _puerto:  puerto TCP/UDP donde se publica el servicio
        :param _descripcion: información adicional del nodo minador
        :param _fechaCreacion: fecha de adición del nodo a la red 
        :param _cadenaBloques: Recibe una copia de la cadena de bloques
        :param _hashRateNodo : Capacidad de resolución de hash por segundo del nodo
        :param _usuariosMineros: Conjunto de usuarios participantes en el nodo minero
        """
        self._direccion = direccion;
        self._puerto = puerto;
        self._descripcion = descripcion; 
        self._utilidad = 0;
        self._cantidadBloquesMinados = 0;
        self._fechaCreacion = time.time();
        self._hashRateNodo = 100;
        self._cadenaBloques = [];
        self._usuariosMineros = copy.copy(usuariosMineros);
        
        
    def actualizarCadena(self, nuevaCadena):
        """
        El proceso de minería requiere que el nodo actualice la blockchain 
        :param: Cadena de bloques actualizada
        """
        self._cadenaBloques = copy.copy(nuevaCadena)
        
    def infoCadena(self):
        """
        Genera un string con la información básica de la cadena de bloques
        :return: una cadena con el reporte del total de nodos de la cadena
        """
        return "La cadena tiene {} bloques".format(str(len(self._cadenaBloques)))
    
    def __str__(self):
        """
        Genera un string con la información de un nodo de minería
        :return: representación en String del nodo
        """
        return "{} , {} , {} , {} , {}".format(self._descripcion , str(self._direccion) + ":" + str(self._puerto), self._utilidad, self._cantidadBloquesMinados, len(self._usuariosMineros)); 
   