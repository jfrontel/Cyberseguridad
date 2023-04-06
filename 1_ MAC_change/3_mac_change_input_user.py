#Optimizacion_2 --> input de usuario, queremos que el la interface y el mac sean establecidos por teclado
import subprocess 

interface = input("interface: ") #si utilizas python 2 usar raw_input, para python 3 input
new_mac = input("nuevo_mac: ")

print("[+] Cambiando direccion MAC para " + interface + " a " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)