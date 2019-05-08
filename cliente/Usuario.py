#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
import hashlib
from cadena.Transaccion import Transaccion
"""
.. module:: blockChainTest
"""


class Usuario(object):

    def __init__(self, idUsuario):
        """
        Creación de un usuario en el sistema
        :param _idUsuario Identificador entero del usuario
        :param hashUsuario:  Código Hash del usuario
        :param saldo: Saldo del usuario 
        :param marcaTiempo: Instante de tiempo de creación del usuario
        """
        self._idUsuario  = idUsuario;
        self._saldo = 0;
        self._hashUsuario = 0;
        self._marcaTiempo = time.time();
        """
        Usuario Génesis toma 100 de saldo
        """
        if self._idUsuario == 0:
            self._saldo = 100;
        

    def gethashUsuario(self):
        """
        Obtiene el valor actual del hash del usuario
        :return: Hash del bloque
        """
        return self._hashUsuario;
    
    def setHashUsuario(self):
        self._hashUsuario = self.generarUsuarioHash();
    
    
    def generarUsuarioHash(self):
        """
        Genera Hash la información del bloque
        :return: Hash construido a partir de la información del usuario
        """
        return hashlib.sha256(str(self).encode()).hexdigest()
    
    
    def __str__(self):
        """
        Genera un string con la información del usuario
        :return: representación en String del usuario
        """
        return "{}, {} , {}".format(self._idUsuario, self._hashUsuario, self._saldo)
    
    def enviar(self, valor, receptor):
        """
        :param receptor: hash del usuario receptor de la transferencia
        :param valor: Cantidad que se desea transferir
        :return: La nueva transacción que será enviada a validación
        """
        if valor < self._saldo:
            self._saldo -= valor;
            self.recibir(valor, receptor);
            return Transaccion(self._hashUsuario, receptor._hashUsuario,valor);

    def recibir(self, valor, receptor):
        """
        :param receptor: hash del usuario receptor de la transferencia
        :param valor: Cantidad que se ha recibido
        """
        receptor._saldo += valor;