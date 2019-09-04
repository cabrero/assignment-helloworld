# coding: utf-8

from pathlib import Path


from ipmrunner.checks import requirement

@requirement("Existe un fichero llamado {filename}")
def existe(world, filename):
    assert Path(filename).exists()

@requirement("El fichero {filename} es ejecutable")
def es_ejecutable(world, filename):
    assert False

@requirement('Al ejecutar el fichero "helloworld.py" imprime el texto: "Hello World!"')
def imprime_hello_world(world):
    assert False

@requirement("No hay ficheros pendientes de commit")
def nothing_to_commit(world):
    assert False

@requirement("El último commit tiene la etiqueta {tagname}")
def tiene_etiqueta(world, tagname):
    assert False

@requirement("El nombre del repositorio remote es {remote_name}")
def el_remote_es(world, remote_name):
    assert False

@requirement("El repositorio remote esta actualizado")
def el_remote_esta_up_to_date(world):
    assert False

