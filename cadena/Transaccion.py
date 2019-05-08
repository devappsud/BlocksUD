#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Define los elementos que componen una transacción.
"""

class Transaccion(object):

    def __init__(self, emisor, receptor, cantidad):
        """
        Creación de una transaccióna
        :param emisor: Hash de quién envía
        :param receptor:  Hash de quién recibe
        :param cantidad: valor de la transacción 
        """
        self._emisor = emisor
        self._receptor = receptor
        self._cantidad = cantidad
        
    def getEmisor(self):
        """
        Obtiene el valor actual del hash del emisor
        :return: Hash del emisor
        """
        return self._emisor;
    
    def getReceptor(self):
        """
        Obtiene el valor actual del hash del receptor
        :return: Hash del receptor
        """
        return self._receptor;
        
    def getCantidad(self):
        """
        Obtiene el valor de la transacción
        :return: Valor de la transacción
        """
        return self._cantidad;
    
    def __str__(self):
        """
        Genera un string con la información de la transacción
        :return: representación en String de una transacción
        """
        return str(self._emisor) + " " + str(self._receptor) +  " " + str(self._cantidad);