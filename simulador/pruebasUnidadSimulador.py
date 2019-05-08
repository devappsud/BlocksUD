#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from simulador.Simulador import Simulador
from datetime import datetime

"""
En esta clase se realizan pruebas de unidad
"""
class pruebasUnidadSimulador(object):

    def main():
       sm = Simulador("Simulación del comportamiento de una cadena de bloques");
       cantidadUsuarios = 100;
       sm.crearUsuarios(cantidadUsuarios);
       cantidadMineros = 5;
       maxTransaccionesPorBloque = 20;
       totalBloquesCaena = 3000;
       print("Creando la cadena de bloques...Adicionando Bloque Génesis...");
       print("Hash usuario génesis: " + str(sm.consultarHashUsuario(0)));
       sm.inicializarBlockchain(cantidadUsuarios,cantidadMineros);
       print("Imprimiendo Bloque Génesis...")
       print(sm._blockchain.getCadenaSerializada());

       tsimulacion = open('../output/timesimulacion6.txt', 'x');
       instanteInicial = datetime.now()
       sm.simular(maxTransaccionesPorBloque,totalBloquesCaena,cantidadUsuarios);
       instanteFinal = datetime.now()
       tiempo = instanteFinal - instanteInicial 
       segundos = tiempo.seconds;
       tsimulacion.write("Simulacion \n");
       tsimulacion.write("cantidadUsuarios " + str(cantidadUsuarios) + "\n");
       tsimulacion.write("cantidadMineros " + str(cantidadMineros)+ "\n");
       tsimulacion.write("maxTransaccionesPorBloque " + str(maxTransaccionesPorBloque)+ "\n");
       tsimulacion.write("totalBloquesCadena " + str(totalBloquesCaena)+ "\n");
       tsimulacion.write("demoro " + str(segundos) + " segundos"+ "\n");
       tsimulacion.write("\nFin de la simulación: demoró " + str(segundos) + " segundos" + "\n");
       tsimulacion.write("Estado de los Nodos Mineros...");
       tsimulacion.write("{} , {} , {} , {}, {}".format(str("Descripción"),str("Direccion"), str("Utilidad"),str("Bloques"),str("Usuarios"))+ "\n")
       tsimulacion.write(str(sm.verNodosMineros()));
       tsimulacion.write("Estado de los Usuarios"+ "\n")
       tsimulacion.write("{}, {} , {} ".format(str("#id"),str("Direccion Hash del Usario"), str("Saldo"))+ "\n");
       tsimulacion.write(sm.verUsuarios()+ "\n");
       tsimulacion.write("Cadena de Bloques\n");
       tsimulacion.write(sm._blockchain.getCadenaSerializada()+ "\n");
       tsimulacion.close();
    if __name__ == "__main__":
        main()