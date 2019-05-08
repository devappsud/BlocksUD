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
       valorPorDefecto = int(input("Desea una ejecución con valores por defecto (1 en caso afirmativo, otro numero en caso contrario): "));
       
       if valorPorDefecto == 1:
           cantidadUsuarios = 100;
           sm.crearUsuarios(cantidadUsuarios);
           cantidadMineros = 5;
           maxTransaccionesPorBloque = 20;
           totalBloquesCaena = 3000;
       else:
           iterar = True;
           while iterar:
             cantidadUsuarios = int(input("Cantidad de usuarios [100,500] en la simulación: "));
             if (cantidadUsuarios>=100 and cantidadUsuarios<=500):
                 iterar = False
           sm.crearUsuarios(cantidadUsuarios);
           
           iterar = True;
           while iterar:
             cantidadMineros = int(input("Cantidad de pools de Minería [2,5] de la blockchain: "));
             if (cantidadMineros>=2 and cantidadMineros<=5):
                 iterar = False
           
           iterar = True;
           while iterar:
             maxTransaccionesPorBloque = int(input("Maxima cantidad de transacciones [10,30] por Bloque: "));
             if (maxTransaccionesPorBloque>=10 and maxTransaccionesPorBloque<=30):
                 iterar = False
           
           iterar = True;
           while iterar:
             totalBloquesCaena = int(input("Cantidad de Bloques en la Cadena [1000,3000]: "));
             if (totalBloquesCaena>=1000 and totalBloquesCaena<=3000):
                 iterar = False
             
       print("Creando la cadena de bloques...Adicionando Bloque Génesis...");
       print("Hash usuario génesis: " + str(sm.consultarHashUsuario(0)));
       sm.inicializarBlockchain(cantidadUsuarios,cantidadMineros);
       print("Imprimiendo Bloque Génesis...")
       print(sm._blockchain.getCadenaSerializada());

       fsalida = input("nombre Archivo de salida [sin espacios, ni caracteres especiales]: ");
       tsimulacion = open(fsalida + '.txt', 'x');
       instanteInicial = datetime.now()
       sm.simular(maxTransaccionesPorBloque,totalBloquesCaena,cantidadUsuarios,None);
       instanteFinal = datetime.now()
       tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
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
