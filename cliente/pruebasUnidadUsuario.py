#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from cliente.Usuario import Usuario


"""
En esta clase se realizan pruebas de unidad
"""
class pruebasUnidadUsuario(object):
    
    @staticmethod
    def jsonDefault(object):
        return object.__dict__
    
    def main():
       usuarios = {};
       for i in range(10):
           temp = Usuario(i);
           temp.setHashUsuario();
           usuarios[temp.gethashUsuario] = temp;
    
       print("CONJUNTO DE USUARIOS")
       print("id\t hash \t saldo");
       for key in usuarios:
           print(str(usuarios[key]));


    if __name__ == "__main__":
        main()