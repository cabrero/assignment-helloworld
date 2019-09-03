# coding: utf-8

import sys
import ast
import re

def pattern2regexp(pattern):
    tree = ast.parse(f"f'{pattern}'")
    values = tree.body[0].value.values
    regexp = ""
    for value in values:
        if isinstance(value, ast.Str):
            regexp += value.s
        elif isinstance(value, ast.FormattedValue) and isinstance(value.value, ast.Name):
            regexp += f"(?P<{value.value.id}>.+)"
        else:
            raise SyntaxError(pattern)
    return re.compile(regexp)


def requirement(pattern):
    regexp = pattern2regexp(pattern)
    def decorator(f):
        def check_builder(match):
            return lambda world: f(world, **match.groupdict())

        module = sys.modules[f.__module__]
        if not hasattr(module, "__checks__"):
            module.__checks__ = []
        module.__checks__.append((regexp, check_builder))
        return f
    return decorator


# ----------------------------------------------------------------------

@requirement("Existe un fichero llamado {filename}")
def existe(world, filename):
    assert False

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

