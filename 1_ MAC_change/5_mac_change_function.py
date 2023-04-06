import subprocess
import optparse 

def ft_coger_argumentos():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest = "interface", help="Interface para cambiar direccion MAC")
    parser.add_option("-m", "--mac", dest = "new_mac", help="Nuevo MAC")
    return parser.parse_args()

def ft_cambiar_mac(interface, new_mac):
    print("[+] Cambiando direccion MAC para " + interface + " a " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = ft_coger_argumentos()
ft_cambiar_mac(options.interface, options.new_mac)