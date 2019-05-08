#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
from cliente.Usuario import Usuario
from cadena.CadenaBloques import CadenaBloques
from cadena.NodoMinador import NodoMinador
from cadena.PoolMinado import PoolMinado
from random import randrange
from random import random
from random import seed
from datetime import datetime
from PyQt5.QtWidgets import QProgressBar

"""
Define la estructura del bloque.
"""

class Simulador(object):

    def __init__(self, nombre):
        """
        Creación del escenario final de simulación
        :param _nombre Nombre Asignado al escenario
        :param _usuarios Conjunto de usuarios en la simulación
        :param _blockchain Cadena de Bloques
        :param _pool Conjunto de nodos mineros de la cadena
        """
        self._nombre = nombre;
        self._usuarios = {};
        self._blockchain = CadenaBloques();
        self._pool = PoolMinado()

    def crearUsuarios(self, cantidadUsuarios):
        """
        Inicializa el conjunto de usuarios de la cadena de bloques
        :param cantidadUsuarios: Conjunto inicial de Usuarios en la Simulación
        """
        for i in range(cantidadUsuarios):
           temp = Usuario(i);
           temp.setHashUsuario();
           self._usuarios[temp.gethashUsuario()] = temp;
           
    def distribuirUsuariosMineros(self, maxUsuarios, maxMineros):
        """
        Permite distribuir de manera uniforme los usuarios a los nodos mineros
        :param maxMineros: Conjunto de Nodos mineros de la blockchain
        :param maxUsuarios: Total de usuarios en el sistema
        :return arreglo con los usuarios distribuidos para cada nodo minero
        """
        #Se construye una conjunto aleatorio de nodos mineros
        usuariosNodo = [];
        usuariosMineros = {};
        contador = maxUsuarios//maxMineros - 1;
        aux = 0;
        for key in self._usuarios:
            usuariosMineros[key] = self._usuarios[key];
            if(aux < contador):
                aux += 1;
            else:
                usuariosNodo.append(usuariosMineros);
                aux = 0;
                usuariosMineros = {};
        return usuariosNodo;
    
    def verUsuarios(self):
        """
        Consulta el total de usuarios registrados en un momento dado en la cadena de bloques
        :return  Representación en string del conjunto de Usuarios en la Simulación
        """
        a = "";
        for key in self._usuarios:
           a += str(self._usuarios[key])+"\n";
        return a;

    def consultarHashUsuario(self, idUsuario):
        """
        Retorna el Hash de un usuario dado su número de identificación
        :param idUsuario identificador entero de cada usuario en el sistema
        :return Hash de usuario que corresponde al identificador dado
        """
        for key in self._usuarios:
            if(self._usuarios[key]._idUsuario == idUsuario ):
                return self._usuarios[key].gethashUsuario();
            
    def consultarUsuario(self, hashUsuario):
        """
        Consulta la información de un usuario dado su hash
        :param hashUsuario LLave del diccionario
        :return usuario que corresponde con la llave dada
        """
        return self._usuarios[hashUsuario];
    
    def inicializarBlockchain(self, maxUsuarios, cantidadMineros):
        """
        Creación del bloque génesis de la cadena y asignación de nodos mineros
        :param cantidadMineros, Total de nodos Mineros para la cadena
        :param maxUsuarios: Total de usuarios en el sistema
        """
        emisor = self.consultarUsuario(self.consultarHashUsuario(0));
        receptor = self.consultarUsuario(self.consultarHashUsuario(0));
        transacciones = [];
        transacciones.append(emisor.enviar(100,receptor.gethashUsuario()));
        self._blockchain.bloqueGenesis(transacciones);
        usuariosNodo = self.distribuirUsuariosMineros(maxUsuarios,cantidadMineros);
        self.creacionMineros(cantidadMineros,usuariosNodo);
       
    def creacionMineros(self, cantidadMineros, usuariosNodo):
        """
        Adiciona los nodos mineros a la blockchain. Cada nodo minero tendrá asociado
        un grupo de usuarios, quienés recibirán recompensa por su esfuerzo de minado.
        :param cantidadMineros, Total de nodos Mineros para la cadena
        :param usuariosNodo, Distribución de usuarios mineros para cada nodo Minero
        """
        for m in range(cantidadMineros):
           address = "127.0.0." + str(1+randint(1,250));
           puerto = 1025+randint(1000,10000);
           descripcion = "Minero " + str(m);
           minerito = NodoMinador(address, puerto,descripcion,usuariosNodo[m]);
           minerito.actualizarCadena(self._blockchain);
           self._pool.adicionarMinero(minerito);
           
    def simular(self, maxTransaccionesPorBloque,totalBloquesCaena, cantidadUsuarios,barraProgreso):
        """
        Realiza una simulación de evolución de la blockchain con los parámetros dados.
        :param cantidadUsuarios, Total de usuarios activos en la cadena
        :param cantidadMineros, Total de nodos Mineros para la cadena
        :param usuariosNodo, Distribución de usuarios mineros para cada nodo Minero
        """
        seed();
        transacciones = [];
        emisor = self.consultarHashUsuario(0);
        receptor = self.consultarHashUsuario(1);
        cantidad =  self.consultarUsuario(emisor)._saldo * random();
        transacciones.append(self.consultarUsuario(emisor).enviar(cantidad, self.consultarUsuario(receptor)));
        self._pool.torneoPorNuevoBloque(transacciones);
        cantidadPosibleReceptores = 1;
        for i in range(1,totalBloquesCaena):
           transacciones = [];
           if cantidadPosibleReceptores == cantidadUsuarios-1:
               cantidadPosibleReceptores = 1;
           #Se construye una conjunto aleatorio de transacciones
           for tr in range(1+randrange(maxTransaccionesPorBloque)):
               seed();
               if cantidadPosibleReceptores == cantidadUsuarios-1:
                   cantidadPosibleReceptores = 1;
               intemisor = self.seleccionarUsuario(cantidadPosibleReceptores,-1);
               intreceptor = self.seleccionarUsuario(cantidadPosibleReceptores,intemisor);
               emisor = self.consultarHashUsuario(intemisor);
               receptor = self.consultarHashUsuario(intreceptor);
               cantidad =  self.consultarUsuario(emisor)._saldo * random();
               #print("Cantidad receptores " + str(cantidadPosibleReceptores)+ " receptor " + str(intreceptor) + " emisor " + str(intemisor) + " cantidad " + str(cantidad));
               #print(".", end="");

               transacciones.append(self.consultarUsuario(emisor).enviar(cantidad, self.consultarUsuario(receptor)));
               cantidadPosibleReceptores = cantidadPosibleReceptores + 1;
           instanteInicial = datetime.now() 
           #print("len transacciones = " + str(len(transacciones)));
           self._pool.torneoPorNuevoBloque(transacciones);
           instanteFinal = datetime.now()
           tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
           segundos = tiempo.microseconds
           #print("Torneo " + str(i) + " " + str(segundos) + " microseconds");
           if barraProgreso is not None:
               barraProgreso.setValue(1 + ((100*i) // totalBloquesCaena))
           else :
               print("Bloque " + str(i))
           
               
           
    def seleccionarUsuario(self,cantidadPosibleReceptores, diferentea):
        seed();
        x = randint(0,cantidadPosibleReceptores+1);
        while x == diferentea:
            x = randint(0,cantidadPosibleReceptores+1);
        return x;
        
    def verNodosMineros(self):
        """
        Consulta el total de nodos mineros registrados en la cadena de bloques
        :return pool de mineros de la blockchain
        """
        return self._pool;
    
    def logEjecucion(self, file, mensaje):
        file.write(mensaje + "\n")