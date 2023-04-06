#Nuestro programa funciona pero no es muy seguro, una persona que sabe hackear programas lo haria con gran facilidad
#y esto se debe a shell=True, si escribimos en la terminal cuando nos pide la interface eth0;(punto y coma para decirle a la terminal que queremos correr otro comando)
# --> eth0;ls;pwd nos correra comandos que no queremos.


#Optimizacion_3 eliminar shell=True para que nuestro programa no corra comandos que no debe; para ello
#cambiaremos las cadenas de texto por listas

import subprocess
import optparse #para poder importar los comandos

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar direccion MAC")
parser.add_option("-m", "--mac", dest = "new_mac", help="Nuevo MAC")

parser.parse_args() #Guardamos en parse_arg las opciones de arriba

interface = input("interface: ") #si utilizas python 2 usar raw_input, para python 3 input
new_mac = input("nuevo_mac: ")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])