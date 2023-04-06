#Optimizacion_1 --> uso de variables
import subprocess

interface = "eth0"
new_mac = "00:11:22:33:44:77"

print("[+] Cambiando direccion MAC para " + interface + " a " + new_mac)
subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)