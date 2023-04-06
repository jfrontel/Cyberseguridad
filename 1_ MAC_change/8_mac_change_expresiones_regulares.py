import subprocess
import optparse 
import re

def ft_coger_argumentos():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar direccion MAC")
    parser.add_option("-m", "--mac", dest = "new_mac", help="Nuevo MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Introducir una interface valida, usa --help en caso de duda")
    elif not options.new_mac:
        parser.error("[-] Introducir una direccion MAC valida, usa --help en caso de duda")
    return(options)


def ft_cambiar_mac(interface, new_mac):
    print("[+] Cambiando direccion MAC para " + interface + " a " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def ft_coger_mac_actual(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", options.interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0) #cada vez que encuentra la expresion la guarda en group, nosotros queremos la primera group(0)
    else:
        return("[-] No pudimos encontrar la direccion MAC")
    
options = ft_coger_argumentos()
mac_address = ft_coger_mac_actual(options.interface)
print("MAC actual: " + str(mac_address))

ft_cambiar_mac(options.interface, options.new_mac)
mac_address = ft_coger_mac_actual(options.interface)

if(mac_address == options.new_mac):
    print("[+] Direccion MAC cambio correctamente a: " + str(mac_address))
else:
    print("[-] Hubo un error, no se pudo cambiar la direccion MAC")
