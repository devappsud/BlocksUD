#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
En esta clase almacena la cadena de bloques
"""

from cadena.Bloque import Bloque
from cadena.PoolMinado import PoolMinado
import json
import copy

class CadenaBloques(object):

    def __init__(self):
        """
        Inicialización de la blockchain
        :param _cadena: Estructura de datos tipo array para almacenar la cadena de bloques.
        """
        self._cadena = []

    
    def getCadenaSerializada(self):
        """
        Serializa la cadena de bloques en un documento JSON
        :return conjunto de bloques en formato JSON
        """
        salida = ""
        for i in range(len(self._cadena)):
            salida = salida +"\nInicio de Bloque\n"
            salida = salida + str(self._cadena[i].consultarBloque());  
            salida = salida + "\nFin Bloque " + str(i) + str(". \n");
        return salida

    def bloqueGenesis(self,trs):
        """
        Crea el primer bloque en la cadena. Es el bloque seminal.
        """
        self.nuevoBloque(2, Bloque.generarBloqueHash(0), trs.copy())

    def nuevoBloque(self, minado, hashBloque,trans):
        """
        Construye e inserta el siguiente bloque de la cadena
        :param minado Método de minado del bloque
        :param hashBloque Hash generado para el bloque
        :return Bloque nuevo bloque generado
        """
        bloque = Bloque(
            indice = len(self._cadena),
            minado = minado,
            hashBloque = hashBloque,
            transacciones=trans.copy()
        )
        self._cadena.append(bloque)
        return bloque


    def obtenerUltimoBloque(self):
        """
        Devuelve una referencia al último nodo de la blockchain
        @return último nodo
        """
        return self._cadena[-1]
    
    @staticmethod
    def bloqueEsValido(nuevoBloque, ultimoBloque):
        """
        Verifica bajo cuatro reglas básicas la validez de un Bloque
        Regla 1: Secuencia ordenada de bloques por valor del índice
        Regla 2: Secuencia ordenada de bloques por fecha de creación
        Regla 3: Hash diferente entre el último bloque de la cadena y el nuevo bloque
        Regla 4: Bloque correctamente minado
        @return True si el bloque es válido, False en otro caso
        """
        if ultimoBloque._indice + 1 != nuevoBloque._indice:
            return False
        elif nuevoBloque._marcaTiempo <= ultimoBloque._marcaTiempo:
            return False
        elif ultimoBloque.gethashBloque != nuevoBloque.gethashBloque:
            return False
        elif not CadenaBloques.esPrimo(nuevoBloque.minado + ultimoBloque.minado):
            return False
        return True

    

    def validarBlockchain(self):
        """
        Verifica la integridad de la cadena de bloques. 
        para este procedimiento se valida que el índice del siguiente bloque sea
        menor en una unidad del bloque anterior y que el hash de cada bloque sea
        correcto según la política de minado establecida, números primos en este caso. 
        @return True si la cadena esta bien formada, False en otro caso
        """
        bloqueAnterior = self._cadena[0]
        for i in range (1,len(self._cadena)):
            bloqueActual = self._cadena[i]
            if (bloqueAnterior._indice + 1) - bloqueActual._indice != 0:
                print("indice malo")
                return False
            if not PoolMinado.esPrimo(bloqueAnterior._minado + bloqueActual._minado):
                return False
            bloqueAnterior = copy.copy(bloqueActual)
        
        return True
    

    
    def __repr__(self):
        return json.JSONEncoder().encode(self._cadena)

    def __str__(self):
        """
        Genera un string con la información de la cadena
        :return: representación en String del nodo
        """
        a = "";
        for i in range(len(self._cadena)):
            a += str(self._cadena[i]) + "\n";
        return a;