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

#Importanción de los módulos necesarios
import subprocess
import os

#Definición de directorios de trabajo para Termux
global PREFIX, HOME
PREFIX="/data/data/com.termux/files/usr"
HOME="/data/data/com.termux/files/home"

#Chequeo de las herramientas necesarias en el sistema
isjohn=os.path.isfile(PREFIX+"/bin/applets/false")
istor=os.path.isfile(PREFIX+"/bin/tor")
isrb=os.path.isfile(PREFIX+"/bin/ruby")
isnm=os.path.isfile(PREFIX+"/bin/nmap")
isfierce=os.path.isfile(PREFIX+"/bin/fierce")
ismap=os.path.isfile(HOME+"/.sqlmap/sqlmap.py")
isenum=os.path.isfile(HOME+"/.dnsenum/dnsenum.pl")
isnikto=os.path.isfile(HOME+"/.nikto/program/nikto.pl") #Nikto no tiene soporte para SSL en Android actualmente
iswhatw=os.path.isfile(HOME+"/.whatweb/whatweb")
iswp=os.path.isfile(HOME+"/.wpscan/wpscan.rb")
iscurl=os.path.isfile(PREFIX+"/bin/curl")
isgit=os.path.isfile(PREFIX+"/bin/git")

#Chequeo de archivos comunes para definir la distribución
def distribucion():
    #Comprobamos si es Termux en Android.
    isandroid=os.path.isfile(PREFIX+"/bin/termux-info")
    global DISTRO
    if isandroid:
        print "Usted esta usando el emulador Termux en Android!\n"
        DISTRO="Android"
    else:
        print "Usted no usa Termux en Android!."

#Definición de los colores usados en el programa
def cRojo(prt): print("\033[91m {}\033[00m" .format(prt))
def cVerde(prt): print("\033[92m {}\033[00m" .format(prt))
def cAmarillo(prt): print("\033[93m {}\033[00m" .format(prt))
def cMoradoclaro(prt): print("\033[94m {}\033[00m" .format(prt))
def cMorado(prt): print("\033[95m {}\033[00m" .format(prt))
def cCian(prt): print("\033[96m {}\033[00m" .format(prt))
def cGrisclaro(prt): print("\033[97m {}\033[00m" .format(prt))
def cNegro(prt): print("\033[98m {}\033[00m" .format(prt))

#Definimos la función de Actualización de herramientas de acuerdo al sistema usado.
def updatetools(DISTRO):
    respuesta=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")

    #Actualización para Termux an Android.
    if respuesta=="y" and DISTRO=="Android":
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("pkg update")
        cAmarillo("Actualizando Herramientas del sistema...")
        installcorrect=os.system("pkg install util-linux perl clang  nmap make ruby ruby-dev libxslt libxslt-dev git curl tor python python2 libyaml-dev libandroid-glob libandroid-glob-dev \
         && pip3 install fierce -U \
         && pip2 install requests flask -U \
         && cpan install Net::IP Net::DNS Net::Netmask XML::Writer String::Random \
         && cd $PWD/modules/tplmap/ && git pull \
         && cd joomlavs/ && git pull \
         && cd $HOME/.sqlmap && git pull \
         && cd $HOME/.dnsenum && git pull \
         && cd $HOME/.nikto && git pull \
         && cd $HOME/.wpscan && git pull \
         && cd $HOME/.whatweb && git pull \
         && cd $HOME/.wpscan && gem install bundler && bundle install --without test \
         ")
        if installcorrect==0:
            print ""
            cVerde("La actualizacion se realizo correctamente.")
            cVerde("Todo lo necesario esta actualizado, procediendo.")
        else:
            cRojo("Ha ocurrido un error.")
    elif respuesta == "n":
        cAmarillo("Actualizacion abortada, saliendo ...")
        os._exit(0)
    else:
        cRojo("Opcion incorrecta.")
        updatetools(DISTRO)

#Definimos la instalación de todas las herramientas en el sistema detectado.
def installall(DISTRO):
    cRojo("""Para que este framework funcione correctamente, necesitas tener instaladas las siguientes herramientas:
    nmap, fierce, sqlmap, dnsenum, nikto, john, tor, curl, ruby, whatweb & wpscan. Al parecer hay herramientas faltantes en tu sistema!.
    """)
    decision=raw_input("Introduce tu opcion y=continua con la instalación, n=anula la instalación. y/n: ")

    #Instalación en caso de que sea Android.
    if decision=="y" and DISTRO=="Android":
        print ""
        cAmarillo("Actualizando tu lista de paquetes ...")
        os.system("pkg update")
        cAmarillo("Instalando lo necesario en el sistema...")
        correctinstall=os.system("pkg install util-linux perl clang nmap make ruby ruby-dev libxslt libxslt-dev git curl tor python2 python libyaml-dev libandroid-glob libandroid-glob-dev \
                && touch $PREFIX/etc/hosts \
                && pip3 install fierce \
                && pip2 install requests flask \
                && cpan install Net::IP Net::DNS Net::Netmask XML::Writer String::Random \
                && cd modules/tplmap/ && git pull \
                && git clone https://github.com/sqlmapproject/sqlmap $HOME/.sqlmap \
                && git clone https://github.com/fwaeytens/dnsenum $HOME/.dnsenum \
                && git clone https://github.com/sullo/nikto $HOME/.nikto \
                && git clone https://github.com/wpscanteam/wpscan $HOME/.wpscan \
                && git clone https://github.com/urbanadventurer/whatweb $HOME/.whatweb \
                && cd $HOME/.wpscan && gem install bundler && bundle install --without test \
                ")
        if correctinstall==0:
            print ""
            cVerde("La actualizacion se realizo correctamente.")
            cVerde("Todo lo necesario esta actualizado, procediendo.")
        else:
            cRojo("Ha ocurrido un error.")
            installall(DISTRO)
    elif decision == "n":
        print "Instalación abortada, saliendo ..."
        os._exit(0)
    else:
        print "Opcion incorrecta."
        installall(DISTRO)

#Definimos la función que verifica si todo lo necesario está instalado en el sistema.
def check():
    if isnm and isfierce and ismap and isenum and isnikto and iswhatw and iswp and isrb and isgit and iscurl and istor and isjohn:
        cVerde("Todo lo necesario esta instalado, procediendo.")
    else:
        distribucion()
        if DISTRO == "Android":
            installall(DISTRO)
        else:
            print "Distribución desconocida, saliendo."

#Revisamos que TOR esté corriendo en el sistema y si no lo está, lo iniciamos.
def dtor():
    cVerde("Verificando que el servicio TOR esté activo...")
    os.system("tor --quiet &")
    tor=os.system("ps -A| grep -q tor")
    if tor == 0:
        cVerde("0K - TOR")
        pass
    else:
        cRojo("Ha ocurrido un error.")
        pass

#Verificamos que Bundler esté instalado en el sistema.
def gems():
    cVerde("Verificando que Bundler está en el sistema, esto puede tomar varios minutos la primera vez...")
    gem=os.system("bundle | grep -q 'Bundle complete!'")
    if gem == 0:
        cVerde("0K - Bundler")
        pass
    else:
        def gemsinstall():
            cRojo("""Necesitas instalar Bundler, procediendo a la instalación.
    Bundler es requerido por un escanner de vulnerabilidades, necesitas privilegios root o sudo para instalarlo.
    Esto puede tomar un tiempo.""")
            inst = raw_input("Deseas continuar con la instalación? y/n : ")
            if inst=="y":
                os.system("PATH=`ruby -e 'puts Gem.user_dir'`/bin:$PATH")
                cAmarillo("Instalando bundler...")
                correctgem=os.system("gem install bundler && bundle install")
                if correctgem==0:
                    pass
                else:
                    cRojo("Las gemas no se instalaron correctamente, por favor asegurate de estar dentro de la carpeta de webhackshl. esto traera problemas en la opcion d) del menú usando joomlavs. Continuando...")
                    pass
            elif inst=="n":
                cRojo("Instalacion cancelada, esto traera problemas en la opcion d) del menú usando joomlavs. Continuando...")
                pass
            else:
                print "Opción incorrecta.\n"
                gemsinstall()
        gemsinstall()

def utools():
    distribucion()
    updatetools(DISTRO)
