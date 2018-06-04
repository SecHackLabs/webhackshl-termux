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
import os
import checker
import hashid

hashtypelist=['7z','7z-opencl','AFS','agilekeychain','agilekeychain-opencl','aix-smd5','aix-ssha1','aix-ssha256','aix-ssha512','asa-md5','bcrypt','bcrypt-opencl','bfegg','Bitcoin','blackberry-es10','Blockchain','blockchain-opencl','bsdicrypt','chap','Citrix_NS10','Clipperz','cloudkeychain','cq','CRC32','crypt','dahua','descrypt','descrypt-opencl','Django','django-scrypt','dmd5','dmg','dmg-opencl','dominosec','dragonfly3-32','dragonfly3-64','dragonfly4-32','dragonfly4-64','Drupal7','dummy','dynamic_n','eCryptfs','EFS','eigrp','EncFS','encfs-opencl','EPI','EPiServer','fde','FormSpring','Fortigate','gost','gpg','gpg-opencl','HAVAL-128-4','HAVAL-256-3','hdaa','HMAC-MD5','HMAC-SHA1','HMAC-SHA224','HMAC-SHA256','HMAC-SHA384','HMAC-SHA512','hMailServer','hsrp','IKE','ipb2','KeePass','keychain','keychain-opencl','keyring','keyring-opencl','keystore','known_hosts','krb4','krb5','krb5-18','krb5pa-md5','krb5pa-md5-opencl','krb5pa-sha1','krb5pa-sha1-opencl','kwallet','LastPass','LM','lotus5','lotus5-opencl','lotus85','LUKS','MD2','md4-gen','md5crypt','md5crypt-opencl','md5ns','mdc2','MediaWiki','MongoDB','Mozilla','mscash','mscash2','mscash2-opencl','MSCHAPv2','mschapv2-naive','mssql','mssql05','mssql12','mysql','mysql-sha1','mysql-sha1-opencl','mysqlna','net-md5','net-sha1','nethalflm','netlm','netlmv2','netntlm','netntlm-naive','netntlmv2','nk','nsldap','NT','nt-opencl','nt2','ntlmv2-opencl','o5logon','o5logon-opencl','ODF','ODF-AES-opencl','ODF-opencl','Office','Office2007-opencl','office2010-opencl','office2013-opencl','oldoffice','oldoffice-opencl','OpenBSD-SoftRAID','openssl-enc','OpenVMS','oracle','oracle11','osc','Panama','PBKDF2-HMAC-SHA1','PBKDF2-HMAC-SHA1-opencl','PBKDF2-HMAC-SHA256','PBKDF2-HMAC-SHA256-opencl','PBKDF2-HMAC-SHA512','pbkdf2-hmac-sha512-opencl','PDF','PFX','phpass','phpass-opencl','PHPS','pix-md5','PKZIP','po','postgres','PST','PuTTY','pwsafe','pwsafe-opencl','RACF','RAdmin','RAKP','RAKP-opencl','rar','rar-opencl','RAR5','RAR5-opencl','Raw-Blake2','Raw-Keccak','Raw-Keccak-256','Raw-MD4','Raw-MD4-opencl','Raw-MD5','Raw-MD5-opencl','Raw-MD5u','Raw-SHA','Raw-SHA1','Raw-SHA1-Linkedin','Raw-SHA1-ng','Raw-SHA1-opencl','Raw-SHA224','Raw-SHA256','Raw-SHA256-ng','Raw-SHA256-opencl','Raw-SHA384','Raw-SHA512','Raw-SHA512-ng','Raw-SHA512-opencl','ripemd-128','ripemd-160','rsvp','Salted-SHA1','sapb','sapg','scrypt','sha1-gen','sha1crypt','sha1crypt-opencl','sha256crypt','sha256crypt-opencl','sha512crypt','sha512crypt-opencl','Siemens-S7','SIP','skein-256','skein-512','skey','Snefru-128','Snefru-256','SSH','SSH-ng','ssha-opencl','SSHA512','STRIP','strip-opencl','SunMD5','sxc','sxc-opencl','Sybase-PROP','sybasease','tc_aes_xts','tc_ripemd160','tc_sha512','tc_whirlpool','tcp-md5','Tiger','tripcode','VNC','vtp','wbb3','whirlpool','whirlpool0','whirlpool1','WoWSRP','wpapsk','wpapsk-opencl','xsha','xsha512','XSHA512-opencl','ZIP','zip-opencl']


def getwordlist():
    global wdlist
    print """\n¿Que tipo de WordList deseas usar?
    a) Lista por defecto de WebHackSHL (RockYou).
    b) Una WordList que esta en otro directorio.
    """
    wliste=raw_input("Introduce tu opción: ")
    if wliste=="a":
        wdlist="modules/wordlists/rockyou.txt"
        arewdlist=os.path.isfile(wdlist)
        if arewdlist:
            return wdlist
        else:
            print "\nAl parecer no tienes las wordlist necesarias para empezar el ataque."
            descargarwdls()
    elif wliste=="b":
        wdlist=raw_input("Introduce el PATH donde se encuentra la wordlist: ")
        if os.path.isfile(wdlist):
            return wdlist
        else:
            print "El archivo no existe."
            getwordlist()
    else:
        print "Opcion invalida, intentalo de nuevo."
        getwordlist()
        
def descargarwdls():
    try:
        print "\nDesea descargar la wordlist de Kali-Linux?"
        wordlstkali=raw_input("Introduce una opcion y/n:  ")
        if wordlstkali == "y":
            print "Descargando paquetes ..."
            os.system("git clone git://git.kali.org/packages/wordlists.git modules/wordlists")
            print "Descomprimiendo WordList..."
            sinmp=os.system("cd modules/wordlists && gzip -d rockyou.txt.gz")
	    if sinmp == 0:
                print "Descompresion exitosa.."
		print "Regresando al menú anterior, todo esta listo para desencriptar."
                hashid.menu()
	    else:
    	        print "Ha ocurrido un error, saliendo.\n"
	        hashid.menu()
        elif wordlstkali == "n":
            print "Debes tener una wordlist para utilizarlo."
            hashid.menu()
        else:
            print "Opción invalida, intenta de nuevo."
            descargarwdls()
		
    except KeyboardInterrupt:
        print "Saliendo."
        pass

def gethash():
    hashatt=raw_input("Introduce el Hash: ")
    archash=open('hash.txt','w')
    archash.write(hashatt)
    archash.close()
    if hashatt == "":
        checker.cRojo("Hash invalido / No introdujo un Hash.")
        gethash()
    else:
        pass 

def hashdecrypt(hashtype):
    getwordlist()
    gethash()
    print "\nIniciando desencriptación del Hash..."
    print "Intentando desecriptar el hash de tipo ",hashtype,"."
    subprocess.call(["john","--format="+hashtype,"--wordlist="+wdlist,"hash.txt"])
    verdecrypt()

def verdecrypt():
    verhash=raw_input("\n¿Desea ver los hashes desencriptados (En caso de haberlos)? y/n: ")
    if verhash == "y":
        print "Imprimiendo los Hash desencriptados."
        subprocess.call(["john","--show","hash.txt"])
    elif verhash == "n":
        print "Regresando al menú anterior.\n"
        pass
    else:
        print "Opción incorrecta, saliendo al menú anterior.\n"
        pass

def md5hash():
    hashdecrypt("Raw-MD5")

def sha1hash():
    hashdecrypt("Raw-SHA1")

def mysqlhash():
    hashdecrypt("mysql")

def djangohash():
    hashdecrypt("Django")

def anyhash():
    checker.cAmarillo("\nLa lista de tipos Hash que puede desencriptar es:\n")
    checker.cAmarillo(hashtypelist)
    hashtyp=raw_input("\nIntroduce el tipo de Hash que deseas desencriptar usando John The Ripper: ")
    if hashtyp in hashtypelist:
        hashdecrypt(hashtyp)
    else:
        print "El tipo de Hash especificado no es valido, intentalo de nuevo.\n"
        anyhash()



