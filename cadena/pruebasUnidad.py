#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cadena.Bloque import Bloque
import json
"""
En esta clase se realizan pruebas de unidad
"""
def main():
   #Cada bloque de prueba se ha creado sin transacciones
   transacciones=0;
   #0 para indicar que el bloque ha sido minado
   genesis = Bloque(0,0,Bloque.generarBloqueHash(0),transacciones);
   cadena = [genesis];
   #Se construye una pseudocadena con 10 bloques
   for i in range(1,10):
       cadena.append(Bloque(i,0,Bloque.generarBloqueHash(cadena[i-1].gethashBloque()) , transacciones));
   
   print("CADENA DE BLOQUES")
   
   print(json.dumps([vars(Bloque) for Bloque in cadena], indent=4, sort_keys=True))
       
if __name__ == "__main__":
    main()