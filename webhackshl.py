#!/usr/bin/python2
# encoding: utf-8
# Testing Web Framework - Copyright (C) <2016>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import argparse
import sys
from modules import adminder
from modules import sqlimod
from modules import portsmod
from modules import fingerwebmod
from modules import checker
from modules import hashid
from modules import sstimod

#Definición de directorios de trabajo para Termux
global PREFIX, HOME
PREFIX="/data/data/com.termux/files/usr"
HOME="/data/data/com.termux/files/home"

#Definimos la versión
version='v1.5'

def adjust_to_correct_appdir():
    import os, sys
    try:
        appdir = sys.argv[0] 
        if not appdir:
            raise ValueError
        appdir = os.path.abspath(os.path.dirname(sys.argv[0]))
        os.chdir(appdir)
        if not appdir in sys.path:
            sys.path.insert(0,appdir)
    except:
        print 'Por favor, inicia el script desde una consola de comandos.'
        import time
        time.sleep(10)
        sys.exit(1)

adjust_to_correct_appdir()

os.system("cp joomlavs/Gemfile .")

parser = argparse.ArgumentParser(prog='webhackshl.py',usage='python2 webhackshl.py',description='WebHackSHL es un conjunto de herramientas desarrollado por Security Hack Labs, para realizar auditorias de seguridad web desde basicas hasta avanzadas, diseñado especialmente para sistemas ArchLinux y Debian o basados en los mismos. Cualquier problema con la herramienta puede reportarlo en https://github.com/SecHackLabs/webhackshl/issues o en https://www.foro.securityhacklabs.net/viewforum.php?f=40.')
parser.add_argument("-u", "--update", help="Actualiza WebHackSHL a la mas version mas reciente.", action="store_true")
parser.add_argument("-ut", "--utools", help="Actualiza todas las herramientas Necesitadas por WebHackSHL en tu SO.", action="store_true")
parser.add_argument("-v", "--version", help="Version de WebHackSHL", action="store_true")
args = parser.parse_args()

# Aquí procesamos lo que se tiene que hacer con cada argumento
if args.update:   
       print "Actualizando WebHackSHL..."
       os.system("git pull")
       print "WebHackSHL actualizado correctamente."
       os._exit(0)

# Aqui procesamos el update a la herramientas del sistema.
if args.utools:
    checker.cRojo("Iniciando la actualizacion de las Herramientas de tu sistema...")
    checker.utools()
    os._exit(0)

# Version de la herramienta.
if args.version:
    print "Versión: ",version
    os._exit(0)

def logo():
    print """
 __    __     _                      _     __          __  
/ / /\ \ \___| |__   /\  /\__ _  ___| | __/ _\  /\  /\/ /
\ \/  \/ / _ \ '_ \ / /_/ / _` |/ __| |/ /\ \  / /_/ / /   
 \  /\  /  __/ |_) / __  / (_| | (__|   < _\ \/ __  / /_____
  \/  \/ \___|_.__/\/ /_/ \__,_|\___|_|\_\\\\__/\/ /_/\____/""", version, """

    __
_/  |_  ___________  _____  __ _____  ___
\   __\/ __ \_  __ \/     \|  |  \  \/  /
 |  | \  ___/|  | \/  Y Y  \  |  />    <
 |__|  \___  >__|  |__|_|  /____//__/\_ \\
           \/            \/            \/

    Programador: Eduard Eliecer Tolosa Toloza 
      XMPP/Email: edu4rdshl@disroot.org
 Contacto y sala de chat: https://riot.im/app/#/room/#securityhacklabs:matrix.org
    Security Hack Labs Team. @SecHackLabs
    Blog: https://securityhacklabs.net


Uso: python2 webhackshl.py -h - Muestra un mensaje de ayuda.
     python2 webhackshl.py -u - Actualiza WebHackSHL a la versión mas reciente.
     python2 webhachshl.py -ut - Actualiza las Herramientas necesarias para WebHackSHL
"""

def disclaimer():
    checker.cRojo("Advertencia legal: El uso de WebHackSHL-Termux para atacar objetivos sin el consentimiento mutuo previo es ilegal. Es responsabilidad del usuario final a obedecer todas las leyes aplicables locales, estatales y federales. Los desarrolladores no asumen ninguna responsabilidad y no son responsables de cualquier mal uso o daño causado por este programa")
try:
    logo()
    print ""
    disclaimer()
    print ""
    checker.check()
    print ""
    checker.gems()
    print ""
    checker.dtor()
    def webframework():
        print ""
        checker.cAmarillo("""Selecciona una de las siguientes opciones.""")
        print """
	a) Buscar URLs vulnerables a SQLi, LFI, RCE, XSS.
        b) Realizar SQLi a una web vulnerable a SQLi.
        c) Realizar un escaneo completo de un host, enumerar DNS, Bypassear Cloudflare y mas.
	d) Realizar pruebas de penetracion web y analisis de vulnerabilidades.
        e) Buscar el panel admin de un sitio web.
        f) Ataques a contraseñas y hashing.
        g) Realizar inyección Server Side template Injection (SSTI) a un sitio web vulnerable.
        h) Salir.
        """
        sel=raw_input("Selecciona: ")
        if sel == "a":
            try:
                os.system("python2 modules/sqlitest.py")    
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "b":
            try:
                sqlimod.execute()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "c":
            try:
                portsmod.menu()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "d":
            try:
                fingerwebmod.execute()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "e":
            try:
                adminder.adminfind()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "f":
            try:
                hashid.menu()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "g":
            try:
                sstimod.submenu()
                webframework()
            except KeyboardInterrupt:
                webframework()
        elif sel == "h":
            print "Saliendo."
                
        else:
            webframework()
    webframework()

except:
    print "Saliendo."
    pass
os._exit(0)
