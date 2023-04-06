import subprocess  #importamos libreria que nos permite correr comandos


'''
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
'''

#Optimizacion_1 --> uso de variables
'''
interface = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Cambiando direccion MAC para " + interface + " a " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)'''

#Optimizacion_2 --> input de usuario, queremos que el la interface y el mac sean establecidos por teclado
'''
interface = raw_input("interface: ") #si utilizas python 2 usar raw_input, para python 3 input
new_mac = raw_input("nuevo_mac: ")

print("[+] Cambiando direccion MAC para " + interface + " a " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)'''

#Nuestro programa funciona pero no es muy seguro, una persona que sabe hackear programas lo haria con gran facilidad
#y esto se debe a shell=True, si escribimos en la terminal cuando nos pide la interface eth0;(punto y coma para decirle a la terminal que queremos correr otro comando)
# --> eth0;ls;pwd nos correra comandos que no queremos.


#Optimizacion_3 eliminar shell=True para que nuestro programa no corra comandos que no debe; para ello
#quitaremos cadenas de texto por listas
'''
interface = raw_input("interface: ") #si utilizas python 2 usar raw_input, para python 3 input
new_mac = raw_input("nuevo_mac: ")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])'''

#Optimizacion_4: implementacion de comandos por ejem sudo python mac_change --interface para pedir la interface
import optparse #para poder importar los comandos

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar direccion MAC")
parser.add_option("-m", "--mac", dest = "new_mac", help="Nuevo MAC")

parser.parse_args() #Guardamos en parse_arg las opciones de arriba

interface = raw_input("interface: ") #si utilizas python 2 usar raw_input, para python 3 input
new_mac = raw_input("nuevo_mac: ")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

#Optimizacion_5: Estructuraremos nuestro programa en funciones.
