import subprocess
import optparse 

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

options = ft_coger_argumentos()
ft_cambiar_mac(options.interface, options.new_mac)