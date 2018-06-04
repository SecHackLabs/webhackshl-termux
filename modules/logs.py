import random, string, subprocess

def randomarch(directorio,nombre,extension):
    wtwopt = nombre+''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(6)])+extension
    salida="modules/logs/"+directorio+wtwopt
    return salida
